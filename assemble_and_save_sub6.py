# -*- coding: utf-8 -*-
"""
Assemble, balance options, validate and save Subject 6:
বিষয়- ৬. ডেটা কমিউনিকেশন (Data Communication).json
Total MCQs: 200
"""

import json
import os
import sys
import random
import collections

# UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

from gen_sub6_part1 import sub6_questions_part1
from gen_sub6_part2 import sub6_questions_part2

# 10 Supplementary Questions to bridge questions 136-145 (5 for 6.5 and 5 for 6.6)
sub6_supplement = [
    # 6.5 questions
    {
        "id": 136,
        "topic": "অধ্যায় ৬.৫: মাল্টিপ্লেক্সিং ও স্প্রেড স্পেকট্রাম (Multiplexing & Spread Spectrum)",
        "question": "ডিরেক্ট সিকোয়েন্স স্প্রেড স্পেকট্রাম (DSSS) প্রযুক্তিতে প্রতিটি মূল ডেটা বিটকে প্রসারিত করতে যে উচ্চগতির সিউডো-র্যান্ডম বিট প্যাটার্ন ব্যবহার করা হয় তাকে কী বলে?",
        "options": ["চিপিং কোড (Chipping Sequence / PN Code)", "ব্যারিটি সিকোয়েন্স (Parity Sequence)", "ফ্রেম মার্কার (Frame Marker)", "গার্ড সিকোয়েন্স (Guard Sequence)"],
        "answer": "ক",
        "explanation": "DSSS পদ্ধতিতে প্রেরিত ডেটা বিটকে একটি উচ্চ গতির সিউডো-র্যান্ডম কোড (Pseudo-random Noise or Chipping code) দিয়ে গুণ/XOR করা হয়, যা সিগন্যালের ব্যান্ডউইথকে মূল সিগন্যালের চেয়ে বহুগুণ বৃদ্ধি করে।"
    },
    {
        "id": 137,
        "topic": "অধ্যায় ৬.৫: মাল্টিপ্লেক্সিং ও স্প্রেড স্পেকট্রাম (Multiplexing & Spread Spectrum)",
        "question": "স্প্রেড স্পেকট্রাম কমিউনিকেশনে স্প্রেডেড সিগন্যালের ব্যান্ডউইথ এবং মূল আনস্প্রেডেড সিগন্যালের ব্যান্ডউইথের অনুপাতকে কী বলা হয়?",
        "options": ["প্রসেসিং গেইন (Processing Gain)", "মড্যুলেশন ইনডেক্স (Modulation Index)", "ব্যান্ডউইথ ইউটিলাইজেশন (Bandwidth Ratio)", "নয়েজ ফিগার (Noise Figure)"],
        "answer": "ক",
        "explanation": "প্রসেসিং গেইন (Processing Gain = BW_spread / BW_signal) হলো স্প্রেড স্পেকট্রাম ব্যবস্থার একটি প্রধান নির্দেশক, যা জ্যামিং প্রতিরোধ ক্ষমতা এবং সংকেতের গোপনীয়তা নির্ধারণ করে।"
    },
    {
        "id": 138,
        "topic": "অধ্যায় ৬.৫: মাল্টিপ্লেক্সিং ও স্প্রেড স্পেকট্রাম (Multiplexing & Spread Spectrum)",
        "question": "ফ্রিকোয়েন্সি হপিং স্প্রেড স্পেকট্রামে (FHSS) যদি ডেটা বিট হারের চেয়ে ক্যারিয়ার হপিংয়ের হার দ্রুততর হয়, তবে তাকে কী বলা হয়?",
        "options": ["ফাস্ট হপিং (Fast Frequency Hopping)", "স্লো হপিং (Slow Frequency Hopping)", "ডিরেক্ট হপিং (Direct Hopping)", "কন্টিনিউয়াস হপিং (Continuous Hopping)"],
        "answer": "ক",
        "explanation": "যখন ক্যারিয়ার ফ্রিকোয়েন্সি প্রতি ডেটা বিট সময়ের মধ্যে একাধিকবার পরিবর্তন হয় (Hopping rate > Bit rate), তখন তাকে ফাস্ট ফ্রিকোয়েন্সি হপিং (Fast Hopping) বলে।"
    },
    {
        "id": 139,
        "topic": "অধ্যায় ৬.৫: মাল্টিপ্লেক্সিং ও স্প্রেড স্পেকট্রাম (Multiplexing & Spread Spectrum)",
        "question": "স্ট্যাটিস্টিক্যাল টিডিএম (Statistical TDM)-এ প্রতিটি টাইম স্লটের ভেতরে প্রেরিত ডেটার সাথে অতিরিক্ত কোন তথ্য পাঠানো বাধ্যতামূলক?",
        "options": ["উৎস/গন্তব্যের অ্যাড্রেস বা নোড আইডি", "প্যারামিটার ম্যাট্রিক্স", "ফ্রেম সাইজ নির্দেশক", "অতিরিক্ত গার্ড ব্যান্ড"],
        "answer": "ক",
        "explanation": "সিনক্রোনাস TDM-এ স্লটের অবস্থান নির্ধারিত থাকে তাই অ্যাড্রেস লাগে না। কিন্তু স্ট্যাটিস্টিক্যাল TDM-এ যার ডেটা আছে কেবল তাকেই স্লট বরাদ্দ দেওয়ায় প্রতিটি স্লটে কোন ডিভাইসের ডেটা তা চিহ্নিত করতে অ্যাড্রেসিং তথ্য যুক্ত করা বাধ্যতামূলক।"
    },
    {
        "id": 140,
        "topic": "অধ্যায় ৬.৫: মাল্টিপ্লেক্সিং ও স্প্রেড স্পেকট্রাম (Multiplexing & Spread Spectrum)",
        "question": "সিনক্রোনাস TDM-এ যদি ৪টি চ্যানেল প্রতিটিতে ১ Mbps হারে ডেটা প্রেরণ করে এবং প্রতিটি চ্যানেল থেকে ১ বিট করে নিয়ে ১ বিটের ফ্রেম তৈরি হয়, তবে ফ্রেম সাইজ কত হবে?",
        "options": ["৪ বিট", "১ বিট", "১৬ বিট", "৮ বিট"],
        "answer": "ক",
        "explanation": "৪টি চ্যানেলের প্রতিটির জন্য একটি করে বিট বরাদ্দ থাকায় একটি কম্বাইন্ড ফ্রেমের আকার হবে ৪ বিট এবং মাল্টিপ্লেক্সড আউটপুট গতি হবে ৪ Mbps।"
    },
    # 6.6 questions
    {
        "id": 141,
        "topic": "অধ্যায় ৬.৬: এরর ডিটেকশন ও কারেকশন (Error Detection & Correction)",
        "question": "ইন্টারনেট প্রোটোকল সুইটে ব্যবহৃত চেকসাম (Checksum) গণনায় যোগফলের সময় কোনো ক্যারি বিট (Carry-out) তৈরি হলে তা কীভাবে সমন্বয় করা হয়?",
        "options": ["যোগফলের সর্বডানের বিটের সাথে পুনরায় যোগ করা হয় (End-around carry)", "ক্যারি বিটটি স্থায়ীভাবে বাতিল করা হয়", "ক্যারি বিটের জন্য নতুন বাইট তৈরি করা হয়", "হেডারের সর্ববামে বসিয়ে দেওয়া হয়"],
        "answer": "ক",
        "explanation": "ওয়ানস কমপ্লিমেন্ট (1's complement) পাটিগণিতে যোগের সময় ক্যারি আউট তৈরি হলে তাকে ফলাফলের সর্বডানের নিম্নতম বিটের (LSB) সাথে পুনরায় যোগ করতে হয়, যাকে 'End-around carry' বলা হয়।"
    },
    {
        "id": 142,
        "topic": "অধ্যায় ৬.৬: এরর ডিটেকশন ও কারেকশন (Error Detection & Correction)",
        "question": "CRC অ্যালগরিদমে যদি জেনারেটর বহুপদী বা ডিভাইজর পলিনোমিয়ালের সর্বোচ্চ ঘাত বা ডিগ্রি $k$ হয়, তবে উৎপন্ন Frame Check Sequence (FCS)-এর দৈর্ঘ্য কত বিট হবে?",
        "options": ["$k$ বিট", "$k+1$ বিট", "$k-1$ বিট", "$2k$ বিট"],
        "answer": "ক",
        "explanation": "CRC-তে ডিভাইজর যদি $k$ ডিগ্রির হয় (অর্থাৎ $k+1$ বিট দীর্ঘ), তবে মডিউলো-২ ভাগের ভাগশেষ বা FCS ঠিক $k$ বিট দীর্ঘ হবে।"
    },
    {
        "id": 143,
        "topic": "অধ্যায় ৬.৬: এরর ডিটেকশন ও কারেকশন (Error Detection & Correction)",
        "question": "তারবিহীন বা ত্রুটিপূর্ণ মাধ্যমে ট্রান্সমিশনের সময় দীর্ঘ বার্স্ট এরর (Burst Error)-কে ছোট ছোট একক ত্রুটিতে রূপান্তর করে সংশোধনের জন্য কোন কৌশল প্রয়োগ করা হয়?",
        "options": ["ইন্টারলিভিং (Interleaving)", "রিভার্স পোলারিটি (Reverse Polarity)", "জ্যামিং (Jamming)", "বাইপোলার শিফটিং (Bipolar Shifting)"],
        "answer": "ক",
        "explanation": "ইন্টারলিভিং কৌশলে পাশাপাশি ফ্রেম বা কোডওয়ার্ডের বিটগুলোকে ম্যাট্রিক্স আকারে সাজিয়ে মিশ্রিত করে পাঠানো হয়, ফলে একটানা নয়েজে বার্স্ট এরর হলেও প্রতিটি ফ্রেম কেবল একটি করে বিট হারায় যা সহজে সংশোধনযোগ্য।"
    },
    {
        "id": 144,
        "topic": "অধ্যায় ৬.৬: এরর ডিটেকশন ও কারেকশন (Error Detection & Correction)",
        "question": "একটি হ্যামিং কোড ব্যবস্থায় একক বিট ত্রুটি সংশোধনের পাশাপাশি দ্বৈত বিট ত্রুটি শনাক্ত (SEC-DED) করার জন্য কী অতিরিক্ত যুক্ত করা হয়?",
        "options": ["সম্পূর্ণ কোডওয়ার্ডের ওপর একটি অতিরিক্ত সামগ্রিক প্যারিটি বিট", "দ্বিগুণ সংখ্যক ডেটা বিট", "আলাদা CRC ফিল্ড", "টুইন চেকিং বিট"],
        "answer": "ক",
        "explanation": "SEC-DED (Single Error Correction, Double Error Detection) অর্জনে স্ট্যান্ডার্ড হ্যামিং কোডের সাথে পুরো ব্লকের জন্য একটি অতিরিক্ত মাস্টার প্যারিটি বিট যোগ করা হয়, যা নূন্যতম হ্যামিং দূরত্ব ৪ এ উন্নীত করে।"
    },
    {
        "id": 145,
        "topic": "অধ্যায় ৬.৬: এরর ডিটেকশন ও কারেকশন (Error Detection & Correction)",
        "question": "মেমরি বা স্টোরেজ ছাড়াই ডেটার ধারাবাহিক প্রবাহের উপর ভিত্তি করে জটিল ম্যাথমেটিক্যাল পলিনোমিয়াল স্টেট মেশিনে পরিচালিত এরর কারেকশন কোড কোনটি?",
        "options": ["কনভোল্যুশনাল কোড (Convolutional Code)", "প্যারিটি ব্লক কোড (Block Code)", "চেকসাম কোড (Checksum Code)", "ম্যাট্রিক্স কোড (Matrix Code)"],
        "answer": "ক",
        "explanation": "কনভোল্যুশনাল কোড (Convolutional Code) শিফট রেজিস্টারের মাধ্যমে চলমান বিট স্ট্রিমের ওপর ক্রমাগত স্লাইডিং প্রক্রিয়ায় রিডানড্যান্ট বিট তৈরি করে, যা স্যাটেলাইট ও ওয়্যারলেস যোগাযোগে বহুল ব্যবহৃত।"
    }
]

# Merge part 1, supplement, and part 2
combined_questions = sub6_questions_part1 + sub6_supplement + sub6_questions_part2
print(f"Total merged questions: {len(combined_questions)}")
assert len(combined_questions) == 200, f"Expected 200 questions, got {len(combined_questions)}"

# Map of Bengali letters to 0-3 index
letters = ["ক", "খ", "গ", "ঘ"]
l2i = {"ক": 0, "খ": 1, "গ": 2, "ঘ": 3}

# Balance answers across 'ক', 'খ', 'গ', 'ঘ'
random.seed(6066)  # Deterministic seed for Subject 6

for i, q in enumerate(combined_questions, 1):
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
ans_counts = collections.Counter(q["answer"] for q in combined_questions)
print("Answer distribution:", ans_counts)

topics_counts = collections.Counter(q["topic"] for q in combined_questions)
print("Topic distribution:")
for t, cnt in topics_counts.items():
    print(f"  {t} -> {cnt} questions")

output_path = "JSON Data/BPSC Technical AI/বিষয়- ৬. ডেটা কমিউনিকেশন (Data Communication).json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(combined_questions, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully written {len(combined_questions)} verified MCQs to:\n{output_path}")
