from django.urls import path
from .views import UserRegisterView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', views.custom_login_view, name="login"),
    path('logout/', views.custom_logout_view, name='logout'),
    
]
