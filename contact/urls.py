from django.contrib import admin
from django.urls import path, include

from .views import ContactPageView, SuccessPageView

urlpatterns = [
    path('', ContactPageView, name = 'contact'),
    path('success/', SuccessPageView, name = 'success'),
]
