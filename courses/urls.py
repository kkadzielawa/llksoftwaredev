from django.contrib import admin
from django.urls import path, include

from .views import CoursesPageView, SuccessView, CancelledView, stripe_config, create_checkout_session

urlpatterns = [
    path('', CoursesPageView.as_view(), name = 'courses'),
    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),
    path('success/', SuccessView.as_view()), 
    path('cancelled/', CancelledView.as_view()), 
]
