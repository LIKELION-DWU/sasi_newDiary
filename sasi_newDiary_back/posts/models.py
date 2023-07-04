from django.db import models

class Post(models.Model):
    
    content = models.TextField(verbose_name="내용", default="")
    timestamp = models.DateTimeField(verbose_name="작성일", null = True, auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='posts_photo')
    
    def __str__(self): 
        return self.content
