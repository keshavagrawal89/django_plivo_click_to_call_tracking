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
from django.db import connection
import datetime
import requests

def main_page(request):
	variables = {'':''}
	return render_to_response('main_page.html', RequestContext(request, variables))
	
	
def manage_lead(request):
    	lead_numbers = []
    	if request.method == "POST":
        	lead_number = request.POST.get('lead-number')
        	lead_zone = request.POST.get('lead-zone')

        	save_lead_number(lead_number, lead_zone)

    	lead_numbers = get_lead_numbers()
    	variables = {'lead_numbers':lead_numbers}

    	return render_to_response('manage_lead.html', RequestContext(request, variables))
    	
def get_lead_numbers():
    	lead_zone = LeadNumberZones.objects.values('lead_number','zone').order_by('lead_number')
    	return lead_zone.values_list('lead_number','zone')
    	
def save_lead_number(lead_number, lead_zone):
    	lead_number_zone = LeadNumberZones(lead_number = lead_number, zone = lead_zone)
    	lead_number_zone.save()

def track_lead(request):
	cursor = connection.cursor()
	#Yeah I find direct query better sometimes than ORM. Handle SQL injections :)
	cursor.execute("select count(*), to_number, date_of_call from clicktocall_lead group by date_of_call,to_number order by date_of_call, to_number")

	res = cursor.fetchall()

	list_of_numbers = []
	list_of_dates = []
	list_of_tuples = []

	final_list = []

	for row in res:
		list_of_numbers.append(row[1])
		list_of_dates.append(row[2])

	list_of_tuples = res

	list_of_numbers = list(set(list_of_numbers))
	list_of_dates = list(set(list_of_dates))
	
	list_of_dates.sort()
	#Since list_of_numbers is a list of integers so no need of sorting as set() wont mess the sorting.

	for number in list_of_numbers:
		final_list.append([])

	for call_date in list_of_dates:
		for item in final_list:
			item.append(0)
		index_of_date = list_of_dates.index(call_date)
		for tuple_ in list_of_tuples:
			if call_date in tuple_:
				index_of_number = list_of_numbers.index(tuple_[1])
				final_list[index_of_number][index_of_date] = tuple_[0]

	print final_list

	date_list = list_of_dates
	variables = {'date_list':date_list, 'numbers':list_of_numbers, 'final_list':final_list}
	return render_to_response('chart.html', RequestContext(request, variables))


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

def capture_report(request):
    print "I am here"
    if request.method == "POST":
        encoded_img_string = request.POST.get('file')
    if encoded_img_string != '' and encoded_img_string is not None:
        print encoded_img_string[encoded_img_string.index("base64,") + len("base64,"):]
        send_report(encoded_img_string[encoded_img_string.index("base64,") + len("base64,"):])
    return HttpResponse("OK");


def send_report(encoded_img_string):
    fh = open("/tmp/imageToBeSaved.png","wb")
    fh.write(encoded_img_string.decode('base64'))
    fh.close()
    mail_report()

def mail_report():
    from_email = settings.FROM_EMAIL
    to_email = settings.TO_EMAIL
    mailgun_token = settings.MAILGUN_TOKEN
    mail_subject = "Report Capture"
    domain = settings.MAILGUN_DOMAIN

    body = "Here is your captured report. Please find the attachment for the same."
    url = "https://api.mailgun.net/v2/%s/messages" % (domain)

    send_mail_response = requests.post(
        url,
        auth=("api", mailgun_token),
        files = {"attachment": open("/tmp/imageToBeSaved.png", "rb")},
        data = {
            "from": from_email,
            "to": to_email,
            "subject": mail_subject,
            "text": body,
        }
    )
    print send_mail_response
    return send_mail_response

	

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
	call_date = datetime.datetime.date(datetime.datetime.now())
	call_duration = Decimal(request.POST.get('Duration'))
	caller = int(request.POST.get('From'))
	agent_number = int(request.POST.get('To'))
	lead = Lead(from_number = caller, to_number = agent_number, duration = call_duration, date_of_call = call_date)
	lead.save()
	return HttpResponseRedirect('/')

