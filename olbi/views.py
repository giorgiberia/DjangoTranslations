from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

def hello(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)

def hello_world(request):
    if request.LANGUAGE_CODE == 'de-at':
        return HttpResponse("You prefer to read Austrian German.")
    else:
        return HttpResponse("You prefer to read another language.")