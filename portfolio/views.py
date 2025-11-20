from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Simple test line so we know the view runs
        logger.warning("CONTACT FORM HIT")

        try:
            send_mail(
                subject=f"New Contact Form Message from {name}",
                message=f"Message from {name} ({email}):\n\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,  # Never crash the worker
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            logger.error(f"send_mail raised an exception: {e}")
            messages.error(request, 'Sorry, there was an error sending your message.')

           # Prevent form resubmission
        return redirect("/portfolio")
    
    return render(request, "portfolio/index.html")

def web_dev_service_page(request):
    """Renders the detailed case study page for web development."""
    return render(request, 'portfolio/service_web_dev.html')

