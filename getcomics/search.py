#!/usr/bin/env python3


from __future__ import annotations

import urllib.parse

import requests
from bs4 import BeautifulSoup


def search(search_term: str, page: int = None) -> list[dict]:
    url = _makeSearchUrl(search_term, page)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    search = soup.find("div", class_="post-list-posts")

    try:
        results = []
        posts = search.find_all("article", class_="post")

        for post in posts:
            title_div = post.find("h1", class_="post-title")
            content_div = post.find("p", class_="post-excerpt")
            description_text = content_div.find("p").text

            # Remove child p from content div to extract post description
            for child in content_div.find_all("p"):
                child.decompose()

            # Parse html data into fields we can use
            title = title_div.text
            link = title_div.find("a")["href"]
            date = post.find("time")["datetime"]
            desc = content_div.text
            year = description_text.split("|")[0].split(":")[1].strip()
            size = description_text.split("|")[1].split(":")[1].strip()

            result = _makeResultDict(title, link, date, year, size, desc)

            results.append(result)

        return results
    except AttributeError:
        print(f"No results for search term {search_term}")


def _makeSearchUrl(search: str, page: int = None):
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
