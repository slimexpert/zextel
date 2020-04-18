from django.urls import path

from . import views

app_name = 'about'
urlpatterns = [
	path('', views.main, name = 'about'),
	path('news/', views.news, name = 'news'),
	path('news/<int:new_id>/', views.detail, name = 'detail'),
	path('docs/', views.docs, name = 'docs'),
	path('jobs/', views.jobs, name = 'jobs'),
]