"""Fuzzy match helpers ported from ibis-bot's `tools/discover.py`.

Real arr metadata is dirty: year suffixes in Sonarr titles, separator-corrupted
Lidarr author strings, alt-titles in Radarr, MusicBrainz-vs-display name drift.
Tuple-equality misses 90% of overlaps. These helpers use rapidfuzz + lightweight
token normalization that's been calibrated against real Sonarr/Radarr/Lidarr
data via ibis-bot's production usage.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass

from rapidfuzz import fuzz, process

_NON_WORD = re.compile(r"[^a-z0-9]+")
_THE_PREFIX = re.compile(r"^(the|a|an)\s+")

# Match a trailing year tag, in any of the forms a user/LLM commonly writes:
#   "Battlestar Galactica 2004", "Dune (2021)", "BSG [2004]", "TMNT 87", "TMNT '87"
# We deliberately accept 2-digit short forms so a user typing "X (87)" doesn't
# slip past the disambiguation gate.
# Optional apostrophe — straight, backtick, curly left (U+2018), curly right
# (U+2019). Smart quotes are common from macOS auto-correct and iOS Notes copy-
# paste, so the regex has to accept them. The character class is built with
# explicit unicode escapes so ruff doesn't flag literal smart quotes as
# ambiguous source characters.
_APOS = "['`\u2018\u2019]"
_YEAR_TAG = re.compile(
    rf"""
    \s*
    [(\[]?                       # optional opening bracket
    (?:{_APOS}\s*)?              # optional apostrophe
    \b(19\d{{2}}|20\d{{2}}|\d{{2}})\b  # 4-digit year OR 2-digit short form
    [)\]]?                       # optional closing bracket
    \s*$
    """,
    re.VERBOSE,
)
# Stricter: when no year is provided externally, only extract 4-digit years.
# 2-digit short forms are too ambiguous to extract autonomously ("12" could be
# the episode number or the year), so they only count when the caller already
# decided to interpret the field as a year.
_YEAR_TAG_STRICT = re.compile(
    rf"""
    \s*
    [(\[]?
    (?:{_APOS}\s*)?
    \b(19\d{{2}}|20\d{{2}})\b
    [)\]]?
    \s*$
    """,
    re.VERBOSE,
)


def normalize(s: str) -> str:
    """Lowercase, drop articles, collapse punctuation.

    Stable across runs — used as map key, do not change without regenerating
    fingerprints in tests.
    """
    if not s:
        return ""
    out = s.casefold().strip()
    out = _THE_PREFIX.sub("", out)
    out = _NON_WORD.sub(" ", out)
    return " ".join(out.split())


def tokens(s: str) -> set[str]:
    """Tokenize for set-overlap matching. Used for author/artist matching where word order varies."""
    return set(normalize(s).split())


def title_contains(haystack: str, needle: str) -> bool:
    """Loose `needle in haystack` after normalization. Catches series-with-year ('The Office (US) (2005)' contains 'the office')."""
    return normalize(needle) in normalize(haystack)


@dataclass(frozen=True, slots=True)
class FuzzyMatch:
    """A single fuzzy match result. `score` is rapidfuzz token-set ratio scaled 0..100."""

    value: str
    score: float
    index: int


def best_matches(
    query: str,
    candidates: Iterable[str],
    *,
    limit: int = 10,
    threshold: float = 70.0,
) -> list[FuzzyMatch]:
    """Return up to `limit` candidates whose token-set ratio against `query` is ≥ `threshold`.

    Threshold 70 chosen empirically against ibis-bot's Calibre/arr corpus — lower
    yields false positives, higher misses 'Dune 2021' vs 'Dune'.
    """
    candidate_list = list(candidates)
    if not candidate_list:
        return []
    results = process.extract(
        query,
        candidate_list,
        scorer=fuzz.token_set_ratio,
        processor=normalize,
        limit=limit,
    )
    return [FuzzyMatch(value=v, score=s, index=i) for v, s, i in results if s >= threshold]


def extract_year_tag(title: str, hint_year: int | None = None) -> tuple[str, int | None]:
    """Strip a trailing year tag off a title and return ``(clean_title, year)``.

    The Servarr lookup endpoints rank "X (87)" loosely, so a user-typed year
    embedded in the title needs to come out before the upstream call and be
    re-applied as a post-filter. Ported from ibis-bot's ``_clean_title_and_year``.

    - If ``hint_year`` is supplied, it wins and the regex just strips anything
      that looks like a year tag (4-digit or 2-digit) off the title.
    - If no hint, we extract only 4-digit years autonomously; 2-digit forms
      are too ambiguous (could be an episode count, a quality tag, etc.).

    Returns the input unchanged when no year can be confidently identified.
    """
    if not title:
        return "", hint_year

    if hint_year is not None:
        clean = _YEAR_TAG.sub("", title).strip()
        # Don't blank the title — fall back if the strip ate everything.
        return (clean or title.strip()), hint_year

    m = _YEAR_TAG_STRICT.search(title)
    if not m:
        return title.strip(), None

    year = int(m.group(1))
    # 2-digit branch handled above by hint_year-only path.
    clean = _YEAR_TAG_STRICT.sub("", title).strip()
    return (clean or title.strip()), year


_INITIAL_WORD = re.compile(r"[A-Za-z]\w*")
_WORD = re.compile(r"\W+")


def is_acronym_or_substring_match(query: str, target: str) -> bool:
    """True if ``query`` plausibly identifies ``target`` by acronym or token overlap.

    Catches what rapidfuzz's token-set-ratio misses:
    - "TMNT" → "Teenage Mutant Ninja Turtles" (initials of capitalized words)
    - "LOTR" → "The Lord of the Rings"
    - "GOT" → "Game of Thrones"
    - "MCU" → "Marvel Cinematic Universe"
    - Substring / token-set overlap when above threshold

    Ported from ibis-bot's ``_title_relevant`` / ``_acronym_or_substring_match``.
    Used as a post-filter when a year-only match returns too many wrong-show hits.
    """
    if not query or not target:
        return False
    q = query.casefold().strip()
    t = target.casefold().strip()
    if not q or not t:
        return False
    if q == t or q in t or t in q:
        return True

    initials = "".join(w[0] for w in _INITIAL_WORD.findall(target)).casefold()
    # Use the ORIGINAL target's word starts; the initials should also be
    # casefolded so the comparison is symmetric.
    if q == initials or (len(q) >= 2 and q in initials):
        return True

    qt = {w for w in _WORD.split(q) if w}
    tt = {w for w in _WORD.split(t) if w}
    if qt and tt:
        overlap = len(qt & tt)
        # ibis-bot's threshold: majority of query tokens present in target.
        if overlap >= max(1, len(qt) // 2 + 1):
            return True
    return False


def looks_like_acronym(query: str) -> bool:
    """Heuristic for 'should we run the acronym fallback path'.

    All-uppercase OR mixed but no spaces, length ≤ 8 chars. Used to gate the
    extra HTTP round-trip in ``jellyfin.library_search``: a query that's
    obviously a regular title ("the office") doesn't need the fallback.
    """
    if not query:
        return False
    stripped = query.strip()
    if " " in stripped:
        return False
    if len(stripped) > 8:
        return False
    return any(c.isalpha() for c in stripped)
