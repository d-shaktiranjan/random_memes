from django.shortcuts import render
from home.meme import getMemeURL
# Create your views here.
def index(request):
    url = getMemeURL()
    myDict = {"url" : url}
    return render(request, 'index.html', myDict)
