from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import *


urlpatterns = [
    path('user_create_view/', user_create_view, name='user-create'),
    path('user_list_view_all/', user_list_view_all, name='user-list'),
    path('user_detail_view/', user_detail_view, name='user-detail'),
    path('user_update_view/', user_update_view, name='user-update'),
    path('user_update_patch_view/', user_update_patch_view, name='user-update-patch'),
    path('user_delete_view/', user_delete_view, name='user-delete'),
    path('generate_otp/', generate_otp, name='generate_otp'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    

    # path('encode_token_login/', encode_token_login, name='encode_token_login'),
    path('login_user/', logging_user, name='logging_user'),
    # path('forgot_password/', forget_password, name='forgot_password'),
    path('reset_password/', reset_password, name='reset_password'),
    # path('reregister_user/', reregister_user, name='reregister_user'),
    
]