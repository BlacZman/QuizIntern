#!/usr/bin/env python3

from logging import log
import urllib3, certifi, re

url = "https://theinternship.io"

poolmanager = urllib3.PoolManager(ca_certs=certifi.where())
res = poolmanager.request('GET', url)
html = res.data.decode('utf-8')
img = "<img src=\"(.*?)\" alt=\"(.*?)\" class=\"center-logos\" data-v-018ba4ef>"
logo = re.findall("<a href=\"(.*?)\" target=\"_blank\" data-v-018ba4ef>" + img + "</a>", html)
about = re.findall("<span class=\"list-company\" data-v-018ba4ef>(.*?)</span>", html)

newlogo = {}
for i in range(len(logo)):
    newlogo.update({logo[i][1]: about[i]})

result = {key: val for key, val in sorted(newlogo.items(), key = lambda ele: len(ele[1]), reverse=False)}
for item in result:
    print(item)