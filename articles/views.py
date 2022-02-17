from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Tag
from django.template.defaultfilters import slugify
from .forms import PostForm
from django.contrib import messages


class PostListView(ListView):
    template_name = 'articles/article_list.html'
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'articles/create-post.html'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'articles/post-detail.html'
    
    
class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'articles/edit-post.html'
    
    def form_valid(self, form):
        if form.instance.owner == self.request.user.profile:
            
            form.instance.owner = self.request.user.profile
            form.instance.slug = slugify(form.instance.title)
            return super().form_valid(form)
        else:
            return HttpResponseForbidden()
        
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "articles/post-delete.html"
    success_url = '/'
    
    def form_valid(self, form):
        if self.object.owner == self.request.user.profile:
            messages.success(self.request, 'deleted succssesfully!')
            return super().form_valid(form)
        else:
            return HttpResponseForbidden()

class TagListView(ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'tags'
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, id=self.kwargs['tag'])
        return Post.objects.filter(tags=self.tag)