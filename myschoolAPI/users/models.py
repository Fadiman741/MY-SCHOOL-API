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

class Message(models.Model):
        sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
        recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        # Add any additional fields or methods for your messages

class Post(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        title = models.CharField(max_length=100)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        # Add any additional fields or methods for your posts

class Notification(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        is_read = models.BooleanField(default=False)

        # Add any additional fields or methods for your notifications