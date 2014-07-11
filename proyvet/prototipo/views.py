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

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth.decorators import permission_required, user_passes_test


@csrf_protect
def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("mainMenu"))
    return TemplateResponse(request, "index.html", {"form" : CreateUserForm()})


@csrf_protect
@login_required(redirect_field_name='/index')
@user_passes_test(lambda u: u.is_superuser)
def createAccount(request):
    if request.method == 'GET':
        return TemplateResponse(request,"accounts/createAccount.html", {"form" : CreateUserForm()})
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return TemplateResponse(request,"mainMenu.html")
        else:
            return TemplateResponse(request,"accounts/createAccount.html", {"form" : form})


@csrf_protect
def createSuper(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("mainMenu"))
    elif request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print "hola que hace"
            form.save()
            return TemplateResponse(request,"mainMenu.html")
        else:
            return TemplateResponse(request,"createAccount.html", {"form" : form})
    return TemplateResponse(request, "accounts/createAccount.html", {"form" : CreateUserForm()})

#@permission_required("prototipo.can_jugar", login_url="index")
#def Jugar(request):
#    c = {}
#    if request.method == "POST":
#        c['jugar'] = True
#        return TemplateResponse(request, "mainMenu.html",c)
#    else:
#        return TemplateResponse(request,"jugar.html")

@csrf_protect
def Login(request):
    if (request.method=='POST'):
        
        usuario = request.POST['username']
        password = request.POST['password1']
        aux = User.objects.get(username=usuario)
        user = authenticate(username=usuario, password=password)

        if user is not None and user.is_active:
             login(request, user)
             return HttpResponseRedirect(reverse("mainMenu"))
    return TemplateResponse(request, "index.html", {"form" : CreateUserForm()})


@csrf_protect
@login_required(redirect_field_name='/index')
def mainMenu(request):
  return TemplateResponse(request,"mainMenu.html")
    

@csrf_protect
@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@csrf_protect
@login_required
def createClient(request):
    if (request.method == "POST"):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return TemplateResponse(request,"mainMenu.html")
        else:
            return TemplateResponse(request,"mainMenu.html", {"form" : form})
    return TemplateResponse(request, "createClient.html", {"form" : CreateClientForm()})
