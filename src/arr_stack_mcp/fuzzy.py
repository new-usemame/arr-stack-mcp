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
