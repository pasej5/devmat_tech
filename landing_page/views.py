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
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone", "Not provided")
        company = request.POST.get("company", "Not provided")
        service = request.POST.get("service", "Not specified")
        budget = request.POST.get("budget", "Not specified")
        message = request.POST.get("message")

        logger.warning("CONTACT FORM HIT - ABOUT PAGE")

        email_message = f"""
New Contact Form Submission from jmatsika.com/about/

----------------------------------
CONTACT DETAILS
----------------------------------
Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Company: {company}

----------------------------------
PROJECT DETAILS
----------------------------------
Service Interested In: {service}
Estimated Budget: {budget}

----------------------------------
MESSAGE
----------------------------------
{message}
        """

        try:
            send_mail(
                subject=f"New Inquiry from {first_name} {last_name} - {service}",
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            logger.error(f"send_mail raised an exception: {e}")
            messages.error(request, 'Sorry, there was an error sending your message.')

    return render(request, 'about.html')