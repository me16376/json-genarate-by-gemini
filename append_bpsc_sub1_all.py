# -*- coding: utf-8 -*-
"""
Append Chapters 1.2 to 1.6 and output complete 200 MCQs for Subject 1.
"""

import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')
from generate_bpsc_subject_1 import questions

# ==============================================================================
# অধ্যায় ১.২: অপারেটিং এনভায়রনমেন্ট ও সফটওয়্যার পরিচিতি (Questions 41 to 70)
# ==============================================================================
topic_1_2 = "অধ্যায় ১.২: অপারেটিং এনভায়রনমেন্ট ও সফটওয়্যার পরিচিতি"

questions.append({
    "id": 41,
    "topic": topic_1_2,
    "question": "কম্পিউটার চালু করার পর পাওয়ার অন সেলফ টেস্ট (POST) সম্পন্ন করে কোনটি?",
    "options": ["অপারেটিং সিস্টেম", "বেসিক ইনপুট/আউটপুট সিস্টেম (BIOS / UEFI)", "হার্ডডিস্ক ড্রাইভ", "কম্পাইলার"],
    "answer": "খ",
    "explanation": "কম্পিউটার চালু হওয়ার সাথে সাথে মাদারবোর্ডের রম (ROM) থেকে BIOS সক্রিয় হয়ে হার্ডওয়্যার ঠিক আছে কিনা তা পরীক্ষা করতে POST রান করে।"
})

questions.append({
    "id": 42,
    "topic": topic_1_2,
    "question": "কম্পিউটার সম্পূর্ণ বন্ধ থাকা অবস্থা থেকে পাওয়ার বাটনে চাপ দিয়ে চালু করার প্রক্রিয়াকে কী বলে?",
    "options": ["কোল্ড বুটিং (Cold Booting)", "ওয়ার্ম বুটিং (Warm Booting)", "হাইবারনেশন", "স্লিপ মোড"],
    "answer": "ক",
    "explanation": "কম্পিউটার সম্পূর্ণ অফ থাকা অবস্থায় পাওয়ার অন করে চালু করাকে কোল্ড বুট বা হার্ড বুট বলা হয়।"
})

questions.append({
    "id": 43,
    "topic": topic_1_2,
    "question": "চলমান কম্পিউটারকে পুনরায় রিস্টার্ট (Restart) করার প্রক্রিয়াকে কী বলা হয়?",
    "options": ["কোল্ড বুটিং", "ওয়ার্ম বুটিং (Warm Booting / Soft Boot)", "ফ্ল্যাশ বুট", "ড্রাইভার বুট"],
    "answer": "খ",
    "explanation": "সিস্টেম রিস্টার্টের সময় পাওয়ার অফ না করে ওএস পুনরায় লোড হওয়াকে ওয়ার্ম বুটিং বলা হয়।"
})

questions.append({
    "id": 44,
    "topic": topic_1_2,
    "question": "কম্পিউটারের তারিখ, সময় এবং সিস্টেম কনফিগারেশন সেটিংস বিদ্যুৎ বন্ধ থাকলেও সচল রাখে কোনটি?",
    "options": ["SMPS", "CMOS ব্যাটারি (CR2032)", "ক্যাশ মেমোরি", "ইউএসবি পোর্ট"],
    "answer": "খ",
    "explanation": "CMOS (Complementary Metal-Oxide-Semiconductor) ব্যাটারি মাদারবোর্ডের রিয়েল-টাইম ক্লক ও বায়োস সেটিংস সচল রাখে।"
})

questions.append({
    "id": 45,
    "topic": topic_1_2,
    "question": "ঐতিহ্যবাহী লিগ্যাসি BIOS-এর আধুনিক ও সুরক্ষিত বিকল্প কোনটি যা ২ টেরাবাইটের বেশি ডিস্ক পার্টিশন সমর্থন করে?",
    "options": ["UEFI (Unified Extensible Firmware Interface)", "POST", "DOS", "GRUB"],
    "answer": "ক",
    "explanation": "UEFI আধুনিক ফার্মওয়্যার ইন্টারফেস যা দ্রুত বুট, সিকিউর বুট (Secure Boot) এবং GPT পার্টিশন সমর্থন করে।"
})

questions.append({
    "id": 46,
    "topic": topic_1_2,
    "question": "নিচের কোনটি একটি সিস্টেম সফটওয়্যার (System Software)?",
    "options": ["মাইক্রোসফট ওয়ার্ড", "ডিভাইস ড্রাইভার ও অপারেটিং সিস্টেম", "অ্যাডোবি ফটোশপ", "ভিএলসি মিডিয়া প্লেয়ার"],
    "answer": "খ",
    "explanation": "অপারেটিং সিস্টেম, ডিভাইস ড্রাইভার এবং ইউটিলিটি সফটওয়্যার সরাসরি হার্ডওয়্যার পরিচালনা করে, তাই এরা সিস্টেম সফটওয়্যার।"
})

questions.append({
    "id": 47,
    "topic": topic_1_2,
    "question": "নিচের কোনটি ওপেন সোর্স (Open Source) অপারেটিং সিস্টেমের উদাহরণ?",
    "options": ["উইন্ডোজ ১১", "লিনাক্স (Linux)", "ম্যাক ওএস (macOS)", "আইওএস (iOS)"],
    "answer": "খ",
    "explanation": "লিনাক্স কার্নেল ও এর ডিস্ট্রিবিউশনসমূহ উন্মুক্ত সোর্স কোড বিশিষ্ট এবং বিনামূল্যে পরিবর্তনযোগ্য।"
})

questions.append({
    "id": 48,
    "topic": topic_1_2,
    "question": "উইন্ডোজ অপারেটিং সিস্টেমে ফাইল বা ফোল্ডারের নাম পরিবর্তনের (Rename) জন্য কোন ফাংশন কি ব্যবহৃত হয়?",
    "options": ["F1", "F2", "F3", "F5"],
    "answer": "খ",
    "explanation": "উইন্ডোজ এক্সপ্লোরারে যেকোনো ফাইল বা ফোল্ডার নির্বাচন করে 'F2' চাপলে নাম পরিবর্তন করা যায়।"
})

questions.append({
    "id": 49,
    "topic": topic_1_2,
    "question": "উইন্ডোজ সিস্টেমে টাস্ক ম্যানেজার (Task Manager) সরাসরি চালু করার শর্টকাট কী কোনটি?",
    "options": ["Ctrl + Shift + Esc", "Alt + F4", "Ctrl + Alt + Delete", "Win + R"],
    "answer": "ক",
    "explanation": "Ctrl + Shift + Esc সরাসরি কোনো মধ্যবর্তী মেনু ছাড়াই টাস্ক ম্যানেজার ওপেন করে।"
})

questions.append({
    "id": 50,
    "topic": topic_1_2,
    "question": "কোন ফাইল সিস্টেমে ফাইল ও ফোল্ডার লেভেলে পারমিশন, কম্প্রেশন এবং সিকিউরিটি এনক্রিপশন (EFS) ফিচার বিদ্যমান?",
    "options": ["FAT16", "FAT32", "NTFS (New Technology File System)", "exFAT"],
    "answer": "গ",
    "explanation": "NTFS উইন্ডোজের আধুনিক ফাইল সিস্টেম যা ফোল্ডার নিরাপত্তা পারমিশন, এনক্রিপশন এবং জার্নালিং সমর্থন করে।"
})

questions.append({
    "id": 51,
    "topic": topic_1_2,
    "question": "FAT32 ফাইল সিস্টেমে একটি একক ফাইলের সর্বোচ্চ আকার (Maximum Single File Size) কত হতে পারে?",
    "options": ["2 GB", "4 GB", "8 GB", "16 GB"],
    "answer": "খ",
    "explanation": "FAT32 ফাইল সিস্টেমে ৪ গিগাবাইট (4 GB - 1 byte) এর চেয়ে বড় কোনো একক ফাইল কপি বা সংরক্ষণ করা যায় না।"
})

questions.append({
    "id": 52,
    "topic": topic_1_2,
    "question": "উইন্ডোজ ও ম্যাক উভয়ের সাথেই সহজে সামঞ্জস্যপূর্ণ এবং ৪ জিবি-র বড় ফাইল সমর্থনকারী আধুনিক ফ্ল্যাশ ড্রাইভ ফাইল সিস্টেম কোনটি?",
    "options": ["FAT32", "exFAT (Extended File Allocation Table)", "NTFS", "ext4"],
    "answer": "খ",
    "explanation": "exFAT বড় ফাইল ধারণক্ষমতা সম্পন্ন এবং ক্রস-প্ল্যাটফর্ম (Windows ও macOS) ব্যবহারের জন্য আদর্শ।"
})

questions.append({
    "id": 53,
    "topic": topic_1_2,
    "question": "উইন্ডোজ ওএসে 'Run' ডায়ালগ বক্স ওপেন করার কীবোর্ড শর্টকাট কোনটি?",
    "options": ["Win + R", "Win + E", "Win + D", "Win + L"],
    "answer": "ক",
    "explanation": "Windows Key + R চাপলে রান কমান্ড উইন্ডো ওপেন হয়।"
})

questions.append({
    "id": 54,
    "topic": topic_1_2,
    "question": "উইন্ডোজে ফাইল এক্সপ্লোরার (File Explorer) খোলার দ্রুততম শর্টকাট কী কোনটি?",
    "options": ["Win + E", "Win + F", "Win + X", "Ctrl + E"],
    "answer": "ক",
    "explanation": "Windows Key + E চাপলে সরাসরি ফাইল এক্সপ্লোরার ওপেন হয়।"
})

questions.append({
    "id": 55,
    "topic": topic_1_2,
    "question": "কম্পিউটার স্ক্রিন সাথে সাথে লক (Lock Computer) করার শর্টকাট কী কোনটি?",
    "options": ["Win + L", "Win + D", "Ctrl + L", "Alt + L"],
    "answer": "ক",
    "explanation": "Windows Key + L চাপলে উইন্ডোজ সাথে সাথে লক স্ক্রিনে চলে যায়।"
})

questions.append({
    "id": 56,
    "topic": topic_1_2,
    "question": "চলমান সকল উইন্ডো মিনিমাইজ করে সরাসরি ডেস্কটপ প্রদর্শনের শর্টকাট কোনটি?",
    "options": ["Win + D", "Win + M", "Alt + Tab", "Ctrl + D"],
    "answer": "ক",
    "explanation": "Windows Key + D চাপলে সকল উইন্ডো মিনিমাইজ হয়ে মূল ডেস্কটপ প্রদর্শিত হয়।"
})

questions.append({
    "id": 57,
    "topic": topic_1_2,
    "question": "উইন্ডোজ অপারেটিং সিস্টেমের হার্ডওয়্যার, সফটওয়্যার ও ইউজার প্রোফাইলের কেন্দ্রীয় কনফিগারেশন ডেটাবেসকে কী বলে?",
    "options": ["উইন্ডোজ রেজিস্ট্রি (Windows Registry)", "কন্ট্রোল প্যানেল", "গ্রুপ পলিসি", "টাস্ক শিডিউলার"],
    "answer": "ক",
    "explanation": "উইন্ডোজ রেজিস্ট্রি (regedit) হলো ওএস-এর সকল কনফিগারেশন কি এবং ভ্যালু সংরক্ষণের মূল হায়ারারকিক্যাল ডেটাবেস।"
})

questions.append({
    "id": 58,
    "topic": topic_1_2,
    "question": "উইন্ডোজে কোনো ফাইলকে রিসাইকেল বিনে না পাঠিয়ে স্থায়ীভাবে মুছে (Permanently Delete) ফেলার কমান্ড কোনটি?",
    "options": ["Shift + Delete", "Ctrl + Delete", "Alt + Delete", "Delete"],
    "answer": "ক",
    "explanation": "Shift + Delete চাপলে ফাইলটি রিসাইকেল বিনে জমা না হয়ে সরাসরি হার্ডডিস্ক থেকে স্থায়ীভাবে মুছে যায়।"
})

questions.append({
    "id": 59,
    "topic": topic_1_2,
    "question": "হার্ডডিস্কের ছড়িয়ে-ছিটিয়ে থাকা খণ্ড খণ্ড ডেটা ফাইলকে একত্রিত করে ডিস্কের পড়ার গতি বাড়ানোর ইউটিলিটি কোনটি?",
    "options": ["ডিস্ক ডিফ্র্যাগমেন্টার (Disk Defragmenter / Optimize Drives)", "ডিস্ক ক্লিনআপ", "চেক ডিস্ক", "ডিস্কপার্ট"],
    "answer": "ক",
    "explanation": "ডিফ্র্যাগমেন্টেশন ফ্র্যাগমেন্টেড ফাইলগুলোকে কনটিগুয়াস ব্লকে সাজিয়ে হেড মুভমেন্ট ও এক্সেস টাইম কমায়।"
})

questions.append({
    "id": 60,
    "topic": topic_1_2,
    "question": "অপারেটিং সিস্টেমে মেমরি কম পড়ে গেলে হার্ডডিস্কের যে অংশকে সাময়িকভাবে অতিরিক্ত র‍্যাম হিসেবে ব্যবহার করা হয় তাকে কী বলে?",
    "options": ["ভার্চুয়াল মেমোরি (Virtual Memory / Paging File)", "ক্যাশ মেমোরি", "বাফার মেমোরি", "রম"],
    "answer": "ক",
    "explanation": "ভার্চুয়াল মেমোরি ফিজিক্যাল র‍্যামের সম্প্রসারণ হিসেবে হার্ডডিস্কের 'pagefile.sys' অংশ ব্যবহার করে বড় প্রোগ্রাম চালায়।"
})

questions.append({
    "id": 61,
    "topic": topic_1_2,
    "question": "কম্পিউটারের নির্দিষ্ট পেরিফেরাল হার্ডওয়্যার (যেমন প্রিন্টার, গ্রাফিক্স কার্ড) ওএস এর সাথে যোগাযোগের জন্য কোন সফটওয়্যার প্রয়োজন?",
    "options": ["ডিভাইস ড্রাইভার (Device Driver)", "ফার্মওয়্যার", "কম্পাইলার", "অ্যান্টিভাইরাস"],
    "answer": "ক",
    "explanation": "ডিভাইস ড্রাইভার হলো বিশেষ সিস্টেম সফটওয়্যার যা ওএস-কে নির্দিষ্ট হার্ডওয়্যারের সাথে ডেটা আদান-প্রদানের নির্দেশ দেয়।"
})

questions.append({
    "id": 62,
    "topic": topic_1_2,
    "question": "উইন্ডোজে হার্ডওয়্যার ড্রাইভার বা সফটওয়্যার সমস্যার কারণে সিস্টেম ক্র্যাশ করলে যে নীল রঙের ত্রুটি স্ক্রিন আসে তাকে কী বলে?",
    "options": ["BSOD (Blue Screen of Death / Stop Error)", "Red Alert", "System Deadlock", "Memory Dump"],
    "answer": "ক",
    "explanation": "BSOD হলো উইন্ডোজের মারাত্মক কার্নেল ফল্ট বা স্টপ এরর যাতে ডেটা ক্ষতি রোধে ওএস নিজে থেকেই শাটডাউন হয়।"
})

questions.append({
    "id": 63,
    "topic": topic_1_2,
    "question": "উইন্ডোজ ট্রাবলশুটিং করার জন্য ন্যূনতম ড্রাইভার ও সার্ভিস দিয়ে চালু হওয়া মোডকে কী বলে?",
    "options": ["সেফ মোড (Safe Mode)", "নরমাল মোড", "ডিবাগ মোড", "হাইবারনেট মোড"],
    "answer": "ক",
    "explanation": "সেফ মোডে শুধুমাত্র প্রয়োজনীয় ড্রাইভার লোড হয়, ফলে সমস্যা সৃষ্টিকারী ম্যালওয়্যার বা ড্রাইভার অপসারণ করা যায়।"
})

questions.append({
    "id": 64,
    "topic": topic_1_2,
    "question": "কম্পিউটারের ফাইল সিস্টেমে '.exe' কোন ধরনের ফাইলের এক্সটেনশন?",
    "options": ["এক্সিকিউটেবল ফাইল (Executable Program)", "টেক্সট ডকুমেন্ট", "অডিও ফাইল", "সিস্টেম ফাইল"],
    "answer": "ক",
    "explanation": "'.exe' হলো উইন্ডোজের সরাসরি নির্বাহযোগ্য (Executable) বাইনারি প্রোগ্রাম ফাইল।"
})

questions.append({
    "id": 65,
    "topic": topic_1_2,
    "question": "নিচের কোন উইন্ডোজ ইউটিলিটি অপ্রয়োজনীয় অস্থায়ী (Temporary) ফাইল মুছে ডিস্ক স্পেস খালি করে?",
    "options": ["Disk Cleanup (cleanmgr)", "Disk Management", "Event Viewer", "Resource Monitor"],
    "answer": "ক",
    "explanation": "Disk Cleanup সিস্টেম টেম্পোরারি ফাইল, ক্যাশ এবং রিসাইকেল বিনের বর্জ্য অপসারণ করে স্টোরেজ খালি করে।"
})

questions.append({
    "id": 66,
    "topic": topic_1_2,
    "question": "কম্পিউটার বন্ধ হওয়ার ঠিক পূর্বের সমস্ত কাজের অবস্থা হার্ডডিস্কে সেভ করে সম্পূর্ণ পাওয়ার অফ করার মোড কোনটি?",
    "options": ["হাইবারনেট (Hibernate)", "স্লিপ (Sleep)", "লগ অফ", "শাটডাউন"],
    "answer": "ক",
    "explanation": "হাইবারনেশনে র‍্যামের সমস্ত কন্টেন্ট হার্ডডিস্কের 'hiberfil.sys' ফাইলে লিখে শূন্য বিদ্যুৎ খরচ করে বন্ধ হয়ে যায়।"
})

questions.append({
    "id": 67,
    "topic": topic_1_2,
    "question": "উইন্ডোজ ডিফেন্ডার (Windows Defender) মূলত কোন ধরনের সফটওয়্যার?",
    "options": ["বিল্ট-ইন অ্যান্টিভাইরাস ও অ্যান্টি-ম্যালওয়্যার", "ওয়েব ব্রাউজার", "মিডিয়া প্লেয়ার", "ফাইল কম্প্রেসার"],
    "answer": "ক",
    "explanation": "উইন্ডোজ ডিফেন্ডার (বা Microsoft Defender) হলো মাইক্রোসফটের অফিসিয়াল রিয়েল-টাইম সিকিউরিটি সফটওয়্যার।"
})

questions.append({
    "id": 68,
    "topic": topic_1_2,
    "question": "উইন্ডোজে একটি ফাইলকে 'Read-Only' করে রাখলে কী ঘটে?",
    "options": ["ফাইলটি শুধুমাত্র পড়া যাবে, কিন্তু পরিবর্তন বা সেভ করা যাবে না", "ফাইলটি ওপেন করা যাবে না", "ফাইলটি হাইড হয়ে যাবে", "ফাইলটি মুছে যাবে"],
    "answer": "ক",
    "explanation": "Read-Only অ্যাট্রিবিউট দিলে ব্যবহারকারী ফাইলটি দেখতে পারেন কিন্তু মূল ফাইলে কোনো নতুন তথ্য ওভাররাইট করতে পারেন না।"
})

questions.append({
    "id": 69,
    "topic": topic_1_2,
    "question": "উইন্ডোজ ১০ বা ১১-এ ভার্চুয়াল ডেস্কটপ তৈরি করার শর্টকাট কী কোনটি?",
    "options": ["Win + Ctrl + D", "Win + Tab", "Ctrl + Alt + D", "Win + V"],
    "answer": "ক",
    "explanation": "Windows Key + Ctrl + D চাপলে সাথে সাথে একটি নতুন ভার্চুয়াল ডেস্কটপ তৈরি হয়।"
})

questions.append({
    "id": 70,
    "topic": topic_1_2,
    "question": "উইন্ডোজের ক্লিপবোর্ড হিস্ট্রি (Clipboard History) ওপেন করার শর্টকাট কোনটি?",
    "options": ["Win + V", "Ctrl + V", "Win + C", "Alt + V"],
    "answer": "ক",
    "explanation": "Win + V চাপলে একাধিক পূর্বে কপি করা টেক্সট ও ছবির ক্লিপবোর্ড তালিকা প্রদর্শিত হয়।"
})

print("Generated Topic 1.2: 30 questions")

# ==============================================================================
# অধ্যায় ১.৩: ওয়ার্ড প্রসেসিং অ্যাপ্লিকেশন (MS Word & Documentation) (Questions 71 to 105)
# ==============================================================================
topic_1_3 = "অধ্যায় ১.৩: ওয়ার্ড প্রসেসিং অ্যাপ্লিকেশন (MS Word)"

questions.append({
    "id": 71,
    "topic": topic_1_3,
    "question": "মাইক্রোসফট ওয়ার্ড ২০০৭ ও পরবর্তী ভার্সনের ডিফল্ট ফাইল এক্সটেনশন কোনটি?",
    "options": [".docx", ".doc", ".dotx", ".txt"],
    "answer": "ক",
    "explanation": "Office 2007 থেকে এক্সএমএল-ভিত্তিক ওপেন ফরম্যাট হিসেবে '.docx' ডিফল্ট ফাইল এক্সটেনশন।"
})

questions.append({
    "id": 72,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডে বানান ও ব্যাকরণ (Spelling & Grammar) যাচাই করার শর্টকাট কী কোনটি?",
    "options": ["F7", "F5", "F12", "Shift + F7"],
    "answer": "ক",
    "explanation": "F7 চাপলে সরাসরি স্পেলিং ও গ্রামার চেকার ডায়ালগ বক্স ওপেন হয়।"
})

questions.append({
    "id": 73,
    "topic": topic_1_3,
    "question": "শব্দের সমার্থক বা বিপরীতার্থক শব্দ খোঁজার টুল 'থিসরাস' (Thesaurus) খোলার শর্টকাট কী কোনটি?",
    "options": ["Shift + F7", "Ctrl + F7", "Alt + F7", "F7"],
    "answer": "ক",
    "explanation": "Shift + F7 চাপলে নির্বাচিত শব্দের প্রতিশব্দ বা থিসরাস প্যান সক্রিয় হয়।"
})

questions.append({
    "id": 74,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডে একটি ডকুমেন্টের সমস্ত লেখা একবারে সিলেক্ট (Select All) করার কমান্ড কোনটি?",
    "options": ["Ctrl + A", "Ctrl + S", "Ctrl + Shift + A", "Alt + A"],
    "answer": "ক",
    "explanation": "Ctrl + A চাপলে সম্পূর্ণ ডকুমেন্টের সকল কনটেন্ট সিলেক্ট হয়ে যায়।"
})

questions.append({
    "id": 75,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডে টেক্সটকে উভয় প্রান্তে সমান করে সাজানোর 'Justify' অ্যালাইনমেন্টের শর্টকাট কোনটি?",
    "options": ["Ctrl + J", "Ctrl + E", "Ctrl + L", "Ctrl + R"],
    "answer": "ক",
    "explanation": "Ctrl + J টেক্সটকে জাস্টিফাই করে, Ctrl + E সেন্টার করে, Ctrl + L লেফট এবং Ctrl + R রাইট অ্যালাইন করে।"
})

questions.append({
    "id": 76,
    "topic": topic_1_3,
    "question": "সাবস্ক্রিপ্ট (Subscript - যেমন $H_2O$) করার কীবোর্ড শর্টকাট কোনটি?",
    "options": ["Ctrl + =", "Ctrl + Shift + +", "Alt + =", "Ctrl + Sub"],
    "answer": "ক",
    "explanation": "Ctrl + = সাবস্ক্রিপ্ট তৈরি করে এবং Ctrl + Shift + + সুপারস্ক্রিপ্ট ($X^2$) তৈরি করে।"
})

questions.append({
    "id": 77,
    "topic": topic_1_3,
    "question": "সুপারস্ক্রিপ্ট (Superscript - যেমন $X^2$) করার কীবোর্ড শর্টকাট কোনটি?",
    "options": ["Ctrl + Shift + +", "Ctrl + =", "Alt + Shift + +", "Shift + F3"],
    "answer": "ক",
    "explanation": "Ctrl + Shift + + কোনো অক্ষরকে লাইনের ওপরে সুপারস্ক্রিপ্ট হিসেবে বসায়।"
})

questions.append({
    "id": 78,
    "topic": topic_1_3,
    "question": "ইংরেজি লেখার কেস দ্রুত পরিবর্তন (UPPERCASE, lowercase, Title Case) করার শর্টকাট কোনটি?",
    "options": ["Shift + F3", "Ctrl + F3", "Alt + F3", "F3"],
    "answer": "ক",
    "explanation": "Shift + F3 চাপলে পর্যায়ক্রমে ক্যাপিটাল, স্মল ও প্রপার কেসে পরিবর্তন হয়।"
})

questions.append({
    "id": 79,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডে নতুন একটি খালি পেজ বা পেজ ব্রেক (Page Break) দেওয়ার শর্টকাট কী কোনটি?",
    "options": ["Ctrl + Enter", "Shift + Enter", "Alt + Enter", "Ctrl + Shift + Enter"],
    "answer": "ক",
    "explanation": "Ctrl + Enter চাপলে কার্সারের বর্তমান অবস্থান থেকে নতুন পেজ শুরু হয়।"
})

questions.append({
    "id": 80,
    "topic": topic_1_3,
    "question": "প্যারাগ্রাফের মাঝে নতুন লাইন তৈরি করতে কিন্তু প্যারাগ্রাফ ব্রেক না করার জন্য কোনটি ব্যবহার করা হয়?",
    "options": ["Shift + Enter (Soft Return)", "Ctrl + Enter", "Enter", "Alt + Enter"],
    "answer": "ক",
    "explanation": "Shift + Enter দিলে লাইন ব্রেক হয় কিন্তু প্যারাগ্রাফ স্পেসিং ছাড়া একই প্যারাগ্রাফে থাকে।"
})

questions.append({
    "id": 81,
    "topic": topic_1_3,
    "question": "কোন ফিচারের মাধ্যমে একই চিঠি বা নোটিশ শত শত ভিন্ন ঠিকানায় স্বয়ংক্রিয়ভাবে তৈরি ও প্রিন্ট করা যায়?",
    "options": ["মেইল মার্জ (Mail Merge)", "ম্যাক্রো", "হাইপারলিঙ্ক", "ট্র্যাক চেঞ্জেস"],
    "answer": "ক",
    "explanation": "Mail Merge মূল ডকুমেন্টের সাথে ডেটা সোর্স (এক্সেল বা আউটলুক কন্টাক্ট) যুক্ত করে গণ-চিঠিপত্র তৈরি করে।"
})

questions.append({
    "id": 82,
    "topic": topic_1_3,
    "question": "একটি ডকুমেন্টের পৃষ্ঠার হালকা জলছাপের মতো লেখা বা ছবি (যেমন- Confidential, Draft) দেওয়াকে কী বলে?",
    "options": ["ওয়াটারমার্ক (Watermark)", "হেডার", "ফুটার", "বর্ডার"],
    "answer": "ক",
    "explanation": "Watermark হলো পেজের ব্যাকগ্রাউন্ডে টেক্সটের পেছনে থাকা হালকা লোগো বা সতর্কবার্তা।"
})

questions.append({
    "id": 83,
    "topic": topic_1_3,
    "question": "ডকুমেন্টের প্রতিটি পৃষ্ঠার শীর্ষে স্বয়ংক্রিয়ভাবে একই শিরোনাম বা অধ্যায়ের নাম প্রদর্শনের জন্য কোনটি ব্যবহৃত হয়?",
    "options": ["হেডার (Header)", "ফুটার (Footer)", "এন্ডনোট", "পাদটীকা"],
    "answer": "ক",
    "explanation": "Header পেজের টপ মার্জিনে থাকে এবং এটি ডকুমেন্টের প্রতিটি পৃষ্ঠায় স্বয়ংক্রিয়ভাবে পুনরাবৃত্তি হয়।"
})

questions.append({
    "id": 84,
    "topic": topic_1_3,
    "question": "ফুটনোট (Footnote) এবং এন্ডনোট (Endnote) এর মধ্যে মৌলিক পার্থক্য কী?",
    "options": ["ফুটনোট সংশ্লিষ্ট পৃষ্ঠার নিচে থাকে, এন্ডনোট সম্পূর্ণ ডকুমেন্টের সর্বশেষে থাকে", "ফুটনোট শুধু উপরে থাকে", "এন্ডনোট পেজের বামে থাকে", "এদের মাঝে কোনো পার্থক্য নেই"],
    "answer": "ক",
    "explanation": "Footnote রেফারেন্স পেজের নিচে প্রদর্শিত হয়, আর Endnote পুরো ডকুমেন্টের শেষ পৃষ্ঠায় তালিকাভুক্ত হয়।"
})

questions.append({
    "id": 85,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডে পূর্বে সম্পাদিত কোনো কাজ বাতিল করে পূর্বের অবস্থায় ফেরার (Undo) কমান্ড কোনটি?",
    "options": ["Ctrl + Z", "Ctrl + Y", "Ctrl + U", "Ctrl + X"],
    "answer": "ক",
    "explanation": "Ctrl + Z হলো আনডু (Undo) এবং Ctrl + Y হলো রিডু (Redo)।"
})

questions.append({
    "id": 86,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডে 'Save As' ডায়ালগ বক্স সরাসরি ওপেন করার শর্টকাট কী কোনটি?",
    "options": ["F12", "Ctrl + S", "Shift + F12", "Alt + F12"],
    "answer": "ক",
    "explanation": "F12 চাপলে নতুন নাম বা ফরম্যাটে ফাইল সংরক্ষণের 'Save As' উইন্ডো চলে আসে।"
})

questions.append({
    "id": 87,
    "topic": topic_1_3,
    "question": "ডকুমেন্টে কোনো নির্দিষ্ট টেক্সট খুঁজে বের করে অন্য টেক্সট দ্বারা প্রতিস্থাপনের (Find & Replace) শর্টকাট কোনটি?",
    "options": ["Ctrl + H", "Ctrl + F", "Ctrl + G", "Ctrl + R"],
    "answer": "ক",
    "explanation": "Ctrl + F শুধুমাত্র ফাইন্ড (Find) করে, আর Ctrl + H সরাসরি 'Replace' ডায়ালগ বক্স ওপেন করে।"
})

questions.append({
    "id": 88,
    "topic": topic_1_3,
    "question": "টেক্সটের ফরম্যাটিং কপি করে অন্য টেক্সটে হুবহু প্রয়োগ করার জন্য কোন টুল ব্যবহৃত হয়?",
    "options": ["ফরম্যাট পেন্টার (Format Painter)", "কপি-পেস্ট", "স্টাইল গ্যালারি", "ক্লিপবোর্ড"],
    "answer": "ক",
    "explanation": "Format Painter (Ctrl + Shift + C এবং Ctrl + Shift + V) টেক্সটের ফন্ট, সাইজ ও কালার স্টাইল কপি করে।"
})

questions.append({
    "id": 89,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ড টেবিলের একাধিক সেলকে একত্র করে একটি মাত্র সেলে রূপান্তর করাকে কী বলে?",
    "options": ["Merge Cells", "Split Cells", "Wrap Text", "Group"],
    "answer": "ক",
    "explanation": "Merge Cells নির্বাচিত একাধিক পাশাপাশি বা ওপর-নিচের সেলকে একটি একক সেলে রূপান্তর করে।"
})

questions.append({
    "id": 90,
    "topic": topic_1_3,
    "question": "একটি একক সেলকে একাধিক সারি বা কলামে বিভক্ত করাকে কী বলে?",
    "options": ["Split Cells", "Merge Cells", "Delete Cells", "Align Cells"],
    "answer": "ক",
    "explanation": "Split Cells অপশনের মাধ্যমে একটি সেলকে নির্দিষ্ট সংখ্যক রো ও কলামে ভাগ করা যায়।"
})

questions.append({
    "id": 91,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডে হাইপারলিঙ্ক (Hyperlink) ইনসার্ট করার কীবোর্ড শর্টকাট কোনটি?",
    "options": ["Ctrl + K", "Ctrl + H", "Ctrl + L", "Alt + K"],
    "answer": "ক",
    "explanation": "Ctrl + K চাপলে নির্দিষ্ট লেখার সাথে ওয়েব লিংক বা অন্য ফাইলের সংযোগ স্থাপনের অপশন আসে।"
})

questions.append({
    "id": 92,
    "topic": topic_1_3,
    "question": "ডকুমেন্টের প্রিন্ট আউট নেওয়ার পূর্বে কেমন দেখাবে তা দেখার অপশনকে কী বলে?",
    "options": ["প্রিন্ট প্রিভিউ (Print Preview)", "রিড মোড", "ওয়েব লেআউট", "আউটলাইন ভিউ"],
    "answer": "ক",
    "explanation": "Ctrl + F2 বা Print Preview মার্জিন ও লেআউট ঠিক আছে কিনা তা প্রিন্ট করার আগেই প্রদর্শন করে।"
})

questions.append({
    "id": 93,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডে ড্রপ ক্যাপ (Drop Cap) ফিচারের মূল কাজ কী?",
    "options": ["প্যারাগ্রাফের প্রথম অক্ষরটিকে অনেক বড় করে কয়েক লাইন জুড়ে প্রদর্শন করা", "সব লেখা ছোট করা", "প্রথম শব্দ ডিলিট করা", "পাসওয়ার্ড দেওয়া"],
    "answer": "ক",
    "explanation": "সংবাদপত্র বা ম্যাগাজিনে প্যারাগ্রাফের প্রথম বর্ণ বড় করে ৩/৪ লাইন উচ্চতায় উপস্থাপন করতে Drop Cap ব্যবহৃত হয়।"
})

questions.append({
    "id": 94,
    "topic": topic_1_3,
    "question": "ডকুমেন্টে একাধিক ব্যবহারকারীর করা সম্পাদনা, সংশোধন ও মন্তব্য ট্র্যাক করার ফিচারের নাম কী?",
    "options": ["ট্র্যাক চেঞ্জেস (Track Changes)", "ম্যাক্রো", "স্পেল চেকার", "কম্পেয়ার"],
    "answer": "ক",
    "explanation": "Track Changes (Ctrl + Shift + E) চালুকৃত অবস্থায় যেকোনো সংযোজন বা বিয়োজন আলাদা রঙে দৃশ্যমান থাকে।"
})

questions.append({
    "id": 95,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডে বারবার করতে হওয়া একাধিক কমান্ড রেকর্ড করে পরবর্তীতে এক ক্লিকে চালানোর প্রযুক্তি কোনটি?",
    "options": ["ম্যাক্রো (Macro - VBA)", "মেইল মার্জ", "টেমপ্লেট", "স্মার্টআর্ট"],
    "answer": "ক",
    "explanation": "ম্যাক্রো পুনরাবৃত্তিমূলক কাজ রেকর্ড করে এবং শর্টকাট কি দিয়ে স্বয়ংক্রিয়ভাবে রান করতে পারে।"
})

questions.append({
    "id": 96,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডের ডিফল্ট পেজ ওরিয়েন্টেশন (Page Orientation) কোনটি থাকে?",
    "options": ["পোর্ট্রেট (Portrait - খাড়া)", "ল্যান্ডস্কেপ (Landscape - আড়াআড়ি)", "বুকলেট", "ইনভার্টেড"],
    "answer": "ক",
    "explanation": "এমএস ওয়ার্ড ডকুমেন্টের স্বাভাবিক পেজ ওরিয়েন্টেশন থাকে Portrait বা উলম্ব।"
})

questions.append({
    "id": 97,
    "topic": topic_1_3,
    "question": "বই বাঁধানোর জন্য পেজের ভেতর যে অতিরিক্ত মার্জিন স্পেস যোগ করা হয় তাকে কী মার্জিন বলে?",
    "options": ["গাটার মার্জিন (Gutter Margin)", "টপ মার্জিন", "লেফট মার্জিন", "মিরর মার্জিন"],
    "answer": "ক",
    "explanation": "Gutter Margin বই বাঁধাই বা স্পাইরাল বাইন্ডিংয়ের সময় লেখা যাতে কেটে না যায় সেজন্য বরাদ্দ থাকে।"
})

questions.append({
    "id": 98,
    "topic": topic_1_3,
    "question": "শব্দের নিচে লাল রঙের আঁকাবাঁকা রেখা (Red Wavy Underline) কী নির্দেশ করে?",
    "options": ["বানান ভুল (Spelling Error)", "ব্যাকরণগত ভুল (Grammar Error)", "হাইপারলিঙ্ক", "ফরম্যাটিং অসঙ্গতি"],
    "answer": "ক",
    "explanation": "লাল আঁকাবাঁকা দাগ দিয়ে স্পেলিং ভুল এবং নীল বা সবুজ দাগ দিয়ে ব্যাকরণগত (Grammar) ত্রুটি নির্দেশ করে।"
})

questions.append({
    "id": 99,
    "topic": topic_1_3,
    "question": "শব্দের নিচে নীল রঙের আঁকাবাঁকা রেখা (Blue Wavy Underline) কী নির্দেশ করে?",
    "options": ["ব্যাকরণগত বা কনটেক্সচুয়াল ভুল (Grammar / Contextual Error)", "বানান ভুল", "প্রিন্ট এরর", "ফন্ট মিসিং"],
    "answer": "ক",
    "explanation": "আধুনিক ওয়ার্ডে নীল দাগ ব্যাকরণগত অসঙ্গতি বা ব্যাকরণগত ভুল নির্দেশ করে।"
})

questions.append({
    "id": 100,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ডে ফন্ট সাইজ এক পয়েন্ট করে বড় (Grow Font) করার কীবোর্ড শর্টকাট কোনটি?",
    "options": ["Ctrl + ]", "Ctrl + [", "Ctrl + Shift + >", "Alt + ]"],
    "answer": "ক",
    "explanation": "Ctrl + ] এক পয়েন্ট বৃদ্ধি করে এবং Ctrl + [ এক পয়েন্ট হ্রাস করে।"
})

questions.append({
    "id": 101,
    "topic": topic_1_3,
    "question": "এমএস ওয়ার্ড ডকুমেন্টের জুম লেভেল সর্বনিম্ন এবং সর্বোচ্চ কত শতাংশ হতে পারে?",
    "options": ["১০% থেকে ৫০০%", "২০% থেকে ২০০%", "১০% থেকে ১০০%", "১% থেকে ১০০০%"],
    "answer": "ক",
    "explanation": "এমএস ওয়ার্ডে ভিউ জুম সর্বনিম্ন 10% এবং সর্বোচ্চ 500% পর্যন্ত বাড়ানো যায়।"
})

questions.append({
    "id": 102,
    "topic": topic_1_3,
    "question": "এক পেজের লেখা থেকে অন্য সেকশনে আলাদা মার্জিন বা হেডার দিতে কোনটি ইনসার্ট করতে হয়?",
    "options": ["সেকশন ব্রেক (Section Break)", "পেজ ব্রেক", "কলাম ব্রেক", "টেক্সট র‍্যাপিং"],
    "answer": "ক",
    "explanation": "Section Break একই ডকুমেন্টে আলাদা পৃষ্ঠা বিন্যাস, মার্জিন বা ভিন্ন হেডার/ফুটার ব্যবহার করার সুবিধা দেয়।"
})

questions.append({
    "id": 103,
    "topic": topic_1_3,
    "question": "ডকুমেন্টের একটি শব্দ বা অনুচ্ছেদের ওপর মন্তব্য লিখে রাখার টুলের নাম কী?",
    "options": ["কমেন্ট (Comment)", "ফুটনোট", "ক্যাপশন", "বুকমার্ক"],
    "answer": "ক",
    "explanation": "Comment টুলের মাধ্যমে মূল টেক্সট অপরিবর্তিত রেখে ডানপাশে মন্তব্য যুক্ত করা যায়।"
})

questions.append({
    "id": 104,
    "topic": topic_1_3,
    "question": "ডকুমেন্টের ভেতরের নির্দিষ্ট কোনো স্থানে দ্রুত জাম্প করার জন্য যে ল্যান্ডমার্ক তৈরি করা হয় তাকে কী বলে?",
    "options": ["বুকমার্ক (Bookmark)", "হাইপারলিঙ্ক", "ক্রস-রেফারেন্স", "ইনডেক্স"],
    "answer": "ক",
    "explanation": "Bookmark কোনো নির্দিষ্ট টেক্সট বা স্থানে নাম দিয়ে চিহ্নিত করে রাখে যাতে পরবর্তীতে সহজে লিংক করা যায়।"
})

questions.append({
    "id": 105,
    "topic": topic_1_3,
    "question": "একটি এমএস ওয়ার্ড ডকুমেন্টকে অপরিবর্তনীয় ও সুরক্ষিত পিডিএফ (PDF) ফরম্যাটে সংরক্ষণের জন্য কোনটি ব্যবহার করা হয়?",
    "options": ["Export / Save as PDF", "Print to Word", "Save as HTML", "Convert to RTF"],
    "answer": "ক",
    "explanation": "File -> Export -> Create PDF/XPS দিয়ে সহজেই নিরাপদ ও বহনযোগ্য পিডিএফ তৈরি করা যায়।"
})

print("Generated Topic 1.3: 35 questions")

# ==============================================================================
# অধ্যায় ১.৪: স্প্রেডশিট অ্যানালাইসিস (MS Excel & Data Analytics) (Questions 106 to 145)
# ==============================================================================
topic_1_4 = "অধ্যায় ১.৪: স্প্রেডশিট অ্যানালাইসিস (MS Excel)"

questions.append({
    "id": 106,
    "topic": topic_1_4,
    "question": "মাইক্রোসফট এক্সেলের প্রতিটি ফাইলকে প্রযুক্তিগতভাবে কী বলা হয়?",
    "options": ["ওয়ার্কবুক (Workbook)", "ওয়ার্কশিট (Worksheet)", "স্প্রেডশিট ডাটাবেস", "সেল ডকুমেন্ট"],
    "answer": "ক",
    "explanation": "এক্সেলের একটি পূর্ণাঙ্গ ফাইলকে Workbook বলা হয়, যার ভেতরে একাধিক Worksheet থাকতে পারে।"
})

questions.append({
    "id": 107,
    "topic": topic_1_4,
    "question": "এমএস এক্সেলে একটি কলাম এবং একটি সারির মিলনস্থলকে কী বলা হয়?",
    "options": ["সেল (Cell)", "ব্লক", "গ্রিড", "বক্স"],
    "answer": "ক",
    "explanation": "কলাম ও রো পরস্পরকে ছেদ করে যে আয়তাকার ক্ষেত্র তৈরি করে তাকে Cell বলে।"
})

questions.append({
    "id": 108,
    "topic": topic_1_4,
    "question": "এমএস এক্সেল ২০০৭ থেকে বর্তমান সংস্করণে একটি একক শিটে মোট কতটি সারি (Rows) থাকে?",
    "options": ["১০,৪৮,৫৭৬ ($2^{20}$)", "৬৫,৫৩৬", "১৬,৩৮৪", "১,০০,০০০"],
    "answer": "ক",
    "explanation": "Excel 2007 থেকে মোট সারি সংখ্যা ১,০৪৮,৫৭৬ এবং কলাম সংখ্যা ১৬,৩৮৪ (A থেকে XFD)।"
})

questions.append({
    "id": 109,
    "topic": topic_1_4,
    "question": "বর্তমান সক্রিয় সেলের নাম বা রেফারেন্স এক্সেলের কোন অংশে প্রদর্শিত হয়?",
    "options": ["নেম বক্স (Name Box)", "ফর্মুলা বার (Formula Bar)", "স্ট্যাটাস বার", "টাইটেল বার"],
    "answer": "ক",
    "explanation": "ফর্মুলা বারের বাম পাশে অবস্থিত Name Box-এ সক্রিয় সেলের অ্যাড্রেস (যেমন C5) দেখা যায়।"
})

questions.append({
    "id": 110,
    "topic": topic_1_4,
    "question": "এমএস এক্সেলে যেকোনো ফর্মুলা বা সূত্র লেখার পূর্বে কোন চিহ্নটি দেওয়া বাধ্যতামূলক?",
    "options": ["= (সমান চিহ্ন)", "@ (অ্যাট চিহ্ন)", "+ (প্লাস চিহ্ন)", "# (হ্যাশ চিহ্ন)"],
    "answer": "ক",
    "explanation": "এক্সেল কোনো এন্ট্রিকে ফর্মুলা হিসেবে বিবেচনা করার জন্য সর্বপ্রথম '=' চিহ্ন দিতে হয়।"
})

questions.append({
    "id": 111,
    "topic": topic_1_4,
    "question": "এক্সেলে '$A$1' কোন ধরনের সেল রেফারেন্সের উদাহরণ?",
    "options": ["অ্যাবসলিউট রেফারেন্স (Absolute Reference)", "রিলেটিভ রেফারেন্স", "মিক্সড রেফারেন্স", "সার্কুলার রেফারেন্স"],
    "answer": "ক",
    "explanation": "কলাম ও রো উভয়ের আগে ডেইলার ($) চিহ্ন থাকলে তা সূত্র কপি করার সময় লক থাকে, একে Absolute Reference বলে।"
})

questions.append({
    "id": 112,
    "topic": topic_1_4,
    "question": "এক্সেলে সেল রেফারেন্সকে রিলেটিভ থেকে অ্যাবসলিউটে রূপান্তর করার ফাংশন কি কোনটি?",
    "options": ["F4", "F2", "F9", "F12"],
    "answer": "ক",
    "explanation": "ফর্মুলা এডিট করার সময় 'F4' চাপলে A1 ক্রমানুসারে $A$1, A$1, $A1-এ পরিবর্তিত হয়।"
})

questions.append({
    "id": 113,
    "topic": topic_1_4,
    "question": "A1 থেকে A10 পর্যন্ত সেলের সংখ্যার গড় নির্ণয়ের সঠিক ফর্মুলা কোনটি?",
    "options": ["=AVERAGE(A1:A10)", "=AVG(A1:A10)", "=MEAN(A1:A10)", "=TOTAL(A1:A10)/10"],
    "answer": "ক",
    "explanation": "এক্সেলে গাণিতিক গড় নির্ণয়ের বিল্ট-ইন ফাংশন হলো AVERAGE।"
})

questions.append({
    "id": 114,
    "topic": topic_1_4,
    "question": "কোন ফাংশনটি শুধুমাত্র সংখ্যাযুক্ত (Numeric) সেল গণনা করে, টেক্সট বা ফাঁকা সেল গণনা করে না?",
    "options": ["COUNT()", "COUNTA()", "COUNTBLANK()", "COUNTIF()"],
    "answer": "ক",
    "explanation": "COUNT() শুধু সংখ্যা গণনা করে; আর COUNTA() ফাঁকা বাদে যেকোনো ধরনের ডেটাযুক্ত সেল গণনা করে।"
})

questions.append({
    "id": 115,
    "topic": topic_1_4,
    "question": "একটি নির্দিষ্ট শর্তের ভিত্তিতে সংখ্যা যোগ করার জন্য কোন এক্সেল ফাংশন ব্যবহৃত হয়?",
    "options": ["SUMIF()", "SUM()", "COUNTIF()", "IF()"],
    "answer": "ক",
    "explanation": "SUMIF(range, criteria, [sum_range]) নির্দিষ্ট শর্ত পূরণকারী সেলসমূহের যোগফল প্রদান করে।"
})

questions.append({
    "id": 116,
    "topic": topic_1_4,
    "question": "এক্সেলে টেবিলের প্রথম কলামে কোনো মান উল্লম্বভাবে খুঁজে সংশ্লিষ্ট সারির অন্য কলামের ডেটা আনার ফাংশন কোনটি?",
    "options": ["VLOOKUP()", "HLOOKUP()", "MATCH()", "OFFSET()"],
    "answer": "ক",
    "explanation": "VLOOKUP (Vertical Lookup) বাম কলামে ভ্যালু খুঁজে ডানপাশের নির্দিষ্ট ইনডেক্সের মান রিটার্ন করে।"
})

questions.append({
    "id": 117,
    "topic": topic_1_4,
    "question": "টেবিলের প্রথম সারিতে কোনো মান অনুভূমিকভাবে (Horizontally) খোঁজার ফাংশন কোনটি?",
    "options": ["HLOOKUP()", "VLOOKUP()", "LOOKUP()", "XLOOKUP()"],
    "answer": "ক",
    "explanation": "HLOOKUP (Horizontal Lookup) টেবিলের শীর্ষ সারিতে ভ্যালু খুঁজে নিচের সারির মান নিয়ে আসে।"
})

questions.append({
    "id": 118,
    "topic": topic_1_4,
    "question": "আধুনিক এক্সেলে VLOOKUP ও HLOOKUP-এর সীমাবদ্ধতা দূরকারী শক্তিশালী দ্বি-মুখী লুকআপ ফাংশন কোনটি?",
    "options": ["XLOOKUP()", "ZLOOKUP()", "POWERLOOKUP()", "INDEX()"],
    "answer": "ক",
    "explanation": "XLOOKUP যেকোনো দিকে (বামে, ডানে, উপরে, নিচে) কোনো ঝামেলা ছাড়াই সরাসরি লুকআপ করতে সক্ষম।"
})

questions.append({
    "id": 119,
    "topic": topic_1_4,
    "question": "এক্সেলে শর্তাধীন লজিক্যাল সিদ্ধান্ত গ্রহণের ফাংশন কোনটি?",
    "options": ["IF()", "AND()", "OR()", "CHECK()"],
    "answer": "ক",
    "explanation": "IF(Logical_test, Value_if_true, Value_if_false) হলো মৌলিক শর্তাধীন ফাংশন।"
})

questions.append({
    "id": 120,
    "topic": topic_1_4,
    "question": "এক্সেলে একাধিক টেক্সট বা স্ট্রিংকে একসাথে জোড়া লাগানোর ফাংশন কোনটি?",
    "options": ["CONCATENATE() বা CONCAT()", "JOIN()", "MERGE()", "COMBINE()"],
    "answer": "ক",
    "explanation": "CONCATENATE() বা '&' অপারেটর একাধিক সেলের লেখাকে একত্রিত করে একক স্ট্রিং তৈরি করে।"
})

questions.append({
    "id": 121,
    "topic": topic_1_4,
    "question": "একটি সেলের টেক্সটের মোট অক্ষরের সংখ্যা গণনা করার ফাংশন কোনটি?",
    "options": ["LEN()", "LENGTH()", "COUNT()", "TEXTCOUNT()"],
    "answer": "ক",
    "explanation": "LEN(text) ফাংশন টেক্সটে বিদ্যমান স্পেস সহ মোট ক্যারেক্টার সংখ্যা গণনা করে।"
})

questions.append({
    "id": 122,
    "topic": topic_1_4,
    "question": "টেক্সটের শুরুতে ও শেষে থাকা অপ্রয়োজনীয় অতিরিক্ত স্পেস দূর করার ফাংশন কোনটি?",
    "options": ["TRIM()", "CLEAN()", "REMOVE()", "CLEAR()"],
    "answer": "ক",
    "explanation": "TRIM(text) শব্দের মধ্যবর্তী একক স্পেস রেখে বাকি সব অতিরিক্ত স্পেস মুছে ফেলে।"
})

questions.append({
    "id": 123,
    "topic": topic_1_4,
    "question": "বিশাল পরিমাণ ডেটাকে তাৎক্ষণিকভাবে সারসংক্ষেপ, গ্রুপিং ও বিশ্লেষণ করার শক্তিশালী এক্সেল টুল কোনটি?",
    "options": ["পিভট টেবিল (Pivot Table)", "ম্যাক্রো", "ডাটা ভ্যালিডেশন", "শর্টিং"],
    "answer": "ক",
    "explanation": "Pivot Table ড্র্যাগ-অ্যান্ড-ড্রপ ফিল্ডের মাধ্যমে জটিল ডেটার সামারি, ফিল্টারিং ও ক্রস-ট্যাবুলেশন করে।"
})

questions.append({
    "id": 124,
    "topic": topic_1_4,
    "question": "এক্সেলে সেলের ভেতরে ভুল ডেটা প্রবেশ রোধে ড্রপডাউন তালিকা বা নিয়ম তৈরি করার টুলের নাম কী?",
    "options": ["ডেটা ভ্যালিডেশন (Data Validation)", "কন্ডিশনাল ফরম্যাটিং", "প্রটেক্ট শিট", "কনসলিডেট"],
    "answer": "ক",
    "explanation": "Data Validation সেলে কোন ধরনের ডেটা বা সীমা (যেমন ১-১০০, ড্রপডাউন লিস্ট) ইনপুট দেওয়া যাবে তা নিয়ন্ত্রণ করে।"
})

questions.append({
    "id": 125,
    "topic": topic_1_4,
    "question": "নির্দিষ্ট শর্ত পূরণ করলে সেলের রঙ স্বয়ংক্রিয়ভাবে পরিবর্তন (যেমন ৮০-এর বেশি পেলে সবুজ) করার টুলের নাম কী?",
    "options": ["কন্ডিশনাল ফরম্যাটিং (Conditional Formatting)", "ফরম্যাট সেলস", "স্টাইল", "অটো কালার"],
    "answer": "ক",
    "explanation": "Conditional Formatting সেলের মানের ওপর ভিত্তি করে কালার স্কেল বা হাইলাইট রুলস প্রয়োগ করে।"
})

questions.append({
    "id": 126,
    "topic": topic_1_4,
    "question": "কাঙ্ক্ষিত ফলাফল পাওয়ার জন্য কোনো নির্দিষ্ট ইনপুট ভ্যালু কত হতে হবে তা বের করার টুল কোনটি?",
    "options": ["গোল সিক (Goal Seek)", "সিনারিও ম্যানেজার", "সলভার", "ডাটা টেবিল"],
    "answer": "ক",
    "explanation": "Goal Seek হলো What-If অ্যানালাইসিসের একটি টুল যা ব্যাকওয়ার্ড ক্যালকুলেশন করে ইনপুট নির্ধারণ করে।"
})

questions.append({
    "id": 127,
    "topic": topic_1_4,
    "question": "বড় টেবিলে নিচের দিকে স্ক্রোল করার সময়ও শীর্ষ কলাম শিরোনাম যাতে সবসময় দৃশ্যমান থাকে সেজন্য কী করা হয়?",
    "options": ["ফ্রিজ প্যানস (Freeze Panes)", "স্প্লিট উইন্ডো", "হাইড রো", "লক সেলস"],
    "answer": "ক",
    "explanation": "Freeze Top Row বা Freeze Panes নির্দিষ্ট সারি ও কলামকে স্ক্রিনে স্থির আটকে রাখে।"
})

questions.append({
    "id": 128,
    "topic": topic_1_4,
    "question": "এক্সেলে সেলের প্রস্থের চেয়ে সংখ্যা বড় হয়ে গেলে সেলে কোন এরর মেসেজ প্রদর্শিত হয়?",
    "options": ["#####", "#VALUE!", "#DIV/0!", "#NAME?"],
    "answer": "ক",
    "explanation": "কলামের প্রস্থ সংখ্যা বা তারিখ প্রদর্শনের জন্য অপর্যাপ্ত হলে '#####' প্রদর্শিত হয়।"
})

questions.append({
    "id": 129,
    "topic": topic_1_4,
    "question": "এক্সেলে কোনো সংখ্যাকে শূন্য (0) দিয়ে ভাগ করার চেষ্টা করলে কোন এরর কোড আসে?",
    "options": ["#DIV/0!", "#NULL!", "#NUM!", "#REF!"],
    "answer": "ক",
    "explanation": "গাণিতিকভাবে শূন্য দিয়ে ভাগ অসংজ্ঞায়িত হওয়ায় এক্সেল '#DIV/0!' প্রদর্শন করে।"
})

questions.append({
    "id": 130,
    "topic": topic_1_4,
    "question": "ফর্মুলায় কোনো ফাংশনের নাম বা সেলের নাম ভুল টাইপ করলে কোন এরর আসে?",
    "options": ["#NAME?", "#VALUE!", "#N/A", "#REF!"],
    "answer": "ক",
    "explanation": "অচেনা ফাংশনের নাম বা নামহীন টেক্সট রেফারেন্সের ক্ষেত্রে '#NAME?' ত্রুটি আসে।"
})

questions.append({
    "id": 131,
    "topic": topic_1_4,
    "question": "ফর্মুলার রেফারেন্স দেওয়া কোনো সেল বা কলাম ডিলিট করে দিলে কোন এরর আসে?",
    "options": ["#REF!", "#VALUE!", "#NULL!", "#N/A"],
    "answer": "ক",
    "explanation": "বৈধ সেল রেফারেন্স হারিয়ে গেলে ইনভ্যালিড সেল রেফারেন্স '#REF!' আসে।"
})

questions.append({
    "id": 132,
    "topic": topic_1_4,
    "question": "এক্সেলে বর্তমান তারিখ (Current Date) স্বয়ংক্রিয়ভাবে ইনসার্ট করার ফাংশন কোনটি?",
    "options": ["=TODAY()", "=NOW()", "=DATE()", "=CURRENT()"],
    "answer": "ক",
    "explanation": "=TODAY() বর্তমান সিস্টেম তারিখ দেয়, আর =NOW() তারিখ এবং বর্তমান সময় উভয়ই দেয়।"
})

questions.append({
    "id": 133,
    "topic": topic_1_4,
    "question": "এক্সেলে বর্তমান তারিখ ও সময় (Current Date & Time) একসাথে পাওয়ার ফাংশন কোনটি?",
    "options": ["=NOW()", "=TODAY()", "=TIME()", "=DATETIME()"],
    "answer": "ক",
    "explanation": "=NOW() ফর্মুলাটি বর্তমান তারিখের সাথে সময়ও রিটার্ন করে।"
})

questions.append({
    "id": 134,
    "topic": topic_1_4,
    "question": "এক্সেলে স্বয়ংক্রিয়ভাবে অটো-সাম (AutoSum) করার কীবোর্ড শর্টকাট কোনটি?",
    "options": ["Alt + =", "Ctrl + =", "Shift + =", "Ctrl + S"],
    "answer": "ক",
    "explanation": "Alt + = চাপলে স্বয়ংক্রিয়ভাবে সংলগ্ন সারির যোগফলের SUM ফর্মুলা বসে যায়।"
})

questions.append({
    "id": 135,
    "topic": topic_1_4,
    "question": "সমগ্র শতকরা অংশের অনুপাত (Percentage of Whole) প্রদর্শনের জন্য কোন চার্ট সবচেয়ে উপযুক্ত?",
    "options": ["পাই চার্ট (Pie Chart)", "লাইন চার্ট", "বার চার্ট", "স্ক্যাটার প্লট"],
    "answer": "ক",
    "explanation": "Pie Chart ১০০% অংশের মধ্যে বিভিন্ন উপাদানের আনুপাতিক শেয়ার বৃত্তাকারে দেখায়।"
})

questions.append({
    "id": 136,
    "topic": topic_1_4,
    "question": "সময়ের সাথে ডেটার গতিবিধি বা ট্রেন্ড (Trend over time) প্রদর্শনের জন্য কোন চার্ট সেরা?",
    "options": ["লাইন চার্ট (Line Chart)", "পাই চার্ট", "রাডার চার্ট", "ডোনাট চার্ট"],
    "answer": "ক",
    "explanation": "দিন, মাস বা বছর অনুযায়ী ডেটার উত্থান-পতন প্রদর্শনে Line Chart সবচেয়ে জনপ্রিয়।"
})

questions.append({
    "id": 137,
    "topic": topic_1_4,
    "question": "এক্সেলে দুটি ভিন্ন ভ্যারিয়েবলের পারস্পরিক সম্পর্ক বা সহসম্বন্ধ প্রদর্শনে কোন চার্ট ব্যবহৃত হয়?",
    "options": ["স্ক্যাটার চার্ট (Scatter Plot / XY Chart)", "কলাম চার্ট", "পাই চার্ট", "বার চার্ট"],
    "answer": "ক",
    "explanation": "Scatter Plot দুটি সংখ্যাসূচক চলকের মধ্যকার রিলেশনশিপ বিন্দু আকারে প্রদর্শন করে।"
})

questions.append({
    "id": 138,
    "topic": topic_1_4,
    "question": "এক্সেলে একটি সেলের ভেতরেই ছোট আকারের ট্রেন্ড গ্রাফ প্রদর্শনকারী ফিচারকে কী বলে?",
    "options": ["স্পার্কলাইনস (Sparklines)", "মিনি চার্ট", "পিভট চার্ট", "ডাটা বার"],
    "answer": "ক",
    "explanation": "Sparklines হলো একক সেলের ভেতরে থাকা অতিক্ষুদ্র লাইন বা কলাম গ্রাফ।"
})

questions.append({
    "id": 139,
    "topic": topic_1_4,
    "question": "এক্সেলে সেলের ভেতর নতুন লাইন শুরু করতে (Wrap Text বাদে) কোন শর্টকাট চাপতে হয়?",
    "options": ["Alt + Enter", "Ctrl + Enter", "Shift + Enter", "Enter"],
    "answer": "ক",
    "explanation": "Alt + Enter চাপলে একই সেলের মধ্যে নতুন আরেকটি লাইন শুরু হয়।"
})

questions.append({
    "id": 140,
    "topic": topic_1_4,
    "question": "এক্সেলে স্বয়ংক্রিয় ধারাবাহিক প্যাটার্ন বুঝে বাকি সেল স্বয়ংক্রিয়ভাবে পূরণ করার জাদুকরী টুলের নাম কী?",
    "options": ["ফ্ল্যাশ ফিল (Flash Fill - Ctrl + E)", "অটো ফিল", "ফিল সিরিজ", "জাস্টিফাই"],
    "answer": "ক",
    "explanation": "Flash Fill (Ctrl + E) ব্যবহারকারীর প্যাটার্ন বুঝে ডেটা বিভাজন বা সমন্বয় স্বয়ংক্রিয়ভাবে সম্পন্ন করে।"
})

questions.append({
    "id": 141,
    "topic": topic_1_4,
    "question": "এক্সেলে কোনো সেলে কমেন্ট বা নোট যুক্ত করার শর্টকাট কী কোনটি?",
    "options": ["Shift + F2", "Ctrl + F2", "Alt + F2", "F2"],
    "answer": "ক",
    "explanation": "Shift + F2 চাপলে নির্বাচিত সেলে নোট বা কমেন্ট বক্স ওপেন হয়।"
})

questions.append({
    "id": 142,
    "topic": topic_1_4,
    "question": "এক্সেলে ফিল্টার (Filter) চালু বা বন্ধ করার কীবোর্ড শর্টকাট কোনটি?",
    "options": ["Ctrl + Shift + L", "Ctrl + F", "Alt + F", "Ctrl + Alt + L"],
    "answer": "ক",
    "explanation": "Ctrl + Shift + L চাপলে টেবিল হেডারে ড্রপডাউন ফিল্টার টগল হয়।"
})

questions.append({
    "id": 143,
    "topic": topic_1_4,
    "question": "এক্সেলে সেলের সম্পূর্ণ কন্টেন্ট মুছে না ফেলে শুধুমাত্র ফরম্যাটিং ক্লিয়ার করার অপশন কোনটি?",
    "options": ["Clear Formats", "Clear All", "Clear Contents", "Delete"],
    "answer": "ক",
    "explanation": "Clear Formats মূল ডেটা অক্ষত রেখে কেবল ফন্ট, রঙ ও বর্ডার রিসেট করে।"
})

questions.append({
    "id": 144,
    "topic": topic_1_4,
    "question": "এক্সেলে নির্বাচিত ডেটা রেঞ্জ থেকে তাৎক্ষণিকভাবে একটি অফিসিয়াল চার্ট তৈরি করার শর্টকাট কোনটি?",
    "options": ["F11", "F1", "Ctrl + F1", "Shift + F11"],
    "answer": "ক",
    "explanation": "F11 চাপলে একটি আলাদা চার্ট শিটে সরাসরি ডিফল্ট চার্ট তৈরি হয়।"
})

questions.append({
    "id": 145,
    "topic": topic_1_4,
    "question": "এক্সেলে শিট সুরক্ষার জন্য পাসওয়ার্ড সেট করতে কোন রিবন ট্যাবে যেতে হয়?",
    "options": ["Review -> Protect Sheet", "View -> Lock", "Data -> Secure", "Insert -> Password"],
    "answer": "ক",
    "explanation": "Review ট্যাবের অন্তর্গত 'Protect Sheet' দিয়ে স্প্রেডশিটে অননুমোদিত এডিটিং লক করা যায়।"
})

print("Generated Topic 1.4: 40 questions")

# ==============================================================================
# অধ্যায় ১.৫: প্রেজেন্টেশন গ্রাফিক্স (MS PowerPoint & Slide Design) (Questions 146 to 170)
# ==============================================================================
topic_1_5 = "অধ্যায় ১.৫: প্রেজেন্টেশন গ্রাফিক্স (MS PowerPoint)"

questions.append({
    "id": 146,
    "topic": topic_1_5,
    "question": "মাইক্রোসফট পাওয়ারপয়েন্ট ২০০৭ এবং পরবর্তী ভার্সনের ডিফল্ট ফাইল এক্সটেনশন কোনটি?",
    "options": [".pptx", ".ppt", ".ppsx", ".potx"],
    "answer": "ক",
    "explanation": "Office 2007 থেকে পাওয়ারপয়েন্ট প্রেজেন্টেশনের মূল এক্সটেনশন হলো '.pptx'।"
})

questions.append({
    "id": 147,
    "topic": topic_1_5,
    "question": "পাওয়ারপয়েন্টে প্রথম স্লাইড থেকে স্লাইড শো (Slide Show) শুরু করার কীবোর্ড শর্টকাট কোনটি?",
    "options": ["F5", "Shift + F5", "Ctrl + F5", "Alt + F5"],
    "answer": "ক",
    "explanation": "F5 চাপলে প্রথম স্লাইড থেকে ফুল স্ক্রিন স্লাইড শো শুরু হয়।"
})

questions.append({
    "id": 148,
    "topic": topic_1_5,
    "question": "বর্তমান সক্রিয় স্লাইড (Current Slide) থেকে স্লাইড শো শুরু করার শর্টকাট কী কোনটি?",
    "options": ["Shift + F5", "F5", "Ctrl + F5", "Alt + Shift + F5"],
    "answer": "ক",
    "explanation": "Shift + F5 চাপলে ইউজার বর্তমানে যে স্লাইডে আছেন ঠিক সেখান থেকেই শো শুরু হয়।"
})

questions.append({
    "id": 149,
    "topic": topic_1_5,
    "question": "পাওয়ারপয়েন্টে একটি প্রেজেন্টেশনের মাঝে নতুন একটি স্লাইড যোগ (New Slide) করার শর্টকাট কোনটি?",
    "options": ["Ctrl + M", "Ctrl + N", "Alt + N", "Shift + N"],
    "answer": "ক",
    "explanation": "Ctrl + M চাপলে নতুন স্লাইড ইনসার্ট হয়, আর Ctrl + N চাপলে সম্পূর্ণ নতুন ফাইল তৈরি হয়।"
})

questions.append({
    "id": 150,
    "topic": topic_1_5,
    "question": "চলমান কোনো স্লাইড ডুপ্লিকেট (Duplicate Slide) করার শর্টকাট কোনটি?",
    "options": ["Ctrl + D", "Ctrl + C", "Ctrl + Shift + D", "Alt + D"],
    "answer": "ক",
    "explanation": "Ctrl + D নির্বাচিত স্লাইডের হুবহু আরেকটি প্রতিলিপি তৈরি করে।"
})

questions.append({
    "id": 151,
    "topic": topic_1_5,
    "question": "একটি প্রেজেন্টেশনের সকল স্লাইডের ফন্ট, ব্যাকগ্রাউন্ড ও লোগো একবারে নিয়ন্ত্রণ করার টুলের নাম কী?",
    "options": ["স্লাইড মাস্টার (Slide Master)", "হ্যান্ডআউট মাস্টার", "ডিজাইন থিম", "লেআউট বিল্ডার"],
    "answer": "ক",
    "explanation": "Slide Master হলো শীর্ষ স্লাইড যার ডিজাইন পরিবর্তন করলে সম্পূর্ণ প্রেজেন্টেশনের সব স্লাইড স্বয়ংক্রিয়ভাবে আপডেট হয়।"
})

questions.append({
    "id": 152,
    "topic": topic_1_5,
    "question": "একটি স্লাইড থেকে পরবর্তী স্লাইডে যাওয়ার সময়ের ভিজ্যুয়াল এফেক্টকে কী বলা হয়?",
    "options": ["ট্রানজিশন (Transition)", "অ্যানিমেশন (Animation)", "স্লাইড শো", "মরফিং"],
    "answer": "ক",
    "explanation": "Transition দুটি স্লাইডের মধ্যবর্তী ট্রানজিশনাল প্রভাব নিয়ন্ত্রণ করে।"
})

questions.append({
    "id": 153,
    "topic": topic_1_5,
    "question": "স্লাইডের ভেতরের উপাদানসমূহের (টেক্সট, ছবি বা শেপ) চলাচলের ভিজ্যুয়াল এফেক্টকে কী বলা হয়?",
    "options": ["অ্যানিমেশন (Animation)", "ট্রানজিশন", "ইন্টারঅ্যাকশন", "ট্রান্সফর্মেশন"],
    "answer": "ক",
    "explanation": "Animation স্লাইডের মধ্যকার নির্দিষ্ট অবজেক্টের প্রবেশ, প্রস্থান ও নড়াচড়া নিয়ন্ত্রণ করে।"
})

questions.append({
    "id": 154,
    "topic": topic_1_5,
    "question": "পাওয়ারপয়েন্টে অ্যানিমেশনের প্রধান ৪টি প্রকারভেদের মধ্যে নিচের কোনটি অন্তর্ভুক্ত নয়?",
    "options": ["কনভার্সন (Conversion)", "এন্ট্রান্স (Entrance)", "এমফ্যাসিস (Emphasis)", "এক্সিট (Exit)"],
    "answer": "ক",
    "explanation": "অ্যানিমেশনের ৪টি প্রকার হলো: Entrance (প্রবেশ), Emphasis (গুরুত্ব), Exit (প্রস্থান) এবং Motion Paths (গতিপথ)।"
})

questions.append({
    "id": 155,
    "topic": topic_1_5,
    "question": "স্লাইড শো চলাকালীন স্ক্রিন সাময়িকভাবে সম্পূর্ণ কালো (Black Screen) করার জন্য কোন কি চাপতে হয়?",
    "options": ["B", "W", "Esc", "Space"],
    "answer": "ক",
    "explanation": "স্লাইড শো চলাকালে 'B' চাপলে স্ক্রিন কালো (Black) এবং 'W' চাপলে সাদা (White) হয়ে যায়।"
})

questions.append({
    "id": 156,
    "topic": topic_1_5,
    "question": "স্লাইড শো চলাকালীন স্ক্রিনে তাৎক্ষণিক ড্রয়িং বা দাগ দেওয়ার জন্য পেন টুল (Pen Tool) সক্রিয় করার শর্টকাট কোনটি?",
    "options": ["Ctrl + P", "Ctrl + A", "Ctrl + E", "Ctrl + B"],
    "answer": "ক",
    "explanation": "Ctrl + P পয়েন্টারকে পেন টুলে পরিণত করে এবং Ctrl + E ইরেজার সক্রিয় করে।"
})

questions.append({
    "id": 157,
    "topic": topic_1_5,
    "question": "পাওয়ারপয়েন্টে সকল স্লাইড থাম্বনেইল আকারে এক স্ক্রিনে দেখার ভিউ মোডকে কী বলে?",
    "options": ["স্লাইড সর্টার ভিউ (Slide Sorter View)", "নরমাল ভিউ", "রিডিং ভিউ", "আউটলাইন ভিউ"],
    "answer": "ক",
    "explanation": "Slide Sorter View সব স্লাইড গ্রিড আকারে দেখায়, যা স্লাইডের ক্রম পরিবর্তন ও পুনর্বিন্যাসে উপযোগী।"
})

questions.append({
    "id": 158,
    "topic": topic_1_5,
    "question": "স্লাইড শো চলাকালীন প্রেজেন্টার ল্যাপটপে পরবর্তী স্লাইড ও নোট দেখতে পান কিন্তু দর্শক শুধু স্লাইড দেখেন—এ ব্যবস্থার নাম কী?",
    "options": ["প্রেজেন্টার ভিউ (Presenter View)", "স্পিকার ভিউ", "ডুয়াল ভিউ", "অডিয়েন্স ভিউ"],
    "answer": "ক",
    "explanation": "Presenter View স্পিকারকে টাইমার, ব্যক্তিগত স্পিকার নোটস এবং আপকামিং স্লাইড প্রদর্শন করে।"
})

questions.append({
    "id": 159,
    "topic": topic_1_5,
    "question": "পাওয়ারপয়েন্টে প্রতিটি স্লাইড প্রদর্শনের সময় অনুশীলন ও নিখুঁত সময় রেকর্ড করার ফিচার কোনটি?",
    "options": ["রিহার্স টাইমিংস (Rehearse Timings)", "টাইম রেকর্ডার", "স্লাইড টাইমার", "অটো প্লে"],
    "answer": "ক",
    "explanation": "Rehearse Timings ব্যবহারকারীকে প্রতিটি স্লাইডে কত সময় লাগবে তা অনুশীলন ও অটো-অ্যাডভান্স সেভ করতে দেয়।"
})

questions.append({
    "id": 160,
    "topic": topic_1_5,
    "question": "স্লাইড শো বন্ধ করে স্বাভাবিক এডিটিং মোডে ফিরে আসার শর্টকাট কী কোনটি?",
    "options": ["Esc (Escape)", "Space", "Enter", "Backspace"],
    "answer": "ক",
    "explanation": "Esc চাপলে যেকোনো সময় স্লাইড শো সমাপ্ত হয়ে নরমাল এডিটিং উইন্ডো ফিরে আসে।"
})

questions.append({
    "id": 161,
    "topic": topic_1_5,
    "question": "স্লাইডে ক্লিক করলে কোনো অ্যাকশন (যেমন- অন্য স্লাইডে যাওয়া, শব্দ বাজানো) সম্পাদনের বাটনকে কী বলে?",
    "options": ["অ্যাকশন বাটন (Action Buttons)", "ম্যাক্রো বাটন", "ট্রিগার বক্স", "কন্ট্রোল সুইচ"],
    "answer": "ক",
    "explanation": "Action Button হলো বিশেষ শেপ যাতে হাইপারলিঙ্ক বা বিশেষ ম্যাক্রো অ্যাকশন যুক্ত থাকে।"
})

questions.append({
    "id": 162,
    "topic": topic_1_5,
    "question": "পাওয়ারপয়েন্টে সরাসরি ক্লিক করলে প্রেজেন্টেশন ওপেন না হয়ে সরাসরি স্লাইড শো শুরু হওয়ার ফাইল ফরম্যাট কোনটি?",
    "options": [".ppsx (PowerPoint Show)", ".pptx", ".potx", ".pptm"],
    "answer": "ক",
    "explanation": "'.ppsx' হলো পাওয়ারপয়েন্ট শো ফরম্যাট যা ওপেন করলেই সরাসরি পূর্ণ স্ক্রিন স্লাইড শো রান হয়।"
})

questions.append({
    "id": 163,
    "topic": topic_1_5,
    "question": "শ্রোতাদের পড়ার সুবিধার জন্য প্রতি পৃষ্ঠায় একাধিক স্লাইডের মিনিয়েচার প্রিন্ট কপিকে কী বলা হয়?",
    "options": ["হ্যান্ডআউটস (Handouts)", "নোটস পেজ", "ফ্লায়ার", "আউটলাইন"],
    "answer": "ক",
    "explanation": "Handouts হলো অডিয়েন্সের জন্য এক পাতায় ১, ২, ৩, ৪, ৬ বা ৯টি স্লাইড প্রিন্ট করার লেআউট।"
})

questions.append({
    "id": 164,
    "topic": topic_1_5,
    "question": "পাওয়ারপয়েন্টে জটিল তথ্য, প্রসেস ফ্লো বা সাংগঠনিক কাঠামো সহজে ডায়াগ্রামে ফুটিয়ে তোলার টুলের নাম কী?",
    "options": ["স্মার্টআর্ট (SmartArt Graphics)", "ওয়ার্ডআর্ট", "শেপস", "চার্টস"],
    "answer": "ক",
    "explanation": "SmartArt হায়ারার্কি, সাইকেল, রিলেশনশিপ এবং প্রসেস ডায়াগ্রাম দ্রুত তৈরি করতে ব্যবহৃত হয়।"
})

questions.append({
    "id": 165,
    "topic": topic_1_5,
    "question": "স্লাইডে থাকা সুন্দর আকর্ষণীয় স্টাইলাইজড টেক্সট আর্ট যোগ করার ফিচারের নাম কী?",
    "options": ["ওয়ার্ডআর্ট (WordArt)", "স্মার্টআর্ট", "ক্লিপআর্ট", "টেক্সট বক্স"],
    "answer": "ক",
    "explanation": "WordArt টেক্সটকে ত্রিমাত্রিক শ্যাডো, বেভেল ও গ্রেডিয়েন্ট এফেক্ট দিয়ে আকর্ষণীয় করে তোলে।"
})

questions.append({
    "id": 166,
    "topic": topic_1_5,
    "question": "পাওয়ারপয়েন্টে স্লাইড ট্রানজিশনের আধুনিক 'মরফ' (Morph) ফিচারের মূল কাজ কী?",
    "options": ["এক স্লাইডের উপাদানকে মসৃণভাবে অ্যানিমেট করে পরবর্তী স্লাইডের অবস্থানে রূপান্তর করা", "স্লাইড ডিলিট করা", "সাউন্ড ইফেক্ট বন্ধ করা", "ভিডিও কম্প্রেস করা"],
    "answer": "ক",
    "explanation": "Morph ট্রানজিশন সাধারণ উপাদানসমূহ চিহ্নিত করে স্লাইড পরিবর্তনের সময় মসৃণ মুভমেন্ট তৈরি করে।"
})

questions.append({
    "id": 167,
    "topic": topic_1_5,
    "question": "পাওয়ারপয়েন্টে স্লাইডের নিচে বক্তার নিজস্ব তথ্য লিখে রাখার প্যানটিকে কী বলে?",
    "options": ["নোটস প্যান (Notes Pane)", "কমেন্ট বক্স", "স্ট্যাটাস বার", "টাস্ক প্যান"],
    "answer": "ক",
    "explanation": "Notes Pane-এ স্পিকার তার বক্তব্যের সহায়ক ক্লু লিখে রাখেন যা দর্শকরা দেখতে পায় না।"
})

questions.append({
    "id": 168,
    "topic": topic_1_5,
    "question": "স্লাইড শোতে নির্দিষ্ট ক্রমানুসারে স্লাইড প্রদর্শন নিয়ন্ত্রণ (লুপে চলা বা কিয়স্ক মোড) করার অপশন কোনটি?",
    "options": ["Set Up Slide Show", "Custom Show", "Broadcast Slide Show", "Hide Slide"],
    "answer": "ক",
    "explanation": "'Set Up Slide Show' ডায়ালগ বক্স থেকে ফুল স্ক্রিন, লুপ কন্টিনিউয়াসলি এবং কিয়স্ক মোড সেট করা যায়।"
})

questions.append({
    "id": 169,
    "topic": topic_1_5,
    "question": "কোনো স্লাইডকে প্রেজেন্টেশনে রেখেও স্লাইড শো চলাকালীন অদৃশ্য রাখার অপশন কোনটি?",
    "options": ["হাইড স্লাইড (Hide Slide)", "ডিলিট স্লাইড", "কাট স্লাইড", "রিমুভ স্লাইড"],
    "answer": "ক",
    "explanation": "Hide Slide অপশন স্লাইডটি ফাইলে বজায় রাখে কিন্তু স্লাইড শো চলাকালে স্কিপ করে যায়।"
})

questions.append({
    "id": 170,
    "topic": topic_1_5,
    "question": "পাওয়ারপয়েন্টে সম্পূর্ণ প্রেজেন্টেশনকে এমপি৪ (MP4) ভিডিও হিসেবে এক্সপোর্ট করার সুবিধা কোন মেনুতে থাকে?",
    "options": ["File -> Export -> Create a Video", "File -> Print", "Design -> Video", "View -> Export"],
    "answer": "ক",
    "explanation": "Export মেনু থেকে স্লাইড ও অ্যানিমেশন সহ সম্পূর্ণ প্রেজেন্টেশনকে Full HD ভিডিওতে সেভ করা যায়।"
})

print("Generated Topic 1.5: 25 questions")

# ==============================================================================
# অধ্যায় ১.৬: কম্পিউটার রক্ষণাবেক্ষণ ও আইটি সাপোর্ট সার্ভিস (Questions 171 to 200)
# ==============================================================================
topic_1_6 = "অধ্যায় ১.৬: কম্পিউটার রক্ষণাবেক্ষণ ও আইটি সাপোর্ট সার্ভিস"

questions.append({
    "id": 171,
    "topic": topic_1_6,
    "question": "কম্পিউটার পাওয়ার অন করার পর মনিটরে কোনো ডিসপ্লে না আসা এবং বায়োস থেকে বারবার অবিচ্ছিন্ন বিপ (Continuous Beep) শব্দ হওয়ার সম্ভাব্য কারণ কী?",
    "options": ["র‍্যাম (RAM) এর ত্রুটি বা র‍্যাম স্লটে ধুলাবালি জমা", "হার্ডডিস্কের ত্রুটি", "মাউসের সমস্যা", "সিপিইউ ফ্যানের সমস্যা"],
    "answer": "ক",
    "explanation": "পোস্ট (POST) এর সময় র‍্যাম শনাক্ত করতে না পারলে বা র‍্যাম ঢিলা হলে বায়োস দীর্ঘ অবিচ্ছিন্ন বিপ শব্দ দিয়ে সতর্ক করে।"
})

questions.append({
    "id": 172,
    "topic": topic_1_6,
    "question": "সিপিইউ প্রসেসর এবং হিটসিঙ্কের মাঝে নিখুঁত তাপ পরিবহনের জন্য কোনটি প্রয়োগ করা আবশ্যক?",
    "options": ["থার্মাল পেস্ট (Thermal Paste / Grease)", "মবিল লুব্রিকেন্ট", "গ্লু আঠা", "অ্যালকোহল"],
    "answer": "ক",
    "explanation": "থার্মাল পেস্ট প্রসেসর ও মেটাল হিটসিঙ্কের মধ্যবর্তী ক্ষুদ্রাতিক্ষুদ্র বায়ু দূর করে তাপ পরিবাহিতা নিশ্চিত করে।"
})

questions.append({
    "id": 173,
    "topic": topic_1_6,
    "question": "কম্পিউটার চালু হওয়ার কিছুক্ষণের মধ্যেই অতিরিক্ত গরম হয়ে নিজে থেকেই বন্ধ (Thermal Shutdown) হওয়ার মূল কারণ কী?",
    "options": ["সিপিইউ কুলিং ফ্যান বন্ধ থাকা বা থার্মাল পেস্ট শুকিয়ে যাওয়া", "কীবোর্ডের ত্রুটি", "সাউন্ড কার্ডের সমস্যা", "মনিটরের ব্রাইটনেস বেশি হওয়া"],
    "answer": "ক",
    "explanation": "সিপিইউ তাপমাত্রা বিপৎসীমা (৯০°-১০০° সে.) অতিক্রম করলে হার্ডওয়্যার পুড়ে যাওয়া রোধে স্বয়ংক্রিয়ভাবে শাটডাউন হয়।"
})

questions.append({
    "id": 174,
    "topic": topic_1_6,
    "question": "ঐতিহ্যবাহী এমবিআর (MBR - Master Boot Record) পার্টিশন স্কিমে সর্বোচ্চ কতটি প্রাইমারি পার্টিশন তৈরি করা যায়?",
    "options": ["৪টি", "২টি", "৮টি", "১২৮টি"],
    "answer": "ক",
    "explanation": "MBR পার্টিশন টেবিলে সর্বোচ্চ ৪টি প্রাইমারি পার্টিশন (অথবা ৩টি প্রাইমারি ও ১টি এক্সটেন্ডেড পার্টিশন) তৈরি করা যায়।"
})

questions.append({
    "id": 175,
    "topic": topic_1_6,
    "question": "এমবিআর (MBR) পার্টিশন টেবিলের সর্বোচ্চ হার্ডডিস্ক ধারণক্ষমতা সমর্থন কত?",
    "options": ["2 TB (টেরাবাইট)", "4 TB", "1 TB", "500 GB"],
    "answer": "ক",
    "explanation": "৩২-বিট সেক্টর অ্যাড্রেসিং সীমাবদ্ধতার কারণে MBR সর্বোচ্চ ২ টেরাবাইট পর্যন্ত ডিস্ক সমর্থন করে।"
})

questions.append({
    "id": 176,
    "topic": topic_1_6,
    "question": "আধুনিক জিপিটি (GPT - GUID Partition Table) স্কিমে সর্বোচ্চ কতটি পার্টিশন তৈরি করা যায়?",
    "options": ["১২৮টি", "৪টি", "১৬টি", "৬৪টি"],
    "answer": "ক",
    "explanation": "UEFI ভিত্তিক GPT পার্টিশনিং স্কিমে কোনো এক্সটেন্ডেড পার্টিশন ছাড়াই ১২৮টি প্রাইমারি পার্টিশন করা যায়।"
})

questions.append({
    "id": 177,
    "topic": topic_1_6,
    "question": "উইন্ডোজের সিস্টেম ফাইল নষ্ট হয়ে গেলে পূর্বের সংরক্ষিত ভালো অবস্থায় সিস্টেমকে ফিরিয়ে নেওয়ার টুলের নাম কী?",
    "options": ["সিস্টেম রিস্টোর পয়েন্ট (System Restore Point)", "ডিস্ক ক্লিনআপ", "ডিফ্র্যাগমেন্টার", "ফরমেটিং"],
    "answer": "ক",
    "explanation": "System Restore ব্যবহারকারীর ব্যক্তিগত ফাইল নষ্ট না করে রেজিস্ট্রি ও সিস্টেম ফাইলকে পূর্বের সেভ পয়েন্টে ফিরিয়ে নেয়।"
})

questions.append({
    "id": 178,
    "topic": topic_1_6,
    "question": "কম্পিউটারের পাওয়ার সাপ্লাই ইউনিটের (SMPS) ২৪-পিন ATX কানেক্টরের মাদারবোর্ড পাওয়ার-অন সিগন্যাল তারের রঙ কী?",
    "options": ["সবুজ (Green - PS_ON)", "কালো (Black - Ground)", "হলুদ (Yellow - +12V)", "লাল (Red - +5V)"],
    "answer": "ক",
    "explanation": "সবুজ তার (PS_ON) কে যেকোনো কালো (Ground) তারের সাথে শর্ট করলে এসএমপিএস ফ্যান স্বয়ংক্রিয়ভাবে চালু হয়।"
})

questions.append({
    "id": 179,
    "topic": topic_1_6,
    "question": "এসএমপিএস-এর হলুদ (Yellow) তারের আউটপুট ভোল্টেজ মান কত?",
    "options": ["+12V", "+5V", "+3.3V", "-12V"],
    "answer": "ক",
    "explanation": "হলুদ তার হলো +12V (ফ্যান, ডিস্ক মোটর ও প্রসেসরের জন্য), লাল তার হলো +5V এবং কমলা তার হলো +3.3V।"
})

questions.append({
    "id": 180,
    "topic": topic_1_6,
    "question": "হার্ডডিস্কের কোনো ফিজিক্যাল ব্যাড সেক্টর (Bad Sector) বা ফাইল সিস্টেমের ত্রুটি স্ক্যান ও মেরামতের কমান্ড কোনটি?",
    "options": ["chkdsk /f /r", "sfc /scannow", "format c:", "diskpart"],
    "answer": "ক",
    "explanation": "chkdsk (Check Disk) ইউটিলিটি ফাইলের অখণ্ডতা পরীক্ষা করে এবং ক্ষতিগ্রস্ত সেক্টর রিড করে ডেটা উদ্ধারের চেষ্টা করে।"
})

questions.append({
    "id": 181,
    "topic": topic_1_6,
    "question": "উইন্ডোজের করাপ্ট বা বিকৃত হওয়া সিস্টেম ফাইল স্ক্যান করে স্বয়ংক্রিয়ভাবে অরিজিনাল ফাইল দিয়ে প্রতিস্থাপনের কমান্ড কোনটি?",
    "options": ["sfc /scannow (System File Checker)", "chkdsk", "ipconfig /renew", "netsh winsock reset"],
    "answer": "ক",
    "explanation": "SFC (System File Checker) সুরক্ষিত সিস্টেম ফাইলের ইন্টিগ্রিটি চেক করে মাইক্রোসফটের ক্যাশ কপি দিয়ে মেরামত করে।"
})

questions.append({
    "id": 182,
    "topic": topic_1_6,
    "question": "কম্পিউটারের আইপি অ্যাড্রেস, সাবনেট মাস্ক ও ডিফল্ট গেটওয়ে জানার জন্য কমান্ড প্রম্পটে কোন কমান্ড লেখা হয়?",
    "options": ["ipconfig", "ping", "tracert", "netstat"],
    "answer": "ক",
    "explanation": "উইন্ডোজ কমান্ড প্রম্পটে 'ipconfig' চাপলে বর্তমান নেটওয়ার্ক ইন্টারফেসের আইপি তথ্য প্রদর্শিত হয়।"
})

questions.append({
    "id": 183,
    "topic": topic_1_6,
    "question": "নেটওয়ার্কের অন্য একটি কম্পিউটারের সাথে সংযোগ ঠিক আছে কিনা এবং লেটেন্সি কত তা পরীক্ষার কমান্ড কোনটি?",
    "options": ["ping", "ipconfig", "nslookup", "route"],
    "answer": "ক",
    "explanation": "Ping কমান্ড ICMP Echo Request পাঠিয়ে হোস্ট ডিভাইসটির সক্রিয়তা ও রেসপন্স সময় (RTT) যাচাই করে।"
})

questions.append({
    "id": 184,
    "topic": topic_1_6,
    "question": "একটি প্যাকেটের সোর্স থেকে ডেস্টিনেশন সার্ভার পর্যন্ত পৌঁছাতে মধ্যবর্তী সকল রাউটার বা হপ দেখানোর কমান্ড কোনটি?",
    "options": ["tracert (Traceroute)", "ping", "netstat", "arp"],
    "answer": "ক",
    "explanation": "Tracert কমান্ড TTL বাড়িয়ে বাড়িয়ে প্যাকেটের প্রতিটি ট্রাভেল পাথ ও রাউটার আইপি প্রদর্শন করে।"
})

questions.append({
    "id": 185,
    "topic": topic_1_6,
    "question": "কম্পিউটারের হার্ডওয়্যার উপাদানসমূহের (RAM, Display, Sound) বিস্তারিত টেস্ট রিপোর্ট পেতে রান কমান্ডে কী লেখা হয়?",
    "options": ["dxdiag", "msconfig", "regedit", "cleanmgr"],
    "answer": "ক",
    "explanation": "dxdiag (DirectX Diagnostic Tool) গ্রাফিক্স, প্রসেসর, র‍্যাম ও সাউন্ডের সার্বিক অবস্থা যাচাই করে।"
})

questions.append({
    "id": 186,
    "topic": topic_1_6,
    "question": "উইন্ডোজ স্টার্টআপে কোন কোন অ্যাপ স্বয়ংক্রিয়ভাবে চালু হবে তা নিয়ন্ত্রণ করতে কোন কনফিগারেশন ইউটিলিটি ব্যবহৃত হয়?",
    "options": ["msconfig (System Configuration)", "dxdiag", "cmd", "control"],
    "answer": "ক",
    "explanation": "msconfig-এর মাধ্যমে বুট অপশন, সার্ভিস ও স্টার্টআপ অ্যাপ নিয়ন্ত্রণ করে পিসি দ্রুত করা যায়।"
})

questions.append({
    "id": 187,
    "topic": topic_1_6,
    "question": "কম্পিউটারের সকল কানেক্টেড হার্ডওয়্যার ও ড্রাইভারের হলুদ সতর্কতা চিহ্ন (Yellow Exclamation Mark) চেক করার টুল কোনটি?",
    "options": ["ডিভাইস ম্যানেজার (Device Manager - devmgmt.msc)", "ডিস্ক ম্যানেজমেন্ট", "সার্ভিসেস", "ইভেন্ট ভিউয়ার"],
    "answer": "ক",
    "explanation": "Device Manager-এ কোনো ড্রাইভার মিসিং বা ত্রুটিপূর্ণ হলে হলুদ বিস্ময়সূচক চিহ্ন প্রদর্শন করে।"
})

questions.append({
    "id": 188,
    "topic": topic_1_6,
    "question": "নতুন হার্ডডিস্ক পার্টিশন করা, ড্রাইভ লেটার বরাদ্দ করা ও ফরম্যাট করার উইন্ডোজ কনসোল টুল কোনটি?",
    "options": ["ডিস্ক ম্যানেজমেন্ট (Disk Management - diskmgmt.msc)", "ডিভাইস ম্যানেজার", "টাস্ক শিডিউলার", "ফায়ারওয়াল"],
    "answer": "ক",
    "explanation": "Disk Management ড্রাইভ শ্রিঙ্ক, এক্সপ্যান্ড, নতুন ভলিউম তৈরি ও ড্রাইভ লেটার নির্ধারণের মূল টুল।"
})

questions.append({
    "id": 189,
    "topic": topic_1_6,
    "question": "উইন্ডোজের ব্যাকগ্রাউন্ড সিস্টেম সার্ভিসসমূহ (যেমন- Print Spooler, Windows Update) চালু/বন্ধ করার টুল কোনটি?",
    "options": ["services.msc", "eventvwr", "gpedit.msc", "secpol.msc"],
    "answer": "ক",
    "explanation": "Services.msc উইন্ডোজের সকল সিস্টেম ডেমন ও ব্যাকগ্রাউন্ড সার্ভিস পরিচালনা করে।"
})

questions.append({
    "id": 190,
    "topic": topic_1_6,
    "question": "প্রিন্টারে কোনো ডকুমেন্ট প্রিন্ট আটকে গেলে (Print Job Stuck) কোন সার্ভিস রিস্টার্ট দিতে হয়?",
    "options": ["Print Spooler", "Windows Audio", "Workstation", "Remote Desktop"],
    "answer": "ক",
    "explanation": "Print Spooler সার্ভিস রিস্টার্ট দিলে প্রিন্ট কিউ খালি হয়ে প্রিন্টার পুনরায় সচল হয়।"
})

questions.append({
    "id": 191,
    "topic": topic_1_6,
    "question": "কোনো কারণে উইন্ডোজের অডিও সম্পূর্ণ বন্ধ হয়ে গেলে সার্ভিস থেকে কোনটি রিস্টার্ট করতে হয়?",
    "options": ["Windows Audio", "Plug and Play", "Task Scheduler", "Audio Router"],
    "answer": "ক",
    "explanation": "Windows Audio সার্ভিস সাউন্ড চিপ ও ড্রাইভারের সাথে অ্যাপ্লিকেশন সাউন্ড স্ট্রিম সিঙ্ক করে।"
})

questions.append({
    "id": 192,
    "topic": topic_1_6,
    "question": "কম্পিউটারের মাদারবোর্ডে বায়োস চিপকে নতুন ভার্সনে আপডেট করার প্রক্রিয়াকে কী বলা হয়?",
    "options": ["বায়োস ফ্ল্যাশিং (BIOS Flashing / Firmware Update)", "বায়োস ক্লিয়ারিং", "ফার্মওয়্যার ডিলিট", "চিপ ওভারক্লকিং"],
    "answer": "ক",
    "explanation": "মাদারবোর্ডের রম চিপে নতুন মাইক্রোকোড বা ফার্মওয়্যার ইন্সটল করাকে BIOS Flashing বলে।"
})

questions.append({
    "id": 193,
    "topic": topic_1_6,
    "question": "কম্পিউটারের প্রসেসরের নির্ধারিত স্বাভাবিক গতির চেয়ে বেশি গতিতে কৃত্রিমভাবে চালানোর প্রক্রিয়াকে কী বলে?",
    "options": ["ওভারক্লকিং (Overclocking)", "আন্ডারক্লকিং", "বুস্টিং", "হাইপার-থ্রেডিং"],
    "answer": "ক",
    "explanation": "Overclocking ক্লক মাল্টিপ্লায়ার বা ভোল্টেজ বাড়িয়ে কর্মক্ষমতা বৃদ্ধি করে, তবে এর ফলে অতিরিক্ত তাপ উৎপন্ন হয়।"
})

questions.append({
    "id": 194,
    "topic": topic_1_6,
    "question": "একটি সম্পূর্ণ হার্ডডিস্কের হুবহু শতভাগ প্রতিচ্ছবি বা ক্লোন (Exact Sector-by-Sector Copy) তৈরি করার প্রক্রিয়া কোনটি?",
    "options": ["ডিস্ক ক্লোনিং (Disk Cloning)", "ডিস্ক ব্যাকআপ", "ফাইল কপি", "ডিস্ক কম্প্রেশন"],
    "answer": "ক",
    "explanation": "Disk Cloning ওএস, সিস্টেম পার্টিশন ও ফাইল সহ সম্পূর্ণ ড্রাইভের অবিকল রেপ্লিকা ড্রাইভ তৈরি করে।"
})

questions.append({
    "id": 195,
    "topic": topic_1_6,
    "question": "উইন্ডোজে পেনড্রাইভের ক্ষতিকর অটো-রান ভাইরাস ছড়ানো বন্ধে কোন সার্ভিসটি নিষ্ক্রিয় করা উচিত?",
    "options": ["AutoPlay / AutoRun", "Superfetch", "Windows Search", "ReadyBoost"],
    "answer": "ক",
    "explanation": "AutoRun নিষ্ক্রিয় করলে পেনড্রাইভ ঢোকানোর সাথে সাথে কোনো ম্যালওয়্যার স্বয়ংক্রিয়ভাবে রান হতে পারে না।"
})

questions.append({
    "id": 196,
    "topic": topic_1_6,
    "question": "পেনড্রাইভ দিয়ে উইন্ডোজ ইন্সটল করার জন্য বুটেবল ইউএসবি (Bootable USB) তৈরিতে কোন ওপেন-সোর্স সফটওয়্যারটি বহুল ব্যবহৃত?",
    "options": ["Rufus", "VLC", "WinRAR", "Notepad"],
    "answer": "ক",
    "explanation": "Rufus আইএসও (ISO) ইমেজ ফাইল থেকে অতি দ্রুত MBR বা GPT মোডে বুটেবল ইউএসবি ড্রাইভ তৈরি করে।"
})

questions.append({
    "id": 197,
    "topic": topic_1_6,
    "question": "পিসিতে হঠাৎ ইন্টারনেট কাজ না করলে আইপি সংক্রান্ত ক্যাশ ও সকেট রিসেট করার সঠিক কমান্ড কোনটি?",
    "options": ["netsh winsock reset", "ipconfig /all", "ping localhost", "cls"],
    "answer": "ক",
    "explanation": "'netsh winsock reset' টিসিপি/আইপি স্ট্যাক ক্যাটালগ পুনর্নির্মাণ করে নেটওয়ার্ক ত্রুটি দূর করে।"
})

questions.append({
    "id": 198,
    "topic": topic_1_6,
    "question": "কম্পিউটারের লোকাল ডিএনএস ক্যাশ মেমোরি ক্লিয়ার করার কমান্ড কোনটি?",
    "options": ["ipconfig /flushdns", "ipconfig /release", "ipconfig /renew", "net view"],
    "answer": "ক",
    "explanation": "'ipconfig /flushdns' কম্পিউটারের পুরনো জমে থাকা ডিএনএস হোস্টনেম ক্যাশ মুছে ফ্রেশ করে।"
})

questions.append({
    "id": 199,
    "topic": topic_1_6,
    "question": "কম্পিউটার হার্ডওয়্যারের দীর্ঘস্থায়িত্ব বজায় রাখতে নিয়মিত অভ্যন্তরীণ রক্ষণাবেক্ষণে কোনটি জরুরি?",
    "options": ["ব্লোয়ার দিয়ে ধুলাবালি পরিষ্কার ও পর্যাপ্ত বায়ু চলাচল নিশ্চিত করা", "পিসির ভেতর পানি ছিটানো", "ফ্যান খুলে রাখা", "অতিরিক্ত তাপমাত্রায় পিসি চালানো"],
    "answer": "ক",
    "explanation": "ধুলাবালি জমা হলে হিটসিঙ্কের তাপ নির্গমন বন্ধ হয়ে যন্ত্রাংশ ক্ষতিগ্রস্ত হয়, তাই নিয়মিত ব্লোয়ার দিয়ে পরিষ্কার করা প্রয়োজন।"
})

questions.append({
    "id": 200,
    "topic": topic_1_6,
    "question": "অফিসে একাধিক কম্পিউটারের ব্যাকআপ এবং ডেটা সুরক্ষার সবচেয়ে কার্যকর এন্টারপ্রাইজ ব্যাকআপ নীতি কোনটি?",
    "options": ["৩-২-১ ব্যাকআপ রুল (3 কপি ডেটা, 2 ভিন্ন মিডিয়া, 1 কপি অফসাইট/ক্লাউডে)", "পেনড্রাইভে ১ কপি রাখা", "একই হার্ডডিস্কের অন্য ফোল্ডারে কপি রাখা", "ব্যাকআপ না নেওয়া"],
    "answer": "ক",
    "explanation": "3-2-1 ব্যাকআপ নিয়ম অনুযায়ী মূল ডেটাসহ ৩ কপি ডেটা, অন্তত ২টি ভিন্ন স্টোরেজে এবং ১ কপি দূরবর্তী ক্লাউড বা অফসাইটে সুরক্ষিত রাখতে হয়।"
})

print(f"Total questions generated: {len(questions)}")

# Verify all questions
for i, q in enumerate(questions, 1):
    q["id"] = i

# Output file path
output_path = "JSON Data/BPSC Technical AI/বিষয়- ১. কম্পিউটার ফান্ডামেন্টাল (Computer Fundamentals & Office Applications).json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated and wrote {len(questions)} MCQs to: {output_path}")
