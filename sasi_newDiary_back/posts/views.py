from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Post, Comment
from accounts.forms import CommentModelForm

# Create your views here.
def post_main(request) :
    # posts 받아서 render하기 
    return redirect('main')
    #return render(request, 'main.html')
def post_list(request) :
    return render(request, 'main.html')

def post_detail(request) :
    return render(request, 'update.html')

def create_comment(request, post_id) : 
    filled_form = CommentModelForm(request.POST['comment'])

    if filled_form.is_valid() :
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Post, pk=post_id)
        finished_form.author = request.user
        finished_form.save()

    return redirect('update.html', post_id)
