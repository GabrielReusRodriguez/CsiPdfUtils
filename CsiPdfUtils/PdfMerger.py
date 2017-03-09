# -*- coding: utf-8 -*-
#import PdfUtil
from PdfUtil import PdfUtil
from PyPDF2 import PdfFileMerger
import cStringIO
import base64

class PdfMerger(PdfUtil):
    """Clase utilizada para fusionar PDfs"""
    def __init__(self):
        self.merger = PdfFileMerger()

    def add_pdf_b64(self,b64_pdf):
        str_pdf = base64.b64decode(b64_pdf)
        stream_pdf = cStringIO.StringIO(str_pdf)
        self.merger.append(stream_pdf)

    def add_pdf_file(self,file_pdf):
        fichero = open(file_pdf,"rb")
        str_pdf = fichero.read()
        fichero.close()
        b64_pdf = base64.b64encode(str_pdf)
        self.add_pdf_b64(b64_pdf)

    def write_output_b64(self):
        stream_pdf = cStringIO.StringIO()
        self.merger.write(stream_pdf)
        b64_output = base64.b64encode(stream_pdf.getvalue())
        return b64_output

    def write_output_str(self):
        stream_pdf = cStringIO.StringIO()
        self.merger.write(stream_pdf)
        return strean_pdf.getvalue()

    def write_output_str_file(self,file_pdf_out):
        self.merger.write(file_pdf_out)

    def write_output_b64_file(self,file_pdf_out):
        stream_str = cStringIO.StringIO()
        self.merger.write(stream_str)
        b64_output = base64.b64encode(stream_str.getvalue())
        fichero = open(file_pdf_out, "wb")
        fichero.write(b64_output)
        fichero.close()
