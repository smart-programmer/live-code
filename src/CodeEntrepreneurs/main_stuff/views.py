from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
import random
from adkar.models import Adkar



#class Home:



def contact(request):
	template_name = "main_stuff/contact.html"
	adkar = ["الحمد لله", "الله أكبر", "لا حول ولا قوة إلا بالله", "استغفر الله"]
	random_adkar = random.choice(adkar)
	contact_info = ['gbeast123488@gmail.com', '+ 986 58 355 1889']
	content = {"random_adkar": random_adkar, "contact_info": contact_info,}
	return render(request, template_name, content)



class Home(TemplateView):
	template_name="main_stuff/main.html" 

	def get_context_data(self, *args, **kwargs):
		print(self.kwargs)
		context = super(Home, self).get_context_data(*args, **kwargs)
		titls_slugs = self.kwargs.get('slug')
		if titls_slugs:
			queryset = Adkar.objects.filter(
				Q(slug__iexact=titls_slugs) | 
				Q(slug__icontains=titls_slugs))
		else:
			queryset = Adkar.objects.all().order_by('-time_of_addition')[:50]
		context = {'object_list': queryset}
		print(context)
		return context


