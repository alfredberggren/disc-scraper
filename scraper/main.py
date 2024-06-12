"""
Entrypoint of the scraper. 
"""
import time
import random
import crud
import warnings
from html_parser import DiscParser, UnparseableHTMLException

disc_parser = DiscParser()

def collect_manufacturer_urls():
    """
    Collects various url's for disc golf manufacturers, currently only supports one retailer.
    These url's are used to extract url's to individual discs.
    """
    return disc_parser.collect_urls("https://disctorget.se/", "/marken/.*")

def collect_disc_urls(base_url: str):
    """
    Collects url's to potential discs for sale.
    These url's are later parsed
    """
    return disc_parser.collect_urls(base_url, "/discar/.*")

def main():
    """
    The main controller of the scraper.
    """
    manufacturer_urls = collect_manufacturer_urls()
    disc_urls = set()
    for m_url in manufacturer_urls:
        d_urls = collect_disc_urls(m_url)
        for d_url in d_urls:
            disc_urls.add(d_url)
        # Sleeps for a random amount of time inbetween downloads to avoid pattern detection
        time.sleep(random.choice(range(500, 1500))/1000)

    discs = set()
    for url in disc_urls:
        found_disc = None
        try:
            found_disc = disc_parser.get_disc_from_url(url)
        except UnparseableHTMLException as e:
            # Warn when a disc could not be parsed for whatever reason.
            warnings.warn(message=e.message, category=RuntimeWarning)
        print(f"found disc {found_disc.mold_name} from url: {url}")
        discs.add(found_disc)
        time.sleep(random.choice(range(500, 1500))/1000)

    crud.insert_discs(discs)

if __name__ == "__main__":
    main()

