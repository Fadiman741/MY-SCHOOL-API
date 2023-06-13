from rest_framework import serializers
from .models import User,Announcement

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = ['id', 'firstname', 'lastimage', 'email', 'grade', 'image', 'occupation']

class AnnouncementSerializer(serializers.ModelSerializer):
        class Meta:
                model = Announcement
                fields = ['id', 'department', 'description', 'datecreated', 'image', 'tiltle', 'likes', 'unlikes']