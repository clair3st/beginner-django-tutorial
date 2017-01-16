"""Django views are created here."""

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    """Most basic of views."""
    return HttpResponse("Hello, world. You're at the polls index.")

"""When Django finds a regular expression match, Django calls the specified
view function, with an HttpRequest object as the first argument and any
“captured” values from the regular expression as other arguments. If the
regex uses simple captures, values are passed as positional arguments;
if it uses named captures, values are passed as keyword arguments."""
