# -*- coding: utf-8 -*-
"""
Using Proxies with Get Requests in Python
"""

import os
import pprint
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

username = os.getenv('SMARTPROXY_USER')
password = os.getenv('SMARTPROXY_PASS')
url = 'https://ip.smartproxy.com/json'
proxy = f'http://{username}:{password}@gate.smartproxy.com:7000'

def proxy_get(url, proxy):
    try:
        res = requests.get(
            url, 
            proxies = {
                'http': proxy,
                'https': proxy
            },
            timeout=10
        )
        return res
    except requests.RequestException as e:
        return {'error': str(e)} 
    
# Test function    
for i in range(0,2):
    pprint.pp(proxy_get(url, proxy).json())
    
sb_url = 'https://www.scrapingbee.com/blog/python-requests-proxy/'

res = proxy_get(sb_url, proxy)
print(res.text[:1000])

# Parse the HTML
soup = BeautifulSoup(res.text, "html.parser")

# Extract the title
title = soup.title.string if soup.title else "No title found"
print("Page Title:", title)