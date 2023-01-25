from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('feed/', views.feed, name='feed-screen'),
    path('post/<int:postID>/', views.detailPost.as_view(), name='post-detail'),
    path('post/<int:postID>/comments', views.getComments().as_view(), name='comment-section'),
]