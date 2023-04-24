from django.urls import path
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

# urlpatterns = [
#     path('accounts/', include('allauth.urls')),
#     path('dj-rest-auth/', include('dj_rest_auth.urls')),
#     # path('dj-rest-auth/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair')
# ]
urlpatterns = [
    # path('dj-rest-auth/lohagin/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.LandPage, name='landing'),
    path('register/', views.RegisterPage, name='registration'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]