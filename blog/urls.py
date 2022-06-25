"""ProjektNaZaliczenie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='blog-index'),
    path('details/<slug:slug>/', views.DetailsView.as_view(), name='blog-detail'),
    path('login/', views.MyLoginView.as_view(), name='blog-login'),
    path('register/', views.RegisterView.as_view(), name='blog-register'),
    path('new/', views.NewPostView.as_view(), name='blog-new'),
    path('logout/', auth_views.LogoutView.as_view(), name='blog-logout'),
    path('delete/<pk>/', views.PostDeleteView.as_view(), name="blog-delete"),
    path('update/<pk>/', views.PostUpdateView.as_view(), name="blog-update"),

]
