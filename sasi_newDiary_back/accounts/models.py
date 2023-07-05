from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


User = get_user_model()

# Create your models here.
class Post(models.Model) :

    def __self__(self) :
        return self.comment

class Comment(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    #article = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.comment