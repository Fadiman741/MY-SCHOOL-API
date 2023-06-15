from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.models import Announcement,Message ,Post
from users.serializers import AnnouncementSerialiazer , MessageSerializer,PostSerializer

# ======================ANNOUNCEMENT========================================

@api_view(['GET'])
def announcement_list(request):
        announcement = Announcement.objects.all() #complex data
        serializer = AnnouncementSerialiazer(announcement, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_announcement(request):
        # announcement = Announcement.objects.all() #complex data

        serializer = AnnouncementSerialiazer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
                return Response(serializer.errors)
        
@api_view(['PUT','GET', 'DELETE'])
def update_announcement(request,pk):
        announcement = Announcement.objects.get(pk=pk)
        if request.method == 'GET':
                serializer = AnnouncementSerialiazer(announcement)
                return Response(serializer.data)

        if request.method == 'PUT':
                serializer = AnnouncementSerialiazer(announcement, data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors)
        
        if request.method == 'DELETE':
                announcement.delete
                return "Announcement deleted successfull"
        

# =============================MASSEGES=================================

@api_view(['GET'])
def messages(request):
        messages = Message.objects.all() #complex data
        serializer =  MessageSerializer(messages, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def send_messages(request):
        # messages = Message.objects.all() #complex data

        serializer =  MessageSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
                return Response(serializer.errors)
        
        
@api_view(['PUT','GET', 'DELETE'])
def update_messages(request,pk):
        messages = Message.objects.get(pk=pk)
        if request.method == 'GET':
                serializer =  MessageSerializer(messages)
                return Response(serializer.data)

        if request.method == 'PUT':
                serializer =  MessageSerializer(messages, data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors)
        
        if request.method == 'DELETE':
                messages.delete
                return "message deleted successfull"
        
# =============================POSTS=================================

@api_view(['GET'])
def posts(request):
        posts = Post.objects.all() #complex data
        serializer =  PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_post(request):
        # posts = Post.objects.all() #complex data

        serializer =  PostSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
                return Response(serializer.errors)
        
@api_view(['PUT','GET', 'DELETE'])
def update_post(request,pk):
        post = Post.objects.get(pk=pk)
        if request.method == 'GET':
                serializer =  PostSerializer(posts)
                return Response(serializer.data)

        if request.method == 'PUT':
                serializer =  PostSerializer(post, data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors)
        
        if request.method == 'DELETE':
                post.delete
                return "Post deleted successfull"
        
        