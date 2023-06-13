from rest_framework import serializers 
from users.models import Annoucement

class AnnouncementSerialiazer(serializers.Serializer):
        
        department=serializers.CharField(max_length=300)
        description=serializers.CharField(max_length=300)
        datecreated =serializers.DateField()
        image=serializers.CharField(max_length=100)
        heading=serializers.CharField(max_length=100)
        likes=serializers.IntegerField()
        unlikes=serializers.IntegerField()

        def create(self, data):
                return Annoucement.objects.create(**data)