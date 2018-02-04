from django.shortcuts import render_to_response
from metalconstr.models import Category, Construction


def index(request):
	args = {}
	args['test']="работает"
	return render_to_response('index.html', args)

def contact(request):
	args = {}
	return render_to_response('contact.html', args)

def mangal(request):
	args = {}
	args['mangal_text'] = "Мангалы"
	return render_to_response('mangal.html', args)

def naves(request):
	args = {}
	args['naves_text'] = "Навесы"
	return render_to_response('naves.html', args)

def vorota_kalitki(request):
	args = {}
	args['vorota_text'] = "Ворота и калитки"
	return render_to_response('vorota_kalitki.html', args)

def ritual(request):
	args = {}
	args['ritual_text'] = "Ритуал"
	return render_to_response('ritual.html', args)

def ritual(request):
	args = {}
	args['pandus_text'] = "Ритуал"
	return render_to_response('pandus.html', args)

def sitemap(request):
    args = {}
    args['sitemap'] = " "
    return render_to_response('sitemap.xml', args)