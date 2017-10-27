# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .const import *
import platform
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
def vtscan(request):
    return render(request, 'virustotal.html', {'vtscan' : 'active'})

#Command
def cmd(request, cmd):
	result = os.popen(cmd).read()
	return HttpResponse(result)