#!/usr/bin/env python3

import urllib3, certifi, re

url = "https://theinternship.io"

poolmanager = urllib3.PoolManager(ca_certs=certifi.where())
res = poolmanager.request('GET', url)
html = res.data.decode('utf-8')
regtext = "<img src=\"(.*?)\" alt=\"(.*?)\" class=\"center-logos\" (.*?)>"
logo = re.findall("<a href=\"(.*?)\" target=\"_blank\" (.*?)>" + regtext + "</a>", html)
for item in logo:
    print(item[2])