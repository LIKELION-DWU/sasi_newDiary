from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from posts.models import Post
# Create your views here.

def login(request) :
    if request.method == 'POST' :
        id = request.POST['id']
        passwd = request.POST['passwd']
        user = auth.authenticate(request, username=id, password=passwd)
        if user is not None : 
            auth.login(request, user)
            posts = Post.objects.all().order_by('timestamp')
            if posts is not None :
                return render(request, 'main.html', {'posts':posts})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request) :
    if request.method == 'POST' :
        id = request.POST['id']
        passwd = request.POST['passwd']
        user = None
        if id is not None and passwd is not None :
            new_user = User.objects.create_user(username=id, password=passwd)
            auth.login(request, new_user)
            return render(request, 'main.html')
    return render(request, 'signup.html')