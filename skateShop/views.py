# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Voici la page principal du skateshop Bandol")

def product(request, variable_a):
    return HttpResponse("Voici le l'objet " + str(variable_a))


