#!/usr/bin/env python3

import urllib3, certifi, re
import json
from flask import Flask, jsonify, make_response, request

url = "https://theinternship.io/"

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Get Logo Companies test</h1>\n<a href='./companies'>[GET] logo companies</a>"

@app.route("/companies", methods=['GET'])
def getCompaniesPicture():
    poolmanager = urllib3.PoolManager(ca_certs=certifi.where())
    res = poolmanager.request('GET', url)
    html = res.data.decode('utf-8')
    regtext = "<img src=\"(.*?)\" alt=\"(.*?)\" class=\"center-logos\" (.*?)>"
    logoes = re.findall("<a href=\"(.*?)\" target=\"_blank\" (.*?)>" + regtext + "</a>", html)
    result = {"companies": []}
    for item in logoes:
        logo = {"logo": url + item[2]}
        result["companies"].append(logo)
    resultjson = json.dumps(result, sort_keys=True, indent=4)
    response = make_response(jsonify(result), 200)
    return response

# if __name__ == "__main__":
#     app.run(port=8000)