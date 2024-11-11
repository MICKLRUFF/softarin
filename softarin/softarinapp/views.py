from django.shortcuts import render, redirect, get_object_or_404
from django.http import *
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

from .models import *
from .forms import *

menu = [{'title':_('Our Services'), 'pageid':'services'},
        {'title':_('For whom?'), 'pageid':'whom'},
        {'title':_('Stages of work'), 'pageid':'stages'},
        {'title':_('About Us'), 'pageid':'about'},
        {'title':_('Contact'), 'pageid':'contactus'}]

def index(request):
    servicess = Services.objects.all()
    whom = Projects.objects.all()
    stages = Stages.objects.all()
    feedback = Feedback.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                message = f"New request from SOFTARIN.COM\nName: {form.cleaned_data['contact_name']}\nPhone: {form.cleaned_data['contact_phone']}\nEmail: {form.cleaned_data['contact_email']}"
                send_mail('Contact Form', message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL], fail_silently=False)
                return redirect('home')
            except:
                form.add_error(None, 'Something went wrong')
    else:
        form = ContactForm()

    context = {'menu' : menu , 
               'title' : 'Softarin',
               'page_selected':0,
               'form' : form, 
               'servicess':servicess,
               'stages':stages,
               'whom':whom, 
               'feedback':feedback,
               } 
    return render(request, 'softarinapp/index.html', context=context)

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Something went wrong')
#     else:
#         form = ContactForm()

#     return render(request, 'softarinapp/index.html', context=context)