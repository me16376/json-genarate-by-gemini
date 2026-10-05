# -*- coding: utf-8 -*-
import fitz
import glob
import os
import re

pdf_files = sorted(glob.glob('computer probidhan - 2022/*.pdf'))

def parse_units_from_text(theory_text):
    units = []
    lines = [l.strip() for l in theory_text.split('\n') if l.strip()]
    curr_unit = None
    
    for l in lines:
        m_u = re.match(r'^(?:Unit\s*)?(\d{1,2})\s*$', l)
        m_sub = re.match(r'^(\d{1,2})\.(\d{1,2})\s+(.*)$', l)
        
        if m_sub:
            u_n, s_n, desc = m_sub.groups()
            if curr_unit and curr_unit['num'] == u_n:
                curr_unit['topics'].append(f"{u_n}.{s_n} {desc}")
            else:
                ex = [u for u in units if u['num'] == u_n]
                if ex:
                    ex[-1]['topics'].append(f"{u_n}.{s_n} {desc}")
                else:
                    curr_unit = {'num': u_n, 'title': '', 'topics': [f"{u_n}.{s_n} {desc}"]}
                    units.append(curr_unit)
        elif m_u:
            u_n = m_u.group(1)
            curr_unit = {'num': u_n, 'title': '', 'topics': []}
            units.append(curr_unit)
        elif curr_unit and not curr_unit['title'] and len(l) > 3 and not re.match(r'^\d', l):
            if not any(k in l.lower() for k in ['class', 'period', 'marks', 'final', 'unit', 'topics', 'content']):
                curr_unit['title'] = l
                
    return units

# Extract all courses
course_map = {}

for pf in pdf_files:
    doc = fitz.open(pf)
    pages_text = [doc[p].get_text('text') for p in range(len(doc))]
    
    for pno, ptxt in enumerate(pages_text):
        if re.search(r'DETAILED\s+SYLLABUS\s*\(THEORY\)', ptxt, re.IGNORECASE):
            # identify subject code and name
            code = "Unknown"
            name = "Unknown"
            for back_p in range(pno, max(-1, pno-4), -1):
                btxt = pages_text[back_p]
                m_code = re.search(r'\b(285\d\d|268\d\d|267\d\d|658\d\d|259\d\d|258\d\d|257\d\d|290\d\d|210\d\d)\b', btxt)
                if m_code:
                    code = m_code.group(1)
                    lines = [l.strip() for l in btxt.split('\n') if l.strip()]
                    for idx, line in enumerate(lines):
                        if line == code:
                            for j in range(max(0, idx-4), min(len(lines), idx+6)):
                                cand = lines[j]
                                if cand != code and len(cand) > 3 and not re.match(r'^\d+$', cand):
                                    if not any(k in cand.lower() for k in ['subject', 'code', 'period', 'credit', 'marks', 'assessment', 'continuous', 'final', 'probidhan', 'week', 'total', 'grand', 'theory', 'practical']):
                                        name = cand
                                        break
                            break
                    break
            
            # Extract theory text
            theory_text = ""
            for forward_p in range(pno, min(len(pages_text), pno+8)):
                f_txt = pages_text[forward_p]
                if forward_p > pno and re.search(r'DETAILED\s+SYLLABUS\s*\(PRACTICAL\)', f_txt, re.IGNORECASE):
                    practical_idx = re.search(r'DETAILED\s+SYLLABUS\s*\(PRACTICAL\)', f_txt, re.IGNORECASE).start()
                    theory_text += f_txt[:practical_idx] + "\n"
                    break
                elif forward_p > pno and re.search(r'DETAILED\s+SYLLABUS\s*\(THEORY\)', f_txt, re.IGNORECASE):
                    break
                else:
                    theory_text += f_txt + "\n"
            
            units = parse_units_from_text(theory_text)
            course_map[code] = {
                'name': name,
                'file': os.path.basename(pf),
                'page': pno + 1,
                'units': units
            }

with open("parsed_units_summary.txt", "w", encoding="utf-8") as out_f:
    out_f.write(f"Parsed {len(course_map)} courses with units!\n\n")
    for ccode, cdata in course_map.items():
        out_f.write(f"====================================================\n")
        out_f.write(f"COURSE: {ccode} - {cdata['name']} (from {cdata['file']})\n")
        out_f.write(f"====================================================\n")
        for u in cdata['units']:
            out_f.write(f"  Unit {u['num']}: {u['title']}\n")
            for t in u['topics']:
                out_f.write(f"     {t}\n")
        out_f.write("\n")

print(f"Successfully parsed and wrote {len(course_map)} courses to parsed_units_summary.txt")
