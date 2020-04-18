from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import slider
from about.models import new



def main(request):
	sliders_show = slider.objects.filter(sl_show='1').order_by('sl_number')
	news_list = new.objects.order_by('-pub_date')[:5] 
	return render(request, 'main/index.html', {'sliders_show': sliders_show, 'news_list': news_list})

def contact(request):
	return render(request, 'main/contact.html')
