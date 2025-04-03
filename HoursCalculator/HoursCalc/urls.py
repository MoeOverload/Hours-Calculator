from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('Add' , views.AddHours , name='Add'),
    path('View', views.ViewHours, name='View'),
    path('LoginUser',views.LoginUser, name='Login'),
    path('CreateUser', views.CreateUser, name="Create Account"),
]