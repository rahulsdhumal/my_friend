from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('friend_details',FriendsDetailsView.as_view(),name='friend_details'),
    path('location_details',LocationDetailsView.as_view(),name='location_details'),
    path('company_details',CompanyDetailsView.as_view(),name='company_details'),
    path('delete_friend_details',DeleteFriendDetailsView.as_view(),name='delete_friend_details'),
]