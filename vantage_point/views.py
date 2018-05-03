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


def create_session_id():
    return "WEB " + str(timezone.now()) + "_" + alphaencode((int)(1000000000 * random.random()))

def survey_pre(request):
    session_id = create_session_id()
    return survey_pre_session(request,session_id)

def survey_post(request):
    session_id = create_session_id()
    return survey_post_session(request,session_id)

def survey_pre_session (request,session_id):
    obj = {}
    # This is the format of the questions / data that will be linked to google spreadsheet
    # PRE SURVEY spreadsheet:
    # https://docs.google.com/spreadsheets/d/1gDoj6csj2vu2vOP3mMgQWwOZ3obktXMO30ZW71r075I/edit#gid=0
    # Note that it has a script to receive GET data by our survey_pre.js
    # Note that the form_field_id must exactly match the header columns of the spreadsheet for data to propagate correctly
    obj['survey_items'] = survey_items 
    obj['form_field_ids'] = ','.join([item['form_field_id'] for item in survey_items])
    obj['session_id'] = session_id 
    return render(request, "survey_pre.html", obj)

def survey_post_session (request,session_id):
    obj = {}
    # This is the format of the questions / data that will be linked to google spreadsheet
    # POST SURVEY spreadsheet:
    # https://docs.google.com/spreadsheets/d/1gDoj6csj2vu2vOP3mMgQWwOZ3obktXMO30ZW71r075I/edit#gid=0
    obj['survey_items'] = survey_items 
    obj['form_field_ids'] = ','.join([item['form_field_id'] for item in survey_items])
    obj['session_id'] = session_id 
    return render(request, "survey_post.html", obj)



def start(request):
    obj = {}
    return renderWithNav(request, "start.html", obj)

def file_a(request):
    return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")

def file_b(request):
    return HttpResponse("Z9DF236bXRfXjvGlUflaI98PMWAKsG9qpGnrDXllb2o.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")	


survey_items = [
    {
        "number" : 1,
        "form_field_id" : "transparency",
        "required" : "true",
        "question" : "How transparent do you feel your company's policies are around sexual harassment?",
        "scale" : True,
        "options" : [1,2,3,4,5],
        "options_class" : "squareContainer",
        "options_class_li" : "square", 
    }, { 
        "number" : 2,
        "form_field_id" : "discouragement",
        "required" : "true",
        "question" : "Does your current corporate climate discourage sexual harassment?",
        "scale" : True,
        "options" : [1,2,3,4,5],
        "options_class" : "squareContainer",
        "options_class_li" : "square", 
        
    },{ 
        "number" : 3,
        "form_field_id" : "genderPositive",
        "required" : "true",
        "question" : "How gender positive (gender friendly) do you feel your current office culture is?",
        "scale" : True,
        "options" : [1,2,3,4,5],
        "options_class" : "squareContainer",
        "options_class_li" : "square", 
        
    },{ 
        "number" : 4,
        "form_field_id" : "genderParity",
        "required" : "true",
        "question" : "What do you feel your current workplace's scale of gender parity is?",
        "scale" : True,
        "options" : [1,2,3,4,5],
        "options_class" : "squareContainer",
        "options_class_li" : "square", 
        
     },{ 
        "number" : 5,
        "form_field_id" : "previousEncounter",
        "required" : "true",
        "display_trigger" : "display_trigger", #jquery hook
        "display_trigger_elements" : "5a,5b",
        "question" : "Have you previously encountered an experience related to sexual harassment where you feel you could have intervened?",
        "options_class" : "dynamicContainer",
        "options_class_li" : "dynamic", 
        "options" : ["YES","NO","Kind of", "I don't know"],
        
      },{ 
        "display_status" : "none",
        "form_field_id" : "previousEncounterRightAction",
        "required" : "false",
        "number" : "5a",
        "question" : "Do you feel you took the right action?",
        "options_class" : "dynamicContainer2",
        "options_class_li" : "dynamic", 
        "options" : ["YES","NO","I don't know"],
        
      },{ 
        "display_status" : "none",
        "form_field_id" : "previousEncounterRightTime",
        "required" : "false",
        "number" : "5b",
        "question" : "Do you feel you acted at the appropriate time?",
        "options_class" : "dynamicContainer2",
        "options_class_li" : "dynamic", 
        "options" : ["YES","NO", "I don't know"],
    },{ 
        "number" : 6,
        "form_field_id" : "confidenceToIntervene",
        "required" : "true",
        "question" : "How confident do you feel in your ability to determine if a situation might be sexual harassment, and when to intervene?",
        "options" : [1,2,3,4,5],
        "scale" : True,
        "options_class" : "squareContainer",
        "options_class_li" : "square", 
         
     },{ 
        "number" : 7,
        "form_field_id" : "confidenceToInterveneRightAction",
        "required" : "true",
        "question" : "How confident do you feel in your ability to know how to intervene if a situation might be sexual harassment?",
        "options" : [1,2,3,4,5],
        "scale" : True,
        "options_class" : "squareContainer",
        "options_class_li" : "square", 
         
      },{ 
        "number" : 8,
        "form_field_id" : "levelOfAgency",
        "required" : "true",
        "question" : "What do you feel your level of agency is as a bystander in helping to prevent sexual harassment? (How empowered do you feel in your ability as a bystander to help prevent sexual harassment?",
        "options" : [1,2,3],
        "scale" : True,
        "options_class" : "squareContainer",
        "options_class_li" : "square", 
         
    }, 
]
