from django.shortcuts import render
from .models import sm_channel, sm_spisok_ch, sm_tarif
from django.views.generic import View
import requests
# Create your views here.

def tv(request):
    return render(request, 'tv/maintv.html')

def smotreshka(request):
    spisok_tarif = sm_tarif.objects.all()
    spisok_ch = sm_spisok_ch.objects.all()
    return render(request, 'tv/smotreshka.html', {'tarif': spisok_tarif})
