from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView

from .forms import ContactForm

def ContactPageView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["admin@admin.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "contact.html", {"form": form})

def SuccessPageView(request):
    return render(request, 'success.html')
    #return HttpResponse("Success! Thank you for your message.")



# Create your views here.
# class ContactPageView(TemplateView):
#     template_name = 'contact.html'