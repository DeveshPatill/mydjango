from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"app/home.html")

def category(request):
    return render(request,"app/category.html")
