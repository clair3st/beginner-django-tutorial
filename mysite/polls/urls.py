"""The URL configurations used to call our views."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

"""url() function is passed four arguments, two required: regex and view,
and two optional: kwargs, and name. At this point, it’s worth reviewing
what these arguments are for."""

"""Naming your URL lets you refer to it unambiguously from elsewhere in
Django, especially from within templates. This powerful feature allows
you to make global changes to the URL patterns of your project while only
touching a single file."""
