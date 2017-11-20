from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Index
from .models import About
from .models import Service
from .models import Contact

from django.views.generic import TemplateView,CreateView
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import service_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
#from snippets.models import Snippet
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet
# from .serializers import SnippetSerializer


from rest_framework import serializers


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
    

# class SnippetSerializer(serializers.Serializer):
#     rooms_choices   = serializers.IntegerField(read_only=True)
#     HOURS_CHOICES   = serializers.IntegerField(required=False, allow_blank=True, max_length=100)
#     SERVICE_CHOICES = serializers.CharField(max_length=50, choices=HOURS_CHOICE, default=LAUNDRY)
    
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.save()
#         return instance
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        #snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)