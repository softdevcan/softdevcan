import logging

from django.http import JsonResponse
from django.shortcuts import render

from contact.forms import ContactForm
from contact.models import Message

logger = logging.getLogger(__name__)


def contact_form(request):
    if request.POST:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            Message.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )

            try:
                form.send_mail()
            except Exception:
                logger.exception("Failed to send contact form email")

            success = True
            message = 'Contact form sent successfully.'
        else:
            success = False
            message = 'Contact form is not valid.'
    else:
        success = False
        message = 'Request method is not valid.'

    return JsonResponse({'success': success, 'message': message})


def contact(request):
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'contact.html', context)
