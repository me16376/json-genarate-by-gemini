# -*- coding: utf-8 -*-
"""
Build interactive web applications for NTRCA 452 - AI
Based on the exact layout and features of Ict-wizard-NTRCA-313-and-325.html
Includes:
- Noto Sans Bengali as default font
- Transparent background on option hover and click (only text & border colors)
- Dynamic Topic Filter dropdown & topic pill badges
- Real-time chapter loading from 'NTRCA 452 - AI' folder
"""

import json
import os
import glob
import re

base_dir = r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini"
json_dir = os.path.join(base_dir, "JSON Data", "NTRCA 452 - AI")

def to_bn(num):
    bn_digits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
    return ''.join(bn_digits[int(d)] if d.isdigit() else d for d in str(num))

# Syllabus chapters definition for NTRCA 452
syllabus_chapters = [
    ("ch1", "অধ্যায়- ১. Structured and Object Oriented Programming", "১. C & OOP Concept", "Structured and Object Oriented Programming"),
    ("ch2", "অধ্যায়- ২. Introduction to Software Engineering", "২. Software Engineering", "Introduction to Software Engineering"),
    ("ch3", "অধ্যায়- ৩. Data Structure and Algorithm", "৩. Data Structure & Algo", "Data Structure and Algorithm"),
    ("ch4", "অধ্যায়- ৪. Web Technology", "৪. Web Technology", "Web Technology"),
    ("ch5", "অধ্যায়- ৫. Operating System", "৫. Operating System", "Operating System"),
    ("ch6", "অধ্যায়- ৬. Database Management System", "৬. DBMS", "Database Management System"),
    ("ch7", "অধ্যায়- ৭. Data Communications and Networking", "৭. Networking", "Data Communications and Networking"),
]

chapters_data = []
total_questions = 0

all_json_files = glob.glob(os.path.join(json_dir, "*.json"))

for ch_id, full_title, short_title, match_str in syllabus_chapters:
    # Find matching file in json_dir
    matched = None
    for f in all_json_files:
        if match_str.lower() in os.path.basename(f).lower():
            matched = f
            break
    
    if matched and os.path.exists(matched):
        with open(matched, "r", encoding="utf-8") as f:
            q_list = json.load(f)
        chapters_data.append({
            "id": ch_id,
            "title": full_title,
            "short": short_title,
            "count": len(q_list),
            "questions": q_list
        })
        total_questions += len(q_list)
        safe_name = os.path.basename(matched).encode('ascii', errors='backslashreplace').decode('ascii')
        print(f"Loaded: {safe_name} ({len(q_list)} MCQs)")
    else:
        safe_title = full_title.encode('ascii', errors='backslashreplace').decode('ascii')
        print(f"Pending generation: {safe_title}")

if not chapters_data:
    print("No chapters found in NTRCA 452 - AI folder!")
    exit(1)

bn_total = to_bn(total_questions)
print(f"Total loaded: {len(chapters_data)} chapters, {total_questions} questions.")

# Read source HTML template from NTRCA-313-and-325-AI-Exam.html
source_html_path = os.path.join(base_dir, "NTRCA-313-and-325-AI-Exam.html")
with open(source_html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace Title and Header for NTRCA 452
html = html.replace(
    "<title>NTRCA আইসিটি শিক্ষক নিবন্ধন প্রশ্ন ব্যাংক (সহকারী শিক্ষক ও প্রভাষক)</title>",
    "<title>NTRCA 452 - AI প্রশ্ন ব্যাংক ও মডেল টেস্ট (কম্পিউটার সায়েন্স ও আইসিটি)</title>"
)
html = html.replace(
    "<h1>NTRCA আইসিটি শিক্ষক নিবন্ধন প্রশ্ন ব্যাংক</h1>",
    "<h1>NTRCA 452 - AI প্রশ্ন ব্যাংক ও মডেল টেস্ট</h1>"
)
html = html.replace(
    "<p class=\"subtitle\">বিষয় কোড: ৩১৩ ও ৩২৫ (সহকারী শিক্ষক ও প্রভাষক) | মোট প্রশ্ন:",
    "<p class=\"subtitle\">বিষয় কোড: ৪৫২ (কম্পিউটার সায়েন্স / আইসিটি প্রভাষক) | মোট প্রশ্ন:"
)

# Update question count in header subtitle
html = re.sub(r'মোট প্রশ্ন:\s*[\d০-৯]+টি', f'মোট প্রশ্ন: {bn_total}টি', html)
html = re.sub(r'formatNumber\(\d+\)', f'formatNumber({total_questions})', html)

# Replace chaptersData in JavaScript
chapters_json_str = json.dumps(chapters_data, ensure_ascii=False)
ch_start = html.find("const chaptersData = [")
app_state = html.find("// Application State", ch_start)
if ch_start != -1 and app_state != -1:
    html = html[:ch_start] + f"const chaptersData = {chapters_json_str};\n\n    " + html[app_state:]
else:
    print("Warning: Could not locate chaptersData slice boundaries!")

# Update statsInfo
html = re.sub(
    r"statsInfo\.innerHTML = `মোট প্রশ্ন: <strong>\$\{formatNumber\(\d+\)\}</strong> টি",
    f"statsInfo.innerHTML = `মোট প্রশ্ন: <strong>${{formatNumber({total_questions})}}</strong> টি",
    html
)

# Output files for NTRCA 452
targets = [
    os.path.join(base_dir, "NTRCA-452-AI-Exam.html")
]

for t in targets:
    with open(t, "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully created HTML:", os.path.basename(t), f"({len(html)} bytes)")
