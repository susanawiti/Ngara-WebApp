from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Index
from .models import About
from .models import Service
from .models import Contact

from django.views.generic import TemplateView,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User

from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token

class UserLoginView(APIView):
    """returns user token"""
    def post(self, request):
        username = request.data["email"]
        password = request.data["password"]
        
        # check if user exists
        if User.objects.filter(username=username, is_active=True).exists() is False:
            error = {
                "error": "Sorry, user does not exist"
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
            
        user = authenticate(username=username, password=password)
        
        # if user is authenticated, get the token for 
        # token based authentication
        if user: 
            token = Token.objects.get(user_id=user.id)
            data = {
                "token": token.key,
                "name": user.first_name
            }
            return Response(data, status=status.HTTP_200_OK)
        error = {
            "error": "sorry, email or password is incorrect"
        }
        return Response(error, status=status.HTTP_403_FORBIDDEN)
        
class UserView(APIView):
    """returns all users\n POST method creates a new user"""
    def get(self, request):
        user = User.objects.all()
        
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        
        # check if user exists
        if User.objects.filter(username=request.data["email"]).exists():
            error = {
                "error": "sorry, your email is already in use. Please login to continue"
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
            
        data = {
            "first_name": request.data['name'],
            "username": request.data["email"],
            "email": request.data["email"],
            "password": request.data["password"],
        }
        
        serializer = UserSerializer(data=data)
        
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data["password"])
            user.save()
            Token.objects.get_or_create(user=user)
            contact = Contact.objects.create(user_id=user.id, phonenumber=request.data["phonenumber"])
            contact.save()
            success = {
                "email": user.email,
                "token": Token.objects.get(user_id=user.id).key,
                "phonenumber": request.data["phonenumber"],
                "name": user.first_name
            }
            return Response(success, status=status.HTTP_201_CREATED)
        
        # if there are errors in data, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

