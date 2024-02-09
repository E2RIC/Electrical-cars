from django.db import models
from django.contrib.auth.models import User

        
# Create your models here.
class Offer(models.Model):
    images = models.ImageField()
    title = models.CharField(max_length=250)
   

    def __str__(self):
        return self.title


class Offerss(models.Model):
    file_upload = models.FileField(upload_to='uploads/')  

    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content       

class Order(models.Model):
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.product} - {self.name}"   

        
class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length = 255)
    def __str__(self):
        return self.username
          