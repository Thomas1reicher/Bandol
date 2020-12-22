
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('home.twig.html')
    context = {

    }
    return HttpResponse(template.render(context, request))