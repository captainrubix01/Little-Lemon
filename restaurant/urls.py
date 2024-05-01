#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns go here...
    path('', views.index, name='index')
]
