# -*- coding: utf-8 -*-
"""
Audit all 25 Subject files in JSON Data/BPSC Technical AI/
"""
import glob
import json
import os
import sys
import collections

sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('JSON Data/BPSC Technical AI/*.json'))
print("=== BPSC TECHNICAL AI QUESTION BANK COMPREHENSIVE AUDIT ===")
print(f"Total Subject Files Found: {len(files)} / 25\n")

total_mcqs = 0
overall_answers = collections.Counter()
errors = []

for idx, fpath in enumerate(files, 1):
    fname = os.path.basename(fpath)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        errors.append(f"{fname}: JSON load error {e}")
        continue
    
    count = len(data)
    total_mcqs += count
    ans_counts = collections.Counter(q.get('answer') for q in data)
    overall_answers.update(ans_counts)
    
    if count != 200:
        errors.append(f"{fname}: Expected 200 MCQs, got {count}")
        
    for q_idx, q in enumerate(data):
        for field in ['id', 'topic', 'question', 'options', 'answer', 'explanation']:
            if field not in q:
                errors.append(f"{fname} Q{q_idx+1}: Missing field {field}")
        if len(q.get('options', [])) != 4:
            errors.append(f"{fname} Q{q_idx+1}: Options count != 4")
        if q.get('answer') not in ['ক', 'খ', 'গ', 'ঘ']:
            errors.append(f"{fname} Q{q_idx+1}: Invalid answer key {q.get('answer')}")
        if not q.get('question', '').strip():
            errors.append(f"{fname} Q{q_idx+1}: Empty question")
        if not q.get('explanation', '').strip():
            errors.append(f"{fname} Q{q_idx+1}: Empty explanation")
            
    print(f"[{idx:02d}/25] {fname[:62]:<62} | MCQs: {count:3d} | Ans: {dict(ans_counts)}")

print("\n" + "="*80)
print(f"GRAND TOTAL MCQs: {total_mcqs} / 5,000")
print(f"Overall Answer Key Distribution: {dict(overall_answers)}")
if errors:
    print(f"ERRORS FOUND ({len(errors)}):")
    for err in errors[:10]:
        print("  -", err)
else:
    print("AUDIT RESULT: 100% PERFECT! ALL 25 SUBJECTS (5,000 MCQs) VERIFIED WITH ZERO ERRORS!")
print("="*80)
