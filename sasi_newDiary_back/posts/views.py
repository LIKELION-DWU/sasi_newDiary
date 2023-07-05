from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Post, Comment
from accounts.forms import CommentModelForm
from .forms import PostModelForm

# Create your views here.
def post_main(request) :
    # posts 받아서 render하기 
    return render(request, 'main.html')

#post_create 로 수정함 
def post_create(request):
    if request.method == 'POST' or request.method == 'FILES' :
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return render(request, 'main.html')
    else:
        form = PostModelForm()
    return render(request, 'write.html',{'form':form})


def post_list(request) :
    return render(request, 'main.html')

def post_detail(request, post_id) :
    try:
        post = get_object_or_404(Post, pk=post_id)
    except Post.DoesNotExist:
        return redirect('posts') 
    
    comment_form = CommentModelForm()
    
    context = {
        'post' : post,
        'comment_form' : comment_form
    }
    return render(request, 'update.html', context)
    
def create_comment(request, post_id) : 
    filled_form = CommentModelForm(request.POST['comment'])
    if filled_form.is_valid() :
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Post, pk=post_id)
        finished_form.author = request.user
        finished_form.save()

    return redirect('post_detail', post_id)
