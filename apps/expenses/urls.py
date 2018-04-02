from django.urls import path
from . import views

urlpatterns = [
    path('add_purchase', views.add_purchase),
    path('insert_purchase', views.add_purchase_processor)
]
