"""Fuzzy match helpers."""

from __future__ import annotations

from arr_stack_mcp.fuzzy import best_matches, normalize, title_contains, tokens


class TestNormalize:
    def test_lowercases(self) -> None:
        assert normalize("Foo BAR") == "foo bar"

    def test_drops_leading_article(self) -> None:
        assert normalize("The Office") == "office"
        assert normalize("A Series of Unfortunate Events") == "series of unfortunate events"
        assert normalize("An Idea") == "idea"

    def test_does_not_drop_article_mid_string(self) -> None:
        assert normalize("Once Upon a Time") == "once upon a time"

    def test_collapses_punctuation(self) -> None:
        assert normalize("Mr. Robot") == "mr robot"
        assert normalize("Foo-Bar_Baz!") == "foo bar baz"

    def test_empty_string_yields_empty(self) -> None:
        assert normalize("") == ""


class TestTitleContains:
    def test_substring(self) -> None:
        assert title_contains("The Office (US) (2005)", "the office")
        assert title_contains("The Office (US)", "office")

    def test_no_match(self) -> None:
        assert not title_contains("Breaking Bad", "the office")


class TestTokens:
    def test_returns_set(self) -> None:
        assert tokens("The Office US") == {"office", "us"}


class TestBestMatches:
    def test_finds_strong_match(self) -> None:
        results = best_matches("Dune", ["Dune (2021)", "Dune: Part Two", "Foundation"])
        assert len(results) == 2
        assert all(r.score >= 70.0 for r in results)

    def test_threshold_filters_weak_matches(self) -> None:
        results = best_matches("Dune", ["Foundation"], threshold=70.0)
        assert results == []

    def test_empty_candidates(self) -> None:
        assert best_matches("Dune", []) == []

    def test_token_set_handles_word_order(self) -> None:
        results = best_matches("Bad Breaking", ["Breaking Bad"])
        assert len(results) == 1
