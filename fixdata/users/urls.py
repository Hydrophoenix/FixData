'''Modules for proper functoning of this view.py'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup/adduser/', views.adduser, name='adduser'),
    path('signin/', views.signin, name='signin'),
    path('signin/login_user/', views.login_user, name='login_user'),
]