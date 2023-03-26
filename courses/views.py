from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class CoursesPageView(TemplateView):
    template_name = 'courses.html'