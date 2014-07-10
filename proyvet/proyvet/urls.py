from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from prototipo import views
from django.core.urlresolvers import reverse
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyvet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index$', views.index, name="index"),
    url(r'^accounts/$', views.createAccount, name="createAccount"),
    #url(r'^/acounts/$', views.userAcounts, name="mainMenu"),
    #url(r'^principal/cargar_persona$', 'principal.views.cargar_persona', 
    #        name='cargar_persona'),

    url(r'^admin/', include(admin.site.urls)),
)
