from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views import View
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny
from rest_framework import status, serializers, permissions
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .serializers import RegistrationSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         # Add custom claims
#         token['username'] = user.username
#
#         return token
#
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


def LandPage(request):
    return render(request, 'landing_page.html')

def RegisterPage(request):
    return render(request, 'signUp.html')

#8958772869
