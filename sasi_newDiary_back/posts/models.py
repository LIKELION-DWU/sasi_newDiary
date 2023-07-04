from django.db import models

class Post(models.Model):

    body = models.TextField(verbose_name="내용", default="")
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='diary_photo')
    
    def __str__(self): 
        return self.title
