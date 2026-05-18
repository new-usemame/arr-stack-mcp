# ibis-bot follow-ups (post-Phase-A) — applicability to arr-stack-mcp

The operator extended ibis-bot (the local Matrix tool-runner / "elementx" MCP at
`teenyverse:/home/defaultuser/ibis-bot/`) between 2026-05-12 and 2026-05-18, after
arr-stack-mcp's Phase A research snapshot. The diff against
`research/ibis-bot-tools/` falls into three patterns; this note evaluates each
for portability into arr-stack-mcp.

## 1. Year-tag extraction + clean-title-and-year (`tools/arrs.py`)

ibis-bot's `download_tv` and `download_movie` now accept an optional `year:
int | None` and run input through `_clean_title_and_year(title, year)`:

```python
_YEAR_TAG_RE = re.compile(r"\s*[\(\[]?\b(19[0-9]{2}|20[0-9]{2}|[''`]?\d{2})\)?[\]\)]?\s*$")

def _clean_title_and_year(title, hint_year):
    year = hint_year or _extract_year(title)
    clean = _YEAR_TAG_RE.sub("", title).strip() if year else title.strip()
    return clean, year
```

Why: Sonarr's `/series/lookup` treats `"TMNT (87)"` as a literal title and ranks
matches loosely. The user-typed-or-LLM-emitted year hint (in parens, brackets,
two-digit short form) needs to be stripped before query, then applied as a
post-filter.

**Applicable to arr-stack-mcp:** Yes. Our `SeriesSearchInput.year` and
`MovieSearchInput.year` are already structured fields, but if the LLM packs the
year into the query string itself, we silently mismatch the same way.

## 2. Acronym + token-overlap relevance check (`_title_relevant` / `_acronym_or_substring_match`)

Same helper duplicated in `arrs.py` and `jellyfin.py`:

```python
def _title_relevant(query, title):
    # exact / substring
    if q == t or q in t or t in q: return True
    # acronym from first letters
    initials = "".join(w[0] for w in re.findall(r"[A-Za-z]\w*", title)).lower()
    if q == initials or q in initials: return True
    # token-set overlap with majority threshold
    qt, tt = set(re.split(r"\W+", q)), set(re.split(r"\W+", t))
    return qt and tt and len(qt & tt) >= max(1, len(qt) // 2 + 1)
```

Why: rapidfuzz's `token_set_ratio` does not catch `"TMNT"` →
`"Teenage Mutant Ninja Turtles"`. Year-filter-alone admits wrong shows that
happen to share the year. The two-pass `year and _title_relevant` gate is the
fix.

**Applicable to arr-stack-mcp:** Yes — our `fuzzy.py` is missing acronym
handling. Several common franchises (`TMNT`, `LOTR`, `GOT`, `MIB`, `MCU`) only
resolve via initials.

## 3. SearchTerm-then-fall-back-to-recursive (`tools/jellyfin.py`)

When Jellyfin's native `SearchTerm` returns nothing for an acronym query,
ibis-bot pivots to a `Recursive=true, Limit=500` list and applies its own
acronym matcher locally:

```python
res = await _get("/Items", SearchTerm=title, ...)
items = (res or {}).get("Items") or []
yfilt = [it for it in items if (not year or it.get("ProductionYear") == year)]
matches = [_item_to_match(it, libs) for it in yfilt]
if not matches:
    res = await _get("/Items", Limit="500", ...)  # full list, no SearchTerm
    for it in (res or {}).get("Items") or []:
        if year and it.get("ProductionYear") != year:
            continue
        if _acronym_or_substring_match(title, it.get("Name", "")):
            matches.append(_item_to_match(it, libs))
```

Why: Jellyfin's `SearchTerm` is fuzzy-but-not-acronym-aware. The fallback path
is cheap (one extra HTTP call, capped at 500 items) and prevents
"not in jellyfin" replies for items that ARE there under a fuller name.

**Applicable to arr-stack-mcp:** Yes for `jellyfin.library_search` — we
currently send `search_term=args.query` and call it done. The two-stage
fallback should be ported, though gated on `args.query` looking like an
acronym (all-caps and ≤8 chars) so we don't always pay the extra call.

## What does NOT apply

- **`llm.py` SYSTEM_PROMPT updates** — 250+ lines of LLM-facing rules for
  ibis-bot's Matrix-driver mode (authorization, output discipline, vocabulary
  mapping, Spotify-style favorites, reading status tracking, etc.). These
  belong on the *consumer* of arr-stack-mcp (Claude Desktop, Claude Code, n8n
  workflows). arr-stack-mcp itself is the tool surface; our equivalent is
  tool descriptions, which already cross-reference related tools per the
  Anthropic guidance.
- **Room-based authorization model** — Matrix-specific. MCP's auth model is
  carried by the transport (stdio = local trust; HTTP = bearer token).
- **Author-follow / reading-status / Spotify-favorites / series-fill plans** —
  out of v0.1 scope per CLAUDE.md hard rule #7 (no Calibre, no LazyLibrarian,
  no music meta-features unless Jellyfin-native).
- **Self-describing structured tool results so the LLM doesn't need to
  re-render** — already a design rule of arr-stack-mcp (`ToolEnvelope`,
  compact pydantic outputs). The ibis-bot SYSTEM_PROMPT enforces this on the
  consumer side; we enforce it on the server side.

## Recommended changes

Three small, focused patches:

| Change | File | Notes |
|---|---|---|
| Acronym + token-overlap predicate | `src/arr_stack_mcp/fuzzy.py` | Add `is_acronym_or_substring_match(query, target) -> bool`. Pure, well-tested unit. |
| Year-tag extraction from free-text title | `src/arr_stack_mcp/fuzzy.py` | Add `extract_year_tag(title) -> (clean_title, year \| None)`. Same regex as ibis-bot's `_YEAR_TAG_RE`. |
| Two-pass year+relevance gate in `series_search` / `movie_search` | `src/arr_stack_mcp/tools/sonarr/tools.py`, `tools/radarr/tools.py` | After matching by title, if `args.year` is set, only keep candidates that ALSO pass relevance. If the user packed the year into the query string itself, extract via the new helper before matching. |
| Acronym fallback for `jellyfin.library_search` | `src/arr_stack_mcp/tools/jellyfin/tools.py` | When `search_term` returns 0 and the query looks like an acronym, fall back to `Recursive=true, Limit=500` + local relevance filter. |

These are pure-Python additions, no new dependencies, no API shape changes.
Land as `feat(fuzzy)` + `feat(sonarr|radarr|jellyfin)` and let release-please
roll a v0.1.2 patch.

## Score the difference

| Aspect | Our arr-stack-mcp v0.1.1 | ibis-bot 2026-05-18 |
|---|---|---|
| Architecture | Better. Two-layer auto-gen + curated, dotted MCP namespacing, pydantic in/out. ibis-bot is one-layer with hand-coded httpx calls. |
| Confirm tokens | Tied. Same shape, same single-use, same TTL. We bind to payload fingerprint; ibis-bot also does. |
| Per-toolset gating | Better. We have CLI + env flags (`--read-only`, `--disable-destructive`). ibis-bot's `hide_tools.py` is similar but Matrix-specific. |
| Result envelopes | Better. Typed pydantic, MCP catalogue carries schema. ibis-bot returns untyped dicts. |
| Error envelopes | Better. Diagnostic with hints. ibis-bot returns `{ok: False, msg: ...}` strings. |
| Acronym matching | **Worse.** Missing. → Patch. |
| Year-tag extraction from free-text | **Worse.** Missing. → Patch. |
| Two-pass relevance after year filter | **Worse.** Missing. → Patch. |
| Jellyfin recursive-fallback search | **Worse.** Missing. → Patch. |
| Per-user Jellyfin scoping | Worse. Deferred to v0.2. ibis-bot does Matrix-sender → Jellyfin-user mapping. |
| LLM-driver-side prompt | N/A. We are the server; this is consumer-side. |

Net: arr-stack-mcp's structure is stronger; ibis-bot's matching heuristics
have outpaced ours. Four small ports close the gap.
