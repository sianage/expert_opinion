from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404
from django.http import HttpResponse
# Create your views here.
from MainApp.models import Post, Category
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

'''def index(request):
    return render(request, 'index.html', {})
    model = Post
    template_name = 'index.html'
    ordering = ['-id']'''

class index(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']

#HomeView
class Econ_Blog(ListView):
    model = Post
    template_name = 'econ_blog.html'
    ordering = ['-id']

class Polisci_Blog(ListView):
    model = Post
    template_name = 'polisci_blog.html'
    ordering = ['-id']

class Philosophy_Blog(ListView):
    model = Post
    template_name = 'philosophy_blog.html'
    ordering = ['-id']

class Medicine_Blog(ListView):
    model = Post
    template_name = 'medicine_blog.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    success_url = reverse_lazy('article_details')

#detail or list view???
class DebatesView(ListView):
    model = Post
    template_name = 'debates.html'
    success_url = reverse_lazy('debates')

class AddEntryView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_entry.html'
    success_url = reverse_lazy('econ_blog')
    #fields = '__all__'
    #fields = ('title', 'body')

class EditPostView(UpdateView):
    model = Post
    template_name = "edit_blog_post.html"
    fields = ('title', 'body')

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_blog_post.html"
    success_url = reverse_lazy('econ_blog')

def CategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat)
    return render(request, 'categories.html', {'cat': cat, 'category_posts': category_posts})