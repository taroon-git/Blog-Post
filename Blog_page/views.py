from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db import IntegrityError
from django.shortcuts import render, HttpResponseRedirect
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login


def register(request):
    error_message = None  # Initialize error_message as None

    if request.method == 'POST':
        try:
            name = request.POST.get('Name')
            email = request.POST.get('Email')
            password = request.POST.get('CreatePassword')
            
            # Check if a user with the same username or email already exists
            if User.objects.filter(username=name).exists() or User.objects.filter(email=email).exists():
                raise IntegrityError("User already exists.")
            
            # Create a new user
            user = User.objects.create_user(name, email, password=password)
            user.save()

          
            # Redirect to the login page after successful registration
            return redirect('login')
        
        except IntegrityError:
            error_message = "User already exists. Please choose a different username or email."

    context = {
        'error_message': error_message,  # Include error_message in the context
    }
    print(context)

    return render(request, "register.html", context)




def userlogin(request):
    error_message = None
    if request.method == 'POST':
        us = request.POST.get('username')
        ps = request.POST.get('password')
        user = authenticate(request, username=us, password=ps)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Invalid username or password. Please enter the correct username and password."
    context = {
        'error_message': error_message, 
    }
    print(context)
    return render(request, "login.html", context)

def homepage(request):
    return render(request,"home.html")

def homepage2(request):
    return render(request,"home2.html")

def about(request):
    return render(request, 'about.html')

def about2(request):
    return render(request, 'about2.html')

def contact(request):
    return render(request, 'contact.html')

def contact2(request):
    return render(request, 'contact2.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def all_blogs(request):
    posts = Post.objects.all()
    return render(request, 'all_blogs.html', {'posts': posts })


import base64

# def add_post(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PostForm(request.POST, request.FILES)
#             if form.is_valid():
#                 title = form.cleaned_data['title']
#                 description = form.cleaned_data['description']
#                 image = form.cleaned_data['image']

#                 # Encode the image as a base64 string
#                 image_data = base64.b64encode(image.read()).decode('utf-8')

#                 post = Post(title=title, discription=description, image=image_data)
#                 post.save()
#                 form = PostForm()  # This line clears the form after successful submission.
#         else:
#             form = PostForm()

#         posts = Post.objects.all()  # Retrieve all posts including image data
#         return render(request, 'addpost.html', {'form': form, 'posts': posts})
#     else:
#         return HttpResponseRedirect('/login/')

   
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                image = form.cleaned_data['image']

                # Encode the image as a base64 string
                image_data = base64.b64encode(image.read()).decode('utf-8')

                post = Post(title=title, discription=description, image=image_data)
                post.save()
                form = PostForm()  # This line clears the form after successful submission.
        else:
            form = PostForm()

        # Retrieve all posts including image data
        posts = Post.objects.all()

        return render(request, 'addpost.html', {'form': form, 'posts': posts})
    else:
        return HttpResponseRedirect('/login/')
    

 #Update Post view
# def update_post(request, id):
#    if request.user.is_authenticated:
#       if request.method == 'POST':
#          pi = Post.objects.get(pk=id)
#          form = PostForm(request.POST, instance=pi)
#          if form.is_valid():
#           form.save()
#           return HttpResponseRedirect('home/')
#       else:
#          pi = Post.objects.get(pk=id)
#          form = PostForm(instance=pi)

#       return render(request, 'updatepost.html', {'form': form})
#    else:
#       return HttpResponseRedirect('/login/')

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
def update_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                image = form.cleaned_data['image']

                # Encode the updated image as a base64 string
                if image:
                    image_data = base64.b64encode(image.read()).decode('utf-8')
                    post.image = image_data

                post.title = title
                post.description = description
                post.save()

        else:
            form = PostForm(instance=post)

        return render(request, 'updatepost.html', {'form': form, 'post': post})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            post.delete()
            return HttpResponseRedirect('/addpost/')  # Redirect to the add_post view after deletion
        return render(request, 'deletepost.html', {'post': post})
    else:
        return HttpResponseRedirect('/login/')
   
#Delete Post view
# def delete_post(request, id):
#    if request.user.is_authenticated:
#       if request.method == 'POST':
#          pi = Post.objects.get(pk=id)
#          pi.delete()
#          return HttpResponseRedirect('home/')
#    else:
#       return HttpResponseRedirect('/login/')