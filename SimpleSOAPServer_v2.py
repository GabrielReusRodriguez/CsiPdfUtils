#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CsiPdfUtils_services import PdfMerge_ServiceLocator, PdfMerge_BindingSOAP
import sys
import random
from ZSI.ServiceContainer import AsServer
from Maxim_services_server import *



loc = PdfMerge_ServiceLocator()
port = loc.getPdfMerge_PortType()


resp = port.merge2Pdfs(request)
