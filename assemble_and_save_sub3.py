# -*- coding: utf-8 -*-
"""
Assemble, balance options, validate and save Subject 3:
বিষয়- ৩. অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (সি++, জাভা).json
"""

import json
import os
import sys
import random
import collections

# UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

from gen_sub3_part1 import sub3_questions_part1
from gen_sub3_part2 import sub3_questions_part2

all_questions = sub3_questions_part1 + sub3_questions_part2
print(f"Total combined questions: {len(all_questions)}")
assert len(all_questions) == 200, f"Expected 200 questions, got {len(all_questions)}"

# Map of Bengali letters to 0-3 index
letters = ["ক", "খ", "গ", "ঘ"]
l2i = {"ক": 0, "খ": 1, "গ": 2, "ঘ": 3}

# Balance answers across 'ক', 'খ', 'গ', 'ঘ'
random.seed(3033)  # Deterministic seed

for i, q in enumerate(all_questions, 1):
    q["id"] = i
    curr_idx = l2i[q["answer"]]
    correct_text = q["options"][curr_idx]
    distractors = [opt for idx, opt in enumerate(q["options"]) if idx != curr_idx]
    
    # Target index for balanced distribution
    target_idx = random.randint(0, 3)
    new_options = list(distractors)
    random.shuffle(new_options)
    new_options.insert(target_idx, correct_text)
    
    q["options"] = new_options
    q["answer"] = letters[target_idx]
    
    # Assert correctness
    assert q["options"][l2i[q["answer"]]] == correct_text
    assert len(q["options"]) == 4
    assert len(q["question"].strip()) > 5
    assert len(q["explanation"].strip()) > 5

# Verify distribution
ans_counts = collections.Counter(q["answer"] for q in all_questions)
print("Answer distribution:", ans_counts)

topics_counts = collections.Counter(q["topic"] for q in all_questions)
print("Topic distribution:")
for t, cnt in topics_counts.items():
    print(f"  {t} -> {cnt} questions")

output_path = "JSON Data/BPSC Technical AI/বিষয়- ৩. অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (সি++, জাভা).json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully written {len(all_questions)} verified MCQs to:\n{output_path}")
