from . import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('details/', views.details, name='details'),
    path('create/', views.create, name='create'),
    path('author/', views.author, name='author')
]