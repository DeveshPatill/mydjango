# i have created this file - Devesh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   # params={'name':'devesh','place':'mumbai'}
    return render(request,"index.html")

    #return HttpResponse('''<h1>hello devesh keep it up!!!!!</h1> <a href="https://www.wwe.com/"> exercise pratising open wwe official website </a>''')
"""
def about(request):
    return HttpResponse('''<h1>u will do it soon succes will in our hands</h1 ><a href="https://www.codewithharry.com/"> open<a/>''')


def margin(request):
    return HttpResponse("Home")

def removepunc(request):
    #get the text
    djtext=request.GET.get('text','default')
    print(djtext)
    #analyze the text
    return HttpResponse("remove punc")


def capitalizefirst(request):
    return HttpResponse("capitalize first")


def newlineremover(request):
    return HttpResponse("new line remover")

def spaceremover(request):
    return HttpResponse("space remover <a href='/'> back <a/>")

def charcount(request):
    return HttpResponse("char counter")

"""

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        #analyzed=djtext
        punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'removepunctuations','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    else:
        return HttpResponse("error")
