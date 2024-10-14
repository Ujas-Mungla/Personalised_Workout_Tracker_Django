from django.urls import path
from .views import *

urlpatterns = [
    path('meal_list_view/', meal_list_view, name='meal-list'),
    path('meal_detail_view/', meal_detail_view, name='meal-detail'),
    path('meal_create_view/', meal_create_view, name='meal-create'),
    path('meal_update_view/', meal_update_view, name='meal-update'),
    path('meal_partial_update_view/', meal_partial_update_view, name='meal-partial-update'),
    path('meal_delete_view/', meal_delete_view, name='meal-delete'),
]
