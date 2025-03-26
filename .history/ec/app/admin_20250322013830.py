from django.contrib import admin

# Register your models here.


@admin.register()
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category',]