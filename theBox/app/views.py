# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .const import VERSION, OS
from tools.vT import vT
import os

# Create your views here.
#Index
def index(request):
    return render(request, 'index.html', {'index' : 'active', \
    										'version' : VERSION, \
    										'os' : OS, })

#KicomAV
def scan(request):
    return render(request, 'scan.html', {'scan' : 'active'})

#SSHParamiko
def ssh(request):
    return render(request, 'ssh.html', {'ssh' : 'active'})

#VTScan
def vtscan(request, mode=None, data=None):
	if(request.method == 'POST'):
		result = request.POST['mode'] + " " + request.POST['data']
		return HttpResponse(result)
	else:
		return render(request, 'virustotal.html', {'vtscan' : 'active'})

#Command
def cmd(request, cmd=None):
	result = os.popen(cmd).read()
	return HttpResponse(result)