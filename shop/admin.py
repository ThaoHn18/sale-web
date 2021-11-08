from django.contrib import admin
from .models import Order, Products


admin.site.site_header= "Thao Manage Shop"
admin.site.site_title = "Thao Shop"
admin.site.index_title = "Thao Manage"
class Product_Admin(admin.ModelAdmin):
    list_display = ('title','price','category')
    search_fields= ('title','category')

# Register your models here.
admin.site.register(Products,Product_Admin) # phải trong cùng 1 site
admin.site.register(Order)







