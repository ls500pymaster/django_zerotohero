from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError
from django.urls import reverse_lazy
from django.views.generic import FormView
from contact.forms import ContactForm


class ContactViewMain(FormView):
    template_name = 'blog/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:success')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        # copy = form.cleaned_data['copy']
        try:
            send_mail(subject, message, ["admin@localhost.com"], ["admin@example.com"])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return super().form_valid(form)


def contact_us(request):
    return render(request, 'blog/contact_us.html')


def success_view(request):
    return HttpResponse("Success! Thank you for your message.")

