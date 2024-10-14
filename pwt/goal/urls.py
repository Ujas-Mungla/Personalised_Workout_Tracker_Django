from django.urls import path
from .views import *

urlpatterns = [
    path('goal_list_view/', goal_list_view, name='goal-list'),
    path('goal_detail_view/', goal_detail_view, name='goal-detail'),
    path('goal_create_view/', goal_create_view, name='goal-create'),
    path('goal_update_view/', goal_update_view, name='goal-update'),
    path('goal_partial_update_view/', goal_partial_update_view, name='goal-partial-update'),
    path('goal_delete_view/', goal_delete_view, name='goal-delete'),
]
