from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', "token"]
    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'], username=validated_data('username'),)
        token, created = Token.objects.create(user=user)
        user.token = token.key
        return user
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    
    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid Email or Password')
        token, created = Token.objects.create(user=user)
        return {'token': token.key}
    

