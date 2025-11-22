from django.shortcuts import render
from . models import*
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from django.views.generic import UpdateView,DeleteView,DetailView
from blog.models import*
from django.urls import reverse_lazy

# Create your views here.
def Home(request):
    return render (request,'blog/index.html')

class createPost(CreateView):
    model=blogPost
    fields=['title','content']
    template_name='blog/create-post.html'
    success_url=reverse_lazy('home')

class listPosts(ListView):
    model=blogPost
    context_object_name='posts'
    template_name='blog/list-post.html'

class postDetails(DetailView):
    model=blogPost
    template_name='blog/post-detail.html'
    context_object_name='pt'
    
class updatePost(UpdateView):
    model=blogPost
    fields=['title','content']
    template_name='blog/create-post.html'
    success_url=reverse_lazy('list-post')

class deletePost(DeleteView):
    model=blogPost
    template_name='blog/delete-post.html'
    context_object_name='del'
    success_url=reverse_lazy('list-post')
    

