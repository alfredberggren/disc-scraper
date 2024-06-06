"""
HTML parsing
"""

import requests
import json
import re
from bs4 import BeautifulSoup

def init_recognized_plastics():
    base_document = get_html("https://discsport.se/discgolf/guider/om-plast")
    soup = BeautifulSoup(base_document, "html.parser")

    recognized_plastics = set()
    for link in soup.find_all("a"):
        if link.has_attr("href"):
            url = link.get("href")
        else:
            continue
        plastic = re.search("https://discsport.se/plast/\\w*/(.*)", url)
        if plastic:
            recognized_plastics.add(plastic.group(1))

    return recognized_plastics

def get_html(url: str) -> str:
    """
    Gets html content of a url
    """

    return requests.get(url).text


class DiscParser:
    def __init__(self):
        self.recognized_plastics = init_recognized_plastics() 
        self.recognized_molds = init_recognized_molds()
    # TODO: get list of plastics from https://discsport.se/discgolf/guider/om-plast#list-plastic
    # TODO: get list of molds (?)
    # def test():
    #     response = requests.get("https://disctorget.se/discar/photon-proton-7")
    #     with open("/home/alfred/temp.txt", "r") as temp:
    #         data = temp.read()
    #     match = re.search("JSON\\.parse\\('(.*)'\\)", data)
    #     obj = json.loads(match.group(1))
    #     print(obj["items"][0]["price"])
    def collect_urls(base_url: str, pattern: str) -> set[str]:
        """
        Collects URL's under the base url
        """

        base_document = get_html(base_url)
        soup = BeautifulSoup(base_document, "html.parser")
        urls = set()
        for link in soup.find_all("a"):
            url = link.get("href")
            if re.match(pattern, url):
                print(url)
                urls.add(f"https://disctorget.se{url}")
        return urls

    def get_disc_from_url(url: str):
        base_document = get_html(url)
        soup = BeautifulSoup(base_document, "html.parser")

        # TODO: get mold name

        # TODO: get plastic name

        # TODO: get price


