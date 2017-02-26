import urllib.request
import urllib.error
from functools import lru_cache


@lru_cache(maxsize=30)
def get_webpage(section):
    web_page = "http://redesign.swahilipothub.co.ke/{}".format(section)
    try:
        with urllib.request.urlopen(web_page) as request:
            return request.read()
    except urllib.error.HTTPError:
        return None


if __name__ == '__main__':
    sections = ['about', 'contact', 'statups']
    for section in sections:
        page = get_webpage(section)
        if page:
            print("{} section page found".format(section))
