from django import forms
from accounts.models import Comment

# Post 폼 작성 

# Comment 폼 작성 
class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']