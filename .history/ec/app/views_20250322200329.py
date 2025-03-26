from django.shortcuts import render,Cpunt
from django.http import HttpResponse
from django.views import View
from urllib import request
from . models import Product
from django.db.models import Count

# Create your views here.
def home(request):
    return render(request,"app/home.html")



class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())





