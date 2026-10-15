from django.shortcuts import render, redirect
from . import models
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import authenticate, login as auth_login, logout

def blog(request):
    return render(request,'home.html')


def login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request,username=name,password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/home/')
        else:
            return redirect('/login/')
    return render(request, 'login.html')


def signUp(request):
    if request.method=='POST':
        name= request.POST.get('uname')
        email= request.POST.get('uemail')
        password= request.POST.get('upassword')
        newUser= User.objects.create_user(username=name,email=email,password=password)
        newUser.save()
        return redirect('/login')
    return render(request,'signup.html')


def home(request):
    context={
        'posts':Posts.objects.all()
    }
    return render(request,'home.html',context)


def newPost(request):
    if request.method == 'POST':
        title= request.POST.get('title')
        content= request.POST.get('content')
        npost= models.Posts(title=title,content=content,author=request.user)
        npost.save()
        return redirect('/home')
    return render(request,'newpost.html')


def myPost(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    context = {
        'posts': Posts.objects.filter(author=request.user)
    }
    return render(request, 'mypost.html', context)


def signOut(request):
    logout(request)
    return redirect('/login')

