from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path , include
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('register/',views.register ,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('test/',views.test,name="test"),
    path('contact/',views.contact,name="contact"),
    path('product/',views.product,name="product"),
   
    
]

