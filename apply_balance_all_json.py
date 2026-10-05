# -*- coding: utf-8 -*-
"""
Master script to balance answers, remove streaks, and clean options across ALL 39 JSON files:
- JSON Data/NTRCA 313 and 325 - AI (7 files)
- JSON Data/NTRCA 452 - AI (7 files)
- JSON Data/BPSC Technical AI (25 files)

Ensures:
1. Balanced distribution (~25% each, exactly 25 for 100 questions, 50 for 200 questions).
2. Anti-streak guarantee: Max consecutive identical answers <= 2 (NEVER 3+ in a row).
3. Stripping embedded option prefixes like 'ক) ', 'খ) '.
4. Fixing Q94 duplicate options in NTRCA 313/325 Ch 2.
5. Preserving 100% correct answer texts for all 7,100 questions.
"""

import glob
import json
import os
import re
import sys
import random
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

letters = ["ক", "খ", "গ", "ঘ"]
l2i = {"ক": 0, "খ": 1, "গ": 2, "ঘ": 3}

def generate_balanced_sequence(n, fixed_positions=None, max_streak=2, seed=42):
    if fixed_positions is None:
        fixed_positions = {}
        
    random.seed(seed)
    target_count = n // 4
    remainder = n % 4
    
    counts = {l: target_count for l in letters}
    for i in range(remainder):
        counts[letters[i]] += 1
        
    for pos, l in fixed_positions.items():
        counts[l] -= 1
        assert counts[l] >= 0, f"Cannot satisfy fixed position {pos} -> {l}"
        
    seq = [None] * n
    for pos, l in fixed_positions.items():
        seq[pos] = l
        
    def solve(idx):
        if idx == n:
            return True
        if seq[idx] is not None:
            if idx >= max_streak and all(seq[idx - k] == seq[idx] for k in range(1, max_streak + 1)):
                return False
            return solve(idx + 1)
            
        candidates = [l for l in letters if counts[l] > 0]
        valid_candidates = []
        for c in candidates:
            causes_streak = False
            if idx >= max_streak:
                if all(seq[idx - k] == c for k in range(1, max_streak + 1)):
                    causes_streak = True
            if not causes_streak:
                valid_candidates.append(c)
                
        random.shuffle(valid_candidates)
        valid_candidates.sort(key=lambda c: counts[c], reverse=True)
        
        for c in valid_candidates:
            seq[idx] = c
            counts[c] -= 1
            if solve(idx + 1):
                return True
            counts[c] += 1
            seq[idx] = None
            
        return False

    success = solve(0)
    if not success:
        return generate_balanced_sequence(n, fixed_positions, max_streak, seed + 1)
        
    return seq

def clean_option(opt):
    opt = opt.strip()
    # Strip Bengali option prefix like "ক) ", "খ) ", "গ) ", "ঘ) "
    opt = re.sub(r"^[কখগঘ]\)\s*", "", opt).strip()
    return opt

all_files = sorted(glob.glob('JSON Data/**/*.json', recursive=True))
print(f"Total files to process: {len(all_files)}")

modified_count = 0
total_questions_processed = 0

for f_idx, fpath in enumerate(all_files, 1):
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    n = len(data)
    
    # 1. Identify fixed positions (e.g. "উপরের সবগুলো")
    fixed_positions = {}
    for idx, q in enumerate(data):
        opts = [clean_option(o) for o in q['options']]
        curr_idx = l2i[q['answer']]
        correct_text = opts[curr_idx]
        
        if any("উপরের সবগুলো" in o for o in opts):
            if "উপরের সবগুলো" in correct_text:
                fixed_positions[idx] = "ঘ"
                
    # 2. Generate balanced anti-streak sequence
    seq = generate_balanced_sequence(n, fixed_positions, max_streak=2, seed=f_idx * 1000 + 7)
    
    # 3. Apply balanced answers and shuffle options
    rand_gen = random.Random(f_idx * 5000 + 13)
    
    for idx, q in enumerate(data):
        total_questions_processed += 1
        
        # Check special case for duplicate options in NTRCA 313/325 Ch 2 Q94
        if "সংখ্যা পদ্ধতি" in fpath and q['id'] == 94:
            correct_text = "(১০০০০০১)২"
            distractors = ["(১০০০০১০)২", "(১০০০১০০)২", "(১০০০০১১)২"]
        else:
            opts = [clean_option(o) for o in q['options']]
            curr_idx = l2i[q['answer']]
            correct_text = opts[curr_idx]
            distractors = [opt for o_idx, opt in enumerate(opts) if o_idx != curr_idx]
            
        target_letter = seq[idx]
        target_idx = l2i[target_letter]
        
        # Check if one of the distractors is "উপরের সবগুলো"
        uporer_distractor = [d for d in distractors if "উপরের সবগুলো" in d]
        if uporer_distractor:
            # That distractor must stay at position 3 ('ঘ')
            # target_idx is in [0, 1, 2]
            other_distractors = [d for d in distractors if "উপরের সবগুলো" not in d]
            rand_gen.shuffle(other_distractors)
            new_options = [None] * 4
            new_options[3] = uporer_distractor[0]
            new_options[target_idx] = correct_text
            empty_spots = [k for k in [0, 1, 2] if k != target_idx]
            for spot, d in zip(empty_spots, other_distractors):
                new_options[spot] = d
        else:
            rand_gen.shuffle(distractors)
            new_options = list(distractors)
            new_options.insert(target_idx, correct_text)
            
        q['options'] = new_options
        q['answer'] = target_letter
        
        # Validation assertions
        assert q['options'][l2i[q['answer']]] == correct_text, f"Mismatch in {fpath} Q{q['id']}"
        assert len(q['options']) == 4, f"Options count != 4 in {fpath} Q{q['id']}"
        assert len(set(q['options'])) == 4, f"Duplicate options in {fpath} Q{q['id']}: {q['options']}"
        assert q['answer'] in ['ক', 'খ', 'গ', 'ঘ']
        assert len(q['question'].strip()) > 5
        assert len(q['explanation'].strip()) > 5

    # Check streak and counts of updated data
    updated_answers = [q['answer'] for q in data]
    counts = Counter(updated_answers)
    
    max_streak = 0
    curr_streak = 0
    prev_ans = None
    for a in updated_answers:
        if a == prev_ans:
            curr_streak += 1
        else:
            curr_streak = 1
            prev_ans = a
        if curr_streak > max_streak:
            max_streak = curr_streak
            
    assert max_streak <= 2, f"Streak violated in {fpath}"
    assert all(c == n // 4 for c in counts.values()), f"Balance violated in {fpath}"
    
    # Save back to file
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    modified_count += 1
    folder_name = os.path.basename(os.path.dirname(fpath))
    file_name = os.path.basename(fpath)
    print(f"[{f_idx:02d}/39] Saved: {folder_name[:20]}/{file_name[:35]:<35} | N={n:3d} | MaxStreak={max_streak} | Ans={dict(counts)}")

print(f"\n=======================================================")
print(f"SUCCESS: All {modified_count} JSON files ({total_questions_processed} questions) successfully updated and verified!")
print(f"=======================================================")
