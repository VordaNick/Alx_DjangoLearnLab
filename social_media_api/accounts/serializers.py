from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', "bio", "profile_picture", "id"]
        extra_kwargs ={'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data.get('email', ""),
            password=validated_data['password'],
            username=validated_data['username'],
            bio = validated_data.get('bio', ""),
            profile_picture = validated_data.get('profile_picture', None)
            )
        Token.objects.create(user=user)
        return user
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    token = serializers.CharField(read_only=True)
    
    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid Email or Password')
        token, created = Token.objects.create(user=user)
        return {'token': token.key}
    

