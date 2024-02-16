from django.contrib import admin
from .models.product import product
from .models.category import category
from .models.sign import sign
from .models.orders import orders
from .models.admin_login import admin_login


# Register your models here.

class order_data(admin.ModelAdmin):
    list_display=['customer','product','price','quantity','date','phone','address','status']

class Adminproduct(admin.ModelAdmin):
    list_display=['PRODUCT','CATEGORY','DESCRIPTION','PRICE','IMAGE']

class login(admin.ModelAdmin):
    list_display=['email','password']

admin.site.register(product,Adminproduct)
admin.site.register(category)
admin.site.register(sign)
admin.site.register(orders,order_data)
admin.site.register(admin_login,login)