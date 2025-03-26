from django.contrib import admin
from . models import Product,Customer,Cart,Payment,OrderPlaced
# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','mobile','state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']
    

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = 