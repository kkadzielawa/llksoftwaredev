from django.shortcuts import render
from django.conf import settings # new
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic import TemplateView


# Create your views here.

class CoursesPageView(TemplateView):
    template_name = 'courses.html'

print(settings.STRIPE_PUBLISHABLE_KEY)

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)