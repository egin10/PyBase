# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.
myModels = [Data, Detail, Encoding, Event, Icmphdr,\
            Iphdr, Opt, Reference, ReferenceSystem, \
            Schema, Sensor, SigClass, SigReference, Signature, Tcphdr, Udphdr]

admin.site.register(myModels)
