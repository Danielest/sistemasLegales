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


def home(request):
	return HttpResponse('Este es mi super sistema de documentos legales')






