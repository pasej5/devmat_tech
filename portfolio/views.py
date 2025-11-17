from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validate data
        if not name or not email or not message:
            messages.error(request, 'Please fill in all fields.')
            return redirect('portfolio:index')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            send_mail(
                subject=f'New Contact Form Message from {name}',
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

        return redirect('portfolio:index')

    # GET request - just render the page
    return render(request, 'portfolio/index.html')

# You can delete the contact view - you don't need it!
# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         full_message = f"Message from {name} ({email}):\n\n{message}"

#         try:
#             send_mail(
#                 subject=f'New Contact Form Message from {name}',
#                 message=full_message,
#                 from_email=settings.EMAIL_HOST_USER,  # your email
#                 recipient_list=[settings.EMAIL_HOST_USER],  # send to your email
#             )
#             messages.success(request, 'Your message has been sent successfully!')
#         except Exception as e:
#             messages.error(request, f'An error occurred: {e}')

#         return redirect('portfolio:index')  # redirect to home after submission

#     return render(request, 'portfolio/index.html') 