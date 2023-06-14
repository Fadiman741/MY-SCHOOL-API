from rest_framework import serializers
from .models import User,Announcement ,Message, Post, Notification

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = ['id', 'firstname', 'lastimage', 'email', 'grade', 'image', 'occupation']

class AnnouncementSerialiazer(serializers.ModelSerializer):
        class Meta:
                model = Announcement
                fields = ['id', 'department', 'description', 'datecreated', 'image', 'tiltle', 'likes', 'unlikes']

class MessageSerializer(serializers.ModelSerializer):
        class Meta:
                model = Message
                fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
        class Meta:
                model = Post
                fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
        class Meta:
                model = Notification
                fields = '__all__'