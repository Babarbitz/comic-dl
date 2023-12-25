#!/usr/bin/env python3


from __future__ import annotations

import sys
import textwrap

from download import download, parseDownloadPage
from search import search

# import logging as log
# import yaml


def select_item(items: int) -> int:
    while True:
        choice = input(f"Select a result between 1 and {items}: ")
        try:
            choice = int(choice)
            if int(choice) < 1 or int(choice) > items:
                pass
            else:
                break
        except ValueError:
            print("Invalid selection")

    return choice


def input_range() -> list:
    while True:
        entry = input("Select all items to download (1-x,y,z): ")
        try:
            entries = parseRangeString(entry)
            if not isinstance(entries, list):
                pass
            else:
                return entries
        except ValueError:
            print("Invalid selection")


def parseRangeString(x):
    result = []
    for part in x.split(","):
        if "-" in part:
            a, b = part.split("-")
            a, b = int(a) - 1, int(b) - 1
            result.extend(range(a, b + 1))
        else:
            a = int(part) - 1
            result.append(a)
    return result


def print_search_results(results: list[dict]) -> None:
    for idx, result in enumerate(results["data"]):
        print(
            textwrap.dedent(
                f"""\
            {idx+1}) {result["title"]}
            {result["desc"]}
            {result["year"]} | {result["size"]} | {result["date"]}
        """
            )
        )
    print(
        textwrap.dedent(
            f"""\
        page: {results["pages"]["current"]} of {results["pages"]["last"]}
    """
        )
    )


def print_download_results(results: list[dict]) -> None:
    for idx, item in enumerate(results):
        print(f"{idx+1}) {item['title']}")


def print_help() -> None:
    print(
        textwrap.dedent(
            """\
        Usage: comic-dl [OPTION]... [SEARCH TERM]...
        Search or download comics from: https://getcomics.org/

          -h, --help           display this help screen
          -s, --search         search and display results
          -d, --download       search and download a result
     """
        )
    )


def cli_run() -> None:
    for idx, flag in enumerate(sys.argv):
        if flag == "-h" or flag == "--help":
            print_help()
            break
        if flag == "-s" or flag == "--search":
            # Ensures CLI arg for search term is a single string
            search_term = " ".join(str(item) for item in sys.argv[idx + 1 :])
            results = search(search_term)
            if results:
                print_search_results(results)
        if flag == "-d" or flag == "--download":
            url = sys.argv[idx + 1]
            # search_term = " ".join(str(item) for item in sys.argv[idx + 1 :])
            # results = search(search_term)
            # if results:
            # print_results(results)
            # choice = select_item(len(results["data"]))
            # download(results["data"][choice - 1]["link"])
            # parseDownloadPage(url)
            results = parseDownloadPage(url)
            print_download_results(results)
            items = input_range()
            downloads = [results[i] for i in items]
            download(downloads)


###############################################################################

# When python is called on a folder, it looks for __main__.py and triggers this
# Relative base of the repo that would look like:
#   python comic-dl/


if __name__ == "__main__":
    cli_run()
