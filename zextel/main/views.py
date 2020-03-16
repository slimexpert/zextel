from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import slider


def main(request):
	sliders_show = slider.objects.filter(sl_show='1').order_by('sl_number')
	return render(request, 'main/index.html', {'sliders_show': sliders_show })
