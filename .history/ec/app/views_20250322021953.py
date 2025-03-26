from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def home(request):
    return render(request,"app/home.html")


class CategoryView(View):


