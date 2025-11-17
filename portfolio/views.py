from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            full_message = f"Message from {name} ({email}):\n\n{message}"

            try:
                send_mail(
                    subject=f'New Contact Form Message from {name}',
                    message=full_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                     timeout=10,
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                logger.error(f"Email error: {e}")
                messages.error(request, 'An error occurred while sending your message.')

        return redirect('/')  # or return redirect('portfolio:index')

    # This is for GET requests
    return render(request, 'portfolio/index.html')