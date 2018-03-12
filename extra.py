import urllib
import os
import sys
from bs4 import BeautifulSoup;

class getNotification(object):
    def main(self):
        code = self.getHTMLWeb("https://www.packtpub.com/packt/offers/free-learning/")
        title = self.getTitle(code)

    def getHTMLWeb(self, page):
        webURL = urllib.urlopen(page)
        webCode = webURL.read()
        webURL.close()
        return webCode

    def getTitle(self, code):
        soup = BeautifulSoup(code, "html.parser")
        title = soup.find("div", "dotd-title").find("h2").text
        return title

    def sendNotification(self):


if __name__ == "__main__":
    sb = getNotification()
    sb.main()