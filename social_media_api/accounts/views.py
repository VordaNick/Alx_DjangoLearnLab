'''from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
        messages.success(request, 'Account created Successfully')
        return redirect('login')
    else:
        form = UserCreationForm()
        context = {
            'form':form
        }
    return render(request, 'accounts/register.html', context)
        
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializer import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
     serializer_class = UserSerializer
     permission_classes = [permissions.AllowAny]
    
     
class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response ({'error': 'Invalid credentials'}, status=401)'''
            

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token


   
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'Token': token.key, 'user_id': user.id, 'Bio': user.bio, 'Username': user.username})
        return Response(serializer.errors, status=400)
    
class UserLoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=400)
        