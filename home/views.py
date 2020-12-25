from django.shortcuts import render
from home.meme import getMemeURL
# Create your views here.
def index(request):
    url = getMemeURL()
    myDict = {
        "url" : url[0],
        "post" : url[1],
        }
    return render(request, 'index.html', myDict)
