from django.shortcuts import render, redirect
from . forms import RegisterUserForm

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives




# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            # we want to send the user an email once they are successfully registered
            subject = 'Welcome to PostIt'
            #message = f'Hi {form.cleaned_data.get('first_name')}, thank you for registering in PostIt.'
            htmly = get_template('users/Email.html')
            d = {
                'first_name': form.cleaned_data.get('first_name'),
                'last_name': form.cleaned_data.get('last_name')
            }

            html_content = htmly.render(d)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data.get('email'), ]
            #send_mail(subject, html_content, email_from, recipient_list)


            msg = EmailMultiAlternatives(subject, html_content, email_from, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request,'users/register.html',{'form': form})

