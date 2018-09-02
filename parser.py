# parser.py
import requests
from bs4 import BeautifulSoup


# HTTP GET Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

html = req.text

soup = BeautifulSoup(html, 'html.parser')

print(soup)
