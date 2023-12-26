#!/usr/bin/env python3


from __future__ import annotations

import urllib.parse

import requests
from bs4 import BeautifulSoup


def search(search_term: str, page_number: int = 1) -> list[dict]:
    url = _makeSearchUrl(search_term, page_number)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = {}

    try:
        results["data"] = parseSearchResults(soup)
        last_page_number = parseLastPageNumber(soup)
        results["pages"] = _makePaginationDict(page_number, last_page_number)
    except AttributeError:
        print(f"No results for search term {search_term}")

    return results


def parseSearchResults(soup: BeautifulSoup) -> list[dict]:
    posts = soup.find_all("article", class_="post")
    results = []

    for post in posts:
        title_div = post.find("h1", class_="post-title")
        content_div = post.find("p", class_="post-excerpt")
        description_text = content_div.find("p").text

        # Remove child p from content div to extract post description
        for child in content_div.find_all("p"):
            child.decompose()

        title = title_div.text
        link = title_div.find("a")["href"]
        date = post.find("time")["datetime"]
        desc = content_div.text
        year = description_text.split("|")[0].split(":")[1].strip()
        size = description_text.split("|")[1].split(":")[1].strip()

        results.append(_makeResultDict(title, link, date, year, size, desc))

    return results


def parseLastPageNumber(soup: BeautifulSoup) -> int:
    pages = soup.find("ul", class_="page-numbers")
    if pages:
        last = pages.find_all("li")[-1]
        return int(last.text) if last.text else 1
    else:
        return 1


def _makePaginationDict(current: int, last: int) -> dict:
    if current <= 0:
        current = 1

    if last <= 0:
        last = 1

    return {
        "first": 1,
        "current": current,
        "last": last,
        "next": current + 1 if current + 1 <= last else last,
        "prev": current - 1 if current - 1 > 0 else 1,
    }


def _makeSearchUrl(search: str, page: int = None) -> str:
    encoded_search = urllib.parse.quote(search)
    if page:
        return f"https://getcomics.org/page/{page}/?s={encoded_search}"
    else:
        return f"https://getcomics.org/?s={encoded_search}"


def _makeResultDict(
    title: str, link: str, date: str, year: str, size: str, desc: str
) -> dict:
    return {
        "title": title,
        "link": link,
        "date": date,
        "year": year,
        "size": size,
        "desc": desc,
    }
