#!/usr/bin/env python3

from __future__ import annotations

from getcomics.search import _makeResultDict, _makeSearchUrl


class TestSearchUnit:
    def setup_method(self, method):
        self.title = "test title"
        self.link = "test link"
        self.date = "test date"
        self.desc = "test description"
        self.year = "20xx"
        self.size = "0 Mb"
        self.search = "Spider-Man"

    def test_makeResultDict(self):
        result = _makeResultDict(
            self.title, self.link, self.date, self.year, self.size, self.desc
        )

        assert result["title"] and result["title"] == "test title"
        assert result["link"] and result["link"] == "test link"
        assert result["date"] and result["date"] == "test date"
        assert result["desc"] and result["desc"] == "test description"
        assert result["year"] and result["year"] == "20xx"
        assert result["size"] and result["size"] == "0 Mb"

    def test_makeSearchUrl(self):
        page = _makeSearchUrl(self.search, 2)
        no_page = _makeSearchUrl(self.search)

        assert page and page == "https://getcomics.org/page/2/?s=Spider-Man"
        assert no_page and no_page == "https://getcomics.org/?s=Spider-Man"


class TestSearchIntegration:
    def setup_method(self, method):
        pass
