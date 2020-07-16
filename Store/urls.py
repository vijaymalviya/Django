from django.contrib import admin
from django.urls import path,include
from .views import views
from .views import login
from .views import signup
from .views import cart
from .views.login import Login,Logout



urlpatterns = [
    path('',views.Home.as_view(),name = 'homepage'),
   # path('order',views.orders),
    path('signup',signup.Signup.as_view()),
    path('login',login.Login.as_view(), name ='login'),
    path('logout',Logout,name="logout"),
    path('cart',cart.Cart.as_view()),
    ]
    

