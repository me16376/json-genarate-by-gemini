# -*- coding: utf-8 -*-
import fitz
import glob
import os
import re

# Load parsed raw units from PDFs
pdf_files = sorted(glob.glob('computer probidhan - 2022/*.pdf'))

def get_text_from_pdf_pages(pdf_path, start_page, end_page):
    doc = fitz.open(pdf_path)
    text = ""
    for p in range(start_page - 1, min(len(doc), end_page)):
        text += doc[p].get_text('text') + "\n"
    return text

# We will build comprehensive, official chapter-by-chapter mapping for BPSC technical syllabus.txt
print("Building BPSC technical syllabus.txt generator...")
