from bs4 import BeautifulSoup
import pandas as pd
import requests
import xlsxwriter
import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, pyqtSignal, QEventLoop
from PyQt5.QtWebEngineWidgets import QWebEnginePage


class Client(QWebEnginePage):
    toHtmlFinished = pyqtSignal()

    def __init__(self, url):
        self.app=QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

    def store_html(self, html):
        self.html = html
        self.toHtmlFinished.emit()

    def get_html(self):
        self.toHtml(self.store_html)
        loop = QEventLoop()
        self.toHtmlFinished.connect(loop.quit)
        loop.exec_()
        return self.html

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
        client_response = Client(url)
        soups.append(client_response.mainFrame().gethtml)
    return soups




urls = get_urls(input("url file name :"))

for i in soup(urls):
    print(i)