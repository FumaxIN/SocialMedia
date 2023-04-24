from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('feed/', views.feed, name='feed-screen'),
    path('post/<int:postID>/', views.detailPost.as_view(), name='post-detail'),
    path('post/<int:postID>/comments', views.getComments().as_view(), name='comment-section'),
    path('users/<str:userID>/', views.Profile().as_view(), name='profile_info'),
    path('users/<str:userID>/posts/', views.UserSpecificPost().as_view(), name='user_tweets'),
    path('<str:userID>/', views.ProfileSection, name='user-profile'),
    path('users/<str:userID>/likes/', views.UserLikedPosts.as_view()),
    path('post/<int:postID>/likes/', views.PostLikes.as_view())
]