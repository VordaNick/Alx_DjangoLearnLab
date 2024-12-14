from django.shortcuts import render
from rest_framework.response import Response
from .models import Notification
from rest_framework import generics
from rest_framework import permissions

# Create your views here.
class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user, is_read=False)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        notifications = [
            {
                'id': notification.id,
                'actor': notification.actor.username,
                'verb': notification.verb,
                "timestamp": notification.timestamp,
                "target": str(notification.target),
                'is_read': notification.is_read,
            }
            for notification in queryset
        ]
        return Response(notifications)