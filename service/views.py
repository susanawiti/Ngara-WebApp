from django.shortcuts import render
from rest_famework.generics import ListAPIView


# Create your views here.
from .models import SnippetService

class SnippetServiceAPIView(ListAPIView):
    queryset = SnippetService.objects.all()
    