#!/usr/bin/python2.7
from pysimplesoap.pysimplesoap.server import SoapDispatcher,SOAPHandler
#from BaseHTTPServer import HTTPServer
from http.server import HTTPServer

def adder(a,b):
	"Add two values"
	return a+b

dispatcher = SoapDispatcher(
	'my_dispatcher',
	location = "http://localhost:8008/",
	action = 'http://localhost:8008/', #SoapAction
	namespace = "http://example.com/sample.wsdl", prefix="ns0",
	trace = True,
	ns = True)


#register the user function

dispatcher.register_function('Adder', adder, 
	returns = {'AddResult' : int},
	args={ 'a' : int, 'b' : int})

print ("Starting server...")
httpd = HTTPServer(("",8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()

print ("Hola mundo!")

#https://code.google.com/p/pysimplesoap/wiki/SoapServer
