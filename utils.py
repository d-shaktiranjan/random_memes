import urllib.request
import json


def getContent():
    page = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
    siteContent = page.read()
    return siteContent


def getMemeURL():
    content = getContent()
    jFile = json.loads(content)
    linkList = [jFile['url'], jFile['postLink'], jFile['author']]
    return linkList
