from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from rest_framework.generics import ListAPIView
from rest_framework import serializers
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer