from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'landing_page/index.html')

def about(request):
    return render(request, 'landing_page/about.html')

def blog(request):
    return render(request, 'landing_page/insights.html')

def contact(request):
    return render(request, 'landing_page/contact.html')

def portfolio(request):
    return render(request, 'landing_page/portfolio.html')

def careers(request):
    return render(request, 'landing_page/careers.html')

def services(request):
    return render(request, 'landing_page/services.html')

def about(request):
    """Handle the about page with contact form"""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()
        
        logger.info(f"Contact form submitted: {name} <{email}>")
        
        try:
            send_mail(
                subject=f"New Contact Form Message from {name}",
                message=f"From: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('about')
            
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            messages.error(request, 'Sorry, there was an error sending your message.')
            return redirect('about')
    
    return render(request, 'landing_page/about.html')