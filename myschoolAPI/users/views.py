from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.models import Announcement
from users.serializers import AnnouncementSerialiazer 

# Create your views here.

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