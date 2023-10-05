from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "user_app"
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('login/', views.loginClass.as_view(), name='login'),
    path('register/', views.register.as_view(), name='register'),
    path('listuser/', views.listUser.as_view(), name='listuser'),
    path('changeuser/', views.userChange.as_view(), name='changeuser'),
]