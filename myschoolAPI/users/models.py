from django.db import models

class User(models.Model):
        firstname=models.CharField( max_length=100)
        lastimage=models.CharField(max_length=100)
        email=models.CharField(max_length=20)
        grade=models.CharField(max_length=20)
        image=models.CharField(max_length=100)
        occupation=models.CharField(max_length=100) # Teacher / Department / Student / Tutor

        def __str__(self):
                return self.name
class Announcement(models.Model):
        department=models.CharField(max_length=300)
        description=models.CharField(max_length=300)
        datecreated =models.DateField()
        image=models.CharField(max_length=100)
        tiltle=models.CharField(max_length=100)
        likes=models.IntegerField()
        unlikes=models.IntegerField()
                
        def __str__(self):
                return self.department


