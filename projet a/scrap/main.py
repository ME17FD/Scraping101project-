from bs4 import BeautifulSoup
import pandas as pd
import requests
import xlsxwriter
import os
from requests_html import HTMLSession



def get_urls(file):
    urls=[]
    current_directory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(current_directory+'\\'+file,"r")
    for x in f:
        if x[-1] == "\n":
            urls.append(x[:-1])
        else:
            urls.append(x)
    return urls


def soup(urls):
    soups=[]
    for url in urls:
        session = HTMLSession()
        r = session.get(url)
        r.html.render()
        soups.append(r.html)
    return soups




urls = get_urls(input("url file name :"))

for i in soup(urls):
    print(i)