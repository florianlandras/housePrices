#import post process

# from urllib import request library don't fucking work / Use >>> requestS 
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
import requests
import re

 
baseUrl = 'https://www.hemnet.se/salda/villa/'
city = 'soderkopings-kommun'
typeBostad = ''
sizeMin =''
sizeMax = ''


url = baseUrl+city

def dataJson () :

    html = requests.get(url) 
    dataLayer = re.findall("dataLayer = (.+?);\n", html.text, re.S)
    varJson = json.loads(dataLayer[0])
    monJson = varJson[1]["results"]["locations"][0]["id"]
    print(monJson)

    return monJson

dataJson()
