from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from urllib import request
from . models import Product

# Create your views here.
def home(request):
    return render(request,"app/home.html")



class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values
        return render(request,"app/category.html",locals())





