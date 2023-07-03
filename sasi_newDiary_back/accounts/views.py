from django.shortcuts import render

# Create your views here.

def home(request) :
    render(request, 'login.html')

def signup(request) :
    render(request, 'new_membership.html')