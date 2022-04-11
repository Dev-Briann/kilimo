from django.shortcuts import render
from .forms import *
from django.contrib import  messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None) 
        if form.is_valid():
            form.cleaned_data['name']
            form.cleaned_data['email']
            form.save()
            messages.success(request,'Your message was sent successfully')

    else:
        form = ContactForm()

    context = {

    }
    return render(request,'contact.html', context)