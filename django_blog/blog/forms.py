from django import forms
from .models import UserProfile, Comment, Post, Tag

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tags']
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
 #"TagWidget()"
 # "widgets"   