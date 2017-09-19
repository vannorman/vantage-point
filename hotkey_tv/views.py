import json
import uuid
import urllib
import datetime
import re 
import requests # for setting cookies

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

from hotkey_tv.util import *
def simple_page(template):
	def handler(request):
		return renderWithNav(request, template)
	return handler


def home(request):
	obj = {}
	obj['portfolio'] = []
	obj['portfolio'].append({
		"title" : "Super Math World",
		"link" : "https://supermathworld.com",
		"year" : "2016 - 2017",
		"position" : "Founder, CTO",
		"subtitle" : "A WebGL based math sandbox",
		"description" : "I built a content generation platform on top of an educational math game. This allows users to edit, create, and share content from directly inside the application, natively in a web browser.",
		"responsibilities" : 
		[
				"Framework architecture",
				"Game design",
				"Web backend using python/django/SQL",
				"SysAdmin using AWS EC2, Route53, SSL, S3, and Cloudfront",
				"Payment system using Stripe",
		],
		"videos" : [
				{ "source": "https://player.vimeo.com/video/219464062", "image" : "smw_1.jpg" }
		],
		"images" : ["smw_2.jpg","smw_4.jpg","smw_3.jpg"],	
		})
	obj['portfolio'].append({
		"title" : "Mathbreakers",
		"link" : "https://mathbreakers.com",
		"year" : "2013 - 2015",
		"position" : "Co-founder",
		"subtitle" : "A math puzzle platformer for grades 2 - 8",
		"description" : "We partnered with some of the biggest names in math education, including Dan Meyer and Jo Boaler, to discover the intersection between 3-D action gaming and elementary mathematics. The result was a truly immersive, stress free math game that kids love to play.",
		"responsibilities" : ["Game design","Game development","Playtesting","Educational content","Business development"],
		"videos" : [
				{ "source": "https://player.vimeo.com/video/73754523", "image" : "mb_1.jpg" }
		],
		"images" : ["mb_2.jpg","mb_3.jpg","mb_4.jpg"],	
		})
	obj['portfolio'].append({
		"title" : "Mouse Brain Explorer",
		"link" : "https://3scan.com",
		"year" : "2015",
		"position" : "Contractor",
		"subtitle" : "Fly through a real mouse brain",
		"description" : "Using a cubic centimeter of a mouse brain imaged with 3Scan's equipment, I made a virtual reality tour through the vasculature and a mini-game to destroy blood clots. This was on exhibit during the Exploratorium's science week in 2015.",
		"responsibilities" : ["Simulation developer","Oculus, PC, and XBox controller setup"],
		"videos" : [
				{ "source": "https://player.vimeo.com/video/117482417", "image" : "3scan_1.jpg" }
		],
		"images" : [],	
		})



	return renderWithNav(request,'home.html', obj)

def file_a(request):
	return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")

def file_b(request):
	return HttpResponse("Z9DF236bXRfXjvGlUflaI98PMWAKsG9qpGnrDXllb2o.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")	



