from django.urls import path
from .views import *

urlpatterns = [
   

    # Exercise endpoints
    path('exercise_list_view/',exercise_list_view, name='exercise-list'),
    path('exercise_detail_view/',exercise_detail_view, name='exercise-detail'),
    path('exercise_create_view/',exercise_create_view, name='exercise-create'),
    path('exercise_partial_update_view/',exercise_partial_update_view, name='exercise-partial-update'),
    path('exercise_delete_view/',exercise_delete_view, name='exercise-delete'),
]
