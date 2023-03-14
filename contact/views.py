from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError
from django.urls import reverse_lazy
from django.views.generic import FormView
from contact.forms import ContactForm
from django.core.exceptions import ValidationError


class ContactViewMain(FormView):
    template_name = 'blog/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:success')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        try:
            send_mail(subject, message, ["admin@localhost.com"], ["admin@example.com"])
            return JsonResponse({'success': True})
        except BadHeaderError:
            return JsonResponse({'success': False, 'error': 'Invalid header found.'})
        except ValidationError as e:
            return JsonResponse({'success': False, 'error': e.message})

    def form_invalid(self, form):
        return JsonResponse({'success': False, 'error': 'Invalid form data.'})


def contact_success(request):
    return render(request, 'blog/contact_success_modal.html')
