from django.shortcuts import redirect, render
from awardsapp.models import Profile,Post
from awardsapp.forms import ProfileModelForm,PostModelForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .permissions import IsAdminOrReadOnly
from django.http import JsonResponse
from rest_framework import status
from .permissions import IsAdminOrReadOnly


# Create your views here.
# @login_required(login_url='/accounts/login/')

def my_profile_view(request):
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(author=request.user).order_by('-created')
    form = ProfileModelForm(request.POST or None ,request.FILES or None,instance = profile)
    p_form = PostModelForm(request.POST or None,request.FILES or None)

    comfirm = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            comfirm = True

            
    if p_form.is_valid():
        instance = p_form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('home')
    p_form = PostModelForm()            
         
    context = {
        'profile':profile,
        'form':form,
        'comfirm':comfirm,
        'posts':posts,
        'p_form':p_form,


    }
    return render(request,'profiles/myprofile.html',context)

def home(request):
    posts = Post.objects.all()
    date = dt.date.today()

    context = {
        'posts':posts,
        'date':date
    }

    return render(request,'awards/home.html',context)

@login_required(login_url='/accounts/login/')
def reviewPhoto(request,pk):
    post = Post.objects.get(id = pk)
    context = {
        'post':post

    }


    return render(request,'awards/review.html',context)
    
def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_articles = Post.search_by_project_name(search_term)
        message = f"{search_term}"
        context = {"message":message,
        "projects": searched_articles}

        return render(request, 'awards/search.html',context)
    else:
        message = "no projects found"
        context = {
            'message':message
        }
        return render(request, 'awards/home.html',context)  


def delete_project(request,pk): 
    post = Post.objects.get(pk = pk)
    if request.method == 'POST':
        post.delete()

        return redirect('home')

    return render(request, 'awards/delete_project.html',{})        


def update_project(request,pk):
    post = Post.objects.get(id = pk)
    form = PostModelForm(instance = post)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES ,instance = post)
        # We pass in the request.FILES argument because we are going to be uploading an Image file and we want to process that in our form.
        if form.is_valid():
            post.save()
            return redirect('review',pk = pk )
   
    return render(request, 'awards/update_project.html',{'form' :form})


class ProjectList(APIView):
    def get(self, request, format=None):
        allprojects = Post.objects.all()
        serializers = PostSerializer(allprojects, many=True)
        return Response(serializers.data)
    permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
