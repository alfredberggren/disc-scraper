"""
HTML parsing
"""

from disc import Disc
import re

import requests
from bs4 import BeautifulSoup

import plastics


def init_recognized_plastics():
    base_document = get_html("https://discsport.se/discgolf/guider/om-plast")
    soup = BeautifulSoup(base_document, "html.parser")

    recognized_plastics = set()
    for link in soup.find_all("a"):
        if link.has_attr("href"):
            url = link.get("href")
        else:
            continue
        plastic = re.search("https://discsport.se/plast/(.*)", url)
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
        self.recognized_plastics = plastics.PLASTICS

    def collect_urls(self, base_url: str, pattern: str) -> set[str]:
        """
        Collects URL's under the base url
        """

        base_document = get_html(base_url)
        soup = BeautifulSoup(base_document, "html.parser")
        urls = set()
        for link in soup.find_all("a"):
            url = link.get("href")
            if re.match(pattern, url):
                urls.add(f"https://disctorget.se{url}")
        return urls

    def get_disc_from_url(self, url: str):
        base_document = get_html(url)
        soup = BeautifulSoup(base_document, "html.parser")

        price: int = 0

        for c in soup.find_all("meta"):
            if c.get("property") == "og:title" and c.get("content") != "Disctorget":
                title = c.get("content")
            if c.get("itemprop") == "price":
                price = int(c.get("content"))
        title = re.search("(.*) - Disctorget", title).group(1).replace(" ", "-").lower()

        if price == 0:
            return None

        manufacturer = ""
        plastic_name = ""
        mold_name = ""
        for p in self.recognized_plastics:
            p_vars = plastics.variations(p)
            if p_vars is None:
                continue
            for var in p_vars:
                p_match = re.match(f"(.*)-{var}.*", title)
                if p_match:
                    p = p.split("/")
                    manufacturer = p[0]
                    plastic_name = p[1]
                    mold_name = p_match.group(1)

        return Disc(
            mold_name=mold_name,
            plastic=plastic_name,
            manufacturer=manufacturer,
            price=price,
            url=url,
        )
