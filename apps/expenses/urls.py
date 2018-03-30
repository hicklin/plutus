from django.urls import path
from . import views

urlpatterns = [
    path('expenses/add_purchase', views.add_purchase)
]
