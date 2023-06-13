from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Annoucement

from users.serializers import AnnouncementSerialiaze 

# Create your views here.
@api_view(['GET'])
def property_list(request):
        properties = Annoucement.objects.all() #complex data

        serializer = AnnouncementSerialiaze(properties, many=True)
        return Response(serializer.data)