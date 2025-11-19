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
        except Exception as e:
            logger.error(f"send_mail raised an exception: {e}")

        return redirect("/portfolio")   # Prevent form resubmission
    return render(request, "portfolio/index.html")

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New message from {name}"
        body = f"From: {name}\nEmail: {email}\n\n{message}"

        send_mail(subject, body, None, ["your_personal_email@gmail.com"])

        return render(request, "index.html", {"success": True})

    return render(request, "index.html")