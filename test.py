#!/usr/bin/env python3

from bs4 import BeautifulSoup
from os import path
from tqdm import tqdm
import json
import requests
import sys
import textwrap
import urllib.parse


page = requests.get("https://mega.nz/file/aLZCjQBY#cnbFpFNT_uJ1the1JsPvt2-UrmvQzQgZd44JRrxJ9mE")
soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())
