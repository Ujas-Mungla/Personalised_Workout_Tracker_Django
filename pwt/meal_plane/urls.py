from django.urls import path
from .views import *
urlpatterns = [
    path('mealplan_list_view/', mealplan_list_view, name='mealplan-list'),
    path('mealplan_detail_view/', mealplan_detail_view, name='mealplan-detail'),
    path('mealplan_create_view/', mealplan_create_view, name='mealplan-create'),
    path('mealplan_update_view/', mealplan_update_view, name='mealplan-update'),
    path('mealplan_partial_update_view/', mealplan_partial_update_view, name='mealplan-partial-update'),
    path('mealplan_delete_view/', mealplan_delete_view, name='mealplan-delete'),
    
]