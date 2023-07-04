from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import Post

# Create your views here.
def post_main(request) :
    return render(request, 'main.html')
    # posts 받아서 render하기 
    #return redirect('main')
    
def post_list(request) :
    return render(request, 'list.html')


#create /게시글 작성
def create(request):
    if request.method == 'POST' or request.method == 'FILES' :
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:main') 
    else:
        form =PostModelForm()
    return render(request, 'write.html',{'form':form})


#post_list /게시글 목록

def post_list(request):
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'list.html', {'posts':posts})


#post_detail /게시글 디테일 update.html 

def post_detail(request, id):
    post =get_object_or_404(Post,pk=id)
    context= {
        'post':post
    }
    return render(request,'update.html',context)

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