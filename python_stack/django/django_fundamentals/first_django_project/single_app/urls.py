from django.urls import path
from . import views

urlpatterns = [ 
    path('index', views.index),
    path('index/new', views.new),
    path('create', views.create),
    path("index/show/<int:my_val>", views.show),
    path("index/<int:my_val>/edit", views.edit),
    path("<int:my_val>/delete", views.destroy),
]