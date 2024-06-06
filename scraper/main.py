from html_parser import DiscParser

disc_parser = DiscParser()

def main():
    # manufacturer_urls = collect_manufacturer_urls()
    # disc_urls = set()
    # for m_url in manufacturer_urls:
    #     d_urls = collect_disc_urls(m_url)
    #     for d_url in d_urls:
    #         disc_urls.add(d_url)
    #
    # discs = set()
    # for url in disc_urls:
    #     discs.add(disc_parser.get_disc_from_url(url))
    url = "https://disctorget.se/discar/35-magician-active-6"
    disc_parser.get_disc_from_url(url)

if __name__ == "__main__":
    main()

def collect_manufacturer_urls():
    return disc_parser.collect_urls("https://disctorget.se/", "/marken/.*")

def collect_disc_urls(base_url: str):
    return disc_parser.collect_urls(base_url, "/discar/.*")


