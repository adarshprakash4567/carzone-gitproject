from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('accessories',views.accessories,name='accessories'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
]
