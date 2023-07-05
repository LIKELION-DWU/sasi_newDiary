from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField(verbose_name="내용", default="")
    timestamp = models.DateTimeField(verbose_name="작성일", null = True, auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='posts_photo')
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    comment_count = models.IntegerField(verbose_name='댓글수', default=0)
    def __str__(self): 
        return self.content
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    
    def __str__(self) :
        return self.comment

