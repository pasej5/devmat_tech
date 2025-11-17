from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect




def index(request):
    return render(request, 'portfolio/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            subject=f"New message from {name}",
            message=f"Message: {message}\nFrom: {name} <{email}>",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return render(request, 'contact_thank_you.html')
    return render(request, 'contact.html')