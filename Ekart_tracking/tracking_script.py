#!/usr/bin/env python3


import re
import requests
from bs4 import BeautifulSoup

baseurl = "https://ekartlogistics.com/shipmenttrack/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(baseurl, headers=headers)
if not f.ok:
    raise Exception("GET failed with status code {}".format(f.status_code))

soup = BeautifulSoup(f.content, 'html.parser')
