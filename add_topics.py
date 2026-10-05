# -*- coding: utf-8 -*-
import json
import os

# --- Chapter 1 Topic Mapping ---
ch1_topics = [
    (1, 10, "১. কম্পিউটারের সংজ্ঞা"),
    (11, 20, "২. কম্পিউটারের বৈশিষ্ট্যসমূহ"),
    (21, 38, "৩. কম্পিউটারের ইতিহাস (অ্যাবাকাস থেকে প্রথম বাণিজ্যিক কম্পিউটার পর্যন্ত)"),
    (39, 52, "৪. কম্পিউটার প্রজন্ম (প্রথম প্রজন্ম থেকে পঞ্চম প্রজন্ম পর্যন্ত)"),
    (53, 62, "৫. কম্পিউটারের প্রকার ভেদ"),
    (63, 74, "৬. কম্পিউটারের শ্রেণীবিন্যাস"),
    (75, 90, "৭. কম্পিউটার পদ্ধতির সংগঠন"),
    (91, 100, "৮. হার্ডওয়্যার এবং সফটওয়্যার")
]

def get_ch1_topic(qid):
    for start, end, topic in ch1_topics:
        if start <= qid <= end:
            return topic
    return "কম্পিউটার বেসিক"

# --- Chapter 2 Topic Mapping ---
ch2_topics = [
    (1, 10, "১. নন-পজিশনাল পদ্ধতি"),
    (11, 28, "২. পজিশনাল পদ্ধতি"),
    (29, 74, "৩. এক সংখ্যা থেকে অন্যটিতে রূপান্তর"),
    (75, 100, "৪. বাইনারী গণিত (যোগ, বিয়োগ, গুণ ও ভাগ)")
]

def get_ch2_topic(qid):
    for start, end, topic in ch2_topics:
        if start <= qid <= end:
            return topic
    return "সংখ্যা পদ্ধতি"

# Process Chapter 1
ch1_files = [
    r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\NTRCA 313 and 325 - AI\অধ্যায়- ক. কম্পিউটার বেসিক.json",
    r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\JSON Data\NTRCA 313 and 325 - AI\অধ্যায়- ক. কম্পিউটার বেসিক.json"
]

for fpath in ch1_files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for q in data:
        q["topic"] = get_ch1_topic(q["id"])
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated Chapter 1 JSON with topic.")

# Process Chapter 2
ch2_files = [
    r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\NTRCA 313 and 325 - AI\অধ্যায়- খ. সংখ্যা পদ্ধতি.json",
    r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\JSON Data\NTRCA 313 and 325 - AI\অধ্যায়- খ. সংখ্যা পদ্ধতি.json"
]

for fpath in ch2_files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for q in data:
        q["topic"] = get_ch2_topic(q["id"])
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated Chapter 2 JSON with topic.")

print("All JSON files updated with topic successfully.")
