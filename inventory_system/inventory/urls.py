from django.urls import path
from .views import register, login
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
