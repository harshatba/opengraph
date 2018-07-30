import re
import requests
from bs4 import BeautifulSoup
from urllib import urlopen

class OpenGraph:
    url = None
    tags = dict()

    def __init__(self, url):
        self.url = url
        self.tags['url'] = url

    def retrieve_tags(self):
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
        page_data = requests.get(self.url, headers=headers).text
        soup = BeautifulSoup(page_data, "lxml")
        all_og_tags = soup.find_all('meta', {'property': re.compile(r'og\:')})
        for og_tag_obj in all_og_tags:
            tag_property = og_tag_obj.get('property')
            tag_property = tag_property.replace('og:', '')
            self.tags[tag_property] = og_tag_obj.get('content')

        return self.tags
