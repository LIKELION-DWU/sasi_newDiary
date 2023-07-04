from django.shortcuts import render, redirect
from .forms import PostModelForm

# Create your views here.
def post_main(request) :
    # posts 받아서 render하기 
    return redirect('main')
    #return render(request, 'main.html')
def post_list(request) :
    return render(request, 'main.html')

#create
def create(request):
    if request.method == 'POST' or request.method == 'FILES' :
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form =PostModelForm()
    return render(request, 'write.html',{'form':form})