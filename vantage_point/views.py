import json
import uuid
import urllib
import datetime
import re 
import requests # for setting cookies
import base64

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from django.utils import timezone
from django.contrib import auth
#from django.forms.util import ErrorList
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

#import requests

from vantage_point.util import *
def simple_page(template):
	def handler(request):
	    return renderWithNav(request, template)
	return handler

verified_user_codes = []
verified_user_codes.extend([
    {'code':'b0ss', 'response' : 'OK', 'expire' : 'none'},
    {'code':'RaiseTheBar', 'response' : 'OK_SKIP', 'user' : 'RipStandard', 'expire' : '04/09/2018 + 7'},
    {'code':'GoldStandard', 'response' : 'OK_SKIP', 'user' : 'Within', 'expire' : '04/09/2018 + 7'},
])
	
def verify_account(request, code):

    response = "Failed"	
    for o in verified_user_codes:
	if o['code'] == code:
	    response = o['response'] + "|" + str(verified_user_codes)	
    return HttpResponse(response)

def verify_code(request):
    if request.method == 'POST':
        print str(request.POST)
        code = request.POST['code']
        # print "req:" + pretty_request(request) # request.POST['code']
        for o in verified_user_codes:
            if o['code'] == code:
                return json_response({'success':True})
                print "hi"
        print "hello: "+code	
        return json_response({'success':False})
    else:
        return HttpResponse("nope")

def home(request):
    obj = {}
    return render(request, "home.html", obj)

def survey_pre(request):
    obj = {}
    return render(request, "survey_pre.html", obj)



def start(request):
    obj = {}
    return renderWithNav(request, "start.html", obj)

def file_a(request):
    return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")

def file_b(request):
    return HttpResponse("Z9DF236bXRfXjvGlUflaI98PMWAKsG9qpGnrDXllb2o.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")	



