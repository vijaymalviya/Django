from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer
# Register your models here.
class Adminproduct(admin.ModelAdmin):
	list_display = ["name","price","category"]
class  AdminCategory(admin.ModelAdmin):
	list_display = ["name"]
class  AdminCustomer(admin.ModelAdmin):
	list_display = ["fname", "email"]
		
admin.site.register(Product, Adminproduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer , AdminCustomer)