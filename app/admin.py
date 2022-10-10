from django.contrib import admin
from .models import *
# Register your models here.

class Product_Images(admin.TabularInline):
    model = Product_Image

class Additional_Infomations(admin.TabularInline):
    model = Additional_Infomation

class ProductAdmin(admin.ModelAdmin):
    inlines = (Product_Images,Additional_Infomations)
    list_display = ('product_name','Categories','section')
    list_editable = ('Categories','section')


admin.site.register(Section)
admin.site.register(Product,ProductAdmin)
admin.site.register(Product_Image)
admin.site.register(Additional_Infomation)



admin.site.register(slider)
admin.site.register(banner_area)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)