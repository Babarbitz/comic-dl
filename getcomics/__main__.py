#!/usr/bin/env python3


# Libraries
from bs4 import BeautifulSoup

# from os import path
# from tqdm import tqdm


# import json
import requests
import sys
import textwrap

# import urllib.parse

# import logging as log
# import yaml


def search(search_term: str) -> list[dict]:
    # Encode search term for proper url usage
    normalized_search_term = search_term.replace(" ", "%20")

    # Grab list of results
    url = "https://getcomics.org/?s=" + normalized_search_term
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    search = soup.find("div", class_="post-list-posts")

    try:
        results = []
        posts = search.find_all("article", class_="post")

        for post in posts:
            # Get relavent divs for parsing
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

                results.append(
                    {
                        "title": title,
                        "link": link,
                        "date": date,
                        "year": year,
                        "size": size,
                        "desc": desc,
                    }
                )

        return results
    except AttributeError:
        print(f"No results for search term {search_term}")


def download(result: dict) -> None:
    # Get the dl url to scrape for the download link
    page = requests.get(result["link"])
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.find("section", class_="post-contents")

    # Figure out the download url. There are currently 3 know types
    # 1. All-in-one download button which can be found via aio-read
    # 2. Mutliple urls for downloading parts of a full download:
    # https://getcomics.org/other-comics/scott-pilgrim-vol-1-6-color-edition/
    # 3. Prioritize segmented downloads if both available
    table = content.find_all("li")

    urls = []
    for item in table:
        # print(item)
        entries = item.find_all("a")
        for entry in entries:
            if "Main Server" in item.text:
                urls.append
            print(entry)

            # urls.append(url)

    # If no segmented downloads are available then
    # default to single download link
    if not urls:
        url = content.find("a", class_="aio-red")["href"]
        urls.append(url)


# for url in urls:
#     # Determine filename and filepath
#     filename = urllib.parse.unquote(url.split("/")[-1])
#     filepath = path.expanduser("~") + "/Downloads/"

#     # # Download the file via stream and display progress in cli
#     print(f"Downloading {filename}")

#     r = requests.get(url, stream=True)
#     total_size_in_bytes= int(r.headers.get('content-length', 0))
#     progress_bar = tqdm(total=total_size_in_bytes,unit='iB',unit_scale=True)

#     with open(filepath + filename, 'wb') as file:
#         for data in r.iter_content(1024):
#             progress_bar.update(len(data))
#             file.write(data)
#     progress_bar.close()

#     if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
#         print("ERROR, something went wrong")


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


def print_results(results: list[dict]) -> None:
    for idx, result in enumerate(results):
        print(
            textwrap.dedent(
                f"""\
    {idx+1}) {result["title"]}
    desc: {result["desc"]}
    year: {result["year"]} | size: {result["size"]} | posted: {result["date"]}
            """
            )
        )


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


###############################################################################

# When python is called on a folder, it looks for __main__.py and triggers this
# Relative base of the repo that would look like:
#   python comic-dl/
if __name__ == "__main__":
    for idx, flag in enumerate(sys.argv):
        if flag == "-h" or flag == "--help":
            print_help()
            break
        if flag == "-s" or flag == "--search":
            # Ensures CLI arg for search term is a single string
            search_term = " ".join(str(item) for item in sys.argv[idx + 1 :])
            results = search(search_term)
            if results:
                print_results(results)
        if flag == "-d" or flag == "--download":
            search_term = " ".join(str(item) for item in sys.argv[idx + 1 :])
            results = search(search_term)
            if results:
                print_results(results)
                choice = select_item(len(results))
                download(results[choice - 1])
