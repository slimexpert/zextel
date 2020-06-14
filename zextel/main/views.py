from django.shortcuts import render, redirect, get_object_or_404
from .models import slider, contact_support, zone, Rate
from about.models import new
from .forms import ContactForm
from django.views.generic import View
from django.core.mail import send_mail
import requests
#from dadata.plugins.django import DjangoDaDataClient

def stock_valid(stock :str):
	if stock == 'bbdefa2950f49882f295b1285d4fa9dec45fc4144bfb07ee6acc68762d12c2e3':
		stock = 'google'
	if stock == '5ec9c2c2913538bbedadd97c25943dc5fedf8617e6bed980714f5e9a9b2e24e6':
		stock = 'yandex'
	if stock == 'b310e4e6d0ccc8b1b4099e82793090c5dfe111f9e38ff09a24597bca4029b31c':
		stock = '2gis'
	if stock == 'e29a6867b081cdfd3c84eb5cd5dd497ae905eb0d39259bf2411ccd58129b7d98':
		stock = 'baner'
	if stock == '8630c6c9af0730c3e9635a44c97bfb4ac4ff57c449951a60848ac666f5f2de0c':
		stock = 'vk'
	if stock == '0':
		stock = '0'
	return stock

def main(request):
	sliders_show = slider.objects.filter(sl_show='1').order_by('sl_number')
	news_list = new.objects.order_by('-pub_date')[:5]
	zone_list = zone.objects.filter(zone_show='True')
	rate_list = Rate.objects.all().order_by('rate_group', 'rate_number')
	if request.method == 'GET':
		if request.GET.get('zone', False):
			zone_id = str(request.GET['zone'])
			zone_id = zone_id[0]
		else:
			zone_id = '1'
	return render(request, 'main/index.html', {'sliders_show': sliders_show,
	'news_list': news_list, 'zone_list': zone_list, 'rate_list': rate_list,
	'zone_id': zone_id})

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
		form = ContactForm()
		if bount_form.is_valid():
			new_contact = bount_form.save()
			print('прошла валидация')
			return redirect(new_contact)
		print('не прошла валидация')
		return render(request, 'main/contact.html', {'form':bount_form})

class SendConnect(View):
	def send_mess(chat, text):
	    params = {'chat_id': chat, 'text': text}
	    response = requests.post(url + 'sendMessage', data=params)
	    return response

	def post(self, request):
		if request.method == 'POST':
			url = 'https://api.telegram.org/bot862407227:AAHQf3fBAKpPzceomL112WmZJF2UARz3iqA/'
			if request.POST['address'] == "":
				address = 'Адрес не указан'
			else:
				address = request.POST['address']
			if request.POST['name'] == "":
				name = 'Имя не указал'
			else:
				name = request.POST['name']
			telefon = request.POST['phone']
			if request.POST.get('rate', False):
				rate = request.POST['rate']
				if rate == '0':
					rate_title = 'Не указан'
				else:
					rate_odj = Rate.objects.get(id=rate)
					rate_title = rate_odj.rate_title +' '+ rate_odj.rate_title_text
			else:
				rate_title = 'Не указан'
			if request.POST.get('stock', False):
				stock = request.POST['stock']
			else:
				stock = 'Не указан'
			if request.POST.get('promo', False):
				promo = request.POST['promo']
			else:
				promo = 'Не указан'

			message_telegramm = '*Имя:* '+name+'\n'+'*Телефон:* +'+telefon+'\n'+'*Адрес:* '+address+'\n'+'*Тариф:* '+rate_title+'\n'+'*Промокод:* '+promo+'\n'+'*Источник:* '+stock
			subject = 'Заявка с сайта'
			message = 'Заявка' + address + '\n' + telefon
			recepient = 'sait@zextel.ru'
			send_mail(subject, message, 'zextel.site@gmail.com', [recepient], fail_silently = False)
			msg = 'успешно отправлена'
			req = requests.get(url+'sendMessage?chat_id=-1001193659934&text='+message_telegramm+'&parse_mode=Markdown')
			return render(request, 'main/send.html', {'msg': msg,})

		а = 'пост не отправлена'
		return render(request, 'main/send.html', {'msg': msg,})

	def get(self,request):
		msg = 'ГЕТ не отправлена'
		return render(request, 'main/send.html', {'msg': msg,})

class connect(View):
	def post(self, request):
		address_show = True
		news_list = new.objects.order_by('-pub_date')[:5] # для отображения новостей
		address = request.POST['address']
		if address:
			#client = DjangoDaDataClient()
			#client.suggest_address = address
			#client.suggestions.address.request()
			#a = client.result.suggestions[0].get('data')
			address_show = False
			return render(request, 'main/connect.html', {'news_list': news_list, 'address': address, 'address_show': address_show})
		else:
			return render(request, 'main/connect.html', {'news_list': news_list, 'address_show': address_show})

	def get(self, request):
		address_show = True
		news_list = new.objects.order_by('-pub_date')[:5] # для отображения новостей
		if request.GET.get('rate', False):
			rate = str(request.GET['rate'])
		else:
			rate = 0
		if request.GET.get('stock', False):
			stock = stock_valid(str(request.GET['stock']))
		else:
			stock = 'Не указан'
		if request.GET.get('promo', False):
			promo = str(request.GET['promo'])
		else:
			promo = 'Не указан'

		return render(request, 'main/connect.html', {'news_list': news_list, 'stock': stock, 'promo': promo, 'address_show': address_show, 'rate': rate})
