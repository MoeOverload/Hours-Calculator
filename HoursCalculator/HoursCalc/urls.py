from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('Add' , views.AddHours , name='Add'),
    path('View', views.ViewHours, name='View')
]