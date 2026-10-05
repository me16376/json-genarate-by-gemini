# -*- coding: utf-8 -*-
"""
Subject 4: পাইথন প্রোগ্রামিং (Python Programming & App Development) - Part 1 (Questions 1 to 100)
Chapters:
  4.1: পাইথন ভাষার পরিচিতি ও সেটআপ (1-15)
  4.2: ভ্যারিয়েবল ও ডেটা টাইপ (16-30)
  4.3: পাইথন অপারেটর ও এক্সপ্রেশন (31-45)
  4.4: ফরম্যাটেড ইনপুট ও আউটপুট (46-55)
  4.5: কন্ডিশনাল কন্ট্রোল স্টেটমেন্ট (56-70)
  4.6: লুপিং বা পুনরাবৃত্তি স্টেটমেন্ট (71-85)
  4.7: পাইথন স্ট্রিং ও লিস্ট ডেটা স্ট্রাকচার (86-100)
"""

sub4_questions_part1 = []

# ==============================================================================
# অধ্যায় ৪.১: পাইথন ভাষার পরিচিতি ও সেটআপ (Questions 1 to 15)
# ==============================================================================
topic_4_1 = "অধ্যায় ৪.১: পাইথন ভাষার পরিচিতি ও সেটআপ"

sub4_questions_part1.append({
    "id": 1,
    "topic": topic_4_1,
    "question": "পাইথন প্রোগ্রামিং ভাষার জনক কে এবং এটি কত সালে প্রথম প্রকাশিত হয়?",
    "options": ["গুইডো ভ্যান রোসাম (Guido van Rossum), ১৯৯১ সালে", "ডেনিস রিচি, ১৯৭২ সালে", "জেমস গসলিং, ১৯৯৫ সালে", "বিয়ার্নে স্ট্রাউস্ট্রুপ, ১৯৮৩ সালে"],
    "answer": "ক",
    "explanation": "নেদারল্যান্ডসের সিডব্লিউআই (CWI)-তে কর্মরত অবস্থায় গুইডো ভ্যান রোসাম পাইথন ভাষা তৈরি করেন এবং ১৯৯১ সালের ফেব্রুয়ারিতে এটি প্রথম প্রকাশিত হয়।"
})

sub4_questions_part1.append({
    "id": 2,
    "topic": topic_4_1,
    "question": "'পাইথন' (Python) নামটি কোন উৎস থেকে অনুপ্রাণিত হয়ে রাখা হয়েছিল?",
    "options": [
        "বিবিসি কমেডি শো 'মন্টি পাইথন্স ফ্লাইং সার্কাস' (Monty Python's Flying Circus)",
        "একটি বিশালাকার অজগর সাপ থেকে",
        "একটি প্রাচীন গ্রিক পৌরাণিক ড্রাগন থেকে",
        "বিজ্ঞানীর গৃহপালিত প্রাণীর নাম থেকে"
    ],
    "answer": "ক",
    "explanation": "গুইডো ভ্যান রোসাম বিবিসির জনপ্রিয় কমেডি সিরিজ 'Monty Python's Flying Circus'-এর ভক্ত ছিলেন এবং সেই নামানুসারেই এই ভাষার নাম রাখেন পাইথন।"
})

sub4_questions_part1.append({
    "id": 3,
    "topic": topic_4_1,
    "question": "পাইথন ভাষা মূলত কোন ধরনের প্রোগ্রামিং ভাষা?",
    "options": [
        "হাই-লেভেল, ইন্টারপ্রেটেড, ডাইনামিকালি টাইপড ও মাল্টি-প্যারাডাইম ভাষা",
        "লো-লেভেল, কম্পাইলড ও স্ট্যাটিকালি টাইপড ভাষা",
        "শুধুমাত্র অবজেক্ট ওরিয়েন্টেড ভাষা",
        "শুধুমাত্র প্রসিডিউরাল ভাষা"
    ],
    "answer": "ক",
    "explanation": "পাইথন একটি উচ্চস্তরের ইন্টারপ্রেটেড ভাষা যা ওওপি, ফাংশনাল ও প্রসিডিউরাল প্রোগ্রামিং সমর্থন করে এবং এতে টাইপ রান-টাইমে নির্ধারিত হয়।"
})

sub4_questions_part1.append({
    "id": 4,
    "topic": topic_4_1,
    "question": "পাইথন কোন ভাষার উত্তরসূরি হিসেবে বিকশিত হয়েছিল?",
    "options": ["এবিসি (ABC) ভাষা", "বিসিপিএল (BCPL)", "সি (C) ভাষা", "প্যাসকেল (Pascal)"],
    "answer": "ক",
    "explanation": "গুইডো ভ্যান রোসাম পূর্বে ABC ভাষা প্রকল্পে কাজ করেছিলেন এবং ABC ভাষার সহজবোধ্যতা ও এক্সেপশন হ্যান্ডলিং থেকে অনুপ্রাণিত হয়ে পাইথন তৈরি করেন।"
})

sub4_questions_part1.append({
    "id": 5,
    "topic": topic_4_1,
    "question": "পাইথন ৩ (Python 3.0) কত সালে মুক্তি পায় এবং এর অন্যতম প্রধান বৈশিষ্ট্য কী ছিল?",
    "options": [
        "২০০৮ সালে মুক্তি পায় এবং এটি পাইথন ২ এর সাথে ব্যাকওয়ার্ড-ইনকম্প্যাটিবল ছিল",
        "২০০০ সালে মুক্তি পায় এবং পাইথন ২ কোড সরাসরি রান করত",
        "২০১৫ সালে মুক্তি পায়",
        "১৯৯১ সালে মুক্তি পায়"
    ],
    "answer": "ক",
    "explanation": "২০০৮ সালের ডিসেম্বরে পাইথন ৩.০ রিলিজ হয় যা ভাষার মৌলিক ত্রুটিগুলো দূর করে, তবে পাইথন ২-এর সাথে সরাসরি ব্যাকওয়ার্ড কম্প্যাটিবল ছিল না।"
})

sub4_questions_part1.append({
    "id": 6,
    "topic": topic_4_1,
    "question": "পাইথন ইন্টারপ্রেটার মূলত সোর্স কোডকে (.py) প্রথমে কিসে রূপান্তর করে?",
    "options": ["ইন্টারমিডিয়েট বাইটকোড (.pyc)", "সরাসরি মেশিন কোড (.exe)", "অ্যাসেম্বলি ভাষা", "সি সোর্স কোড"],
    "answer": "ক",
    "explanation": "পাইথন প্রথমে সোর্স কোডকে বাইটকোডে রূপান্তর করে `__pycache__` ফোল্ডারে `.pyc` আকারে রাখে এবং পাইথন ভার্চুয়াল মেশিন (PVM) তা রান করে।"
})

sub4_questions_part1.append({
    "id": 7,
    "topic": topic_4_1,
    "question": "পাইথনের স্ট্যান্ডার্ড এবং সর্বাধিক ব্যবহৃত রেফারেন্স ইমপ্লিমেন্টেশন কোনটি যা সি ভাষায় লিখিত?",
    "options": ["সিপাইথন (CPython)", "জাইথন (Jython)", "আয়রনপাইথন (IronPython)", "পাইপাই (PyPy)"],
    "answer": "ক",
    "explanation": "পাইথনের অফিসিয়াল ও স্ট্যান্ডার্ড ইন্টারপ্রেটার হলো CPython, যা সি ভাষায় রচিত।"
})

sub4_questions_part1.append({
    "id": 8,
    "topic": topic_4_1,
    "question": "JIT কম্পাইলার ব্যবহারের মাধ্যমে পাইথন কোডকে সাধারণ CPython-এর চেয়ে বহুগুণ দ্রুত রান করায় কোন ইমপ্লিমেন্টেশন?",
    "options": ["PyPy (পাইপাই)", "Jython", "Cython", "MicroPython"],
    "answer": "ক",
    "explanation": "PyPy একটি বিকল্প পাইথন ইন্টারপ্রেটার যা Just-In-Time কম্পাইলেশন ব্যবহার করে অসাধারণ গতি নিশ্চিত করে।"
})

sub4_questions_part1.append({
    "id": 9,
    "topic": topic_4_1,
    "question": "পাইথনে কোনো ব্লক স্টেটমেন্ট (ফাংশন, লুপ, কন্ডিশন) চিহ্নিত করতে কার্লি ব্রেসের `{}` পরিবর্তে কী ব্যবহৃত হয়?",
    "options": ["ইনডেন্টেশন বা সঠিক ফাঁকা স্থান (Indentation)", "সেমিকোলন (;)", "প্যারেন্থেসিস ()", "হ্যাশ (#)"],
    "answer": "ক",
    "explanation": "পাইথনে কোড ব্লক বা স্কোপ নির্ধারণ করতে হোয়াইটস্পেস ইনডেন্টেশন (সাধারণত ৪টি স্পেস) কঠোরভাবে মেনে চলা বাধ্যতামূলক।"
})

sub4_questions_part1.append({
    "id": 10,
    "topic": topic_4_1,
    "question": "পাইথনে একক লাইনের মন্তব্য (Single-line comment) লেখার চিহ্ন কোনটি?",
    "options": ["# (হ্যাশ চিহ্ন)", "// (ডাবল স্ল্যাশ)", "/* */", "<!-- -->"],
    "answer": "ক",
    "explanation": "পাইথনে `#` দিয়ে যেকোনো কমেন্ট লেখা হয়; কম্পাইলার হ্যাশের পরের অংশ উপেক্ষা করে।"
})

sub4_questions_part1.append({
    "id": 11,
    "topic": topic_4_1,
    "question": "ফাংশন বা ক্লাসের উদ্দেশ্য ব্যাখ্যা করার জন্য প্রথম স্টেটমেন্ট হিসেবে ট্রিপল কোটেশন (`'''` বা `\"\"\"`) দিয়ে লেখা অংশকে কী বলে?",
    "options": ["ডকস্ট্রিং (Docstring)", "ইনলাইন কমেন্ট", "মেটাডাটা", "ডেকোরেটর"],
    "answer": "ক",
    "explanation": "ডকস্ট্রিং হলো ডকুমেন্টেশন স্ট্রিং যা `obj.__doc__` বা `help(obj)` দ্বারা প্রোগ্রাম চলাকালীন পড়া যায়।"
})

sub4_questions_part1.append({
    "id": 12,
    "topic": topic_4_1,
    "question": "পাইথনের ডিজাইন দর্শন ও নির্দেশিকা জানার জন্য ইন্টারপ্রেটারে কোন কমান্ডটি লিখতে হয়?",
    "options": ["import this (The Zen of Python)", "import zen", "help()", "python --rules"],
    "answer": "ক",
    "explanation": "`import this` লিখলে টিম পিটার্সের রচিত 'The Zen of Python' এর ১৯টি দর্শনীয় বাক্য প্রদর্শিত হয়।"
})

sub4_questions_part1.append({
    "id": 13,
    "topic": topic_4_1,
    "question": "পাইথনে প্যাকেজ ও লাইব্রেরি ইনস্টল ও পরিচালনা করার অফিসিয়াল প্যাকেজ ম্যানেজার টুল কোনটি?",
    "options": ["pip (Pip Installs Packages)", "npm", "composer", "gem"],
    "answer": "ক",
    "explanation": "`pip` পাইথনের স্ট্যান্ডার্ড প্যাকেজ ম্যানেজার যা PyPI (Python Package Index) থেকে মডিউল ডাউনলোড ও ইনস্টল করে।"
})

sub4_questions_part1.append({
    "id": 14,
    "topic": topic_4_1,
    "question": "পাইথন স্ক্রিপ্ট ফাইলে প্রথম লাইনে থাকা `#!/usr/bin/env python3` নির্দেশিকাটিকে ইউনিক্স সিস্টেমে কী বলা হয়?",
    "options": ["শেব্যাং (Shebang / Hashbang)", "প্রিপ্রসেসর ডিরেক্টিভ", "কম্পাইলার ফ্ল্যাগ", "মেইন পয়েন্টার"],
    "answer": "ক",
    "explanation": "`#!` হলো শেব্যাং লাইন যা ইউনিক্স/লিনাক্স শেলকে নির্দেশ দেয় ফাইলটি এক্সিকিউট করতে কোন ইন্টারপ্রেটার ব্যবহার করতে হবে।"
})

sub4_questions_part1.append({
    "id": 15,
    "topic": topic_4_1,
    "question": "পাইথন কোডের স্টাইল গাইড এবং আদর্শ কোডিং কনভেনশন কোন পিইপি (PEP) ডকুমেন্টে সংজ্ঞায়িত?",
    "options": ["PEP 8", "PEP 20", "PEP 484", "PEP 257"],
    "answer": "ক",
    "explanation": "PEP 8 (Python Enhancement Proposal 8) হলো পাইথনের অফিসিয়াল কোড স্টাইল গাইড (ইনডেন্টেশন, ভ্যারিয়েবল নেমিং ইত্যাদি)।"
})

# ==============================================================================
# অধ্যায় ৪.২: ভ্যারিয়েবল ও ডেটা টাইপ (Questions 16 to 30)
# ==============================================================================
topic_4_2 = "অধ্যায় ৪.২: ভ্যারিয়েবল ও ডেটা টাইপ"

sub4_questions_part1.append({
    "id": 16,
    "topic": topic_4_2,
    "question": "পাইথনে ভ্যারিয়েবলের ডেটা টাইপ কীভাবে নির্ধারিত হয়?",
    "options": [
        "ডাইনামিকালি (Dynamically Typed - অ্যাসাইন করা মানের ওপর ভিত্তি করে রান-টাইমে স্বয়ংক্রিয়ভাবে)",
        "স্ট্যাটিকালি (কোডে ডেটা টাইপ স্পষ্টভাবে ঘোষণা করতে হয়)",
        "কম্পাইলেশনের পূর্বে ইউজারকে ইনপুট দিতে হয়",
        "পাইথনে কোনো ডেটা টাইপ নেই"
    ],
    "answer": "ক",
    "explanation": "পাইথনে `x = 10` লিখলে x স্বয়ংক্রিয়ভাবে int এবং পরবর্তীতে `x = 'hello'` লিখলে তা str হয়ে যায় (ডাইনামিক টাইপিং)।"
})

sub4_questions_part1.append({
    "id": 17,
    "topic": topic_4_2,
    "question": "কোনো ভ্যারিয়েবলের বর্তমান ডেটা টাইপ জানার জন্য কোন বিল্ট-ইন ফাংশন ব্যবহৃত হয়?",
    "options": ["type(var)", "typeof(var)", "datatype(var)", "isinstance(var)"],
    "answer": "ক",
    "explanation": "`type(x)` ফাংশন ভ্যারিয়েবলের টাইপ ক্লাস নির্দেশ করে (যেমন: `<class 'int'>`)।"
})

sub4_questions_part1.append({
    "id": 18,
    "topic": topic_4_2,
    "question": "পাইথন ৩-এ পূর্ণসংখ্যা (`int`) ডেটা টাইপের মেমরি ধারণক্ষমতা বা সর্বোচ্চ সীমা কত?",
    "options": [
        "অসীম বা সীমাহীন (কম্পিউটারের উপলব্ধ র্যামের পরিমাণের ওপর নির্ভরশীল)",
        "৩২-বিট (-২১৪৭৪৮৩৬৪৮ থেকে +২১৪৭৪৮৩৬৪৭)",
        "৬৪-বিট",
        "১২৮-বিট"
    ],
    "answer": "ক",
    "explanation": "পাইথন ৩ এ ইন্টিজারের সাইজ ফিক্সড নয়; মেমরি থাকা সাপেক্ষে যত খুশি বড় পূর্ণসংখ্যা কোনো ওভারফ্লো ছাড়াই সংরক্ষণ করা যায়।"
})

sub4_questions_part1.append({
    "id": 19,
    "topic": topic_4_2,
    "question": "পাইথনে জটিল সংখ্যা (Complex Number) প্রকাশের সঠিক রূপ কোনটি?",
    "options": ["a + bj (যেমন: 3 + 4j)", "a + bi", "complex(a, b, c)", "a + bk"],
    "answer": "ক",
    "explanation": "পাইথনে কাল্পনিক একক (Imaginary unit) হিসেবে 'i'-এর বদলে 'j' বা 'J' ব্যবহৃত হয়।"
})

sub4_questions_part1.append({
    "id": 20,
    "topic": topic_4_2,
    "question": "পাইথনে বুলিয়ান ডেটা টাইপের (`bool`) দুটি সম্ভাব্য মান কী কী?",
    "options": ["True এবং False (বড় হাতের T এবং F দিয়ে শুরু)", "true এবং false", "0 এবং 1", "YES এবং NO"],
    "answer": "ক",
    "explanation": "পাইথনে বুলিয়ান হলো `int` এর সাবক্লাস এবং এর কীওয়ার্ড দুটি বড় হাতের: `True` (মান 1) এবং `False` (মান 0)।"
})

sub4_questions_part1.append({
    "id": 21,
    "topic": topic_4_2,
    "question": "পাইথনে কোনো মানের অনুপস্থিতি বা শূন্য রেফারেন্স বোঝাতে কোন বিশেষ ডেটা টাইপ ব্যবহৃত হয়?",
    "options": ["None (NoneType)", "null", "nil", "void"],
    "answer": "ক",
    "explanation": "অন্য ভাষায় যা null, পাইথনে তা একক অবজেক্ট `None` যার টাইপ `NoneType`।"
})

sub4_questions_part1.append({
    "id": 22,
    "topic": topic_4_2,
    "question": "পাইথনে ইমিউটেবল (Immutable - যা অপরিবর্তনশীল) ডেটা টাইপের অন্তর্ভুক্ত কোনগুলো?",
    "options": ["int, float, bool, str, tuple, frozenset", "list, dict, set", "list এবং bytearray", "dictionary এবং set"],
    "answer": "ক",
    "explanation": "ইমিউটেবল অবজেক্ট তৈরির পর মেমরিতে এর অভ্যন্তরীণ মান বদলানো যায় না; যেকোনো পরিবর্তন নতুন অবজেক্ট তৈরি করে।"
})

sub4_questions_part1.append({
    "id": 23,
    "topic": topic_4_2,
    "question": "পাইথনে মিউটেবল (Mutable - যা সরাসরি পরিবর্তনযোগ্য) ডেটা টাইপের অন্তর্ভুক্ত কোনগুলো?",
    "options": ["list, dict, set, bytearray", "tuple, str, int", "frozenset, bool", "float, complex"],
    "answer": "ক",
    "explanation": "মিউটেবল ডেটা টাইপের ক্ষেত্রে মেমরি আইডি বা অবজেক্টের অস্তিত্ব পরিবর্তন না করেই উপাদান যোগ-বিয়োগ করা যায়।"
})

sub4_questions_part1.append({
    "id": 24,
    "topic": topic_4_2,
    "question": "মেমরিতে একটি অবজেক্টের অনন্য পরিচয় বা ভার্চুয়াল মেমরি অ্যাড্রেস জানার ফাংশন কোনটি?",
    "options": ["id(obj)", "addr(obj)", "memory(obj)", "ptr(obj)"],
    "answer": "ক",
    "explanation": "`id(x)` অবজেক্টটির অনন্য ইনটিজার আইডি প্রদান করে যা CPython-এ অবজেক্টটির আসল মেমরি অ্যাড্রেস।"
})

sub4_questions_part1.append({
    "id": 25,
    "topic": topic_4_2,
    "question": "নিচের কোনটি পাইথনে একটি অবৈধ (Invalid) ভ্যারিয়েবল নাম?",
    "options": ["2nd_total", "_my_var", "total_sum", "user2"],
    "answer": "ক",
    "explanation": "পাইথনে কোনো ভ্যারিয়েবলের নাম সংখ্যা (Digit) দিয়ে শুরু হতে পারে না; বর্ণ বা আন্ডারস্কোর দিয়ে শুরু হতে হয়।"
})

sub4_questions_part1.append({
    "id": 26,
    "topic": topic_4_2,
    "question": "পাইথনে একই সাথে একাধিক ভ্যারিয়েবলে মান অ্যাসাইন করার সিনট্যাক্স কোনটি?",
    "options": ["x, y, z = 10, 20, 30", "x = 10, y = 20, z = 30", "x; y; z = 10; 20; 30", "x and y and z = 10"],
    "answer": "ক",
    "explanation": "পাইথনে মাল্টিপল অ্যাসাইনমেন্ট বা টাপল আনপ্যাকিংয়ের মাধ্যমে একসাথে একাধিক ভ্যারিয়েবল মান পায়।"
})

sub4_questions_part1.append({
    "id": 27,
    "topic": topic_4_2,
    "question": "পাইথনে দুটি ভ্যারিয়েবল a এবং b এর মান কোনো তৃতীয় ভ্যারিয়েবল ছাড়া অদলবদল (Swap) করার পাইথনিক উপায় কোনটি?",
    "options": ["a, b = b, a", "swap(a, b)", "a = b; b = a", "a.swap(b)"],
    "answer": "ক",
    "explanation": "`a, b = b, a` টাপল প্যাকিং ও আনপ্যাকিংয়ের মাধ্যমে কোনো অতিরিক্ত সহায়ক ভ্যারিয়েবল ছাড়াই তাৎক্ষণিক সোয়াপ সম্পন্ন করে।"
})

sub4_questions_part1.append({
    "id": 28,
    "topic": topic_4_2,
    "question": "স্ট্রিং থেকে পূর্ণসংখ্যায় রূপান্তর করার টাইপকাস্ট ফাংশন কোনটি?",
    "options": ["int(\"123\")", "str.to_int()", "parse_int()", "integer()"],
    "answer": "ক",
    "explanation": "`int()` কনস্ট্রাক্টর ফাংশন সাংখ্যিক স্ট্রিংকে পূর্ণসংখ্যায় রূপান্তর করে।"
})

sub4_questions_part1.append({
    "id": 29,
    "topic": topic_4_2,
    "question": "বাইনোমিয়াল বা বড় সংখ্যার পাঠযোগ্যতা বৃদ্ধির জন্য পাইথন ৩.৬ থেকে ডিজিট সেপারেটর হিসেবে কী বৈধ করা হয়?",
    "options": ["আন্ডারস্কোর `_` (যেমন: 1_000_000)", "কমা `,`", "ডট `.`", "স্পেস"],
    "answer": "ক",
    "explanation": "সংখ্যার মাঝে `_` দিলে কম্পাইলার তা উপেক্ষা করে, ফলে `1_000_000` হুবহু `1000000` হিসেবে বিবেচিত হয়।"
})

sub4_questions_part1.append({
    "id": 30,
    "topic": topic_4_2,
    "question": "মেমরি অপ্টিমাইজেশনের জন্য পাইথন ছোট পূর্ণসংখ্যার (Small Integer Caching) কোন রেঞ্জকে পূর্বে থেকেই ক্যাশ করে রাখে?",
    "options": ["-৫ থেকে ২৫৬ পর্যন্ত (-5 to 256)", "০ থেকে ১০০", "-১২৮ থেকে ১২৭", "সকল ধনাত্মক সংখ্যা"],
    "answer": "ক",
    "explanation": "CPython -5 থেকে 256 পর্যন্ত ইন্টিজার অবজেক্টগুলোকে প্রি-অ্যালোকেট করে রাখে, ফলে এদের `id()` সর্বদা অভিন্ন হয়।"
})

# ==============================================================================
# অধ্যায় ৪.৩: পাইথন অপারেটর ও এক্সপ্রেশন (Questions 31 to 45)
# ==============================================================================
topic_4_3 = "অধ্যায় ৪.৩: পাইথন অপারেটর ও এক্সপ্রেশন"

sub4_questions_part1.append({
    "id": 31,
    "topic": topic_4_3,
    "question": "পাইথনে ফ্লোর ডিভিশন বা পূর্ণসংখ্যা ভাগফল (Floor Division) অপারেটর কোনটি?",
    "options": ["//", "/", "%", "**"],
    "answer": "ক",
    "explanation": "`//` অপারেটর ভাগফলের দশমিক অংশ ছেঁটে নিকটবর্তী ছোট পূর্ণসংখ্যা প্রদান করে (যেমন: `7 // 2` হয় 3, এবং `-7 // 2` হয় -4)।"
})

sub4_questions_part1.append({
    "id": 32,
    "topic": topic_4_3,
    "question": "পাইথনে সাধারণ ট্রু ডিভিশন (True Division) অপারেটর `/` এর আউটপুট সর্বদা কোন ডেটা টাইপ হয়?",
    "options": ["float (ফ্লোটিং পয়েন্ট সংখ্যা)", "int", "ডাবল", "ইনপুটের ওপর নির্ভর করে"],
    "answer": "ক",
    "explanation": "পাইথন ৩-এ `/` অপারেটর দিয়ে দুটি পূর্ণসংখ্যাকে ভাগ করলেও (যেমন: `4 / 2`) ফলাফল সর্বদা `float` (2.0) হয়।"
})

sub4_questions_part1.append({
    "id": 33,
    "topic": topic_4_3,
    "question": "পাইথনে ঘাত বা এক্সপোনেনশিয়েশন (Power / Exponentiation) অপারেটর কোনটি?",
    "options": ["** (যেমন: 2 ** 3 = 8)", "^", "^^", "pow"],
    "answer": "ক",
    "explanation": "`**` দিয়ে পাওয়ার হিসাব করা হয়; অন্যদিকে `^` হলো বিটওয়াইজ এক্স-অর অপারেটর।"
})

sub4_questions_part1.append({
    "id": 34,
    "topic": topic_4_3,
    "question": "পাইথনে এক্সপোনেনশিয়েশন অপারেটরের (`**`) অ্যাসোসিয়েটিভিটি কোন দিক থেকে কোন দিকে কাজ করে?",
    "options": ["ডান থেকে বামে (Right to Left)", "বাম থেকে ডানে (Left to Right)", "র‍্যান্ডম", "কোনো অ্যাসোসিয়েটিভিটি নেই"],
    "answer": "ক",
    "explanation": "`2 ** 3 ** 2` এর ক্ষেত্রে প্রথমে ডানের `3 ** 2 = 9` হিসাব হয়, তারপর `2 ** 9 = 512` হয়।"
})

sub4_questions_part1.append({
    "id": 35,
    "topic": topic_4_3,
    "question": "পাইথনে লজিক্যাল অপারেটর কোনগুলো?",
    "options": ["and, or, not (ইংরেজি শব্দে)", "&&, ||, !", "&, |, ~", "AND, OR, NOT"],
    "answer": "ক",
    "explanation": "পাইথনে সি-এর মতো `&&` বা `||` নেই; ছোট হাতের ইংরেজি শব্দ `and`, `or`, `not` ব্যবহৃত হয়।"
})

sub4_questions_part1.append({
    "id": 36,
    "topic": topic_4_3,
    "question": "পাইথনে দুটি অবজেক্ট মেমরির একই ঠিকানা নির্দেশ করছে কিনা তা পরীক্ষা করার আইডেন্টিটি অপারেটর (Identity Operator) কোনটি?",
    "options": ["is এবং is not", "==", "equals", "in"],
    "answer": "ক",
    "explanation": "`is` অপারেটর দুটি ভ্যারিয়েবলের মেমরি আইডি (`id(a) == id(b)`) তুলনা করে; অন্যদিকে `==` মান তুলনা করে।"
})

sub4_questions_part1.append({
    "id": 37,
    "topic": topic_4_3,
    "question": "যদি `a = [1, 2, 3]` এবং `b = [1, 2, 3]` হয়, তবে `a == b` এবং `a is b` এর ফলাফল যথাক্রমে কী হবে?",
    "options": [
        "True এবং False",
        "True এবং True",
        "False এবং False",
        "False এবং True"
    ],
    "answer": "ক",
    "explanation": "উভয়ের মান একই হওয়ায় `a == b` হলো True; কিন্তু দুটি পৃথক লিস্ট মেমরিতে ভিন্ন ভিন্ন জায়গায় তৈরি হওয়ায় `a is b` হলো False।"
})

sub4_questions_part1.append({
    "id": 38,
    "topic": topic_4_3,
    "question": "কোনো সিকোয়েন্সে (স্ট্রিং, লিস্ট বা টাপলে) নির্দিষ্ট কোনো মান বিদ্যমান আছে কিনা তা পরীক্ষা করার মেম্বারশিপ অপারেটর (Membership Operator) কোনটি?",
    "options": ["in এবং not in", "has", "contains", "exists"],
    "answer": "ক",
    "explanation": "`'a' in 'apple'` সত্য রিটার্ন করে; `in` ও `not in` হলো মেম্বারশিপ অপারেটর।"
})

sub4_questions_part1.append({
    "id": 39,
    "topic": topic_4_3,
    "question": "পাইথনে টার্নারি অপারেটর বা কন্ডিশনাল এক্সপ্রেশনের সঠিক সিনট্যাক্স কোনটি?",
    "options": ["value_if_true if condition else value_if_false", "condition ? exp1 : exp2", "if condition then exp1 else exp2", "select(condition, exp1, exp2)"],
    "answer": "ক",
    "explanation": "পাইথনে টার্নারি সিনট্যাক্স হলো: `x = 'Even' if n % 2 == 0 else 'Odd'`।"
})

sub4_questions_part1.append({
    "id": 40,
    "topic": topic_4_3,
    "question": "পাইথন ৩.৮ এ প্রবর্তিত অ্যাসাইনমেন্ট এক্সপ্রেশন বা ওয়ালরাস অপারেটর (Walrus Operator) কোনটি?",
    "options": [":= (কোলন ও সমান)", "=: ", "=>", "=="],
    "answer": "ক",
    "explanation": "`:=` (দেখতে সিন্ধুর ঘোড়ার চোখের মতো) এক্সপ্রেশনের ভেতরেই ভ্যারিয়েবলে মান অ্যাসাইন ও মান রিটার্ন করতে পারে।"
})

sub4_questions_part1.append({
    "id": 41,
    "topic": topic_4_3,
    "question": "পাইথনে বিটওয়াইজ নট (Bitwise NOT) অপারেটরে `~x` এর গাণিতিক সূত্র কোনটি?",
    "options": ["-(x + 1)", "-x", "x + 1", "1 - x"],
    "answer": "ক",
    "explanation": "টুজ কমপ্লিমেন্ট নিয়মে `~x` সর্বদা `-(x + 1)` প্রদান করে (যেমন: `~5` এর ফলাফল -6)।"
})

sub4_questions_part1.append({
    "id": 42,
    "topic": topic_4_3,
    "question": "নিচের এক্সপ্রেশনের ফলাফল কী হবে?\n`1 < 2 < 3 == 3`",
    "options": [
        "True (চেইনড কম্প্যারিজন: 1 < 2 and 2 < 3 and 3 == 3)",
        "False",
        "টাইপ এরর",
        "কম্পাইল এরর"
    ],
    "answer": "ক",
    "explanation": "পাইথন Chained Comparison সমর্থন করে, যার প্রতিটি অংশ সত্য হওয়ায় সামগ্রিক ফলাফল True হয়।"
})

sub4_questions_part1.append({
    "id": 43,
    "topic": topic_4_3,
    "question": "পাইথনে শর্ট সার্কিট ইভালুয়েশনে `10 or 20` এক্সপ্রেশনের আউটপুট কী হবে?",
    "options": ["10 (কারণ প্রথম অংশ অশূন্য/সত্য হওয়ায় দ্বিতীয় অংশে যায় না)", "True", "20", "30"],
    "answer": "ক",
    "explanation": "`or` এর প্রথম মান সত্য (ট্রুথি) হলে পাইথন সেই মানটিই সরাসরি রিটার্ন করে।"
})

sub4_questions_part1.append({
    "id": 44,
    "topic": topic_4_3,
    "question": "পাইথনে শর্ট সার্কিট ইভালুয়েশনে `10 and 20` এর আউটপুট কী হবে?",
    "options": ["20 (কারণ প্রথম অংশ সত্য হলে দ্বিতীয় অংশের মানের ওপর ফলাফল নির্ভর করে)", "10", "True", "False"],
    "answer": "ক",
    "explanation": "`and` এর ক্ষেত্রে উভয় শর্ত সত্য হতে হয়, তাই প্রথমটি সত্য হলে শেষ অপারেন্ডের মানটিই চূড়ান্ত মান হয়।"
})

sub4_questions_part1.append({
    "id": 45,
    "topic": topic_4_3,
    "question": "পাইথনে কোন মানগুলো বুলিয়ান যাচাইয়ে 'ফলসি' (Falsy) হিসেবে গণ্য হয়?",
    "options": [
        "None, False, 0, 0.0, খালি স্ট্রিং \"\", খালি লিস্ট [], খালি টাপল (), খালি ডিকশনারি {}, খালি সেট set()",
        "শুধুমাত্র 0 এবং False",
        "শুধুমাত্র ঋণাত্মক সংখ্যা",
        "কেবলমাত্র None"
    ],
    "answer": "ক",
    "explanation": "পাইথনে শূন্য, নান এবং যেকোনো খালি কালেকশন বা সিকোয়েন্স শর্ত হিসেবে দিলে মিথ্যা (False) বিবেচনা করা হয়।"
})

# ==============================================================================
# অধ্যায় ৪.৪: ফরম্যাটেড ইনপুট ও আউটপুট (Questions 46 to 55)
# ==============================================================================
topic_4_4 = "অধ্যায় ৪.৪: ফরম্যাটেড ইনপুট ও আউটপুট"

sub4_questions_part1.append({
    "id": 46,
    "topic": topic_4_4,
    "question": "পাইথনে ব্যবহারকারীর কাছ থেকে কীবোর্ড ইনপুট নেওয়ার বিল্ট-ইন ফাংশন কোনটি?",
    "options": ["input()", "raw_input()", "read()", "scanf()"],
    "answer": "ক",
    "explanation": "পাইথন ৩-এ `input()` ফাংশন কনসোল থেকে ইনপুট নিয়ে সর্বদা স্ট্রিং (`str`) আকারে রিটার্ন করে।"
})

sub4_questions_part1.append({
    "id": 47,
    "topic": topic_4_4,
    "question": "`input()` ফাংশন দিয়ে পূর্ণসংখ্যা ইনপুট নিতে হলে কোন অতিরিক্ত ফাংশন ব্যবহার করতে হয়?",
    "options": ["int(input())", "input.to_int()", "cin >> x", "scan_int()"],
    "answer": "ক",
    "explanation": "যেহেতু `input()` সর্বদা স্ট্রিং দেয়, তাই গাণিতিক কাজের জন্য একে `int()` দিয়ে টাইপকাস্ট করতে হয়।"
})

sub4_questions_part1.append({
    "id": 48,
    "topic": topic_4_4,
    "question": "কনসোলে এক লাইনে স্পেস দিয়ে একাধিক ইনপুট গ্রহণ করতে কোন পদ্ধতি কার্যকর?",
    "options": ["input().split()", "input().multiple()", "input().all()", "read_all()"],
    "answer": "ক",
    "explanation": "`split()` ফাংশন স্পেসের ওপর ভিত্তি করে ইনপুট লাইনটিকে স্ট্রিংয়ের লিস্টে বিভক্ত করে।"
})

sub4_questions_part1.append({
    "id": 49,
    "topic": topic_4_4,
    "question": "একই লাইনে ইনপুট নিয়ে সরাসরি পূর্ণসংখ্যায় রূপান্তর করতে কোনটি ব্যবহৃত হয়?",
    "options": ["map(int, input().split())", "int(input().split())", "input().toInt()", "split(int)"],
    "answer": "ক",
    "explanation": "`map(int, input().split())` স্পেসযুক্ত সকল ইনপুটকে ইন্টিজারে রূপান্তর করে।"
})

sub4_questions_part1.append({
    "id": 50,
    "topic": topic_4_4,
    "question": "পাইথন `print()` ফাংশনে উপাদানগুলোর মধ্যকার সংযোগকারী চিহ্ন পরিবর্তনের প্যারামিটার কোনটি?",
    "options": ["sep (Separator)", "end", "flush", "delimiter"],
    "answer": "ক",
    "explanation": "`print(a, b, sep='-')` দিলে উপাদানগুলোর মাঝে ডিফল্ট স্পেসের বদলে হাইফেন বসবে।"
})

sub4_questions_part1.append({
    "id": 51,
    "topic": topic_4_4,
    "question": "পাইথন `print()` ফাংশনে লাইনের সমাপ্তি চিহ্ন (ডিফল্ট নিউলাইন `\\n`) পরিবর্তনের প্যারামিটার কোনটি?",
    "options": ["end", "sep", "terminate", "line"],
    "answer": "ক",
    "explanation": "`print(\"Hello\", end=' ')` দিলে আউটপুটের শেষে নতুন লাইনে না গিয়ে স্পেস যোগ হবে।"
})

sub4_questions_part1.append({
    "id": 52,
    "topic": topic_4_4,
    "question": "পাইথন ৩.৬ থেকে প্রবর্তিত আধুনিক, দ্রুততম ও সর্বাধিক পঠিত ফরম্যাটেড স্ট্রিং কোনটি?",
    "options": ["f-string (Formatted string literals - f\"Hello {name}\")", "str.format()", "% ফরম্যাটিং", "template string"],
    "answer": "ক",
    "explanation": "f-string হলো `f\"...{expression}...\"` যা রান-টাইমে এক্সপ্রেশনকে দ্রুত ইভালুয়েট করে প্রতিস্থাপন করে।"
})

sub4_questions_part1.append({
    "id": 53,
    "topic": topic_4_4,
    "question": "f-string ব্যবহার করে একটি ফ্লোট সংখ্যার দশমিকের পর ঠিক ২ ঘর পর্যন্ত দেখানোর সিনট্যাক্স কোনটি?",
    "options": ["f\"{num:.2f}\"", "f\"{num:2}\"", "f\"{round(num, 2)}\"", "f\"{num%2f}\""],
    "answer": "ক",
    "explanation": "`:.2f` ফরম্যাট স্পেসিফায়ার ফ্লোটিং পয়েন্ট সংখ্যাকে দশমিকের পর ২ ঘর প্রদর্শন নিশ্চিত করে।"
})

sub4_questions_part1.append({
    "id": 54,
    "topic": topic_4_4,
    "question": "পাইথনে কোনো টেক্সট বা সংখ্যার বামে শূন্য (Zero) প্যাডিং করে নির্দিষ্ট দৈর্ঘ্য করার মেথড কোনটি?",
    "options": ["str.zfill(width)", "str.pad()", "str.zero()", "str.fill()"],
    "answer": "ক",
    "explanation": "`\"42\".zfill(5)` এর ফলাফল হবে `\"00042\"`।"
})

sub4_questions_part1.append({
    "id": 55,
    "topic": topic_4_4,
    "question": "স্ট্রিংকে কেন্দ্রে রেখে দুইপাশে নির্দিষ্ট ক্যারেক্টার দিয়ে পূর্ণ করার ফরম্যাটিং মেথড কোনটি?",
    "options": ["str.center(width, fillchar)", "str.middle()", "str.justify()", "str.align()"],
    "answer": "ক",
    "explanation": "`\"Python\".center(10, '*')` স্ট্রিংটিকে কেন্দ্রে রেখে দুইপাশে তারা বসিয়ে দৈর্ঘ্য ১০ করবে।"
})

# ==============================================================================
# অধ্যায় ৪.৫: কন্ডিশনাল কন্ট্রোল স্টেটমেন্ট (Questions 56 to 70)
# ==============================================================================
topic_4_5 = "অধ্যায় ৪.৫: কন্ডিশনাল কন্ট্রোল স্টেটমেন্ট"

sub4_questions_part1.append({
    "id": 56,
    "topic": topic_4_5,
    "question": "পাইথনে মাল্টি-ওয়ে ডিসিশন মেকিংয়ের জন্য 'else if'-এর সংক্ষিপ্ত কিওয়ার্ড কোনটি?",
    "options": ["elif", "else if", "elseif", "elsif"],
    "answer": "ক",
    "explanation": "পাইথনে একাধিক শর্তের সিঁড়ি তৈরির জন্য `if ... elif ... else` সিনট্যাক্স ব্যবহৃত হয়।"
})

sub4_questions_part1.append({
    "id": 57,
    "topic": topic_4_5,
    "question": "পাইথনে কোনো ফাংশন, ক্লাস বা কন্ডিশনাল ব্লকে কোনো কাজ না করে ব্লকটি সিনট্যাক্সগতভাবে পূর্ণ রাখতে কী ব্যবহৃত হয়?",
    "options": ["pass স্টেটমেন্ট", "continue", "break", "null"],
    "answer": "ক",
    "explanation": "`pass` হলো একটি নো-অপারেশন (No-op) স্টেটমেন্ট যা খালি কোড ব্লকে ইনডেন্টেশন এরর দূর করতে ব্যবহৃত হয়।"
})

sub4_questions_part1.append({
    "id": 58,
    "topic": topic_4_5,
    "question": "পাইথন ৩.১০ এ প্রবর্তিত প্যাটার্ন ম্যাচিং (সি-এর switch-case এর বিকল্প) স্টেটমেন্ট কোনটি?",
    "options": ["match-case স্টেটমেন্ট", "switch-case স্টেটমেন্ট", "select-case", "choose-when"],
    "answer": "ক",
    "explanation": "পাইথন ৩.১০ এ স্ট্রাকচারাল প্যাটার্ন ম্যাচিংয়ের জন্য `match expr: case pattern:` যুক্ত করা হয়।"
})

sub4_questions_part1.append({
    "id": 59,
    "topic": topic_4_5,
    "question": "পাইথন ৩.১০ এর `match-case` এ ডিফল্ট কেস (Default fallback) বোঝাতে কোন প্যাটার্ন ব্যবহৃত হয়?",
    "options": ["case _:", "case default:", "default:", "case *:"],
    "answer": "ক",
    "explanation": "ওয়াইল্ডকার্ড হিসেবে আন্ডারস্কোর `case _:` হলো ডিফল্ট ম্যাচ যা অন্য কোনো প্যাটার্ন না মিললে কার্যকর হয়।"
})

sub4_questions_part1.append({
    "id": 60,
    "topic": topic_4_5,
    "question": "নিচের কোডের আউটপুট কী হবে?\n`x = []\nif x:\n    print(\"Yes\")\nelse:\n    print(\"No\")`",
    "options": ["No", "Yes", "Error", "None"],
    "answer": "ক",
    "explanation": "খালি লিস্ট `[]` একটি ফলসি (Falsy) মান, তাই if শর্ত মিথ্যা হয়ে else ব্লক চলে এবং 'No' প্রিন্ট হয়।"
})

sub4_questions_part1.append({
    "id": 61,
    "topic": topic_4_5,
    "question": "পাইথনে কোনো শর্তের পূর্বে সত্যকে মিথ্যা এবং মিথ্যাকে সত্য করতে কোন অপারেটর ব্যবহৃত হয়?",
    "options": ["not", "!", "~", "invert"],
    "answer": "ক",
    "explanation": "লজিক্যাল নেগেশনের জন্য পাইথনে `not` কিওয়ার্ড ব্যবহৃত হয় (যেমন: `if not flag:`)।"
})

sub4_questions_part1.append({
    "id": 62,
    "topic": topic_4_5,
    "question": "কোনো একটি শর্তের পেটে আরেকটি শর্ত সন্নিবেশিত করাকে কী বলে?",
    "options": ["নেস্টেড কন্ডিশন (Nested if)", "মাল্টিপল if", "কম্পাউন্ড if", "চেইনড if"],
    "answer": "ক",
    "explanation": "একটি `if` ব্লকের অভ্যন্তরে ইনডেন্টেশন দিয়ে পুনরায় `if` লেখা হলো নেস্টেড কন্ডিশন।"
})

sub4_questions_part1.append({
    "id": 63,
    "topic": topic_4_5,
    "question": "নিচের কোডের আউটপুট কী?\n`a = 5\nprint(\"Big\") if a > 10 else print(\"Small\")`",
    "options": ["Small", "Big", "SyntaxError", "None"],
    "answer": "ক",
    "explanation": "এটি ওয়ান-লাইনার কন্ডিশনাল এক্সপ্রেশন। যেহেতু ৫ > ১০ মিথ্যা, তাই else এর অংশ 'Small' কার্যকর হয়।"
})

sub4_questions_part1.append({
    "id": 64,
    "topic": topic_4_5,
    "question": "লিপ ইয়ার (Leap Year) হওয়ার সঠিক পাইথন শর্ত কোনটি?",
    "options": [
        "(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)",
        "year % 4 == 0",
        "year % 400 == 0 and year % 100 == 0",
        "year % 4 == 0 or year % 100 == 0"
    ],
    "answer": "ক",
    "explanation": "৪০০ দ্বারা বিভাজ্য সাল অথবা ১০০ দ্বারা বিভাজ্য না হয়ে ৪ দ্বারা বিভাজ্য সাল লিপ ইয়ার।"
})

sub4_questions_part1.append({
    "id": 65,
    "topic": topic_4_5,
    "question": "পাইথনে কোনো শর্ত যাচাইয়ের পর কোলন (`:`) না দিলে কোন ধরনের ত্রুটি ঘটে?",
    "options": ["SyntaxError", "IndentationError", "NameError", "TypeError"],
    "answer": "ক",
    "explanation": "`if`, `elif`, `else` এর শেষে কোলন দেওয়া ব্যাকরণগত বাধ্যতামূলক নিয়ম; না দিলে সিনট্যাক্স এরর হয়।"
})

sub4_questions_part1.append({
    "id": 66,
    "topic": topic_4_5,
    "question": "ইনডেন্টেশন বা স্পেসিংয়ে অসঙ্গতি থাকলে পাইথনে কোন সুনির্দিষ্ট এক্সেপশন ঘটে?",
    "options": ["IndentationError", "SyntaxError", "TabError", "SpacingError"],
    "answer": "ক",
    "explanation": "ইনডেন্টেশনে কোনো অমিল হলে পাইথন কম্পাইলার তাৎক্ষণিক `IndentationError` প্রদান করে।"
})

sub4_questions_part1.append({
    "id": 67,
    "topic": topic_4_5,
    "question": "একই ফাইলে ইনডেন্টেশনের জন্য ট্যাব (Tab) এবং স্পেসের (Space) মিশ্রণ ঘটালে কোন এরর আসে?",
    "options": ["TabError: inconsistent use of tabs and spaces in indentation", "ValueError", "TypeError", "ZeroDivisionError"],
    "answer": "ক",
    "explanation": "পাইথন ৩-এ একই ফাইলে ট্যাব ও স্পেসের সংমিশ্রণ সম্পূর্ণ নিষিদ্ধ এবং এটি `TabError` সৃষ্টি করে।"
})

sub4_questions_part1.append({
    "id": 68,
    "topic": topic_4_5,
    "question": "তিনটি সংখ্যার মধ্যে বৃহত্তম সংখ্যা নির্ণয়ে পাইথনের বিল্ট-ইন ফাংশন কোনটি?",
    "options": ["max(a, b, c)", "maximum(a, b, c)", "greatest(a, b, c)", "big(a, b, c)"],
    "answer": "ক",
    "explanation": "`max()` ফাংশন প্রদত্ত আর্গুমেন্টসমূহের মধ্যে বৃহত্তম মানটি সরাসরি রিটার্ন করে।"
})

sub4_questions_part1.append({
    "id": 69,
    "topic": topic_4_5,
    "question": "কোনো ভ্যারিয়েবলের মান None কিনা তা যাচাই করার সবচেয়ে আদর্শ পাইথনিক উপায় কোনটি?",
    "options": ["if x is None:", "if x == None:", "if not x:", "if x is not None:"],
    "answer": "ক",
    "explanation": "PEP 8 অনুযায়ী `None` একটি সিঙ্গেলটন অবজেক্ট, তাই এর তুলনা সর্বদা আইডেন্টিটি অপারেটর `is` দিয়ে করতে হয়।"
})

sub4_questions_part1.append({
    "id": 70,
    "topic": topic_4_5,
    "question": "কন্ডিশনাল ব্লকে `assert condition, \"Error Message\"` এর ভূমিকা কী?",
    "options": [
        "শর্তটি মিথ্যা হলে AssertionError তুলে ধরে প্রোগ্রাম বন্ধ করে দেয় (ডিবাগিংয়ে কার্যকর)",
        "শর্তটি ট্রু হলে এরর দেয়",
        "লুপ তৈরি করে",
        "মেমরি ক্লিয়ার করে"
    ],
    "answer": "ক",
    "explanation": "`assert` স্টেটমেন্ট অভ্যন্তরীণ যাচাইকরণ বা ডিবাগিংয়ের জন্য কোডের সঠিক অবস্থা নিশ্চিত করতে ব্যবহৃত হয়।"
})

# ==============================================================================
# অধ্যায় ৪.৬: লুপিং বা পুনরাবৃত্তি স্টেটমেন্ট (Questions 71 to 85)
# ==============================================================================
topic_4_6 = "অধ্যায় ৪.৬: লুপিং বা পুনরাবৃত্তি স্টেটমেন্ট"

sub4_questions_part1.append({
    "id": 71,
    "topic": topic_4_6,
    "question": "পাইথনে মৌলিকভাবে কয় ধরনের লুপ রয়েছে?",
    "options": ["২ ধরনের (for লুপ এবং while লুপ)", "৩ ধরনের (for, while, do-while)", "১ ধরনের", "৪ ধরনের"],
    "answer": "ক",
    "explanation": "পাইথনে সরাসরি কোনো `do-while` লুপ নেই; কেবল `for` এবং `while` লুপ রয়েছে।"
})

sub4_questions_part1.append({
    "id": 72,
    "topic": topic_4_6,
    "question": "পাইথনে সংখ্যার অনুক্রম তৈরি করার ফাংশন `range(start, stop, step)` এর ক্ষেত্রে `stop` মানটির বৈশিষ্ট্য কী?",
    "options": [
        "`stop` মানটি অন্তর্ভুক্ত হয় না (Exclusive - stop-1 পর্যন্ত চলে)",
        "`stop` মানটি সহ চলে (Inclusive)",
        "`stop` মানটি দ্বিগুণ হয়",
        "স্টপ মান দেওয়া বাধ্যতামূলক নয়"
    ],
    "answer": "ক",
    "explanation": "`range(1, 5)` উৎপন্ন করে 1, 2, 3, 4 (অর্থাৎ শেষ সীমা ৫ অন্তর্ভুক্ত হয় না)।"
})

sub4_questions_part1.append({
    "id": 73,
    "topic": topic_4_6,
    "question": "`range(5)` এক্সপ্রেশনটি কোন কোন সংখ্যা তৈরি করে?",
    "options": ["0, 1, 2, 3, 4", "1, 2, 3, 4, 5", "0, 1, 2, 3, 4, 5", "1, 2, 3, 4"],
    "answer": "ক",
    "explanation": "ডিফল্টভাবে `start` শূন্য (0) থেকে শুরু হয় এবং ৫ এর আগ পর্যন্ত মোট ৫টি সংখ্যা উৎপন্ন করে।"
})

sub4_questions_part1.append({
    "id": 74,
    "topic": topic_4_6,
    "question": "১০ থেকে ১ পর্যন্ত উল্টো ক্রমে সংখ্যা প্রিন্ট করতে `range` এর সঠিক রূপ কোনটি?",
    "options": ["range(10, 0, -1)", "range(10, 1, -1)", "range(1, 10, -1)", "range(10, -1, 0)"],
    "answer": "ক",
    "explanation": "শুরু ১০, শেষ ০ (এক্সক্লুসিভ হওয়ায় ১ পর্যন্ত আসবে) এবং স্টেপ -১।"
})

sub4_questions_part1.append({
    "id": 75,
    "topic": topic_4_6,
    "question": "পাইথনে কোনো লুপের সাথে যুক্ত `else` ব্লক কখন এক্সিকিউট হয়?",
    "options": [
        "যখন লুপটি কোনো `break` ছাড়াই স্বাভাবিকভাবে সম্পূর্ণ সমাপ্ত হয়",
        "যখন লুপের ভেতর `break` কার্যকর হয়",
        "লুপের প্রতিটি পুনরাবৃত্তিতে",
        "পাইথনে লুপের সাথে else লেখা যায় না"
    ],
    "answer": "ক",
    "explanation": "পাইথনের অনন্য বৈশিষ্ট্য হলো `for-else` বা `while-else`; লুপ যদি ব্রেক ছাড়া স্বাভাবিকভাবে শেষ হয় কেবল তখনই `else` চলে।"
})

sub4_questions_part1.append({
    "id": 76,
    "topic": topic_4_6,
    "question": "লুপ থেকে তাৎক্ষণিকভাবে সম্পূর্ণ বের হয়ে আসার নির্দেশ কোনটি?",
    "options": ["break", "continue", "pass", "exit"],
    "answer": "ক",
    "explanation": "`break` স্টেটমেন্ট চলমান লুপ বন্ধ করে কন্ট্রোলকে লুপের পরবর্তী স্টেটমেন্টে নিয়ে যায়।"
})

sub4_questions_part1.append({
    "id": 77,
    "topic": topic_4_6,
    "question": "লুপের বর্তমান পুনরাবৃত্তির অবশিষ্ট অংশ বাদ দিয়ে পরবর্তী পুনরাবৃত্তিতে যাওয়ার নির্দেশ কোনটি?",
    "options": ["continue", "break", "pass", "return"],
    "answer": "ক",
    "explanation": "`continue` তাৎক্ষণিক চলতি চক্র স্কিপ করে লুপের পরবর্তী ধাপে অগ্রসর হয়।"
})

sub4_questions_part1.append({
    "id": 78,
    "topic": topic_4_6,
    "question": "পাইথনে কোনো কালেকশন ইটারেট করার সময় একই সাথে ইনডেক্স ও উপাদান পাওয়ার ফাংশন কোনটি?",
    "options": ["enumerate(iterable)", "zip(iterable)", "range(len(iterable))", "items(iterable)"],
    "answer": "ক",
    "explanation": "`for idx, val in enumerate(['a', 'b']):` এটি স্বয়ংক্রিয়ভাবে ইনডেক্স ও ভ্যালুর টাপল জোড়া প্রদান করে।"
})

sub4_questions_part1.append({
    "id": 79,
    "topic": topic_4_6,
    "question": "একাধিক সমদৈর্ঘ্যের লিস্টকে একসাথে সমান্তরালে ইটারেট করতে কোন বিল্ট-ইন ফাংশন ব্যবহৃত হয়?",
    "options": ["zip(list1, list2)", "enumerate()", "combine()", "merge()"],
    "answer": "ক",
    "explanation": "`zip()` একাধিক সিকোয়েন্সের সংশ্লিষ্ট উপাদানগুলোকে জোড়া বেঁধে টাপলের ইটারেটর বানায়।"
})

sub4_questions_part1.append({
    "id": 80,
    "topic": topic_4_6,
    "question": "পাইথনে একটি অসীম লুপ (Infinite Loop) তৈরির সহজ সিনট্যাক্স কোনটি?",
    "options": ["while True:", "for(;;)", "while(1 == 0):", "loop forever:"],
    "answer": "ক",
    "explanation": "`while True:` শর্ত সর্বদা সত্য থাকায় এটি একটি অসীম লুপ তৈরি করে।"
})

sub4_questions_part1.append({
    "id": 81,
    "topic": topic_4_6,
    "question": "নিচের কোডের আউটপুট কী হবে?\n`for i in range(3):\n    if i == 1:\n        break\nelse:\n    print(\"Done\")`",
    "options": ["কিছুই প্রিন্ট হবে না (কারণ break কার্যকর হওয়ায় else ব্লক চলবে না)", "Done", "0 1 Done", "Error"],
    "answer": "ক",
    "explanation": "লুপটি `break` দিয়ে অকালে বন্ধ হওয়ায় লুপের সাথে থাকা `else` ব্লকটি আর এক্সিকিউট হবে না।"
})

sub4_questions_part1.append({
    "id": 82,
    "topic": topic_4_6,
    "question": "পাইথনে লুপ ভ্যারিয়েবলের মান প্রয়োজন না হলে ঐতিহ্যগতভাবে কোন প্রতীককে ডামি ভ্যারিয়েবল হিসেবে ব্যবহার করা হয়?",
    "options": ["_ (আন্ডারস্কোর, যেমন: for _ in range(5):)", "x", "dummy", "null"],
    "answer": "ক",
    "explanation": "পাইথনিক নিয়মে অব্যবহৃত লুপ ভ্যারিয়েবল বোঝাতে একক আন্ডারস্কোর `_` ব্যবহার প্রচলিত।"
})

sub4_questions_part1.append({
    "id": 83,
    "topic": topic_4_6,
    "question": "লুপের ভেতর একটি লিস্ট মডিফাই (উপাদান ডিলিট) করার সময় সূক্ষ্ম ভুল এড়াতে কী করা উচিত?",
    "options": [
        "লিস্টের একটি কপি নিয়ে লুপ চালানো (যেমন: `for item in my_list.copy():`)",
        "সরাসরি লিস্ট দিয়ে চালানো",
        "while লুপ ব্যবহার নিষিদ্ধ",
        "লিস্টের নাম পরিবর্তন করা"
    ],
    "answer": "ক",
    "explanation": "চলমান লিস্টের উপাদান ডিলিট করলে ইনডেক্স শিফট হয়ে কিছু উপাদান স্কিপ হয়ে যায়; কপি দিয়ে লুপ চালালে এ ভুল হয় না।"
})

sub4_questions_part1.append({
    "id": 84,
    "topic": topic_4_6,
    "question": "নেস্টেড লুপের (Nested Loop) ক্ষেত্রে অভ্যন্তরীণ লুপে `break` দিলে কী ঘটে?",
    "options": [
        "শুধুমাত্র যে অভ্যন্তরীণ লুপটিতে break দেওয়া হয়েছে সেটি বন্ধ হয়",
        "একসাথে সকল লুপ বন্ধ হয়ে যায়",
        "প্রোগ্রাম বন্ধ হয়ে যায়",
        "ফাংশন থেকে রিটার্ন করে"
    ],
    "answer": "ক",
    "explanation": "`break` কেবল তার নিজস্ব সবচেয়ে ভেতরের (Innermost) লুপ বন্ধ করে।"
})

sub4_questions_part1.append({
    "id": 85,
    "topic": topic_4_6,
    "question": "কোনো সিকোয়েন্সকে রিভার্স বা উল্টো দিক থেকে ইটারেট করার মেমরি-সাশ্রয়ী ফাংশন কোনটি?",
    "options": ["reversed(sequence)", "sequence.reverse()", "sequence[::-1]", "sort_desc()"],
    "answer": "ক",
    "explanation": "`reversed()` নতুন কপি না বানিয়ে উল্টো দিকের রিভার্স ইটারেটর প্রদান করে যা অত্যন্ত মেমরি সাশ্রয়ী।"
})

# ==============================================================================
# অধ্যায় ৪.৭: পাইথন স্ট্রিং ও লিস্ট ডেটা স্ট্রাকচার (Questions 86 to 100)
# ==============================================================================
topic_4_7 = "অধ্যায় ৪.৭: পাইথন স্ট্রিং ও লিস্ট ডেটা স্ট্রাকচার"

sub4_questions_part1.append({
    "id": 86,
    "topic": topic_4_7,
    "question": "পাইথনে স্ট্রিংয়ের নেগেটিভ ইনডেক্সিংয়ে `-1` কোন উপাদানকে নির্দেশ করে?",
    "options": ["স্ট্রিংয়ের একদম শেষ ক্যারেক্টার (Last Character)", "প্রথম ক্যারেক্টার", "দ্বিতীয় ক্যারেক্টার", "নাল ক্যারেক্টার"],
    "answer": "ক",
    "explanation": "পাইথনে নেগেটিভ ইনডেক্স পেছন দিক থেকে গোনে; ফলে `-1` হলো সর্বশেষ উপাদান এবং `-2` হলো শেষ দিক থেকে দ্বিতীয়।"
})

sub4_questions_part1.append({
    "id": 87,
    "topic": topic_4_7,
    "question": "পাইথনে স্লাইসিং (Slicing) সিনট্যাক্স `s[start:stop:step]` ব্যবহার করে একটি স্ট্রিং রিভার্স করার সংক্ষিপ্ততম উপায় কোনটি?",
    "options": ["s[::-1]", "s[0:-1]", "s[-1:0]", "s.reverse()"],
    "answer": "ক",
    "explanation": "`s[::-1]` স্টেপ -১ দিয়ে পুরো স্ট্রিংকে শুরু থেকে শেষ পর্যন্ত সম্পূর্ণ উল্টে দেয়।"
})

sub4_questions_part1.append({
    "id": 88,
    "topic": topic_4_7,
    "question": "স্ট্রিংয়ের দুই প্রান্তের অবাঞ্ছিত স্পেস বা হোয়াইটস্পেস মুছে ফেলার স্ট্রিং মেথড কোনটি?",
    "options": ["strip()", "trim()", "clean()", "lstrip()"],
    "answer": "ক",
    "explanation": "`strip()` উভয় পাশের স্পেস মোছে, `lstrip()` কেবল বাম পাশের এবং `rstrip()` ডান পাশের স্পেস মোছে।"
})

sub4_questions_part1.append({
    "id": 89,
    "topic": topic_4_7,
    "question": "একটি লিস্টের স্ট্রিং উপাদানগুলোকে নির্দিষ্ট ডিলিমিটার দিয়ে জোড়া লাগিয়ে একক স্ট্রিং বানানোর মেথড কোনটি?",
    "options": ["delimiter.join(list)", "list.join(delimiter)", "concat(list)", "merge(list)"],
    "answer": "ক",
    "explanation": "`'-'.join(['a', 'b', 'c'])` এর ফলাফল হবে `'a-b-c'`।"
})

sub4_questions_part1.append({
    "id": 90,
    "topic": topic_4_7,
    "question": "পাইথনে লিস্ট (List) ডেটা স্ট্রাকচারের প্রধান বৈশিষ্ট্য কোনটি?",
    "options": [
        "অর্ডারড (Ordered), মিউটেবল (Mutable) এবং ভিন্ন ভিন্ন ডেটা টাইপের মিশ্রণ ধারণ করতে সক্ষম",
        "ইমিউটেবল এবং ফিক্সড সাইজ",
        "শুধুমাত্র সমজাতীয় উপাত্ত ধারণ করতে পারে",
        "আন-অর্ডার্ড"
    ],
    "answer": "ক",
    "explanation": "লিস্ট হলো পরিবর্তনযোগ্য ক্রম যাতে ইনটিজার, স্ট্রিং, অবজেক্ট যেকোনো ধরনের ডেটা একসাথে রাখা যায়।"
})

sub4_questions_part1.append({
    "id": 91,
    "topic": topic_4_7,
    "question": "একটি বিদ্যমান লিস্টের একদম শেষে নতুন একটি একক উপাদান যুক্ত করার মেথড কোনটি?",
    "options": ["append(item)", "extend(item)", "insert(item)", "add(item)"],
    "answer": "ক",
    "explanation": "`list.append(x)` উপাদানটিকে লিস্টের শেষ প্রান্তে একক উপাদান হিসেবে যুক্ত করে।"
})

sub4_questions_part1.append({
    "id": 92,
    "topic": topic_4_7,
    "question": "`list.append([4, 5])` এবং `list.extend([4, 5])` এর মধ্যে পার্থক্য কী?",
    "options": [
        "`append` পুরো [4, 5] লিস্টটিকে একটিমাত্র নেস্টেড উপাদান হিসেবে যোগ করে; আর `extend` উপাদান দুটিকে আলাদা আলাদাভাবে যোগ করে",
        "`extend` কেবল স্ট্রিং যোগ করে",
        "উভয়ের কার্যপদ্ধতি হুবহু একই",
        "`append` শুরুতে যোগ করে"
    ],
    "answer": "ক",
    "explanation": "`append` একক এলিমেন্ট যোগ করে (লিস্ট যোগ করলে নেস্টেড লিস্ট হয়); আর `extend` ইটারেবলের প্রতিটি উপাদান আনপ্যাক করে মূল লিস্ট বাড়ায়।"
})

sub4_questions_part1.append({
    "id": 93,
    "topic": topic_4_7,
    "question": "লিস্টের কোনো নির্দিষ্ট ইনডেক্সে উপাদান ঢোকানোর মেথড কোনটি?",
    "options": ["insert(index, item)", "add(index, item)", "push(index, item)", "put(index, item)"],
    "answer": "ক",
    "explanation": "`list.insert(0, 'first')` ইনডেক্স ০-তে নতুন উপাদান ঢুকিয়ে বাকিগুলোকে ডানে সরিয়ে দেয়।"
})

sub4_questions_part1.append({
    "id": 94,
    "topic": topic_4_7,
    "question": "লিস্ট থেকে নির্দিষ্ট কোনো উপাদান মানের ভিত্তিতে প্রথম উপস্থিতি মুছে ফেলার মেথড কোনটি?",
    "options": ["remove(value)", "pop(value)", "delete(value)", "discard(value)"],
    "answer": "ক",
    "explanation": "`list.remove(x)` তালিকার প্রথম ম্যাচিং মানটি মুছে ফেলে; মান না থাকলে `ValueError` দেয়।"
})

sub4_questions_part1.append({
    "id": 95,
    "topic": topic_4_7,
    "question": "লিস্টের নির্দিষ্ট ইনডেক্স থেকে উপাদান মুছে ফেলে সেই মুছে ফেলা মানটি রিটার্ন করে কোন মেথডটি?",
    "options": ["pop(index)", "remove(index)", "del(index)", "pull(index)"],
    "answer": "ক",
    "explanation": "`list.pop()` ডিফল্টভাবে শেষ উপাদানটি মুছে রিটার্ন করে; `list.pop(i)` নির্দিষ্ট ইনডেক্সের উপাদান দেয়।"
})

sub4_questions_part1.append({
    "id": 96,
    "topic": topic_4_7,
    "question": "লিস্ট কম্প্রিহেনশন (List Comprehension) ব্যবহারের মূল সুবিধা কী?",
    "options": [
        "সংক্ষিপ্ত, পরিচ্ছন্ন এবং সাধারণ লুপের চেয়ে দ্রুতগতিতে নতুন লিস্ট তৈরি করা যায়",
        "লিস্টকে ইমিউটেবল করে",
        "মেমরি ব্যবহার দ্বিগুণ করে",
        "শুধুমাত্র সংখ্যার জন্য প্রযোজ্য"
    ],
    "answer": "ক",
    "explanation": "`[x**2 for x in range(10) if x % 2 == 0]` পাইথনিক ও অত্যন্ত অপ্টিমাইজড লিস্ট তৈরির উপায়।"
})

sub4_questions_part1.append({
    "id": 97,
    "topic": topic_4_7,
    "question": "`list.sort()` মেথড এবং `sorted(list)` ফাংশনের মধ্যে মূল পার্থক্য কী?",
    "options": [
        "`list.sort()` মূল লিস্টটিকে মেমরিতে সরাসরি সাজিয়ে ফেলে (In-place); আর `sorted()` মূল লিস্ট অপরিবর্তিত রেখে নতুন সর্টেড লিস্ট দেয়",
        "`sorted()` কেবল রিভার্স করে",
        "`list.sort()` নতুন কপি দেয়",
        "উভয়ের আচরণ এক"
    ],
    "answer": "ক",
    "explanation": "`sort()` মেথড ইন-প্লেস সর্ট করে `None` রিটার্ন করে; `sorted()` একটি নতুন সর্টেড লিস্ট রিটার্ন করে।"
})

sub4_questions_part1.append({
    "id": 98,
    "topic": topic_4_7,
    "question": "পাইথনে শ্যালো কপি (Shallow Copy) এবং ডিপ কপির (Deep Copy) মধ্যে পার্থক্য কী?",
    "options": [
        "শ্যালো কপি ভেতরের নেস্টেড অবজেক্টের রেফারেন্স কপি করে; ডিপ কপি ভেতরের সকল নেস্টেড অবজেক্টের সম্পূর্ণ স্বাধীন ক্লোন কপি তৈরি করে",
        "ডিপ কপি কোনো অবজেক্ট ক্লোন করে না",
        "শ্যালো কপিতে মেমরি বেশি লাগে",
        "উভয় কপি হুবহু এক"
    ],
    "answer": "ক",
    "explanation": "নেস্টেড লিস্টে শ্যালো কপি করলে ভেতরের লিস্ট মডিফাই করলে দুটোতেই বদলে যায়; `copy.deepcopy()` সম্পূর্ণ স্বাধীন কপি দেয়।"
})

sub4_questions_part1.append({
    "id": 99,
    "topic": topic_4_7,
    "question": "নিচের কোডের আউটপুট কী হবে?\n`a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)`",
    "options": ["[1, 2, 3, 4] (কারণ b এবং a একই মেমরি রেফারেন্স শেয়ার করে)", "[1, 2, 3]", "[4]", "Error"],
    "answer": "ক",
    "explanation": "`b = a` কোনো নতুন লিস্ট বানায় না, শুধু রেফারেন্স কপি করে; তাই b পরিবর্তন করলে a-ও পরিবর্তিত হয়।"
})

sub4_questions_part1.append({
    "id": 100,
    "topic": topic_4_7,
    "question": "একটি লিস্টের সকল উপাদান সম্পূর্ণ খালি করে ফেলার ইন-প্লেস মেথড কোনটি?",
    "options": ["clear()", "empty()", "clean()", "erase()"],
    "answer": "ক",
    "explanation": "`list.clear()` লিস্টটির অস্তিত্ব অক্ষুণ্ণ রেখে ভেতরের সকল উপাদান মুছে ফেলে ফাঁকা লিস্ট `[]` বানায়।"
})

print(f"Generated Subject 4 Part 1: {len(sub4_questions_part1)} questions")
