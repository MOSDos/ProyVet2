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


@csrf_protect
def createAccount(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("mainMenu"))
    elif request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("mainMenu"))
    return TemplateResponse(request, "createAccount.html", {"form" : CreateUserForm()})

 
@csrf_protect
def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("mainMenu"))
    return TemplateResponse(request, "index.html", {"form" : CreateUserForm()})


@csrf_protect
def Login(request):
    if (request.method=='POST'):
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=usuario, password=password)
        if user is not None and user.is_active:
             login(request, user)
             return HttpResponseRedirect(reverse("mainMenu"))
    return TemplateResponse(request, "index.html", {"form" : UserForm()})