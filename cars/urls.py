from django.urls import path
from .import views


urlpatterns = [
path('',views.cars,name='cars'),
path('cars',views.cars,name='cars'),
]
