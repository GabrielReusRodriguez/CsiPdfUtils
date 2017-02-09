
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from ConfigurationServer import ConfigurationServer

import Constants
import random


#Van con valor por defecto xq son opcionales.
def pdfUtilsDispatcher_logic(
						ADT_A01=None,
						ADT_A03=None,
						ADT_A11=None,
						ADT_A13=None,
						ADT_A31=None,
						ADT_A34=None,
						ADT_A40=None
						  ):
	#print "Hola!!"

	fileName = ""
	if random.randint(0,9) <= 4:
		fileName = Constants.HOME_DIR + '/TriatgeWS/responses/resp_ack.xml'
	else:
		fileName = Constants.HOME_DIR + '/TriatgeWS/responses/resp_ack_error.xml'
	f = open(fileName,"r")
	response = f.read()
	f.close
	return response


def pdfUtilsDispatcher_init():
	config =  ConfigurationServer()
	config.port = 8009
	config.nombre = "PdfUtils"
	config.dispatcher = SoapDispatcher(
		'pdfUtilsDispatcher',
		location = "http://localhost:8009",
		action = 'http://localhost:8009', #SOAPAction
#		namespace = "urn:hl7-org:v2xml", prefix = "ns0",
		namespace = "http://xml.apache.org/axis/wsdd/", prefix = "wsdd",
		trace = True,
		ns = True
	)

	config.dispatcher.register_function('pdfUtils',pdfUtilsDispatcher_logic,
		returns = {'pdfUtilsResp' : str},
		args = {
			'pdfUtilsReq' : {
				'operacio' : str,
				'llistaPdfs_b64' : [ { 'pdf_b64' : str} ]
			}


			print "Recibido!\n"
#			'ADT_A01' : str,
#			'ADT_A03' : str,
#			'ADT_A11' : str,
#			'ADT_A13' : str,
#			'ADT_A31' : str,
#			'ADT_A34' : str,
#			'ADT_A40' : str

			 }

#		args={'MSH' : 	{'MSH.1' : str,
#				 'MSH.2' : str,
#				 'MSH.3' : {'HD.1' : str},
#				 'MSH.4' : {'HD.1' : str},
#				 'MSH.5' : {'HD.1' : str},
#				 'MSH.6' : {'HD.1' : str},
#				 'MSH.7' : {'TS.1' : str},
#				 'MSH.9' : {'MSG.1' : str, 'MSG.2' : str},
#				 'MSH.10' : str,
#				 'MSH.11' : {'PT.1' : str},
#				 'MSH.12' : {'VID.1' : str},
#				 'MSH.13' : str,
#				 'MSH.16' : str,
#				 'MSH.18' : str
#				} ,
#			'PID' : {
#				'PID.3' : { 'CX.1' : str},
#				['PID.5' : { 'XPN.1' : str}]
#			},
#			'ORU_R30.VISIT': str,
#			'ORC' :	str,
#			'OBR' : str,
#			'ORU_R30.OBSERVATION' : str,
#		}
	)

#	config.dispatcher.register_function('Adder',adder,
#		returns = {'AddResult' : int},
#		args = {'a':int, 'b':int}
#	)

	return config
