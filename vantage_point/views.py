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
    survey_items = [
        {
            "number" : 1,
            "question" : "How transparent do you feel your company's policies are around sexual harassment?",
            "options" : [1,2,3,4,5],
            "options_class" : "squareContainer",
            "options_class_li" : "square", 
        }, { 
            "number" : 2,
            "question" : "Does your current corporate climate discourage sexual harassment?",
            "options" : [1,2,3,4,5],
            "options_class" : "squareContainer",
            "options_class_li" : "square", 
            
        },{ 
            "number" : 3,
            "question" : "How gender positive (gender friendly) do you feel your current office culture is?",
            "options" : [1,2,3,4,5],
            "options_class" : "squareContainer",
            "options_class_li" : "square", 
            
        },{ 
            "number" : 4,
            "question" : "What do you feel your current workplace's scale of gender parity is?",
            "options" : [1,2,3,4,5],
            "options_class" : "squareContainer",
            "options_class_li" : "square", 
            
         },{ 
            "number" : 5,
            "display_trigger" : "display_trigger", #jquery hook
            "display_trigger_elements" : "6,7",
            "question" : "Have you previously encountered an experience related to sexual harassment where you feel you could have intervened?",
            "options_class" : "dynamicContainer",
            "options_class_li" : "dynamic", 
            "options" : ["YES","NO","Kind of", "I don't know"],
            
          },{ 
            "display_status" : "none",
            "number" : "6",
            "question" : "Do you feel you took the right action?",
            "options_class" : "dynamicContainer2",
            "options_class_li" : "dynamic", 
            "options" : ["YES","NO","I don't know"],
            
          },{ 
            "display_status" : "none",
            "number" : "7",
            "question" : "Do you feel you acted at the appropriate time?",
            "options_class" : "dynamicContainer2",
            "options_class_li" : "dynamic", 
            "options" : ["YES","NO", "I don't know"],
        },{ 
            "number" : 8,
            "question" : "How confident do you feel in your ability to determine if a situation might be sexual harassment, and when to intervene?",
            "options" : [1,2,3,4,5],
            "options_class" : "squareContainer",
            "options_class_li" : "square", 
             
         },{ 
            "number" : 9,
            "question" : "How confident do you feel in your ability to know how to intervene if a situation might be sexual harassment?",
            "options" : [1,2,3,4,5],
            "options_class" : "squareContainer",
            "options_class_li" : "square", 
             
          },{ 
            "number" : 10,
            "question" : "What do you feel your level of agency is as a bystander in helping to prevent sexual harassment? (How empowered do you feel in your ability as a bystander to help prevent sexual harassment?",
            "options" : [1,2,3],
            "options_class" : "squareContainer",
            "options_class_li" : "square", 
             
        }, 
    ]
    obj['survey_items'] = survey_items 
    return render(request, "survey_pre.html", obj)



def start(request):
    obj = {}
    return renderWithNav(request, "start.html", obj)

def file_a(request):
    return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")

def file_b(request):
    return HttpResponse("Z9DF236bXRfXjvGlUflaI98PMWAKsG9qpGnrDXllb2o.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")	



