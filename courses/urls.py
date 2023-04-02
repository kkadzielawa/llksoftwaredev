from django.contrib import admin
from django.urls import path, include

from .views import CoursesPageView, stripe_config

urlpatterns = [
    path('', CoursesPageView.as_view(), name = 'courses'),
    path('config/', stripe_config),
]
