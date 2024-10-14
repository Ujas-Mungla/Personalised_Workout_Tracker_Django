from django.urls import path
from .views import *
urlpatterns = [
    path('exercise_library_list_view/', exercise_library_list_view, name='exercise-library-list'),
    path('exercise_library_detail_view/', exercise_library_detail_view, name='exercise-library-detail'),
    path('exercise_library_create_view/', exercise_library_create_view, name='exercise-library-create'),
    path('exercise_library_partial_update_view/', exercise_library_partial_update_view, name='exercise-library-partial-update'),
    path('exercise_library_delete_view/', exercise_library_delete_view, name='exercise-library-delete'),
]
