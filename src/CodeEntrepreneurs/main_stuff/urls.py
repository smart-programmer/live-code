from __future__ import unicode_literals
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView, TemplateView
from adkar.models import Adkar
from adkar.views import Adkar_List




#url(r'^$', views.test),
urlpatterns = [ 
		url(r'^$', views.Home.as_view()), 
		#url(r'^(?P<slug>[\w-]+)/$', views.Home.as_view()), 
		url(r'^contact/$', views.contact, name="contact"), 

		
		

    
]