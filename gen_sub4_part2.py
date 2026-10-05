# -*- coding: utf-8 -*-
"""
Subject 4: পাইথন প্রোগ্রামিং (Python Programming & App Development) - Part 2 (Questions 101 to 200)
Chapters:
  4.8: টাপল ডেটা স্ট্রাকচার (101-110)
  4.9: সেট ডেটা স্ট্রাকচার (111-120)
  4.10: ডিকশনারি ডেটা স্ট্রাকচার (121-135)
  4.11: ফাংশন অপারেশন ও মডিউল (136-155)
  4.12: ফাইল আই/ও অপারেশন (156-170)
  4.13: অবজেক্ট ওরিয়েন্টেড পাইথন (171-190)
  4.14: পাইথন জিইউআই ও ডেটাবেস অ্যাপ্লিকেশন (191-200)
"""

sub4_questions_part2 = []

# ==============================================================================
# অধ্যায় ৪.৮: টাপল ডেটা স্ট্রাকচার (Questions 101 to 110)
# ==============================================================================
topic_4_8 = "অধ্যায় ৪.৮: টাপল ডেটা স্ট্রাকচার (Tuple Structure)"

sub4_questions_part2.append({
    "id": 101,
    "topic": topic_4_8,
    "question": "পাইথনে টাপল (Tuple) ডেটা স্ট্রাকচারের মৌলিক বৈশিষ্ট্য কোনটি?",
    "options": [
        "অর্ডারড (Ordered), ইনডেক্সড কিন্তু ইমিউটেবল (Immutable - পরিবর্তন করা যায় না)",
        "মিউটেবল এবং আন-অর্ডার্ড",
        "ডুপ্লিকেট উপাদান অনুমোদন করে না",
        "শুধুমাত্র সংখ্যা সংরক্ষণ করতে পারে"
    ],
    "answer": "ক",
    "explanation": "টাপল প্যারেন্থেসিস `()` দিয়ে গঠিত একটি অপরিবর্তনশীল ক্রম, যার উপাদান একবার তৈরির পর আর পরিবর্তন বা মোছা যায় না।"
})

sub4_questions_part2.append({
    "id": 102,
    "topic": topic_4_8,
    "question": "পাইথনে একটি মাত্র উপাদান বিশিষ্ট টাপল তৈরির সঠিক সিনট্যাক্স কোনটি?",
    "options": ["t = (5,) বা 5,", "t = (5)", "t = [5]", "t = tuple(5)"],
    "answer": "ক",
    "explanation": "একক উপাদানের পর কমা `,` না দিলে পাইথন তাকে সাধারণ বন্ধনীযুক্ত সংখ্যা মনে করে (যেমন `(5)` হলো int, কিন্তু `(5,)` হলো tuple)।"
})

sub4_questions_part2.append({
    "id": 103,
    "topic": topic_4_8,
    "question": "পাইথনে টাপল আনপ্যাকিংয়ে অতিরিক্ত অবশিষ্ট উপাদানগুলোকে একটি লিস্টে ধারণ করতে কোন সিনট্যাক্স ব্যবহৃত হয়?",
    "options": ["স্টার বা এস্টারিস্ক `*` (যেমন: first, *rest = t)", "অ্যাম্পারস্যান্ড `&`", "ডাবল ডট `..`", "কোলন `:`"],
    "answer": "ক",
    "explanation": "এক্সটেন্ডেড আনপ্যাকিংয়ে `*rest` দিলে মধ্যবর্তী বা শেষের বাকি সকল উপাদান স্বয়ংক্রিয়ভাবে একটি লিস্টে জমা হয়।"
})

sub4_questions_part2.append({
    "id": 104,
    "topic": topic_4_8,
    "question": "লিস্টের তুলনায় টাপল ব্যবহারের প্রধান সুবিধা কোনটি?",
    "options": [
        "টাপল ইমিউটেবল হওয়ায় ডেটা সুরক্ষিত থাকে, মেমরি কম নেয় এবং এক্সেস স্পিড তুলনামূলক দ্রুত",
        "টাপলে অনেক বেশি বিল্ট-ইন মেথড থাকে",
        "টাপলে নতুন উপাদান সহজে যোগ করা যায়",
        "টাপল সাইজ ডাইনামিকালি বাড়ে"
    ],
    "answer": "ক",
    "explanation": "ফিক্সড সাইজ ও ইমিউটেবিলিটির কারণে পাইথন ইন্টারপ্রেটার টাপলের মেমরি দারুণভাবে অপ্টিমাইজ করতে পারে।"
})

sub4_questions_part2.append({
    "id": 105,
    "topic": topic_4_8,
    "question": "টাপল কি পাইথনে ডিকশনারির 'কী' (Dictionary Key) হিসেবে ব্যবহৃত হতে পারে?",
    "options": [
        "হ্যাঁ, যদি টাপলের ভেতরের সকল উপাদান ইমিউটেবল/হ্যাশেবল হয়",
        "না, টাপল কখনো কী হতে পারে না",
        "শুধুমাত্র স্ট্রিং থাকলে পারে",
        "যেকোনো টাপল সবসময় পারে"
    ],
    "answer": "ক",
    "explanation": "টাপলের ভেতর যদি মিউটেবল কোনো অবজেক্ট (যেমন লিস্ট `(1, [2, 3])`) না থাকে, তবে তা হ্যাশেবল বিধায় ডিকশনারি কী হতে পারে।"
})

sub4_questions_part2.append({
    "id": 106,
    "topic": topic_4_8,
    "question": "টাপল অবজেক্টের নিজস্ব বিল্ট-ইন মেথড কয়টি?",
    "options": ["২টি (count() এবং index())", "৫টি", "১০টি", "কোনো মেথড নেই"],
    "answer": "ক",
    "explanation": "যেহেতু টাপলে উপাদান যোগ বা বিয়োগ করা যায় না, তাই এতে শুধু উপাদান গণনা `count()` ও অবস্থান খোঁজার `index()` মেথড আছে।"
})

sub4_questions_part2.append({
    "id": 107,
    "topic": topic_4_8,
    "question": "নিচের কোডের আউটপুট কী হবে?\n`t = (1, 2, [3, 4])\nt[2].append(5)\nprint(t)`",
    "options": ["(1, 2, [3, 4, 5])", "TypeError", "(1, 2, [3, 4])", "ValueError"],
    "answer": "ক",
    "explanation": "টাপল ইমিউটেবল হলেও তার অভ্যন্তরে থাকা রেফারেন্সড লিস্টটি নিজে মিউটেবল, তাই লিস্টটির ভেতরের উপাদান পরিবর্তন সম্ভব।"
})

sub4_questions_part2.append({
    "id": 108,
    "topic": topic_4_8,
    "question": "কোনো বিদ্যমান টাপলে নতুন উপাদান যোগ করতে চাইলে প্রচলিত কার্যকর পদ্ধতি কোনটি?",
    "options": [
        "টাপলটিকে লিস্টে রূপান্তর করে পরিবর্তন শেষে পুনরায় টাপলে কনভার্ট করা",
        "tuple.append() মেথড কল করা",
        "tuple.insert() মেথড কল করা",
        "টাপলে কখনোই পরিবর্তন সম্ভব নয়"
    ],
    "answer": "ক",
    "explanation": "`temp = list(my_tuple); temp.append(x); my_tuple = tuple(temp)` এর মাধ্যমে নতুন টাপল তৈরি করা হয়।"
})

sub4_questions_part2.append({
    "id": 109,
    "topic": topic_4_8,
    "question": "ইনডেক্সের পাশাপাশি নামের মাধ্যমে টাপলের উপাদান অ্যাক্সেস করার সুবিধাজনক স্ট্যান্ডার্ড ক্লাস কোনটি?",
    "options": ["collections.namedtuple", "collections.OrderedDict", "typing.Tuple", "dataclass"],
    "answer": "ক",
    "explanation": "`namedtuple` ব্যবহার করে অবজেক্টের মতো ফিল্ড নেমে (যেমন: `pt.x`, `pt.y`) হালকা ওজনে টাপল উপাদান অ্যাক্সেস করা যায়।"
})

sub4_questions_part2.append({
    "id": 110,
    "topic": topic_4_8,
    "question": "একটি টাপল মেমরিতে কতটুকু স্থান নিয়েছে তা জানতে কোন ফাংশনটি ব্যবহৃত হয়?",
    "options": ["sys.getsizeof(t)", "len(t)", "sizeof(t)", "memory(t)"],
    "answer": "ক",
    "explanation": "`sys` মডিউলের `getsizeof()` যেকোনো পাইথন অবজেক্টের দখলকৃত মেমরি বাইট সংখ্যা প্রকাশ করে।"
})

# ==============================================================================
# অধ্যায় ৪.৯: সেট ডেটা স্ট্রাকচার (Questions 111 to 120)
# ==============================================================================
topic_4_9 = "অধ্যায় ৪.৯: সেট ডেটা স্ট্রাকচার (Set Structure)"

sub4_questions_part2.append({
    "id": 111,
    "topic": topic_4_9,
    "question": "পাইথনে সেট (Set) ডেটা স্ট্রাকচারের মৌলিক বৈশিষ্ট্য কোনটি?",
    "options": [
        "আন-অর্ডার্ড (Unordered), আন-ইনডেক্সড এবং ডুপ্লিকেটহীন কেবল অনন্য (Unique) উপাদান ধারণকারী",
        "অর্ডারড এবং ডুপ্লিকেট অনুমোদন করে",
        "কি-ভ্যালু জোড়া ধারণ করে",
        "ইমিউটেবল ডেটা স্ট্রাকচার"
    ],
    "answer": "ক",
    "explanation": "সেট গাণিতিক সেটের মতো অনন্য উপাদান ধারণ করে এবং এতে উপাদানের কোনো নির্দিষ্ট ক্রম বা ইনডেক্স থাকে না।"
})

sub4_questions_part2.append({
    "id": 112,
    "topic": topic_4_9,
    "question": "পাইথনে একটি সম্পূর্ণ খালি সেট (Empty Set) তৈরির সঠিক উপায় কোনটি?",
    "options": ["s = set()", "s = {}", "s = []", "s = set([])"],
    "answer": "ক",
    "explanation": "খালি কার্লি ব্র্যাকেট `{}` দিলে তা ডিকশনারি (`dict`) তৈরি করে; খালি সেট তৈরি করতে অবশ্যই `set()` লিখতে হয়।"
})

sub4_questions_part2.append({
    "id": 113,
    "topic": topic_4_9,
    "question": "একটি বিদ্যমান সেটে নতুন একটি একক উপাদান যুক্ত করার মেথড কোনটি?",
    "options": ["add(item)", "append(item)", "insert(item)", "push(item)"],
    "answer": "ক",
    "explanation": "সেটে উপাদান যোগ করার মেথড হলো `s.add(x)`।"
})

sub4_questions_part2.append({
    "id": 114,
    "topic": topic_4_9,
    "question": "সেটের মেথড `remove(x)` এবং `discard(x)` এর মধ্যে সূক্ষ্ম পার্থক্য কী?",
    "options": [
        "উপাদানটি সেটে না থাকলে `remove` KeyError ছুড়ে দেয়, কিন্তু `discard` কোনো এরর ছাড়াই শান্ত থাকে",
        "`discard` সমস্ত উপাদান মুছে দেয়",
        "`remove` কেবল প্রথম উপাদানটি মোছে",
        "উভয়ের আচরণ হুবহু এক"
    ],
    "answer": "ক",
    "explanation": "`s.discard(x)` নিরাপদ কারণ উপাদান বিদ্যমান না থাকলেও কোনো এক্সেপশন ঘটে না।"
})

sub4_questions_part2.append({
    "id": 115,
    "topic": topic_4_9,
    "question": "দুটি সেটের সংযোগ বা ইউনিয়ন (Union) করার পাইথন অপারেটর কোনটি?",
    "options": ["| (পাইপ প্রতীক)", "&", "^", "-"],
    "answer": "ক",
    "explanation": "`set1 | set2` অথবা `set1.union(set2)` উভয় সেটের সকল অনন্য উপাদান নিয়ে সংযোগ সেট গঠন করে।"
})

sub4_questions_part2.append({
    "id": 116,
    "topic": topic_4_9,
    "question": "দুটি সেটের সাধারণ উপাদান বা ইন্টারসেকশন (Intersection) পাওয়ার অপারেটর কোনটি?",
    "options": ["& (অ্যাম্পারস্যান্ড)", "|", "^", "%"],
    "answer": "ক",
    "explanation": "`set1 & set2` অথবা `set1.intersection(set2)` কেবল উভয় সেটে বিদ্যমান সাধারণ উপাদানগুলো প্রদান করে।"
})

sub4_questions_part2.append({
    "id": 117,
    "topic": topic_4_9,
    "question": "সেট বিয়োগ বা ডিফারেন্স (Difference) এর অপারেটর কোনটি?",
    "options": ["- (মাইনাস চিহ্ন)", "/", "~", "^"],
    "answer": "ক",
    "explanation": "`A - B` হলো প্রথম সেটের সেই সকল উপাদান যা দ্বিতীয় সেটে নেই।"
})

sub4_questions_part2.append({
    "id": 118,
    "topic": topic_4_9,
    "question": "সিমেট্রিক ডিফারেন্স (Symmetric Difference) অপারেশনের কাজ কী?",
    "options": [
        "উভয় সেটের কমন উপাদানগুলো বাদ দিয়ে বাকি সকল উপাদান প্রদান করা (`^` অপারেটর)",
        "কেবল কমন উপাদান দেওয়া",
        "সকল উপাদান যোগ করা",
        "প্রথম সেটের উপাদান মোছা"
    ],
    "answer": "ক",
    "explanation": "`A ^ B` হলো এমন উপাদানসমূহ যা A অথবা B এর যেকোনো একটিতে আছে কিন্তু উভয়ে নেই।"
})

sub4_questions_part2.append({
    "id": 119,
    "topic": topic_4_9,
    "question": "সেটের একটি অপরিবর্তনশীল (Immutable) রূপ যা ডিকশনারির কী বা অন্য সেটের উপাদান হিসেবে ব্যবহারযোগ্য তাকে কী বলে?",
    "options": ["frozenset", "constset", "tupleset", "staticset"],
    "answer": "ক",
    "explanation": "`frozenset()` হলো ইমিউটেবল ও হ্যাশেবল সেট যাতে উপাদান পরিবর্তন করা নিষিদ্ধ।"
})

sub4_questions_part2.append({
    "id": 120,
    "topic": topic_4_9,
    "question": "লিস্ট থেকে সমস্ত ডুপ্লিকেট উপাদান দূর করে অনন্য উপাদান পাওয়ার দ্রুততম উপায় কোনটি?",
    "options": ["list(set(my_list))", "my_list.unique()", "my_list.distinct()", "filter(my_list)"],
    "answer": "ক",
    "explanation": "লিস্টকে সেটে রূপান্তর করলে স্বয়ংক্রিয়ভাবে ডুপ্লিকেট বাদ হয়ে যায়, তারপর পুনরায় লিস্টে আনা যায়।"
})

# ==============================================================================
# অধ্যায় ৪.১০: ডিকশনারি ডেটা স্ট্রাকচার (Questions 121 to 135)
# ==============================================================================
topic_4_10 = "অধ্যায় ৪.১০: ডিকশনারি ডেটা স্ট্রাকচার (Dictionary Structure)"

sub4_questions_part2.append({
    "id": 121,
    "topic": topic_4_10,
    "question": "পাইথনে ডিকশনারি (Dictionary) ডেটা স্ট্রাকচার কীভাবে উপাত্ত সংরক্ষণ করে?",
    "options": [
        "কী-মান জোড়া (Key-Value Pair) হিসেবে, যেখানে কী অনন্য ও ইমিউটেবল",
        "শুধুমাত্র ইনডেক্স অনুযায়ী",
        "সিরিয়াল বাইনারি আকারে",
        "ট্রি ডেটা স্ট্রাকচার আকারে"
    ],
    "answer": "ক",
    "explanation": "ডিকশনারি হ্যাশ টেবিল নীতিতে প্রতিটি অনন্য কী-এর সাথে সংশ্লিষ্ট মান সংরক্ষণ করে।"
})

sub4_questions_part2.append({
    "id": 122,
    "topic": topic_4_10,
    "question": "পাইথন ৩.৭ থেকে ডিকশনারির উপাদানের ক্রমের ক্ষেত্রে কোন আনুষ্ঠানিক গ্যারান্টি দেওয়া হয়েছে?",
    "options": [
        "ইনসার্শন অর্ডার বজায় থাকে (Insertion order is guaranteed)",
        "উপাদানগুলো স্বয়ংক্রিয়ভাবে সর্টেড থাকে",
        "সম্পূর্ণ র‍্যান্ডম থাকে",
        "রিভার্স অর্ডারে থাকে"
    ],
    "answer": "ক",
    "explanation": "পাইথন ৩.৭ থেকে ডিকশনারি উপাদান ঢোকানোর মূল ক্রম অক্ষুণ্ণ রাখার বিষয়টি ভাষার স্থায়ী বৈশিষ্ট্য হিসেবে নির্ধারণ করা হয়।"
})

sub4_questions_part2.append({
    "id": 123,
    "topic": topic_4_10,
    "question": "ডিকশনারির কোনো কী খুঁজতে গিয়ে কী না থাকলে এরর এড়াতে নিরাপদ মেথড কোনটি?",
    "options": ["dict.get(key, default)", "dict[key]", "dict.find(key)", "dict.search(key)"],
    "answer": "ক",
    "explanation": "`d[key]` দিলে কি না থাকলে `KeyError` হয়; কিন্তু `d.get(key, 'default')` দিলে এরর না দিয়ে ডিফল্ট মান দেয়।"
})

sub4_questions_part2.append({
    "id": 124,
    "topic": topic_4_10,
    "question": "ডিকশনারি থেকে নির্দিষ্ট কী মুছে ফেলে তার মানটি ফেরত পাওয়ার মেথড কোনটি?",
    "options": ["dict.pop(key)", "dict.remove(key)", "del dict[key]", "dict.discard(key)"],
    "answer": "ক",
    "explanation": "`d.pop('name')` উপাদানটি ডিকশনারি থেকে ডিলিট করে তার ভ্যালুটি রিটার্ন করে।"
})

sub4_questions_part2.append({
    "id": 125,
    "topic": topic_4_10,
    "question": "ডিকশনারির সর্বশেষ যুক্ত হওয়া কী-ভ্যালু জোড়া মুছে ফেলার (LIFO ক্রম) মেথড কোনটি?",
    "options": ["dict.popitem()", "dict.pop()", "dict.delete_last()", "dict.remove_item()"],
    "answer": "ক",
    "explanation": "`d.popitem()` শেষ ইনসার্ট করা `(key, value)` টাপলটি রিমুভ করে রিটার্ন করে।"
})

sub4_questions_part2.append({
    "id": 126,
    "topic": topic_4_10,
    "question": "ডিকশনারির সকল কী ও মানের জোড়াকে টাপল আকারে পাওয়ার মেথড কোনটি?",
    "options": ["dict.items()", "dict.keys()", "dict.values()", "dict.pairs()"],
    "answer": "ক",
    "explanation": "`d.items()` একটি ডিকশনারি ভিউ দেয় যাতে `[(key1, val1), (key2, val2)]` থাকে।"
})

sub4_questions_part2.append({
    "id": 127,
    "topic": topic_4_10,
    "question": "একটি বিদ্যমান ডিকশনারিতে অন্য একটি ডিকশনারির উপাদানসমূহ মার্জ বা আপডেট করার মেথড কোনটি?",
    "options": ["dict.update(other_dict)", "dict.merge()", "dict.append()", "dict.add()"],
    "answer": "ক",
    "explanation": "`d1.update(d2)` d1-এর ভেতরে d2-এর কী-ভ্যালু জোড়া সংযোজন বা ওভাররাইট করে।"
})

sub4_questions_part2.append({
    "id": 128,
    "topic": topic_4_10,
    "question": "পাইথন ৩.৯ এ দুটি ডিকশনারি মার্জ করার জন্য কোন নতুন অপারেটর যুক্ত করা হয়?",
    "options": ["| (যেমন: d3 = d1 | d2)", "+", "&", "**"],
    "answer": "ক",
    "explanation": "পাইথন ৩.৯ থেকে ডিকশনারি ইউনিয়ন বা মার্জ করার জন্য `|` এবং ইন-প্লেস আপডেটের জন্য `|=` অপারেটর যোগ করা হয়।"
})

sub4_questions_part2.append({
    "id": 129,
    "topic": topic_4_10,
    "question": "যদি ডিকশনারিতে নির্দিষ্ট কোনো কী বিদ্যমান না থাকে তবে ডিফল্ট মান সেট করা এবং বিদ্যমান থাকলে বর্তমান মান পাওয়ার মেথড কোনটি?",
    "options": ["dict.setdefault(key, default)", "dict.get()", "dict.add_default()", "dict.insert()"],
    "answer": "ক",
    "explanation": "`d.setdefault(k, 0)` কি না থাকলে মান ০ সেট করে ০ দেয়, আর কি থাকলে আগের মান অক্ষুণ্ণ রেখে তা রিটার্ন করে।"
})

sub4_questions_part2.append({
    "id": 130,
    "topic": topic_4_10,
    "question": "ডিকশনারি কম্প্রিহেনশনের (Dictionary Comprehension) সঠিক উদাহরণ কোনটি?",
    "options": ["{x: x**2 for x in range(5)}", "[x: x**2 for x in range(5)]", "(x: x**2 for x in range(5))", "{x, x**2 for x in range(5)}"],
    "answer": "ক",
    "explanation": "কার্লি ব্র্যাকেটে `{key: value for item in iterable}` সিনট্যাক্স দিয়ে ডিকশনারি কম্প্রিহেনশন হয়।"
})

sub4_questions_part2.append({
    "id": 131,
    "topic": topic_4_10,
    "question": "নিচের কোনটি পাইথনে ডিকশনারির 'কী' হিসেবে ব্যবহার করা সম্পূর্ণ নিষিদ্ধ?",
    "options": ["লিস্ট [1, 2, 3]", "স্ট্রিং \"name\"", "টাপল (1, 2)", "পূর্ণসংখ্যা 42"],
    "answer": "ক",
    "explanation": "লিস্ট একটি মিউটেবল অবজেক্ট যা হ্যাশেবল নয় (Unhashable type: 'list'), তাই এটি কী হতে পারে না।"
})

sub4_questions_part2.append({
    "id": 132,
    "topic": topic_4_10,
    "question": "কী অনুপস্থিত থাকলে স্বয়ংক্রিয়ভাবে ডিফল্ট টাইপ ইনিশিয়ালাইজ করার স্ট্যান্ডার্ড কালেকশন ক্লাস কোনটি?",
    "options": ["collections.defaultdict", "collections.Counter", "collections.OrderedDict", "dict.default()"],
    "answer": "ক",
    "explanation": "`defaultdict(int)` বা `defaultdict(list)` অনুপস্থিত কী-তে কল করলে স্বয়ংক্রিয়ভাবে 0 বা [] তৈরি করে নেয়।"
})

sub4_questions_part2.append({
    "id": 133,
    "topic": topic_4_10,
    "question": "যেকোনো ইটারেবলের উপাদানসমূহের পৌনঃপুনিকতা (Frequency count) সহজে বের করতে কোন ক্লাস ব্যবহৃত হয়?",
    "options": ["collections.Counter", "collections.defaultdict", "dict.count()", "math.frequency()"],
    "answer": "ক",
    "explanation": "`Counter(['a', 'b', 'a'])` একটি বিশেষ ডিকশনারি যাতে উপাদান ও তাদের সংখ্যা সংরক্ষিত হয়।"
})

sub4_questions_part2.append({
    "id": 134,
    "topic": topic_4_10,
    "question": "ডিকশনারির সমস্ত কী-এর ওপর লুপ চালানোর ডিফল্ট সিনট্যাক্স কোনটি?",
    "options": ["for k in my_dict:", "for k in my_dict.all():", "for k, v in my_dict:", "for k in keys(my_dict):"],
    "answer": "ক",
    "explanation": "ডিকশনারিকে সরাসরি ইটারেট করলে ডিফল্টভাবে কেবল তার 'কী' (Keys) গুলো পাওয়া যায়।"
})

sub4_questions_part2.append({
    "id": 135,
    "topic": topic_4_10,
    "question": "দুটি তালিকা (কী তালিকা এবং মান তালিকা) থেকে একটি পূর্ণাঙ্গ ডিকশনারি বানানোর পাইথনিক উপায় কোনটি?",
    "options": ["dict(zip(keys_list, values_list))", "zip(dict(keys, values))", "dict.merge(keys, values)", "combine(keys, values)"],
    "answer": "ক",
    "explanation": "`zip` উপাদানগুলোকে জোড়া বানায় এবং `dict()` তাকে সরাসরি ডিকশনারিতে রূপান্তর করে।"
})

# ==============================================================================
# অধ্যায় ৪.১১: ফাংশন অপারেশন ও মডিউল (Questions 136 to 155)
# ==============================================================================
topic_4_11 = "অধ্যায় ৪.১১: ফাংশন অপারেশন ও মডিউল (Function Operation & Modules)"

sub4_questions_part2.append({
    "id": 136,
    "topic": topic_4_11,
    "question": "পাইথনে ফাংশন সংজ্ঞায়িত করার জন্য কোন কিওয়ার্ড ব্যবহৃত হয়?",
    "options": ["def", "function", "fn", "define"],
    "answer": "ক",
    "explanation": "পাইথনে ফাংশন তৈরির মূল কীওয়ার্ড হলো `def` (Definition)।"
})

sub4_questions_part2.append({
    "id": 137,
    "topic": topic_4_11,
    "question": "পাইথনে প্যারামিটার পাসিং মেকানিজমকে প্রযুক্তিগতভাবে কী বলা হয়?",
    "options": [
        "পাস বাই অবজেক্ট রেফারেন্স বা কল বাই শেয়ারিং (Pass by Object Reference)",
        "বিশুদ্ধ কল বাই ভ্যালু",
        "বিশুদ্ধ কল বাই রেফারেন্স",
        "পাস বাই নেম"
    ],
    "answer": "ক",
    "explanation": "অবজেক্টের মেমরি রেফারেন্স পাস হয়; অবজেক্ট মিউটেবল হলে ভেতরের পরিবর্তন মূল অবজেক্টে দেখা যায়, কিন্তু নতুন মান রি-অ্যাসাইন করলে পরিবর্তন হয় না।"
})

sub4_questions_part2.append({
    "id": 138,
    "topic": topic_4_11,
    "question": "পাইথনে অনির্দিষ্ট সংখ্যক পজিশনাল আর্গুমেন্ট গ্রহণের জন্য ফাংশন প্যারামিটারে কী ব্যবহৃত হয়?",
    "options": ["*args (যা একটি টাপল হিসেবে গৃহীত হয়)", "**kwargs", "*kwargs", "&args"],
    "answer": "ক",
    "explanation": "`*args` যেকোনো সংখ্যক সাধারণ আর্গুমেন্টকে একটি একক টাপলে আবদ্ধ করে ফাংশনে প্রদান করে।"
})

sub4_questions_part2.append({
    "id": 139,
    "topic": topic_4_11,
    "question": "পাইথনে অনির্দিষ্ট সংখ্যক কীওয়ার্ড আর্গুমেন্ট (Named arguments) গ্রহণের জন্য কী ব্যবহৃত হয়?",
    "options": ["**kwargs (যা একটি ডিকশনারি হিসেবে গৃহীত হয়)", "*kwargs", "*args", "&kwargs"],
    "answer": "ক",
    "explanation": "`**kwargs` প্যারামিটারগুলোকে কি-ভ্যালু জোড়া হিসেবে ডিকশনারির আকারে গ্রহণ করে।"
})

sub4_questions_part2.append({
    "id": 140,
    "topic": topic_4_11,
    "question": "পাইথনে ডিফল্ট আর্গুমেন্ট (Default Argument) লেখার ক্ষেত্রে কোন নিয়মটি বাধ্যতামূলক?",
    "options": [
        "ডিফল্ট আর্গুমেন্ট সর্বদা নন-ডিফল্ট আর্গুমেন্টের পরে বসতে হবে",
        "ডিফল্ট আর্গুমেন্ট সবার প্রথমে থাকতে হবে",
        "যেকোনো স্থানে বসানো যায়",
        "ডিফল্ট আর্গুমেন্ট কেবল একটিই হতে পারে"
    ],
    "answer": "ক",
    "explanation": "নন-ডিফল্ট প্যারামিটারের আগে ডিফল্ট প্যারামিটার দিলে `SyntaxError: non-default argument follows default argument` ঘটে।"
})

sub4_questions_part2.append({
    "id": 141,
    "topic": topic_4_11,
    "question": "ফাংশন প্যারামিটারে ডিফল্ট মান হিসেবে মিউটেবল অবজেক্ট (যেমন `def f(x=[]):`) ব্যবহারের বিপজ্জনক ফল কোনটি?",
    "options": [
        "পরবর্তী প্রতিটি ফাংশন কলে পূর্ববর্তী কলের ডেটা ওই ডিফল্ট লিস্টে সংরক্ষিত থেকে যায় (ভাগাভাগি হয়)",
        "প্রতিবার নতুন খালি লিস্ট তৈরি হয়",
        "কম্পাইল এরর প্রদর্শন করে",
        "ফাংশন ক্র্যাশ করে"
    ],
    "answer": "ক",
    "explanation": "ডিফল্ট আর্গুমেন্ট কেবল ফাংশন সংজ্ঞায়নের সময় একবার তৈরি হয়; তাই মিউটেবল ডিফল্টের বদলে `None` ব্যবহার করা আদর্শ।"
})

sub4_questions_part2.append({
    "id": 142,
    "topic": topic_4_11,
    "question": "ফাংশনের ভেতর থেকে গ্লোবাল ভ্যারিয়েবলের মান পরিবর্তন করতে কোন কীওয়ার্ড ঘোষণা করতে হয়?",
    "options": ["global", "extern", "public", "nonlocal"],
    "answer": "ক",
    "explanation": "`global x` ঘোষণা না করে ফাংশনে `x = 5` লিখলে পাইথন তাকে নতুন লোকাল ভ্যারিয়েবল গণ্য করে।"
})

sub4_questions_part2.append({
    "id": 143,
    "topic": topic_4_11,
    "question": "নেস্টেড ফাংশনে তার বাইরের এনক্লোজিং স্কোপের ভ্যারিয়েবল মডিফাই করতে কোন কীওয়ার্ড ব্যবহৃত হয়?",
    "options": ["nonlocal", "global", "parent", "outer"],
    "answer": "ক",
    "explanation": "ক্লোজার বা নেস্টেড ফাংশনে বাইরের অবজেক্ট পরিবর্তন করতে পাইথন ৩-এ `nonlocal` যুক্ত করা হয়।"
})

sub4_questions_part2.append({
    "id": 144,
    "topic": topic_4_11,
    "question": "পাইথনে ভ্যারিয়েবলের স্কোপ অনুসন্ধানের নিয়ম (Scope Resolution Rule) কোনটি?",
    "options": ["LEGB নিয়ম (Local -> Enclosing -> Global -> Built-in)", "BLEG নিয়ম", "LIFO নিয়ম", "FIFO নিয়ম"],
    "answer": "ক",
    "explanation": "পাইথন প্রথমে লোকাল, তারপর এনক্লোজিং, তারপর গ্লোবাল এবং সর্বশেষ বিল্ট-ইন নেমস্পেসে ভ্যারিয়েবল খোঁজে।"
})

sub4_questions_part2.append({
    "id": 145,
    "topic": topic_4_11,
    "question": "পাইথনে এক লাইনে লেখা নামহীন ছোট ফাংশনকে (Anonymous Function) কী বলে?",
    "options": ["ল্যাম্বডা ফাংশন (Lambda Function)", "ম্যাক্রো ফাংশন", "ইনলাইন ফাংশন", "ডেকোরেটর"],
    "answer": "ক",
    "explanation": "`lambda x, y: x + y` সিনট্যাক্স দিয়ে সংক্ষিপ্ত অন-দ্য-ফ্লাই ফাংশন তৈরি করা যায়।"
})

sub4_questions_part2.append({
    "id": 146,
    "topic": topic_4_11,
    "question": "যেকোনো ইটারেবলের প্রতিটি উপাদানের ওপর নির্দিষ্ট কোনো ফাংশন প্রয়োগ করে ফলাফল পেতে কোনটি ব্যবহৃত হয়?",
    "options": ["map(func, iterable)", "filter()", "reduce()", "apply()"],
    "answer": "ক",
    "explanation": "`map(lambda x: x*2, [1, 2, 3])` প্রতিটি উপাদানকে দ্বিগুণ করে [2, 4, 6] এর ইটারেটর দেয়।"
})

sub4_questions_part2.append({
    "id": 147,
    "topic": topic_4_11,
    "question": "ইটারেবলের কেবল সেই সকল উপাদান ফিল্টার করে নেওয়া যেগুলোর ক্ষেত্রে প্রদত্ত শর্ত সত্য হয় তা কার কাজ?",
    "options": ["filter(func, iterable)", "map()", "reduce()", "clean()"],
    "answer": "ক",
    "explanation": "`filter()` বুলিয়ান রিটার্নকারী ফাংশন প্রয়োগ করে সত্য উপাদানগুলো বজায় রাখে।"
})

sub4_questions_part2.append({
    "id": 148,
    "topic": topic_4_11,
    "question": "ইটারেবলের সকল উপাদানকে ক্রমপুঞ্জিতভাবে একটি একক মানে পরিণত করার ফাংশন `reduce()` কোন মডিউলে থাকে?",
    "options": ["functools", "itertools", "math", "builtins"],
    "answer": "ক",
    "explanation": "পাইথন ৩-এ `reduce()` কে বিল্ট-ইন থেকে সরিয়ে `functools.reduce` এ স্থানান্তরিত করা হয়।"
})

sub4_questions_part2.append({
    "id": 149,
    "topic": topic_4_11,
    "question": "অন্য একটি ফাংশনকে আর্গুমেন্ট হিসেবে গ্রহণ করে তার আচরণ সম্প্রসারণকারী ফাংশনকে কী বলে?",
    "options": ["ডেকোরেটর (Decorator)", "ল্যাম্বডা", "কনস্ট্রাক্টর", "ইটারেটর"],
    "answer": "ক",
    "explanation": "ডেকোরেটর (`@decorator_name`) মূল কোডে হাত না দিয়ে ফাংশনের ক্ষমতা বৃদ্ধি বা লগিং ইত্যাদিতে ব্যবহৃত হয়।"
})

sub4_questions_part2.append({
    "id": 150,
    "topic": topic_4_11,
    "question": "যে ফাংশন সম্পূর্ণ ফলাফল একসাথে মেমরিতে না রেখে `yield` স্টেটমেন্ট দিয়ে একের পর এক ভ্যালু জেনারেট করে তাকে কী বলে?",
    "options": ["জেনারেটর ফাংশন (Generator Function)", "ল্যাম্বডা ফাংশন", "রিকার্সিভ ফাংশন", "পাসিভ ফাংশন"],
    "answer": "ক",
    "explanation": "জেনারেটর `yield` দিয়ে স্টেট ধরে রাখে এবং মেমরি অত্যন্ত সাশ্রয় করে বিশাল ডেটাসেট তৈরি করতে পারে।"
})

sub4_questions_part2.append({
    "id": 151,
    "topic": topic_4_11,
    "question": "জেনারেটর অবজেক্ট থেকে পরবর্তী মানটি পাওয়ার জন্য কোন বিল্ট-ইন ফাংশন কল করতে হয়?",
    "options": ["next(gen)", "gen.get()", "gen.step()", "yield(gen)"],
    "answer": "ক",
    "explanation": "`next(gen)` জেনারেটরের পরবর্তী `yield` মান দেয় এবং মান শেষ হলে `StopIteration` এরর ঘটে।"
})

sub4_questions_part2.append({
    "id": 152,
    "topic": topic_4_11,
    "question": "একটি পাইথন স্ক্রিপ্ট সরাসরি রান করা হয়েছে নাকি অন্য ফাইলে ইমপোর্ট করা হয়েছে তা যাচাই করার শর্ত কোনটি?",
    "options": ["if __name__ == '__main__':", "if __main__ == True:", "if name == 'main':", "if __run__ == 1:"],
    "answer": "ক",
    "explanation": "ফাইলটি সরাসরি টার্মিনালে চালালে `__name__` এর মান হয় `'__main__'`, আর ইমপোর্ট করলে মডিউলের নিজস্ব নাম ধারণ করে।"
})

sub4_questions_part2.append({
    "id": 153,
    "topic": topic_4_11,
    "question": "একটি ডিরেক্টরিকে পাইথনের প্রাতিষ্ঠানিক প্যাকেজ হিসেবে চিহ্নিত করতে ঐতিহ্যগতভাবে কোন ফাইল রাখা হতো?",
    "options": ["__init__.py", "__main__.py", "__package__.py", "setup.py"],
    "answer": "ক",
    "explanation": "`__init__.py` ফাইলটি ডিরেক্টরিটিকে প্যাকেজ হিসেবে ঘোষণা করে এবং প্যাকেজ লোডের ইনিশিয়ালাইজেশন করে।"
})

sub4_questions_part2.append({
    "id": 154,
    "topic": topic_4_11,
    "question": "বর্তমান সিস্টেমের তারিখ ও সময় পেতে `datetime` মডিউলের সঠিক কোড কোনটি?",
    "options": ["datetime.datetime.now()", "datetime.today_now()", "time.current()", "date.get_now()"],
    "answer": "ক",
    "explanation": "`from datetime import datetime; datetime.now()` বর্তমান তারিখ ও স্থানীয় সময় অবজেক্ট দেয়।"
})

sub4_questions_part2.append({
    "id": 155,
    "topic": topic_4_11,
    "question": "`datetime` অবজেক্টকে নির্দিষ্ট ফরম্যাটের স্ট্রিংয়ে পরিণত করার এবং স্ট্রিং থেকে ডেট অবজেক্ট বানানোর মেথড দুটি কোনটি?",
    "options": [
        "strftime() (Format to String) এবং strptime() (Parse from String)",
        "format() এবং parse()",
        "toString() এবং toDate()",
        "date_format() এবং date_parse()"
    ],
    "answer": "ক",
    "explanation": "`strftime` (String Format Time) টেক্সট বানায় এবং `strptime` (String Parse Time) টেক্সটকে অবজেক্ট বানায়।"
})

# ==============================================================================
# অধ্যায় ৪.১২: ফাইল আই/ও অপারেশন (Questions 156 to 170)
# ==============================================================================
topic_4_12 = "অধ্যায় ৪.১২: ফাইল আই/ও অপারেশন (Files I/O Operation)"

sub4_questions_part2.append({
    "id": 156,
    "topic": topic_4_12,
    "question": "পাইথনে কোনো ফাইল ওপেন করার স্ট্যান্ডার্ড বিল্ট-ইন ফাংশন কোনটি?",
    "options": ["open(filename, mode)", "file.open()", "load_file()", "read_file()"],
    "answer": "ক",
    "explanation": "`open('data.txt', 'r')` ফাইল হ্যান্ডলার অবজেক্ট রিটার্ন করে।"
})

sub4_questions_part2.append({
    "id": 157,
    "topic": topic_4_12,
    "question": "ফাইল খোলার পর কাজ শেষে স্বয়ংক্রিয়ভাবে ক্লোজ নিশ্চিত করতে এবং এক্সেপশন প্রতিরোধে কোন কনটেক্সট ম্যানেজার ব্যবহৃত হয়?",
    "options": ["with open(...) as f:", "try open(...) as f:", "using open(...) as f:", "auto open(...) as f:"],
    "answer": "ক",
    "explanation": "`with` স্টেটমেন্ট Context Management Protocol (`__enter__` ও `__exit__`) মেনে ফাইল অটোমেটিক ক্লোজ করে।"
})

sub4_questions_part2.append({
    "id": 158,
    "topic": topic_4_12,
    "question": "বিদ্যমান ফাইলের কনটেন্ট না মুছে তার একদম শেষে নতুন লেখা যোগ করার ফাইল ওপেনিং মোড কোনটি?",
    "options": ["'a' (Append mode)", "'w' (Write mode)", "'r' (Read mode)", "'x' (Exclusive mode)"],
    "answer": "ক",
    "explanation": "`'a'` মোড পয়েন্টারকে ফাইলের শেষে রাখে এবং নতুন ডেটা অ্যাপেন্ড করে।"
})

sub4_questions_part2.append({
    "id": 159,
    "topic": topic_4_12,
    "question": "ফাইলটি ডিস্কে আগে থেকেই বিদ্যমান থাকলে এরর তৈরি করে নতুন ফাইল খোলার এক্সক্লুসিভ ক্রিয়েশন মোড কোনটি?",
    "options": ["'x' (Exclusive creation)", "'w'", "'a'", "'r'"],
    "answer": "ক",
    "explanation": "`'x'` মোড কেবল তখনই ফাইল তৈরি করে যদি ফাইলটি আগে থেকে না থাকে; ফাইল থাকলে `FileExistsError` দেয়।"
})

sub4_questions_part2.append({
    "id": 160,
    "topic": topic_4_12,
    "question": "একটি বড় টেক্সট ফাইলের প্রতিটি লাইন মেমরি-সাশ্রয়ী উপায়ে লাইন বাই লাইন পড়ার পাইথনিক নিয়ম কোনটি?",
    "options": ["for line in file:", "file.read().splitlines()", "file.readlines()", "while file.read():"],
    "answer": "ক",
    "explanation": "`for line in f:` সম্পূর্ণ ফাইল একসাথে র্যামে না এনে ইটারেটর হিসেবে একটি একটি করে লাইন লোড করে।"
})

sub4_questions_part2.append({
    "id": 161,
    "topic": topic_4_12,
    "question": "ফাইলের সমস্ত লাইন পড়ে একটি স্ট্রিংয়ের লিস্ট আকারে পাওয়ার মেথড কোনটি?",
    "options": ["file.readlines()", "file.read()", "file.readline()", "file.getlines()"],
    "answer": "ক",
    "explanation": "`readlines()` প্রতিটি লাইনকে একক উপাদান হিসেবে নিয়ে একটি পূর্ণাঙ্গ লিস্ট প্রদান করে।"
})

sub4_questions_part2.append({
    "id": 162,
    "topic": topic_4_12,
    "question": "ফাইলের কার্সরের বর্তমান বাইট পজিশন জানার মেথড কোনটি?",
    "options": ["file.tell()", "file.seek()", "file.pos()", "file.loc()"],
    "answer": "ক",
    "explanation": "`file.tell()` ফাইল পয়েন্টারটির বর্তমান অবস্থান নির্দেশ করে।"
})

sub4_questions_part2.append({
    "id": 163,
    "topic": topic_4_12,
    "question": "ফাইল পয়েন্টারকে ফাইলের একদম শুরুতে (০ বাইটে) নিয়ে যাওয়ার নির্দেশ কোনটি?",
    "options": ["file.seek(0)", "file.tell(0)", "file.rewind()", "file.reset()"],
    "answer": "ক",
    "explanation": "`file.seek(offset)` কার্সরকে নির্দিষ্ট অফসেটে সরায়; `seek(0)` শুরুতে নিয়ে যায়।"
})

sub4_questions_part2.append({
    "id": 164,
    "topic": topic_4_12,
    "question": "ছবি, অডিও বা পিডিএফের মতো নন-টেক্সট বাইনারি ফাইল খোলার জন্য মোডের সাথে কোন অক্ষর যুক্ত করতে হয়?",
    "options": ["'b' (যেমন: 'rb', 'wb')", "'t'", "'bin'", "'raw'"],
    "answer": "ক",
    "explanation": "বাইনারি মোড `'rb'` বা `'wb'` কোনো এনকোডিং ছাড়াই সরাসরি র বাইট অবজেক্ট প্রসেস করে।"
})

sub4_questions_part2.append({
    "id": 165,
    "topic": topic_4_12,
    "question": "পাইথনে কোনো ফাইল ডিস্ক থেকে মুছে ফেলার ফাংশন কোনটি?",
    "options": ["os.remove(filename) বা os.unlink()", "os.delete()", "file.delete()", "os.erase()"],
    "answer": "ক",
    "explanation": "`os` মডিউলের `remove()` অথবা `unlink()` দিয়ে ডিস্ক থেকে নির্দিষ্ট ফাইল ডিলিট করা হয়।"
})

sub4_questions_part2.append({
    "id": 166,
    "topic": topic_4_12,
    "question": "নির্দিষ্ট কোনো ফাইল বা ফোল্ডার ডিস্কে বিদ্যমান আছে কিনা তা পরীক্ষা করার মেথড কোনটি?",
    "options": ["os.path.exists(path)", "os.is_file()", "os.check()", "path.find()"],
    "answer": "ক",
    "explanation": "`os.path.exists(path)` ফাইল বা ফোল্ডার উপস্থিত থাকলে `True` দেয়।"
})

sub4_questions_part2.append({
    "id": 167,
    "topic": topic_4_12,
    "question": "অপারেটিং সিস্টেম নিরপেক্ষভাবে একাধিক ডিরেক্টরি পাথ যুক্ত করার নিরাপদ ফাংশন কোনটি?",
    "options": ["os.path.join(dir, file)", "dir + '/' + file", "dir + '\\' + file", "os.concat()"],
    "answer": "ক",
    "explanation": "`os.path.join()` উইন্ডোজের ব্যাকস্ল্যাশ এবং লিনাক্সের ফরওয়ার্ড স্ল্যাশ স্বয়ংক্রিয়ভাবে সমন্বয় করে।"
})

sub4_questions_part2.append({
    "id": 168,
    "topic": topic_4_12,
    "question": "পাইথনে অবজেক্ট সিরিয়ালাইজেশন বা বাইনারি সংরক্ষণের বিল্ট-ইন মডিউল কোনটি?",
    "options": ["pickle মডিউল", "json মডিউল", "marshal", "serialize"],
    "answer": "ক",
    "explanation": "`pickle.dump()` পাইথন অবজেক্টকে বাইট স্ট্রিমে রূপান্তর করে এবং `pickle.load()` দ্বারা ফিরিয়ে আনে।"
})

sub4_questions_part2.append({
    "id": 169,
    "topic": topic_4_12,
    "question": "ফাইল থেকে রিড করার সময় যদি ফাইলটি না থাকে তবে কোন নির্দিষ্ট এক্সেপশন ঘটে?",
    "options": ["FileNotFoundError", "IOError", "FileMissingException", "PathError"],
    "answer": "ক",
    "explanation": "অনুপস্থিত ফাইল রিড মোডে ওপেন করলে `FileNotFoundError` (বা OSError) নিক্ষেপ হয়।"
})

sub4_questions_part2.append({
    "id": 170,
    "topic": topic_4_12,
    "question": "ফাইল অবজেক্টে `write()` মেথড সফলভাবে সম্পন্ন হওয়ার পর কী রিটার্ন করে?",
    "options": [
        "ফাইলে লেখা মোট অক্ষরের (Characters/Bytes) সংখ্যা",
        "True",
        "None",
        "ফাইলের নতুন সাইজ"
    ],
    "answer": "ক",
    "explanation": "পাইথন ৩-এ `f.write('abc')` মেথড ফাইলে মোট যতটি ক্যারেক্টার লেখা হয়েছে সেই সংখ্যাটি রিটার্ন করে।"
})

# ==============================================================================
# অধ্যায় ৪.১৩: অবজেক্ট ওরিয়েন্টেড পাইথন (Questions 171 to 190)
# ==============================================================================
topic_4_13 = "অধ্যায় ৪.১৩: অবজেক্ট ওরিয়েন্টেড পাইথন (Object-Oriented Python)"

sub4_questions_part2.append({
    "id": 171,
    "topic": topic_4_13,
    "question": "পাইথনে কোনো ক্লাসের ইনস্ট্যান্স তৈরির সময় স্বয়ংক্রিয়ভাবে ইনিশিয়ালাইজ করার কনস্ট্রাক্টর মেথড কোনটি?",
    "options": ["__init__(self)", "__new__(self)", "__create__(self)", "__construct__(self)"],
    "answer": "ক",
    "explanation": "`__init__` হলো পাইথনের ডান্ডার মেথড যা নতুন অবজেক্ট তৈরির পর তার ইনিশিয়াল অ্যাট্রিবিউট সেট করে।"
})

sub4_questions_part2.append({
    "id": 172,
    "topic": topic_4_13,
    "question": "ইনস্ট্যান্স মেথডের প্রথম প্যারামিটার হিসেবে প্রচলিত `self` মূলত কী নির্দেশ করে?",
    "options": [
        "যে অবজেক্টটি মেথডটিকে কল করছে তার নিজস্ব বর্তমান ইনস্ট্যান্স রেফারেন্স",
        "ক্লাসের মেমরি অ্যাড্রেস",
        "গ্লোবাল ভ্যারিয়েবল",
        "প্যারেন্ট ক্লাসের রেফারেন্স"
    ],
    "answer": "ক",
    "explanation": "`self` হলো পাইথনের সেই কনভেনশন যার মাধ্যমে অবজেক্টের নিজস্ব অ্যাট্রিবিউট ও মেথড অ্যাক্সেস করা যায়।"
})

sub4_questions_part2.append({
    "id": 173,
    "topic": topic_4_13,
    "question": "ক্লাসের বডিতে সরাসরি ঘোষিত ভ্যারিয়েবল (যা ক্লাসের সকল অবজেক্টের মধ্যে শেয়ার হয়) তাকে কী বলে?",
    "options": ["ক্লাস বা স্ট্যাটিক ভ্যারিয়েবল (Class / Static Variable)", "ইনস্ট্যান্স ভ্যারিয়েবল", "লোকাল ভ্যারিয়েবল", "গ্লোবাল ভ্যারিয়েবল"],
    "answer": "ক",
    "explanation": "ক্লাস ভ্যারিয়েবল মেমরিতে একবার থাকে এবং সকল ইনস্ট্যান্স তা শেয়ার করে; আর `self.x` হলো প্রতিটি অবজেক্টের পৃথক ইনস্ট্যান্স ভ্যারিয়েবল।"
})

sub4_questions_part2.append({
    "id": 174,
    "topic": topic_4_13,
    "question": "যে মেথড অবজেক্ট নয় বরং স্বয়ং ক্লাসকে প্রথম প্যারামিটার (`cls`) হিসেবে গ্রহণ করে তাকে কী বলে?",
    "options": ["ক্লাস মেথড (@classmethod)", "স্ট্যাটিক মেথড (@staticmethod)", "ইনস্ট্যান্স মেথড", "অ্যাবস্ট্রাক্ট মেথড"],
    "answer": "ক",
    "explanation": "`@classmethod` ডেকোরেটরযুক্ত মেথড `cls` প্যারামিটার নেয় এবং অল্টারনেটিভ কনস্ট্রাক্টর হিসেবে জনপ্রিয়।"
})

sub4_questions_part2.append({
    "id": 175,
    "topic": topic_4_13,
    "question": "যে মেথড কোনো `self` বা `cls` গ্রহণ করে না, সাধারণ ফাংশনের মতো আচরণ করে তাকে কী বলে?",
    "options": ["স্ট্যাটিক মেথড (@staticmethod)", "ক্লাস মেথড", "ইনস্ট্যান্স মেথড", "প্রাইভেট মেথড"],
    "answer": "ক",
    "explanation": "`@staticmethod` ক্লাসের নেমস্পেসে থাকা ইউটিলিটি ফাংশন যা অবজেক্ট বা ক্লাসের স্টেট নিয়ে কাজ করে না।"
})

sub4_questions_part2.append({
    "id": 176,
    "topic": topic_4_13,
    "question": "পাইথনে কোনো অ্যাট্রিবিউটকে প্রাইভেট (Private) করার জন্য নেম ম্যাংলিং (Name Mangling) মেকানিজম কোনটি?",
    "options": ["ডাবল আন্ডারস্কোর প্রিফিক্স `__var`", "সিঙ্গেল আন্ডারস্কোর `_var`", "private কিওয়ার্ড", "final কিওয়ার্ড"],
    "answer": "ক",
    "explanation": "`__var` দিলে পাইথন তার নাম বদলে `_ClassName__var` করে দেয়, ফলে বাইরে থেকে সরাসরি ওভাররাইট বা অ্যাক্সেস রোধ হয়।"
})

sub4_questions_part2.append({
    "id": 177,
    "topic": topic_4_13,
    "question": "মেথডকে সাধারণ ভ্যারিয়েবলের মতো রিড ও গেটার-সেটার নিয়ন্ত্রণের সুযোগ দেয় কোন ডেকোরেটর?",
    "options": ["@property এবং @var.setter", "@getter", "@attribute", "@accessor"],
    "answer": "ক",
    "explanation": "`@property` মেথডকে ফিল্ডের মতো সিনট্যাক্সে (`obj.x`) পড়ার অনুমতি দেয় এবং এনক্যাপসুলেশন নিশ্চিত করে।"
})

sub4_questions_part2.append({
    "id": 178,
    "topic": topic_4_13,
    "question": "চাইল্ড ক্লাসের ভেতর থেকে প্যারেন্ট ক্লাসের মেথড বা কনস্ট্রাক্টর কল করার ফাংশন কোনটি?",
    "options": ["super()", "parent()", "base()", "this()"],
    "answer": "ক",
    "explanation": "`super().__init__()` মেথড রেজোলিউশন অর্ডার অনুযায়ী প্যারেন্ট ক্লাসের ইনিশিয়ালাইজার কার্যকর করে।"
})

sub4_questions_part2.append({
    "id": 179,
    "topic": topic_4_13,
    "question": "পাইথনে মাল্টিপল ইনহেরিটেন্সের ক্ষেত্রে কোন নিয়মে প্যারেন্ট মেথড খোঁজা হয় (MRO)?",
    "options": ["C3 Linearization অ্যালগরিদম (Method Resolution Order)", "ডেপথ-ফার্স্ট সার্চ", "ব্রেডথ-ফার্স্ট সার্চ", "র‍্যান্ডম সার্চ"],
    "answer": "ক",
    "explanation": "পাইথন মেথড রেজোলিউশন অর্ডারে (MRO) C3 Linearization ব্যবহার করে ডায়মন্ড সমস্যার যৌক্তিক সমাধান করে।"
})

sub4_questions_part2.append({
    "id": 180,
    "topic": topic_4_13,
    "question": "পাইথনে কোনো ক্লাসের MRO বা মেথড অনুসন্ধান ক্রম দেখার প্রোপার্টি কোনটি?",
    "options": ["ClassName.__mro__ বা ClassName.mro()", "ClassName.order()", "ClassName.__path__", "ClassName.__tree__"],
    "answer": "ক",
    "explanation": "`__mro__` টাপলটি ইনহেরিটেন্স শৃঙ্খলের ক্লাস অগ্রাধিকার তালিকা প্রদান করে।"
})

sub4_questions_part2.append({
    "id": 181,
    "topic": topic_4_13,
    "question": "পাইথনের পলিমরফিজমে 'ডাক টাইপিং' (Duck Typing) দর্শনের অর্থ কী?",
    "options": [
        "অবজেক্টটি কোন নির্দিষ্ট ক্লাসের তা মুখ্য নয়; বরং অবজেক্টটিতে কাঙ্ক্ষিত মেথড বা আচরণ বিদ্যমান আছে কিনা সেটাই মুখ্য",
        "কেবল প্রাণীর অবজেক্ট তৈরি করা",
        "ক্লাস ইনহেরিট করতেই হবে",
        "অবজেক্ট টাইপ ফিক্সড রাখা"
    ],
    "answer": "ক",
    "explanation": "'If it walks like a duck and quacks like a duck, it's a duck'—পাইথনে ইন্টারফেস ছাড়াই মেথড থাকলে কোড কাজ করে।"
})

sub4_questions_part2.append({
    "id": 182,
    "topic": topic_4_13,
    "question": "`print(obj)` কল করলে বা স্ট্রিং কনভার্সনে ব্যবহারকারীর জন্য পাঠযোগ্য টেক্সট ফেরত দেয় কোন ডান্ডার মেথড?",
    "options": ["__str__(self)", "__repr__(self)", "__text__(self)", "__show__(self)"],
    "answer": "ক",
    "explanation": "`__str__` সাধারণ ব্যবহারকারীর সহজে পড়ার জন্য ইনফরমাল স্ট্রিং রূপান্তর করে।"
})

sub4_questions_part2.append({
    "id": 183,
    "topic": topic_4_13,
    "question": "ডিবাগিং ও ডেভেলপারদের জন্য অবজেক্টের নিখুঁত ও দ্ব্যর্থহীন স্ট্রিং রূপ প্রদর্শন করে কোন ডান্ডার মেথড?",
    "options": ["__repr__(self)", "__str__(self)", "__doc__", "__format__"],
    "answer": "ক",
    "explanation": "`__repr__` আনুষ্ঠানিক স্ট্রিং প্রকাশ করে যা দিয়ে আদর্শ ক্ষেত্রে অবজেক্টটি পুনরায় পুনর্গঠন (`eval(repr(obj))`) করা যায়।"
})

sub4_questions_part2.append({
    "id": 184,
    "topic": topic_4_13,
    "question": "পাইথনে যোগ অপারেটর `+` ওভারলোড করার ডান্ডার মেথড কোনটি?",
    "options": ["__add__(self, other)", "__plus__(self, other)", "__sum__(self, other)", "__concat__(self, other)"],
    "answer": "ক",
    "explanation": "কাস্টম অবজেক্টের ওপর `a + b` লিখলে পাইথন অভ্যন্তরীণভাবে `a.__add__(b)` কল করে।"
})

sub4_questions_part2.append({
    "id": 185,
    "topic": topic_4_13,
    "question": "পাইথনে `len(obj)` ফাংশনটির কাজ কাস্টম ক্লাসে সমর্থন করাতে কোন ডান্ডার মেথড লিখতে হয়?",
    "options": ["__len__(self)", "__size__(self)", "__count__(self)", "__length__(self)"],
    "answer": "ক",
    "explanation": "`__len__` মেথড বাস্তবায়ন করলে সেই অবজেক্টের ওপর স্ট্যান্ডার্ড `len()` ফাংশন কাজ করে।"
})

sub4_questions_part2.append({
    "id": 186,
    "topic": topic_4_13,
    "question": "পাইথনে এক্সেপশন হ্যান্ডলিংয়ের মৌলিক কাঠামো কোনটি?",
    "options": [
        "try ... except ... else ... finally",
        "try ... catch ... finally",
        "begin ... rescue ... ensure",
        "try ... error ... end"
    ],
    "answer": "ক",
    "explanation": "পাইথনে `catch`-এর বদলে `except` কিওয়ার্ড ব্যবহৃত হয় এবং অপশনাল `else` ও `finally` যুক্ত থাকে।"
})

sub4_questions_part2.append({
    "id": 187,
    "topic": topic_4_13,
    "question": "এক্সেপশন ব্লকে `else` এর ভূমিকা কী?",
    "options": [
        "`try` ব্লকে কোনো এক্সেপশন না ঘটলে কেবল তখনই `else` ব্লকটি রান করে",
        "এক্সেপশন ঘটলে চলে",
        "সর্বদা চলে",
        "ফাইনালাইজ করতে চলে"
    ],
    "answer": "ক",
    "explanation": "যদি `try` এর কোড শতভাগ সফল হয়, কেবল তখনই `else` ব্লকের কাজ শুরু হয়।"
})

sub4_questions_part2.append({
    "id": 188,
    "topic": topic_4_13,
    "question": "প্রোগ্রামার কর্তৃক ইচ্ছাকৃতভাবে বা শর্তসাপেক্ষে কোনো এক্সেপশন নিক্ষেপ করার কিওয়ার্ড কোনটি?",
    "options": ["raise", "throw", "throws", "fire"],
    "answer": "ক",
    "explanation": "জাভায় যা `throw`, পাইথনে তা হলো `raise` (যেমন: `raise ValueError(\"Invalid age\")`)।"
})

sub4_questions_part2.append({
    "id": 189,
    "topic": topic_4_13,
    "question": "পাইথনে নিজস্ব কাস্টম এক্সেপশন তৈরির জন্য ক্লাসকে কোন ক্লাসের সাবক্লাস করতে হয়?",
    "options": ["Exception (বা BaseException)", "Error", "Throwable", "Object"],
    "answer": "ক",
    "explanation": "`class MyError(Exception): pass` লিখে ব্যবহারকারী-সংজ্ঞায়িত এক্সেপশন তৈরি করা হয়।"
})

sub4_questions_part2.append({
    "id": 190,
    "topic": topic_4_13,
    "question": "একটি অবজেক্টকে ফাংশনের মতো কলযোগ্য (`obj()`) করতে কোন ডান্ডার মেথড ডিফাইন করতে হয়?",
    "options": ["__call__(self, *args, **kwargs)", "__invoke__(self)", "__run__(self)", "__exec__(self)"],
    "answer": "ক",
    "explanation": "`__call__` মেথড সংজ্ঞায়িত থাকলে ইনস্ট্যান্স অবজেক্ট স্বয়ং একটি ফাংশনের মতো কল করা যায়।"
})

# ==============================================================================
# অধ্যায় ৪.১৪: পাইথন জিইউআই ও ডেটাবেস অ্যাপ্লিকেশন (Questions 191 to 200)
# ==============================================================================
topic_4_14 = "অধ্যায় ৪.১৪: পাইথন জিইউআই ও ডেটাবেস অ্যাপ্লিকেশন (Python GUI & DB Application)"

sub4_questions_part2.append({
    "id": 191,
    "topic": topic_4_14,
    "question": "পাইথনের স্ট্যান্ডার্ড এবং বিল্ট-ইন ডেস্কটপ জিইউআই (GUI) লাইব্রেরি কোনটি?",
    "options": ["tkinter", "PyQt", "wxPython", "Kivy"],
    "answer": "ক",
    "explanation": "`tkinter` হলো Tcl/Tk-এর ওপর প্রতিষ্ঠিত পাইথনের অফিশিয়াল স্ট্যান্ডার্ড উইন্ডো লাইব্রেরি।"
})

sub4_questions_part2.append({
    "id": 192,
    "topic": topic_4_14,
    "question": "Tkinter অ্যাপ্লিকেশনের মূল উইন্ডো সচল ও প্রদর্শন করতে সর্বশেষ কোন ইভেন্ট লুপ মেথডটি কল করতে হয়?",
    "options": ["root.mainloop()", "root.run()", "root.start()", "root.show()"],
    "answer": "ক",
    "explanation": "`mainloop()` হলো ব্লকিং ইভেন্ট লুপ যা মাউস ক্লিক ও কীবোর্ড ইভেন্টের জন্য উইন্ডোটি উন্মুক্ত রাখে।"
})

sub4_questions_part2.append({
    "id": 193,
    "topic": topic_4_14,
    "question": "Tkinter-এ উইজেটগুলোকে টেবিল বা সারি ও কলামের (Row and Column) আকারে সাজানোর জিওমেট্রি ম্যানেজার কোনটি?",
    "options": ["grid()", "pack()", "place()", "table()"],
    "answer": "ক",
    "explanation": "`widget.grid(row=0, column=1)` সারি ও কলামের গ্রিড লেআউট তৈরি করে।"
})

sub4_questions_part2.append({
    "id": 194,
    "topic": topic_4_14,
    "question": "Tkinter-এ এক লাইনের টেক্সট ইনপুট বক্স তৈরির উইজেট কোনটি?",
    "options": ["Entry", "TextBox", "Input", "Text"],
    "answer": "ক",
    "explanation": "`Entry` একক লাইনের ইনপুটের জন্য এবং `Text` বহুলিনের টেক্সট এরিয়ার জন্য ব্যবহৃত হয়।"
})

sub4_questions_part2.append({
    "id": 195,
    "topic": topic_4_14,
    "question": "পাইথনে কোনো অতিরিক্ত সার্ভার ইনস্টল ছাড়াই স্বয়ংসম্পূর্ণ ফাইল-ভিত্তিক রিলেশনাল ডেটাবেস মডিউল কোনটি?",
    "options": ["sqlite3", "mysql.connector", "psycopg2", "cx_Oracle"],
    "answer": "ক",
    "explanation": "`sqlite3` পাইথনের সাথে ডিফল্টভাবে যুক্ত জিরো-কনফিগারেশন সার্ভারলেস এসকিউএল ইঞ্জিন।"
})

sub4_questions_part2.append({
    "id": 196,
    "topic": topic_4_14,
    "question": "পাইথনে ডেটাবেসে এসকিউএল কুয়েরি তৈরি ও এক্সিকিউট করার জন্য কোন অবজেক্টটি তৈরি করতে হয়?",
    "options": ["কার্সর অবজেক্ট (conn.cursor())", "কানেকশন অবজেক্ট", "কোয়েরি অবজেক্ট", "টেবিল অবজেক্ট"],
    "answer": "ক",
    "explanation": "`cursor = conn.cursor()` এর মাধ্যমে `cursor.execute(\"...\")` চালিয়ে কুয়েরি রান করানো হয়।"
})

sub4_questions_part2.append({
    "id": 197,
    "topic": topic_4_14,
    "question": "ডেটাবেস থেকে কুয়েরির সমস্ত ম্যাচিং রেকর্ড একসাথে লিস্ট আকারে পাওয়ার মেথড কোনটি?",
    "options": ["cursor.fetchall()", "cursor.fetchone()", "cursor.get_all()", "cursor.fetchmany()"],
    "answer": "ক",
    "explanation": "`fetchall()` কুয়েরির সমস্ত রেকর্ড টাপলের একটি পূর্ণাঙ্গ তালিকা আকারে প্রদান করে।"
})

sub4_questions_part2.append({
    "id": 198,
    "topic": topic_4_14,
    "question": "ডেটাবেসে INSERT বা UPDATE করার পর পরিবর্তনগুলো স্থায়ীভাবে ফাইলে সংরক্ষণ নিশ্চিত করতে কোনটি আবশ্যক?",
    "options": ["conn.commit()", "conn.save()", "cursor.commit()", "conn.flush()"],
    "answer": "ক",
    "explanation": "`commit()` না কল করলে ট্রানজেকশনের পরিবর্তনগুলো ডিস্ক ফাইলে সংরক্ষিত না হয়ে হারিয়ে যায়।"
})

sub4_questions_part2.append({
    "id": 199,
    "topic": topic_4_14,
    "question": "পাইথন অবজেক্ট বা ডিকশনারিকে জেএসএন (JSON) স্ট্রিংয়ে রূপান্তর করার ফাংশন কোনটি?",
    "options": ["json.dumps()", "json.loads()", "json.stringify()", "json.encode()"],
    "answer": "ক",
    "explanation": "`json.dumps(data)` পাইথন ডেটাকে JSON স্ট্রিংয়ে পরিণত করে; আর `json.loads(str)` JSON টেক্সটকে ডিকশনারিতে রূপান্তর করে।"
})

sub4_questions_part2.append({
    "id": 200,
    "topic": topic_4_14,
    "question": "পাইথনে ডেটা সায়েন্স ও টেবিল ডেটা বিশ্লেষণের জন্য বিশ্বখ্যাত ডেটাফ্রেম লাইব্রেরি কোনটি?",
    "options": ["Pandas", "Matplotlib", "Scipy", "Requests"],
    "answer": "ক",
    "explanation": "প্যান্ডাস (Pandas) হলো 2D টেবুলার ডেটা (DataFrame) হ্যান্ডলিং, ক্লিনিং ও বিশ্লেষণের প্রধান পাইথন লাইব্রেরি।"
})

print(f"Generated Subject 4 Part 2: {len(sub4_questions_part2)} questions")
