from django.urls import path

from . import views
from .views import *

app_name = 'tv'
urlpatterns = [
	path('', views.tv, name = 'tv'),
	path('smotreshka', views.smotreshka, name = 'smotreshka'),
	path('channel100', views.channel100, name = 'channel100'),
]
