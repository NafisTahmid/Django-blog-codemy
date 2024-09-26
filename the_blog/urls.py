from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryPostView
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post', AddPostView.as_view(), name='add-post'),
    path('edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
    path('add_category/', CategoryPostView.as_view(), name='add_category'),
    path('category/<str:cats>', views.CategoryView, name="category"),
    path('categories/', views.ListAllCategories, name='categories')
]
