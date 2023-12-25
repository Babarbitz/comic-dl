#!/usr/bin/env python3


from __future__ import annotations

import urllib.parse
from os import path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def download(downloads: list) -> None:
    for item in downloads:
        links = item["links"]
        if "main server" in links:
            downloadMainServer(links["main server"])
        elif "download now" in links:
            downloadMainServer(links["download now"])
        elif "mediafire" in links:
            pass
        elif "mega" in links:
            pass
        else:
            pass


def parseDownloadPage(url: str) -> dict:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.find("section", class_="post-contents")
    results = None

    table = content.find_all("li")
    results = []

    split_items = parseListItems(table)
    button_items = parseDownloadButtons(content)

    if split_items:
        results = results + split_items
    if button_items:
        results = results + button_items

    return results


# def parseMultiFormatPage(soup: BeautifulSoup) -> dict:
#     results = { }
#     for form in soup:
#         format_type = form.text.casefold()
#         items = {}
#         for tag in form.next_siblings:
#             if tag.name == "h3": break
#             if tag.name != "ul": continue
#             posts = tag.find_all("li")
#             items.update(parseListItems(posts))
#         results[format_type] = items

#     if results["regular issues"]: return results["regular issues"]
#     elif results["trades"]: return results["trades"]
#     elif results["omnibuses"]: return results["omnibuses"]
#     else: return results


def parseListItems(soup: BeautifulSoup) -> dict:
    results = []
    dl_types = ["main server", "mega", "mediafire"]
    for post in soup:
        title = post.text.split(":")[0].strip()
        links = {}
        for link in post.find_all("a"):
            key = link.text.casefold().strip()
            if key not in dl_types:
                continue
            try:
                links[key] = link["href"]
            except KeyError:
                pass
        if links:
            results.append({"title": title, "links": links})

    if results:
        return results
    else:
        return None


def parseDownloadButtons(soup: BeautifulSoup) -> dict:
    results = []
    dl_types = ["download now", "mega", "mediafire"]
    title = soup.find("h2").text
    links = {}
    for button in soup.find_all("div", class_="aio-pulse"):
        if not button.find("a"):
            continue
        key = button.text.casefold().strip()
        if key not in dl_types:
            continue
        links[key] = button.find("a")["href"]
    if links:
        results.append({"title": title, "links": links})

    if results:
        return results
    else:
        return None


def downloadMainServer(url: str) -> None:
    print(url)
    # Determine filename and filepath
    filename = urllib.parse.unquote(url.split("/")[-1])
    filepath = path.expanduser("~") + "/Downloads/"
    print(filename)
    print(filepath)

    # Download the file via stream and display progress in cli
    print(f"Downloading {filename}")

    r = requests.get(url, stream=True)
    total_size_in_bytes = int(r.headers.get("content-length", 0))
    progress_bar = tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True)

    with open(filepath + filename, "wb") as file:
        for data in r.iter_content(1024):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
