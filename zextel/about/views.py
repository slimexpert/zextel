from django.shortcuts import render
from .models import new, document

def main(request):
	return render(request, 'about/about.html')

def news(request):
	news_list = new.objects.order_by('-pub_date')
	return render(request, 'about/news.html', {'news_list': news_list})

def detail(request, new_id):
	try:
		det = new.objects.get(id = new_id)
	except:
		raise Http404("Новость не найдена")
	return render(request, 'about/news_detail.html', {'det': det})

def docs(request):
	doc_list = document.objects.filter(doc_show='1')
	return render(request, 'about/docs.html', {'doc_list': doc_list})

def jobs(request):
	jobs_list = document.objects.filter(doc_show='1')
	return render(request, 'about/jobs.html', {'jobs_list': jobs_list})