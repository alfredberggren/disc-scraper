import time
import random
import crud
from html_parser import DiscParser

disc_parser = DiscParser()

def collect_manufacturer_urls():
    return disc_parser.collect_urls("https://disctorget.se/", "/marken/.*")

def collect_disc_urls(base_url: str):
    return disc_parser.collect_urls(base_url, "/discar/.*")

def main():
    manufacturer_urls = collect_manufacturer_urls()
    disc_urls = set()
    for m_url in manufacturer_urls:
        d_urls = collect_disc_urls(m_url)
        for d_url in d_urls:
            disc_urls.add(d_url)
        time.sleep(random.choice(range(500, 1500))/1000)

    discs = set()
    for url in disc_urls:
        found_disc = disc_parser.get_disc_from_url(url)
        if found_disc is None:
            continue
        discs.add(found_disc)
        time.sleep(random.choice(range(500, 1500))/1000)

    crud.insert_discs(discs)

if __name__ == "__main__":
    main()

