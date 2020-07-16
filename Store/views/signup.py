from django.shortcuts import render,redirect
from Store.models import Product
from Store.models import Customer
from Store.models import Category
from django.views import View


class Signup(View):
    def get(self,req):
        return  render(req , 'signup.html')
    def post(self,req):
        fname  = req.POST.get('fname')
        lname  = req.POST.get('lname')
        email  = req.POST.get('email')
        mobile  = req.POST.get('mobile')
        password  = req.POST.get('pass')
        customer = Customer(fname  = fname , lname = lname  , email  = email  , mobile = mobile ,  password  = password)
        customer.register()
        return render(req  , 'login.html')
        

