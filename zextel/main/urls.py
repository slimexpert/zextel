from django.urls import path

from . import views
from .views import *

app_name = 'main'
urlpatterns = [
	path('', views.main, name = 'main'),
	path('contact/', ContactSupport.as_view(), name = 'contact_support_url'),
	path('contact/<str:supp_name>/', support.as_view(), name = 'support_url'),
	path('connect/', connect.as_view(), name = 'connect_url'),
	path('connect/send/', SendConnect.as_view(), name = 'send_connect'),
	path('payment/', payment.as_view(), name = 'payment_url'),
	path('cards_payment/', cards_payment.as_view(), name = 'cards_payment_url'),
	path('stock/', spec_stock.as_view(), name = 'spec_stock_url')
]
