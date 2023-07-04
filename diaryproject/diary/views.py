from django.shortcuts import render , redirect
from .forms import PostModelForm

def home(request):
    return render(request,'main.html')

#다이어리 작성
def create(request):
    if request.method == 'POST' or request.method == 'FILES' :
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form =PostModelForm()
    return render(request, 'write.html',{'form':form})
