from __future__ import unicode_literals
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView
#import random
from adkar.forms import CreateAdkarForm, CreateAdkarModelForm, RegisterForm
from adkar.models import Adkar, Activation
from django.contrib.auth import get_user_model
import datetime


# def AdkarModelFormCreateView(request, *argas, **kwargs):
#     errors = None
#     form = CreateAdkarModelForm(request.POST or None)
#     if form.is_valid():
#         # you can customize here it's like a pre_save
#         if request.user.is_authenticated:
#             instance = form.save(commit=False)
#             instance.owner = request.user
#             instance.save()
#             # form.save()
#             # this is like post_save
#
#             # obj = Adkar.objects.create(
#             # 		title=form.cleaned_data.get('title'),
#             # 		body=form.cleaned_data.get('body')
#             # 	)
#             return HttpResponseRedirect("/")
#         else:
#             return HttpResponseRedirect("/")
#     if form.errors:
#         print(form.errors)
#         errors = form.errors
#     template_name = "adkar/my_form.html"
#     context = {"as_p": form, "error": errors}
#     return render(request, template_name, context)


class Adkar_List(ListView):
    template_name = 'adkar/adkar_list.html'

    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Adkar.objects.filter(
                Q(slug__iexact=slug) |
                Q(slug__icontains=slug)
            ).order_by('-time_of_addition')
        else:
            queryset = Adkar.objects.all().order_by('-time_of_addition')

        return queryset

    def get(self, request, *args, **kwargs):
        start = datetime.datetime.now()
        print(start)
        return super().get(request, *args, **kwargs)


class Adkar_DetailView(DetailView):
    template_name = "adkar/adkar.html"
    queryset = Adkar.objects.all()
# or queryset = Adka.objects.filter(??)
# because all() and filter(??) both of them return a list i can't do get(??) becaus it returns an object and DetailView alredy looks for an object depending on the query set
# but i can do get() in a function based view for example:

#	def detailview(request, slug):
#			obj = Adkar.objects.get(slug=slug)
#			return render(request, template_name, {'object': obj})^---

    # you don't need this get context data method it's just a metod that shows you what data is beeing passed to this View and how it gets it's data because every
    def get_context_data(self, *args, **kwargs):
                                                                                # class view is diffrent when it comes to getting data and
                                                                                # thats what makes them special if you want to know how a class view gets it's data do this method in it.
                                                                                # for example: a ListView gets a queryset that you can iterate through it and list all the objects
                                                                                # but a DetailVeiw takes a queryset and id's and only shows the object that has that id for example:
                                                                                # object.title for id 15
                                                                                # id's is plural for id
        print(self.kwargs)
        # basically this is saying i want to inharit or get the get_context_data() function args a and kwargs
        context = super(Adkar_DetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get(self, request, *args, **kwargs):
        start = Adkar.objects.get(title='ammar8').time_of_addition
        print(start)
        return super().get(request, *args, **kwargs)

    # def get_object(self, *args, **kwargs):
    # 	adkar_id = self.kwargs.get("adkar_id")
    # 	obj = get_object_or_404(Adkar, id=adkar_id) # this how <pk> is defined so insted of id=adkar_id you can put pk or anything
    # 	return obj


class AdkarModelFormCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateAdkarModelForm
    template_name = "adkar/my_form.html"
    login_url = "/app/Login/M/"
    success_url = "/"

    def form_valid(self, form):
        # if self.request.user.is_authenticated:
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(AdkarModelFormCreateView, self).form_valid(form)
        # else:
        #     return HttpResponseRedirect("/")


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'adkar/register.html'
    success_url = '/'

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            return redirect('/')
        # https://stackoverflow.com/questions/47808652/what-is-dispatch-used-for-in-django
        return super().dispatch(*args, **kwargs)


def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        qs = Activation.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            activation = qs.first()
            if not activation.activated:
                user_obj = activation.user
                user_obj.is_active = True
                user_obj.save()
                activation.actevated = True
                activation.activation_key = None
                activation.save()
                return HttpResponseRedirect("/app/Login/M/")
    # invalid code
    return HttpResponseRedirect("/app/Login/M/")
