# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {'index' : 'active'})

def scan(request):
    return render(request, 'scan.html', {'scan' : 'active'})

def ssh(request):
    return render(request, 'ssh.html', {'ssh' : 'active'})

def vtscan(request):
    return render(request, 'virustotal.html', {'vtscan' : 'active'})