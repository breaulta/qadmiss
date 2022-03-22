from django.urls import path

from . import views

app_name = 'admiss'
urlpatterns = [
	path('', views.index, name='index'),
	path('app/', views.app, name='app'),
	path('submit_app/', views.submit_app, name='submit_app'),
	path('app_submitted/', views.app_submitted, name='app_submitted'),
]
