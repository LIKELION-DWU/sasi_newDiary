from django.shortcuts import render, redirect

# Create your views here.
def post_main(request) :
    # posts 받아서 render하기 
    return redirect('main')
    #return render(request, 'main.html')
def post_list(request) :
    return render(request, 'main.html')