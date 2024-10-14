from django.urls import path
from .views import *

urlpatterns = [
    path('meal_ingredient_list_view/', meal_ingredient_list_view, name='meal-ingredient-list'),
    path('meal_ingredient_detail_view/', meal_ingredient_detail_view, name='meal-ingredient-detail'),
    path('meal_ingredient_create_view/', meal_ingredient_create_view, name='meal-ingredient-create'),
    path('meal_ingredient_update_view/', meal_ingredient_update_view, name='meal-ingredient-update'),
    path('meal_ingredient_partial_update_view/', meal_ingredient_partial_update_view, name='meal-ingredient-partial-update'),
    path('meal_ingredient_delete_view/', meal_ingredient_delete_view, name='meal-ingredient-delete'),
]
