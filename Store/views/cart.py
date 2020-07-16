from django.shortcuts import render,redirect
from Store.models import Product
from Store.models import Customer
from Store.models import Category
from django.views import View

class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products =  Product.get_products(ids)
        print(products)
        return render(request,'cart.html',{'products':products})
    def post(self,req):
        email = req.POST.get('email')
        password = req.POST.get('pass')
        customer = Customer.get_customer_by_email(email)
        if customer:
            if password == customer.password:
                req.session['customer'] = customer.id
                req.session['email'] = customer.email
                return redirect('homepage')
            else:
                error = "password not correct"
                return render(req,'login.html',{'error':error})
        else:
            mesge = "customer not exist"
            return render(req,'login.html',{'error':error})


