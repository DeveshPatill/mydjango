from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from urllib import request
# Create your views here.
def home(request):
    return render(request,"app/home.html")


class CategoryView(View):
    def get(self,request,val):
        return render(request,"app/category.html",locals())





