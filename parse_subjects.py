# -*- coding: utf-8 -*-
import fitz
import glob
import os
import re

pdf_files = sorted(glob.glob('computer probidhan - 2022/*.pdf'))

def parse_subject_sections(pdf_path):
    doc = fitz.open(pdf_path)
    subjects = []
    
    # Identify pages where each subject starts
    for pno in range(len(doc)):
        text = doc[pno].get_text('text')
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        
        # Check for Subject Code & Name
        for i, line in enumerate(lines):
            # Matches 5-digit subject code like 28511, 26831, 28542, etc.
            if re.match(r'^(285\d\d|268\d\d|267\d\d|666\d\d|259\d\d)$', line):
                code = line
                # Look for name nearby
                name = ""
                for j in range(max(0, i-4), min(len(lines), i+6)):
                    cand = lines[j]
                    if cand != code and not re.match(r'^\d+$', cand) and len(cand) > 3:
                        if not any(k in cand.lower() for k in ['subject', 'code', 'probidhan', 'period', 'credit', 'marks', 'theory', 'practical', 'assessment']):
                            name = cand
                            break
                subjects.append({
                    'code': code,
                    'name': name,
                    'page': pno,
                    'file': os.path.basename(pdf_path)
                })
                break
    return subjects

all_subjs = []
for pf in pdf_files:
    subjs = parse_subject_sections(pf)
    all_subjs.extend(subjs)

print(f"Total detected subjects across all PDFs: {len(all_subjs)}")
for s in all_subjs:
    print(f"[{s['file']} P.{s['page']+1}] Code: {s['code']} - {s['name']}")
