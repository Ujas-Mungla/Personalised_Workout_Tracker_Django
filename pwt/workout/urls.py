from django.urls import path
from .views import *

urlpatterns = [
    path('workout_list_view/', workout_list_view, name='workout-list'),
    path('workout_detail_view/', workout_detail_view, name='workout-list-all') , # For GET requests
    path('workout_create_view/', workout_create_view, name='workout-create'),  
    path('workout_list_view/', workout_list_view, name='workout-list'),
    # path('workout_update_view/', workout_update_view, name='workout-update'),
    path('workout_partial_update_view/', workout_partial_update_view, name='workout-partial-update'),
    path('workout_delete_view/', workout_delete_view, name='workout-delete'),
]
