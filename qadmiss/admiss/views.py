from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Admiss_app

def index(request):
	template = loader.get_template('admiss/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def app(request):
	template = loader.get_template('admiss/app.html')
	context = {}
	return HttpResponse(template.render(context, request))

def submit_app(request):
	app = Admiss_app(first_name=request.POST['first_name'], middle_name=request.POST['middle_name'], last_name=request.POST['last_name'])
	app.save()
	return HttpResponseRedirect(reverse('admiss:app_submitted', args=()))

def app_submitted(request):
	template = loader.get_template('admiss/submitted.html')
	context = {}
	return HttpResponse(template.render(context, request))


