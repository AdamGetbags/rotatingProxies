# -*- coding: utf-8 -*-
"""
Proxy Demo App
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

username = os.getenv("SMARTPROXY_USER")
password = os.getenv("SMARTPROXY_PASS")
url = 'https://ip.smartproxy.com/json'
proxy = f"http://{username}:{password}@gate.smartproxy.com:7000"

try:
    res = requests.get(
        url, 
        proxies = {
            'http': proxy,
            'https': proxy
        },
        timeout=10
    )
except requests.RequestException as e:
    print("Error:", e)
        
print(res.text)