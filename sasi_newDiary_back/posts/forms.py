from django import forms
from .models import Post,Comment

class PostModelForm(forms.ModelForm):
	class Meta:
		model=Post
		fields= ['photo', 'content',]


		labels ={
                  'photo':'사진',
                  'content':'내용',
		}       
	

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
        
        labels={
              'comment':'댓글',
		}
        
		