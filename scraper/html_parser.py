"""
HTML parsing
"""

from disc import Disc
import re

import requests
from bs4 import BeautifulSoup

import plastics


class UnparseableHTMLException(Exception):
    def __init__(self, message, url):
        self.url = url
        self.message = f"Failed to parse HTML document for url:\n\t{self.url}\n{message}"
        super().__init__(self.message)


def fetch_price(url: str):
    base_document = get_html(url)
    soup = BeautifulSoup(base_document, "html.parser")

    price: int = 0

    for c in soup.find_all("meta"):
        if c.get("itemprop") == "price":
            price = int(c.get("content"))

    if price == 0:
        raise UnparseableHTMLException(message="Could not find price", url=url)
    return price


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
            raise UnparseableHTMLException(message="Could not find price", url=url)

        manufacturer = ""
        plastic_name = ""
        mold_name = ""
        for p in self.recognized_plastics:
            p_vars = plastics.variations(p)
            if p_vars is None:
                continue
            for var in p_vars:
                # TODO: fix bug, if var == 's' (from any s-line), anything beginning with s matches
                p_match = re.match(f"(.*)-{var}.*", title)
                if p_match:
                    p1 = p.split("/")
                    manufacturer = p1[0]
                    plastic_name = p1[1].split(";")[0]
                    mold_name = p_match.group(1)

        if len(plastic_name) == 0: 
            raise UnparseableHTMLException(message="Could not find plastic name", url=url)
        if len(manufacturer) == 0:
            raise UnparseableHTMLException(message="Could not find manufacturer name", url=url)
        if len(mold_name) == 0:
            raise UnparseableHTMLException(message="Could not find mold name", url=url)


        return Disc(
            mold_name=mold_name,
            plastic=plastic_name,
            manufacturer=manufacturer,
            price=price,
            url=url,
        )
