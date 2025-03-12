# i have created this file - Devesh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   # params={'name':'devesh','place':'mumbai'}
    return render(request,"index.html")

def analyze(request):

    #get the text
    djtext=request.GET.get('text','default')

    #checkbox values ko check kro
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
   
   #check which checbox is on
    if (removepunc == "on"):
        #analyzed=djtext
        punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    
    elif (fullcaps == "on"):
        analyzed=" "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'changed to uppercase','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    
    elif (newlineremover == "on"):
        analyzed=" "
        for char in djtext:
            if char != "\n":
                analyzed=analyzed+char
        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    
    elif (extraspaceremover == "on"):
        analyzed=" "
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed=analyzed+char
        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        return render(request,"analyze.html",params)

    else:
        return HttpResponse("error")


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
    fullcaps=request.GET.get('fullcaps','off')

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
    
    elif (fullcaps == "on"):
        analyzed=" "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'changed to uppercase','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    
    else:
        return HttpResponse("error")
