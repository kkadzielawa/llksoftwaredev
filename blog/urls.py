from django.contrib import admin
from django.urls import path, include

from .views import BlogPageView, BlogDetailView

urlpatterns = [
    path('', BlogPageView.as_view(), name = 'blog'),
    path('<slug:slug>/', BlogDetailView.as_view(), name = 'blog_detail'),
]
