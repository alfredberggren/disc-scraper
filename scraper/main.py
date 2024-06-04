import requests
import json
import re
from bs4 import BeautifulSoup

def test():
    # response = requests.get("https://disctorget.se/discar/photon-proton-7")
    with open("/home/alfred/temp.txt", "r") as temp:
        data = temp.read()
    match = re.search("JSON\\.parse\\('(.*)'\\)", data)
    obj = json.loads(match.group(1))
    print(obj["items"][0]["price"])

def get_html(url: str) -> str:
    """
    Gets html content of a url
    """

    return requests.get(url).text

def collect_disc_urls(base_url: str) -> set[str]:
    """
    Collects URL's under the /discar endpoint
    """

    base_document = get_html(base_url)
    soup = BeautifulSoup(base_document, 'html.parser')
    disc_urls = set()
    for link in soup.find_all('a'):
        url = link.get('href')
        if re.match("/discar/.*", url):
            disc_urls.add(f"https://disctorget.se{url}")
    return disc_urls


collect_disc_urls("https://disctorget.se/marken/latitude-64")
