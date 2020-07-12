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
    spisok_ch_id = []
    spisok_dict = {}
    for tar in spisok_tarif:
        for sp in spisok_ch:
            if sp.sm_spisok_title == tar.id:
                spisok_ch_id.append(sp.sm_channel_id)
        spisok_dict[tar.sm_tarif_title] = spisok_ch_id


    return render(request, 'tv/smotreshka.html', {'tarif': spisok_tarif, 'channel': spisok_dict})

def channel100(request):
    return render(request, 'tv/channel100.html')
