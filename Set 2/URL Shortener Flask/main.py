import random
from flask import Flask, redirect, request, make_response

# create a class for the URL shortener


class URLShortener:
    def __init__(self):
        self.url_dict = {}
        self.app = Flask(__name__)

        self.app.add_url_rule(
            '/<code>', 'redirect_to_url', self.redirect_to_url)

    def redirect_to_url(self, code):
        url = self.url_dict.get(code)
        if url:
            return redirect(url)
        else:
            return make_response(f"Invalid short URL code: {code}", 404)

    # method to generate a random code
    def generate_code(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        return "".join(random.choice(letters + digits) for i in range(6))

    # method to shorten the url
    def shorten_url(self, url):
        code = self.generate_code()
        if code not in self.url_dict:
            self.url_dict[code] = url
            return f"http://127.0.0.1:5000/{code}"
        else:
            return self.shorten_url(url)

    # method to start the server
    def start_server(self):
        self.app.run()

    # method to close the server

    def stop_server(self):
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()

# creating objects of the class


shortener = URLShortener()
shortener.start_server()

shortened_url = shortener.shorten_url(
    "https://github.com/sanju50201?tab=repositories")

print(shortened_url)


# stop the server

shortener.stop_server()
