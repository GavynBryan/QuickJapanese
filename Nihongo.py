#! /usr/bin/python3

import sys
import urllib.request, json
from urllib.parse import quote


English = sys.argv[len(sys.argv) - 1]
English = quote(English)

words = []
with urllib.request.urlopen("https://jisho.org/api/v1/search/words?keyword=" + English) as url:
    data = json.loads(url.read().decode())
    words = data["data"]


# converts a bool into yes or no
def y_or_n(sbool):
    if sbool is True:
        return "Yes"
    else:
        return "No"


for word in words:
    # this is just how Jisho has their JSON organized. No bully, plz
    japanese = word["japanese"][0]
    senses = word["senses"][0]

    slug = word.get("slug")
    reading = japanese.get("reading")
    definition = senses.get("english_definitions")

    # only show valid results
    if slug and reading:
        print(f"{slug}  ({reading}) - {definition}")
        if word.get("is_common"):
            print("Common Word?: ", y_or_n(word["is_common"]))


