from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView, TemplateView
from adkar.models import Adkar


# if you look at the DetailView link you'll see that <pk> has been replaced by <adkar_id> if want to know how you can overite <pk> and put what ever you want go to views.Adkar_DetailView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.Adkar_DetailView.as_view()),
    url(r'^(?P<slug>[\w-]+)$', views.Adkar_List.as_view()),
    url(r'^$', views.Adkar_List.as_view()),
    url(r'^Login/M/$', LoginView.as_view(), name="login"), 
    url(r'^resetpasswird/M$', PasswordResetView.as_view(), name="password_reset"), 
    url(r'^resetpasswirddone/M$', PasswordResetDoneView.as_view()), 
    url(r'^resetpasswirconfirm/M$', PasswordResetConfirmView.as_view()),
    url(r'^My_Form/M$', views.AdkarModelFormCreateView.as_view())




]

# url(r'^passwordreset/$', PasswordResetView.as_view(), name="password_reset"),
# url(r'^confirmreset/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
# url(r'^passordresetdone/$', PasswordResetDoneView.as_view(), name='password_reset_done'),