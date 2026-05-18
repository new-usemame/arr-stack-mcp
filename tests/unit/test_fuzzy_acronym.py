"""Acronym + year-tag fuzzy helpers ported from ibis-bot post-Phase-A work.

See ``notes/RESEARCH-ibis-bot-followups.md`` for the source of these patterns.
"""

from __future__ import annotations

from arr_stack_mcp.fuzzy import (
    extract_year_tag,
    is_acronym_or_substring_match,
    looks_like_acronym,
)


class TestExtractYearTag:
    def test_explicit_year_in_parens(self) -> None:
        assert extract_year_tag("Dune (2021)") == ("Dune", 2021)

    def test_explicit_year_in_brackets(self) -> None:
        assert extract_year_tag("Battlestar Galactica [2004]") == ("Battlestar Galactica", 2004)

    def test_explicit_year_unbracketed(self) -> None:
        assert extract_year_tag("Battlestar Galactica 2004") == ("Battlestar Galactica", 2004)

    def test_no_year_returns_input(self) -> None:
        assert extract_year_tag("The Office") == ("The Office", None)

    def test_two_digit_year_requires_hint(self) -> None:
        # No hint: leave the title alone — "87" is too ambiguous to extract
        # autonomously.
        assert extract_year_tag("TMNT (87)") == ("TMNT (87)", None)
        # With a hint, the regex strips the year tag and the hint wins.
        assert extract_year_tag("TMNT (87)", hint_year=1987) == ("TMNT", 1987)

    def test_hint_wins_when_title_carries_different_year(self) -> None:
        assert extract_year_tag("Dune (2021)", hint_year=1984) == ("Dune", 1984)

    def test_apostrophe_short_year_with_hint(self) -> None:
        assert extract_year_tag("BSG '04", hint_year=2004) == ("BSG", 2004)

    def test_curly_apostrophe_short_year_with_hint(self) -> None:
        # macOS / smart-quotes input — left single quotation mark (U+2018)
        assert extract_year_tag("BSG \u201804", hint_year=2004) == ("BSG", 2004)

    def test_empty_input(self) -> None:
        assert extract_year_tag("") == ("", None)
        assert extract_year_tag("", hint_year=2020) == ("", 2020)

    def test_year_with_trailing_whitespace(self) -> None:
        assert extract_year_tag("Dune (2021)   ") == ("Dune", 2021)

    def test_does_not_strip_year_when_alone(self) -> None:
        # Stripping "1987" off "1987" would leave an empty title; we keep the
        # original to avoid blank-query lookups.
        clean, year = extract_year_tag("1987")
        assert year == 1987
        assert clean == "1987"


class TestIsAcronymOrSubstringMatch:
    def test_acronym_initials(self) -> None:
        assert is_acronym_or_substring_match("TMNT", "Teenage Mutant Ninja Turtles")
        assert is_acronym_or_substring_match("LOTR", "The Lord of the Rings")
        assert is_acronym_or_substring_match("MCU", "Marvel Cinematic Universe")
        assert is_acronym_or_substring_match("GOT", "Game of Thrones")

    def test_acronym_case_insensitive(self) -> None:
        assert is_acronym_or_substring_match("tmnt", "Teenage Mutant Ninja Turtles")
        assert is_acronym_or_substring_match("TMNT", "teenage mutant ninja turtles")

    def test_exact_match(self) -> None:
        assert is_acronym_or_substring_match("Dune", "Dune")

    def test_substring(self) -> None:
        assert is_acronym_or_substring_match("Dune", "Dune: Part Two")
        assert is_acronym_or_substring_match("Office", "The Office (US)")

    def test_token_overlap(self) -> None:
        # "Bad Breaking" — token overlap with "Breaking Bad" is 100%
        assert is_acronym_or_substring_match("Bad Breaking", "Breaking Bad")

    def test_partial_acronym_in_initials(self) -> None:
        # Allow "BSG" in "Battlestar Galactica" (initials = "bg") — should NOT match,
        # but "TMNT" in "Teenage Mutant Ninja Turtles" (initials = "tmnt") should.
        assert is_acronym_or_substring_match("TMNT", "Teenage Mutant Ninja Turtles")
        assert not is_acronym_or_substring_match("BSG", "Battlestar Galactica")

    def test_no_match(self) -> None:
        assert not is_acronym_or_substring_match("Dune", "Foundation")
        assert not is_acronym_or_substring_match("XYZ", "The Office")

    def test_empty_inputs(self) -> None:
        assert not is_acronym_or_substring_match("", "Dune")
        assert not is_acronym_or_substring_match("Dune", "")

    def test_short_query_in_longer_initials(self) -> None:
        # Initials of "Star Trek: The Next Generation" = "sttng".
        # "stng" or "sttn" should NOT match (would over-match). "sttng" should.
        assert is_acronym_or_substring_match("STTNG", "Star Trek: The Next Generation")
        assert is_acronym_or_substring_match("sttng", "Star Trek: The Next Generation")

    def test_majority_token_overlap_threshold(self) -> None:
        # 1 of 1 query tokens in target — passes
        assert is_acronym_or_substring_match("breaking", "Breaking Bad")
        # 2 of 4 query tokens — fails the majority threshold (needs floor(4/2)+1 = 3)
        assert not is_acronym_or_substring_match("completely different unrelated query", "completely something else here")


class TestLooksLikeAcronym:
    def test_short_no_space(self) -> None:
        assert looks_like_acronym("TMNT")
        assert looks_like_acronym("LOTR")
        assert looks_like_acronym("MCU")
        assert looks_like_acronym("GOT")

    def test_lowercase_short_no_space(self) -> None:
        # Lowercase short words pass — the agent may emit them.
        assert looks_like_acronym("tmnt")

    def test_with_space_rejected(self) -> None:
        assert not looks_like_acronym("the office")
        assert not looks_like_acronym("LOTR fellowship")

    def test_too_long_rejected(self) -> None:
        assert not looks_like_acronym("Foundation")

    def test_empty_rejected(self) -> None:
        assert not looks_like_acronym("")
        assert not looks_like_acronym("    ")

    def test_numeric_rejected(self) -> None:
        # No alphabetic chars — not a candidate acronym
        assert not looks_like_acronym("1234")
