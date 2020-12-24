from django.shortcuts import render
from home.meme import getMemeURL
# Create your views here.
def index(request):
    url = getMemeURL()
    myDict = {
        "url" : url,
        "host" : "http://127.0.0.1:8000"
        }
    return render(request, 'index.html', myDict)
