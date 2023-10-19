from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = "user_app"
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('login/', views.loginClass.as_view(), name='login'),
    path('register/', views.register.as_view(), name='register'),
    path('listuser/', views.listUser.as_view(), name='listuser'),
    path('edit_user/<int:pk>/', views.EditUserView.as_view(), name='edit_user'),
]

urlpatterns += staticfiles_urlpatterns()