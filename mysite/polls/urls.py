"""The URL configurations used to call our views."""

from django.conf.urls import url

from . import views

app_name = 'polls' # set namespace for many apps

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

"""url() function is passed four arguments, two required: regex and view,
and two optional: kwargs, and name. At this point, it’s worth reviewing
what these arguments are for."""

"""Naming your URL lets you refer to it unambiguously from elsewhere in
Django, especially from within templates. This powerful feature allows
you to make global changes to the URL patterns of your project while only
touching a single file."""
