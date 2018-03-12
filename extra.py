import urllib
from bs4 import BeautifulSoup
import telebot
import sys


class GetNotification(object):
    def __init__(self, botID, chatID):
        self.botID = botID
        self.chatID = chatID

    def main(self):
        code = self.getHTMLWeb("https://www.packtpub.com/packt/offers/free-learning/")
        title = self.getTitle(code)
        self.sendNotification(title)

    def getHTMLWeb(self, page):
        webURL = urllib.urlopen(page)
        webCode = webURL.read()
        webURL.close()
        return webCode

    def getTitle(self, code):
        soup = BeautifulSoup(code, "html.parser")
        title = soup.find("div", "dotd-title").find("h2").text
        return title

    def sendNotification(self, title):
        bot = telebot.TeleBot(self.botID)
        bot.send_message(self.chatID, "Today the free book on Packt is: " + title)
        bot.send_message(self.chatID,
                         "You can download the book on: https://www.packtpub.com/packt/offers/free-learning")


if __name__ == "__main__":
    if (len(sys.argv) == 3):
        notification = GetNotification(sys.argv[1], sys.argv[2])
        notification.main()
    else:
        print "extra.py <Telegram Bot ID> <Telegram chat ID>"