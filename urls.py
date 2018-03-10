from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.graph_page, name='graph'),
]
