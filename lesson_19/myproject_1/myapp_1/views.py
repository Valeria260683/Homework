from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
  model = Post
  template_name = 'myapp_1/post_list.html'
  context_object_name = 'posts'

class PostCreateView(CreateView):
  model = Post
  template_name = 'myapp_1/post_create.html'
  fields = ['title', 'content', 'page']
  success_url = reverse_lazy('post_create')

class PostUpdateView(UpdateView):
  model = Post
  template_name = 'myapp_1/post_update.html'
  fields = ['title', 'content', 'page']
  success_url = reverse_lazy('post_update', args=[1])

class PostDeleteView(DeleteView):
  model = Post
  template_name = 'myapp_1/post_delete.html'
  success_url = reverse_lazy('post_delete', args=[1])