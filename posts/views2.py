from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    #context : post_list, obj_list
    #template : post_list.html, obj_list.html

class PostDetails(generic.DetailView):
    model = Post


class AddPost(generic.CreateView):
    model = Post
    fields = ['author', 'title', 'content', 'tags', 'image']
    success_url = '/blog/'

class EditPost(generic.UpdateView):
    model = Post
    fields = ['author', 'title', 'content', 'tags', 'image']
    success_url = '/blog/'
    template_name = 'posts/edit.html'

class DeletePost(generic.DeleteView):
    model = Post
    success_url = '/blog/'
    
