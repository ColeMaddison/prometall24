from django.conf.urls import patterns, url
from metalconstr import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^mangal/$', views.mangal, name='mangal'),
    url(r'^naves/$', views.naves, name='naves'),
    url(r'^vorota_kalitki/$', views.vorota_kalitki, name='vorota_kalitki'),
    url(r'^ritual/$', views.ritual, name='ritual'),
    url(r'^pandus/$', views.pandus, name='pandus'),
    url(r'^sitemap.xml/$', views.sitemap, name='sitemap'),
)
