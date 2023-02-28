import requests
from bs4 import BeautifulSoup, UnicodeDammit


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    # method to get data
    def fetch_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content

    # method to parse data
    def parse_data(self, html):
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        # Extract data here using soup.find() and soup.select()
        return soup
    # method to save data

    def save_data(self, data):
        # save the data to a file or database
        with open("data.txt", "w") as f:
            f.write(str(data))
        # method to run the scraper

    def scrape(self):
        html = self.fetch_data()
        soup = self.parse_data(html)
        data = self.parse_data(soup)
        self.save_data(data)


scrapper = WebScraper("https://www.google.com")
scrapper.scrape()
