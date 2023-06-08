import random
import string

class URLShortener:
    def __init__(self):
        self.urls = {}
        
    def shorten_url(self, original_url):
        # generate a random string of 6 characters
        letters = string.ascii_lowercase + string.ascii_uppercase
        short_url = ''.join(random.choice(letters) for i in range(6))
        
        # store the original URL and its shortened version in a dictionary
        self.urls[short_url] = original_url
        
        # return the shortened URL
        return "http://localhost:8000/" + short_url
    
    def original_url(self, short_url):
        # retrieve the original URL from the dictionary
        return self.urls.get(short_url, None)
