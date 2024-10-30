from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('', views.home,name='home'),
    path('shop', views.shop,name='shop'),
    path('Read/', views.Read,name='read'),
    path('register/',views.register, name ='register'),
    path('Login/',views.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='home.html'), name ='logout'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),

]