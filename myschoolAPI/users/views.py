from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Property
from api.serializer import PropertySerialiazer 

# Create your views here.
@api_view(['GET'])
def property_list(request):
        properties = Property.objects.all() #complex data

        serializer = PropertySerialiazer(properties, many=True)
        return Response(serializer.data)