from django.contrib.auth.models import User, Group
from rest_framework import serializers

from bookmarks.models import *


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'public', 'user', 'created_at']
        read_only_fields = ('user','created_at')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    bookmark = BookmarkSerializer(many = True, read_only = True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'bookmark']