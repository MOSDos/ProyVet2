from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from prototipo import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyvet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/?$', views.index, name="index"),
    url(r'^accounts/createUser$', views.createAccount, name="createAccount"),
    url(r'^accounts/createSUser$', views.createSuper, name="createSuper"),
    url(r'^jugar/$', views.Jugar, name="jugar"),
    url(r'^accounts/login/$', views.Login, name="login"),
    url(r'^$', views.Logout, name="logout"),
    url(r'^mainMenu$', views.mainMenu, name="mainMenu"),
    url(r'^clients$', views.createClient, name="createClient"),
    #url(r'^/acounts/$', views.userAcounts, name="mainMenu"),
    #url(r'^principal/cargar_persona$', 'principal.views.cargar_persona', 
    #        name='cargar_persona'),

    url(r'^admin/', include(admin.site.urls)),
)
