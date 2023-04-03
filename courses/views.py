from django.shortcuts import render
from django.conf import settings # new
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic import TemplateView

import stripe

# Create your views here.

class CoursesPageView(TemplateView):
    template_name = 'courses.html'

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/courses/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': 'price_1MsZZcCn7iEA5ilu8ey7bynw',
                        #'name': 'Data Structures 101',
                        'quantity': 1
                        #'currency': 'usd'
                    }
                ]
            )
            print(checkout_session)
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class SuccessView(TemplateView):
    template_name = 'courses/success.html'


class CancelledView(TemplateView):
    template_name = 'courses/cancelled.html'