from django.urls import path
from . import views

urlpatterns = [

    path('simple_checkout/', views.simpleCheckout, name="simple_checkout"),


    path('', views.accessories, name='accessories'),
    path('accessories', views.accessories, name='accessories'),
    path('', views.checkout, name='checkout'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('complete/', views.paymentComplete, name='complete'),
]