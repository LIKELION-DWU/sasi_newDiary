from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm

# Create your views here.
def post_main(request) :
    # posts 받아서 render하기 
    posts = Post.objects.all().order_by('timestamp')
    return render(request, 'main.html',  {'posts':posts})

#post_create 
def post_create(request):
    if request.method == 'POST' or request.method == 'FILES' :
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return render(request, 'main.html')
    else:
        form = PostModelForm()
    return render(request, 'write.html',{'form':form})

#post_list /게시글 목록
def post_list(request):
    posts = Post.objects.all().order_by('timestamp')
    return render(request, 'list.html', {'posts':posts})

def post_detail(request, id) :
    try:
        post = get_object_or_404(Post, pk=id)
    except Post.DoesNotExist:
        return redirect('posts') 
    
    comment_form = CommentModelForm()
    context = {
        'post' : post,
        'comment_form' : comment_form
    }
    return render(request, 'update.html', context)

#post_update /게시글 수정 
def post_update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:main')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'write.html', {'form':form, 'id':id})
    
    
#post_delete/게시글 삭제 
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('posts:post_list')

#댓글 생성 
def create_comment(request, id) : 
    filled_form = CommentModelForm(request.POST)
    if filled_form.is_valid() :
        post = Post.objects.get(pk=id)
        finished_form = filled_form.save(commit=False)
        finished_form.comment
        finished_form.article = get_object_or_404(Post, pk=id)
        finished_form.author = request.user
        finished_form.save()
        post.comment_count = post.comment_count + 1
        print(' 댓글 개수는 ----------------------------')
        print(post.comment_count)
        post.save()
    return redirect('posts:post_detail', id)
