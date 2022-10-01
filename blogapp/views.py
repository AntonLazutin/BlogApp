import re
from turtle import title
from django.shortcuts import render, redirect, HttpResponse
from django import views
from django.http import JsonResponse
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from .forms import *
from .models import *
from .serializers import *
from . import services

# class Index(views.View):
#     template_name = ""
#     post_form_class = PostForm
#     comment_form_class = None

#     def get(self, request, *args, **kwargs):

#         try:
#             posts = Post.objects.order_by("-date")
#         except Post.DoesNotExist:
#             posts = None

#         form = self.post_form_class

#         return render(request, 'index.html', {'posts': posts, 'form': form, 'user': request.user})

#     def post(self, request, *args, **kwargs):
#         form = self.post_form_class(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('index')
#         else:
#             print(form.errors.as_data)

def index(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        else:
            print(form.errors.as_data)
    else:
        form = PostForm()
    return render(request, 'index.html', {'posts': posts, 'form': form, 'user': request.user})


def signup_page(request):
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'signup.html', context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data.get("username"), password=data.get("password"))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def post_page(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})


def profile_page(request, pk):
    posts = services.get_posts_by_user(user = request.user)
    return render(request, "profile_page.html", {'user': request.user, 'posts': posts})


@login_required(redirect_field_name='login')
def reacted(request, pk):
    print(request.POST)
    #services.react_to_post(request.POST["sumbit"], pk=pk)
    return redirect('index')


@csrf_exempt
@api_view(['GET', 'POST'])
def post_list(request, pk=None):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        pass