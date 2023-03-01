import random


class URLShortener:
    def __init__(self):
        self.url_dict = {}

    # method to generate code
    def generate_code(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        return "".join(random.choice(letters + digits) for _ in range(6))

    # method to shorten url
    def shorten_url(self, url):
        code = self.generate_code()
        if code not in self.url_dict:
            self.url_dict[code] = url
            return f"short.ly/{code}"
        else:
            return self.shorten_url(url)

    # method to expand url
    def expand_url(self, code):
        if code in self.url_dict:
            return self.url_dict[code]
        else:
            return None


# create an object of URLShortener class

shortener = URLShortener()
shortened_url = shortener.shorten_url("https://www.google.com")
print(shortened_url)
original_url = shortener.expand_url(shortened_url.split("/")[-1])
print(original_url)
