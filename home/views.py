from django.shortcuts import render

# Create your views here.
def index(request):
    myDict = {"url" : "https://i.imgflip.com/487d7e.jpg"}
    return render(request, 'index.html', myDict)
