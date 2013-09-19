# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from decimal import Decimal
import plivo
from django.views.decorators.csrf import csrf_exempt
from clicktocall.views import Lead


def main_page(request):
	variables = {'':''}
	return render_to_response('main_page.html', RequestContext(request, variables))


def send_call(request):
	if request.method == 'POST':
		customer_number = request.POST.get('customer-number')
		send_call_to_agent(customer_number)

		return HttpResponseRedirect('/')
	else:
		return "Go back bugger!"



def send_call_to_agent(customer_number):
	plivo_api = get_plivo_api()
	params = {
		'from':customer_number,
		'to':1XXXXXXXXX,
		'answer_url':'http://server_url/dialagent/',
		'hangup_url':'http://server_url/hangup_lead/',
		'answer_method':'POST',
	}
	plivo_api.make_call(params)
	return "OK"
		


def get_plivo_api():
	auth_id = settings.AUTH_ID
	auth_token = settings.AUTH_TOKEN

	return plivo.RestAPI(auth_id = auth_id, auth_token = auth_token)

@csrf_exempt
def dialagent(request):
	customer_number = request.POST.get('From')
	agent_number = request.POST.get('To')
	print customer_number
	print agent_number
	resp = plivo.XML.Response()
	resp.addSpeak("You are going to be connected with one of the visitor on the website.")
	resp.addDial(callerId = agent_number).addNumber(customer_number)
	
	return HttpResponse(resp.to_xml(),mimetype='text/xml')

@csrf_exempt
def hangup_lead(request):
	call_duration = Decimal(request.POST.get('Duration'))
	caller = int(request.POST.get('From'))
	agent_number = int(request.POST.get('To'))
	
	lead = Lead(from_number = caller, to_number = agent_number, duration = call_duration)
	return HttpResponseRedirect('/')

