from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from urllib import request
from . models import Product,Customer
from django.db.models import Count
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages 

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")


class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())
    

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Registered Succesfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/customerregistration.html',locals())

class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(Self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            result=Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            result.save()
            messages.success(request,"profile saved succesfully!")
        else:
            messages.warning(request,"Invalid input data")    
        return render(request,'app/profile.html',locals())
    
def Address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())

class UpdateAddress(request):
    def get(self,request,pk):
        return render(request,'app/address.html',locals())
        











