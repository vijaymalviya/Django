from django.shortcuts import render,redirect
from Store.models import Product
from Store.models import Customer
from Store.models import Category
from django.views import View

class Home(View):
    def post(self,req):
        product = req.POST.get('product')
        remove = req.POST.get('remove')
        cart = req.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity  <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product]  = quantity +1
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product] = 1
        req.session['cart'] = cart
        return redirect('homepage')

    def get(self,req):
         cart = req.session.get('cart')
         if not cart:
            req.session['cart'] = {}
         products = None
         category = Category.get_all_categories();
         cat_id = req.GET.get('cat')
         if cat_id:
             products  = Product.get_all_products_by_id(cat_id);
         else:
             products = Product.get_all_products();
   
         data = {}
         data['products'] = products
         data['category'] = category
         return render(req,'home.html',data)