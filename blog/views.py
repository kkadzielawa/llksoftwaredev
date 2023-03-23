from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class BlogPageView(TemplateView):
    template_name = 'blog.html'