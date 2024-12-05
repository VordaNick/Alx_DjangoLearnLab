from django.contrib import admin
from .models import Post, Tag

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    filter_horizontal = ['tags']
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'content']
    
    