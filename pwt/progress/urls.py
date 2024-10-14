from django.urls import path
from .views import *
urlpatterns = [
    path('progress_list_view/', progress_list_view, name='progress-list'),  # List all progress records
    path('progress_detail_view/', progress_detail_view, name='progress-detail'),  # Retrieve a single progress record
    path('progress_create_view/', progress_create_view, name='progress-create'),  # Create a new progress record
    path('progress_partial_update_view/', progress_partial_update_view, name='progress-update'),  # Partially update a progress record
    path('progress_delete_view/', progress_delete_view, name='progress-delete'),  # Delete a progress record
]