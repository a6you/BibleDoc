import re
import requests
from bs4 import BeautifulSoup
import urllib.parse

def BGWRequests(reference, version):
    quoted_reference = urllib.parse.quote(reference)
    quoted_version = urllib.parse.quote(version)
    query = f'https://www.biblegateway.com/passage/?search={quoted_reference}&version={quoted_version}'
    page = requests.get(query)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.findAll('span', {'class': 'text'})

    full_text = ''
    for i in range(5, len(result)):
        text = result[i].text
        # Remove letters indicating parts that are parenthesized
        # i.e. Remove (A), (B), and (C) from the following:
        # 20 And God said, “Let the water teem with living creatures,(A) 
        # and let birds fly above the earth across the vault of the sky.”(B) 
        # 21 So God created(C)
        text = re.sub(r'\([A-Z]+\)\s+', ' ', text)
        text = re.sub(r'\([A-Z]+\)\s*', '', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\[[a-z]+\]', '', text)
        full_text = full_text + '\n' + text

    return full_text

def tests():
    BGWRequests('2 Samuel 3:3,5', 'NIV')