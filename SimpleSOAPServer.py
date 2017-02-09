#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ZSI.ServiceContainer import ServiceContainer, SOAPRequestHandler, SOAPContext, _contexts, _Dispatch
#from ZSI.ServiceContainer import *
#import ZSI.ServiceContainer

from ZSI import ParseException, FaultFromException
from ZSI import ParsedSoap
from CsiPdfUtils_services_server import PdfMerge_Service
from CsiPdfUtils_services_types import *
from CsiPdfUtils_services import PdfMerge_ServiceLocator, PdfMerge_BindingSOAP, PdfMergeRequest, PdfMergeResponse

from CsiPdfUtils import PdfMerger

import urlparse, sys, thread,re

import os

class MySOAPRequestHandler(SOAPRequestHandler):

    def _getOperacio(self, parsedSoap):
        operacio = parsedSoap.body_root.getElementsByTagName("operacio").item(0).firstChild.nodeValue
        return operacio

    def _getLlistaPdfs(self, parsedSoap):
        llistatNodeList = parsedSoap.body_root.getElementsByTagName("llistaPdfs_b64")
        llistatPDFs = []
        if llistatNodeList.length > 0:
            llistatPdfsNodeList = parsedSoap.body_root.getElementsByTagName("pdf_b64")
            for i in range(llistatPdfsNodeList.length):
                pdf = llistatPdfsNodeList.item(i).firstChild.nodeValue
                llistatPDFs.append(pdf)
                print "pdf: "+pdf+"\n"
        return llistatPDFs

    def do_GET(self):
    #Return the WSDL file. We expect to get the location from the
    #invocation URL ("path").
        #wsdlfile = os.path.join('.', self.path.replace('/', "", 1) + ".wsdl")
        wsdlfile = os.path.join('.', "./ws.wsdl")
        print ">>>>> using wsdl file", wsdlfile
        wsdl = open(wsdlfile).read()
        self.send_xml(wsdl)

    def do_POST(self):
        soapAction = self.headers.getheader('SOAPAction')
        post = self.path
        if not post:
            raise PostNotSpecified('HTTP POST not specified in request')
        if soapAction:
            soapAction = soapAction.strip('\'"')
        post = post.strip('\'"')
        try:
            ct = self.headers['content-type']
            if ct.startswith('multipart/'):
                cid = resolvers.MIMEResolver(ct, self.rfile)
                xml = cid.GetSOAPPart()
                ps = ParsedSoap(xml, resolver=cid.Resolve)
            else:
                length = int(self.headers['content-length'])
                xml = self.rfile.read(length)
                ps = ParsedSoap(xml)

        except ParseException, e:
            self.send_fault(FaultFromZSIException(e))
        except Exception, e:
            # Faulted while processing; assume it's in the header.
            self.send_fault(FaultFromException(e, 1, sys.exc_info()[2]))
        #Else del try catch
        else:
            # Keep track of calls
            thread_id = thread.get_ident()
            _contexts[thread_id] = SOAPContext(self.server, xml, ps,
                                               self.connection,
                                               self.headers, soapAction)

            try:
                _Dispatch(ps, self.server, self.send_xml, self.send_fault,
                    post=post, action=soapAction)
            except Exception, e:
                self.send_fault(FaultFromException(e, 0, sys.exc_info()[2]))

            # Clean up after the call
            if thread_id in _contexts:
                del _contexts[thread_id]

# Copied from ZSI.ServiceContainer, extended to instantiate with a custom
# request handler

def AsServer(port=80, services=(), RequestHandlerClass=SOAPRequestHandler):
    address = ('172.28.105.55', port)
    sc = ServiceContainer(address, RequestHandlerClass=RequestHandlerClass)
    for service in services:
        path = service.getPost()
        sc.setNode(service, path)
    sc.serve_forever()

AsServer(port=8080, services=[PdfMerge_Service()], RequestHandlerClass=MySOAPRequestHandler)
