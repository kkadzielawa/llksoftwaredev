from django.contrib import admin
from django.urls import path, include

from .views import CoursesPageView

urlpatterns = [
    path('', CoursesPageView.as_view(), name = 'courses'),
]
