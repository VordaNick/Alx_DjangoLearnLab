from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from rest_framework.generics import ListAPIView
from rest_framework import serializers
from .serializers import BookSerializer


# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer