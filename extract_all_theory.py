# -*- coding: utf-8 -*-
import fitz
import glob
import os
import re

pdf_files = sorted(glob.glob('computer probidhan - 2022/*.pdf'))

def extract_subject_details(pdf_path):
    doc = fitz.open(pdf_path)
    # Collect all pages text
    pages_text = [doc[p].get_text('text') for p in range(len(doc))]
    
    # We want to find each subject block
    # Start of subject is usually marked by:
    # "Subject Code" followed by 5-digit code or Course Structure table
    # And then "DETAILED SYLLABUS (THEORY)"
    
    subjects = []
    
    # Let's search for "DETAILED SYLLABUS (THEORY)" or "DETAILED SYLLABUS(THEORY)"
    for pno, ptxt in enumerate(pages_text):
        if re.search(r'DETAILED\s+SYLLABUS\s*\(THEORY\)', ptxt, re.IGNORECASE):
            # Find subject name and code in previous pages
            code = "Unknown"
            name = "Unknown"
            for back_p in range(pno, max(-1, pno-4), -1):
                btxt = pages_text[back_p]
                m_code = re.search(r'\b(285\d\d|268\d\d|267\d\d|658\d\d|259\d\d|258\d\d|257\d\d|290\d\d|210\d\d)\b', btxt)
                if m_code:
                    code = m_code.group(1)
                    # Find subject name
                    lines = [l.strip() for l in btxt.split('\n') if l.strip()]
                    for idx, line in enumerate(lines):
                        if line == code:
                            # look around
                            for j in range(max(0, idx-4), min(len(lines), idx+6)):
                                cand = lines[j]
                                if cand != code and len(cand) > 3 and not re.match(r'^\d+$', cand):
                                    if not any(k in cand.lower() for k in ['subject', 'code', 'period', 'credit', 'marks', 'assessment', 'continuous', 'final', 'probidhan', 'week', 'total', 'grand', 'theory', 'practical']):
                                        name = cand
                                        break
                            break
                    break
            
            # Now extract theory units from pno onwards until "DETAILED SYLLABUS (PRACTICAL)"
            theory_text = ""
            for forward_p in range(pno, min(len(pages_text), pno+10)):
                f_txt = pages_text[forward_p]
                if forward_p > pno and re.search(r'DETAILED\s+SYLLABUS\s*\(PRACTICAL\)', f_txt, re.IGNORECASE):
                    # reached practical
                    practical_idx = re.search(r'DETAILED\s+SYLLABUS\s*\(PRACTICAL\)', f_txt, re.IGNORECASE).start()
                    theory_text += f_txt[:practical_idx] + "\n"
                    break
                elif forward_p > pno and re.search(r'DETAILED\s+SYLLABUS\s*\(THEORY\)', f_txt, re.IGNORECASE):
                    # next subject theory started
                    break
                else:
                    theory_text += f_txt + "\n"
            
            subjects.append({
                'code': code,
                'name': name,
                'page': pno + 1,
                'file': os.path.basename(pdf_path),
                'theory_raw': theory_text
            })
            
    return subjects

all_extracted = []
for pf in pdf_files:
    subjs = extract_subject_details(pf)
    all_extracted.extend(subjs)

print(f"Total extracted theory syllabi: {len(all_extracted)}")
for s in all_extracted:
    print(f"[{s['file']} P.{s['page']}] {s['code']} - {s['name']} (Raw length: {len(s['theory_raw'])})")
