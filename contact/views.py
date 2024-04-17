from django.http import JsonResponse
# Create your views here.

def contact_form(request):
    context = {
        'success': True,
        'message': 'Contact form sent successfully',
    }
    return JsonResponse(context)