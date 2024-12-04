from django import forms
from .models import UserProfile, Comment

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']