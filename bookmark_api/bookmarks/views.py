from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from bookmarks.serializers import BookmarkSerializer,UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


from bookmarks.models import *

class BookmarkViewSet(viewsets.ModelViewSet):
    
    queryset = Bookmark.objects.filter(public=True).order_by('created_at')
    serializer_class = BookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        query_set = super(BookmarkViewSet, self).get_queryset()        
        if self.request.user.is_authenticated:
            query_set = Bookmark.objects.filter(user=self.request.user.id)
            extra_query_set = Bookmark.objects.filter(public=True).exclude(user=self.request.user.id)
            return query_set | extra_query_set
        return query_set
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsAuthenticated, ]
        
        elif self.action in ['list']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]