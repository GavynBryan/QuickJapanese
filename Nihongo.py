#! /usr/bin/python3

import sys
import urllib.request, json
from urllib.parse import quote


app_parameter = sys.argv[len(sys.argv) - 1]
api_url = "https://jisho.org/api/v1/search/words?keyword="


# converts a bool into yes or no
def y_or_n(sbool):
    if sbool is True:
        return "Yes"
    else:
        return "No"


def lookup(phrase):
    phrase = quote(phrase)
    words = []
    with urllib.request.urlopen(api_url + phrase) as url:
        data = json.loads(url.read().decode())
        words = data["data"]

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


if app_parameter == sys.argv[0]:
    finished = False
    while not finished:
        m_input = input("\nEnter word or type !quit to cancel: ")
        if m_input != "!quit":
            lookup(m_input)
        else:
            finished = True
else:
    lookup(app_parameter)
