from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm, CategoryForm
from django.urls import reverse_lazy
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class=EditForm
    template_name = 'update_post.html'
    # fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class CategoryPostView(CreateView):
    form = CategoryForm
    model = Category
    fields= '__all__'
    template_name = 'add_category.html'
    # success_url= 'home.html'


def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    diction = {'cats':cats.title().replace('-', ' '), 'category_post':category_post}
    return render(request, 'categories.html', context=diction)

def ListAllCategories(request):
    model = Category.objects.all()
    diction = {'categories':model}
    return render(request, 'all_categories.html', context=diction)
