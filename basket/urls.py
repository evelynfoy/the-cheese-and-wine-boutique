from django.urls import path
from . import views

urlpatterns = [
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
]