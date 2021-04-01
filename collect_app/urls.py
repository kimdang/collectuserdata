from . import views
from django.urls import path 

urlpatterns = [
    path('', views.getnameage, name='index'),
    path('confirmPage', views.confirm, name='confirm')
]