from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import slider, contact_support
from about.models import new
from .forms import ContactForm
from django.views.generic import View
from django.urls import reverse



def main(request):
	sliders_show = slider.objects.filter(sl_show='1').order_by('sl_number')
	news_list = new.objects.order_by('-pub_date')[:5]
	return render(request, 'main/index.html', {'sliders_show': sliders_show, 'news_list': news_list})

class support(View):
	def get(self, request, supp_name):
		contact = contact_support.objects.get(supp_name__iexact=supp_name)
		return render(request, 'main/support.html', {'contact':contact})


class ContactSupport(View):
	def get(self, request):
		form = ContactForm()
		return render(request, 'main/contact.html', {'form':form})

	def post(self, request):
		bount_form = ContactForm(request.POST)
		if bount_form.is_valid():
			new_contact = bount_form.save()
			print('прошла валидация')
			return redirect(new_contact)
		else:
			print('не прошла валидация')
			return render(request, 'main/contact.html', {'form':bount_form})
