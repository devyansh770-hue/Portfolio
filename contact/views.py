from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import ContactMessage


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name, email=email, subject=subject, message=message
            )
            try:
                send_mail(
                    subject=f"Portfolio Contact: {subject}",
                    message=f"From: {name} <{email}>\n\n{message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, "Message sent! I'll get back to you soon.")
            return redirect('contact:contact')
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'contact/contact.html')
