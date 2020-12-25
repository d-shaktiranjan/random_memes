import urllib.request
import json

def getContent():
    page = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
    siteContent = page.read()
    return siteContent

def getMemeURL():
    content = getContent()
    jFile = json.loads(content)
    linkList = [jFile['url'], jFile['postLink']]
    return linkList
        

if __name__ == "__main__":
    # test = getContent()
    # print(test)
    url = getMemeURL()
    print(url)