#!/usr/bin/env python3

from __future__ import annotations

import getcomics.search as search


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
        result = search._makeResultDict(
            self.title, self.link, self.date, self.year, self.size, self.desc
        )
        assert result["title"] and result["title"] == "test title"
        assert result["link"] and result["link"] == "test link"
        assert result["date"] and result["date"] == "test date"
        assert result["desc"] and result["desc"] == "test description"
        assert result["year"] and result["year"] == "20xx"
        assert result["size"] and result["size"] == "0 Mb"

    def test_makePaginationDict(self):
        result = search._makePaginationDict(0, 0)
        assert result["first"] and result["first"] == 1
        assert result["current"] and result["current"] == 1
        assert result["last"] and result["last"] == 1
        assert result["next"] and result["next"] == 1
        assert result["prev"] and result["prev"] == 1
        result = search._makePaginationDict(1, 1)
        assert result["first"] and result["first"] == 1
        assert result["current"] and result["current"] == 1
        assert result["last"] and result["last"] == 1
        assert result["next"] and result["next"] == 1
        assert result["prev"] and result["prev"] == 1
        result = search._makePaginationDict(5, 20)
        assert result["first"] and result["first"] == 1
        assert result["current"] and result["current"] == 5
        assert result["last"] and result["last"] == 20
        assert result["next"] and result["next"] == 6
        assert result["prev"] and result["prev"] == 4
        result = search._makePaginationDict(20, 20)
        assert result["first"] and result["first"] == 1
        assert result["current"] and result["current"] == 20
        assert result["last"] and result["last"] == 20
        assert result["next"] and result["next"] == 20
        assert result["prev"] and result["prev"] == 19

    def test_makeSearchUrl(self):
        page = search._makeSearchUrl(self.search, 2)
        no_page = search._makeSearchUrl(self.search)

        assert page and page == "https://getcomics.org/page/2/?s=Spider-Man"
        assert no_page and no_page == "https://getcomics.org/?s=Spider-Man"


class TestSearchIntegration:
    def setup_method(self, method):
        pass
