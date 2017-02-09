#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Imports

import sys
import random
from ZSI.ServiceContainer import AsServer
from CsiPdfUtils_services_server import *

quotations = [ "All men by nature desire knowledge. Aristotle",
"Man is by nature a political animal. Aristotle",
"Many people would sooner die than think. In fact they do. Russell",
"Science may be described as the art of systematic over-simplification. Popper",
"The smallest minority on earth is the individual. Rand",
"The limits of my language mean the limits of my world. Wittgenstein" ]

#class Service(PdfMerge_BindingSOAP):
#    def soap_ForToday(self, ps):
#        response = ns0.PdfMergeResponse_Def("","").pyclass()

        #response = ns0.ForTodayResponse_Dec().pyclass()
        #response.ForTodayResult = random.choice(quotations)

#        return response


if __name__ == "__main__" :
#    AsServer(8080, (Service("cwlh"),))
    AsServer(8080, (PdfMerge_ServiceLocator,))
