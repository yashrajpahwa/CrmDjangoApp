"""MyFirstWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:cid>/', views.customer, name="customer"),
    path('create/order/', views.createOrder, name="create-order"),
    path('user/', views.userPage, name="user-page"),
    path('order/update/<str:oid>/', views.updateOrder, name="update-order"),
    path('order/delete/<str:oid>/', views.deleteOrder, name="delete-order"),
    path('customer/delete/<str:cid>/',
         views.deleteCustomer, name="delete-customer"),
    path('customer/update/<str:cid>/',
         views.updateCustomer, name="update-customer"),
    path('create/customer/',
         views.createCustomer, name="create-customer"),
    path('create/products/', views.createProduct, name="create-product"),
    path('products/update/<str:pid>/',
         views.updateProduct, name="update-product"),
    path('customer/create/order/<str:cid>/',
         views.createCustomerOrder, name="create-customer-order"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout")
]
