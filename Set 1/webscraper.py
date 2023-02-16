import requests
from bs4 import BeautifulSoup


# define a class for the scraper


class Scraper:
    def __init__(self, url):
        self.url = url
        self.html_content = None
        self.soup = None

    # fucntion to fetch the content
    def fetch_content(self):
        response = requests.get(self.url)
        self.html_content = response.content

    # function to parse the content
    def parse_content(self):
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    # function to find elements
    def find_elements(self, element, attrs):
        return self.soup.find_all(element, attrs)


# creating objects of the scraper class

url = "https://www.bbc.com/news"
scraper = Scraper(url)
scraper.fetch_content()
scraper.parse_content()
articles = scraper.find_elements('a', {'class': 'gs-c-promo-heading'})


for article in articles:
    title = article.get_text().strip()
    link = article.get('href')
    print(f"Title: {title}\n Link: ({link})")
