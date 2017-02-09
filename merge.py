#!/usr/bin/env python
# -*- coding: utf-8 -*-
from CsiPdfUtils.PdfMerger import PdfMerger

file_a = "./a.pdf"
file_b = "./b.pdf"
file_output = "./res.pdf"

print "Inicio"
pdfMerger = PdfMerger()
pdfMerger.add_pdf_file(file_a)
pdfMerger.add_pdf_file(file_b)
pdfMerger.write_output_str_file(file_output)

print "Final"
