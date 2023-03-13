from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            recipients = ['your_email@example.com']
            if copy:
                recipients.append(email)
            send_mail(
                subject,
                f'Name: {name}\nEmail: {email}\n\n{message}',
                email,
                recipients,
                fail_silently=False,
            )
            return render(request, "contact/contact_success.html")
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})