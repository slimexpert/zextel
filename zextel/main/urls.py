from django.urls import path

from . import views
from .views import *

app_name = 'main'
urlpatterns = [
	path('', views.main, name = 'main'),
	path('contact/new', ContactSupport.as_view(), name = 'contact_support_url'),
	path('contact/<str:supp_name>', support.as_view(), name = 'support_url')
]
