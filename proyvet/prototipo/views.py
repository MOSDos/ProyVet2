# -*- encoding: utf-8 -*-
import string

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
#import models
from prototipo.forms import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    #bienvenido
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("mainMenu"))
    return TemplateResponse(request, "index.html", {"form" : CrearCliente()})


@csrf_protect
def createAccount(request):
    if request.method == 'POST':
        form = CrearCliente(request.POST)
        if form.is_valid():
            form.save() #save world
            return HttpResponseRedirect(reverse("mainMenu"))
    return HttpResponseRedirect(reverse("index"))