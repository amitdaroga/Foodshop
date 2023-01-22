"""login_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from shop_admin import views

urlpatterns = [
    path('', views.login,name='login'),
    path('Registration/',views.Registration,name='Registration'),
    path('OTPVerification/',views.OTPVerification,name='OTPVerification'),
    path('Home/',views.Home,name='Home'),
    path('Logout/',views.Logout,name='Logout'),
    path('ProductDetails/',views.Product_Details,name='ProductDetails'),
    path('UpdateProduct/<int:pk>',views.UpdateProduct,name="UpdateProduct"),
    path('Delete/<int:pk>',views.Delete,name="Delete"),
    path('search/',views.search,name='search'),
]
