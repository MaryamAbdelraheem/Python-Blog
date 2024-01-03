from django.shortcuts import render, redirect 
from .models import Post
from .forms import PostForm
# Create your views here.
#logic

def post_list(request):
    data = Post.objects.all() #orm -> sql -> db -> list{all posts}
    return render(request, 'posts.html', {'posts' : data })

def post_details(request, post_id):
    data = Post.objects.get(id=post_id)
    return render(request, 'post_details.html', {'post': data})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False )
            myform.author = request.user
            myform.save()
            return redirect('/blog/')
    else:
        form = PostForm()
    return render(request, 'new.html', {'form': form})

def edit_post(request, post_id):
    data = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = data)
        if form.is_valid():
            myform = form.save(commit=False )
            myform.author = request.user
            myform.save()
            return redirect('/blog/')
    else:
        form = PostForm(instance = data)
    return render(request, 'edit.html', {'form': form})

def post_delete(request, post_id):
    data = Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog/')

def about_me(request):
    return render(request, 'about.html')
