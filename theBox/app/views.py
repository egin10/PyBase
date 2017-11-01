# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .const import VERSION, OS, KICOMAV, VT_API_KEY, KIBANA
from tools.vT import ipReport, domainReport, urlScan, urlReport
import os

# Create your views here.
#Index
def index(request):
    return render(request, 'index.html', {'index' : 'active', \
    										'version' : VERSION, \
    										'os' : OS, 'kibana' : KIBANA})

#KicomAV
def scan(request):
	if(request.method == 'POST'):
		path = request.POST['path']
		opt = request.POST['options']
		cmd = KICOMAV + " " + path + " " + opt
		result = os.popen(cmd).read()
		return render(request, 'scan.html', {'scan' : 'active', 'cDir': os.getcwd(), \
												'result': result })
	else:
		return render(request, 'scan.html', {'scan' : 'active', 'cDir': os.getcwd()})

#VTScan
def vtscan(request):
	if(request.method == 'POST'):
		#result = request.POST['mode'] + " " + request.POST['data']
		if(request.POST['mode'] == 'ip'):
			ip = request.POST['data']
			result = ipReport(ip, VT_API_KEY)
			return JsonResponse(result, safe=False)

		elif(request.POST['mode'] == 'domain'):
			domain = request.POST['data']
			result = domainReport(domain, VT_API_KEY)
			return JsonResponse(result, safe=False)

		elif(request.POST['mode'] == 'url'):
			url = request.POST['data']
			scan = urlScan(url, VT_API_KEY)
			result = urlReport(scan['scan_id'], VT_API_KEY)
			return JsonResponse(result, safe=False)
	else:
		return render(request, 'virustotal.html', {'vtscan' : 'active'})

#Command
def cmd(request, path=None):
	cmd = KICOMAV + " " + path
	result = os.popen(cmd).read()
	return HttpResponse(result)