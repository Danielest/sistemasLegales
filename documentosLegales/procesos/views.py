from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import Context
from datetime import datetime
from models import *
#from forms import *



def procesos(request):
	procesos = Proceso.objects.all()
	template = 'procesos/procesos.html'
	return render_to_response(template, locals())

def procesosEnDesarrollo(request):
	template = 'procesos/enDesarrollo.html'
	return render_to_response(template, locals())

def historico(request):
	template = 'procesos/historico.html'
	return render_to_response(template, locals())

def clientes(request):
	template='procesos/clientes.html'
	return render_to_response(template, locals())

def miPerfil(request):
	template = 'procesos/miperfil.html'
	return render_to_response(template, locals())





