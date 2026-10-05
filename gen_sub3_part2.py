# -*- coding: utf-8 -*-
"""
Subject 3: অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (সি++, জাভা) - Part 2 (Questions 86 to 200)
Chapters:
  3.4: জাভায় ক্লাস, মেথড ও ইনহেরিটেন্স (86-115)
  3.5: এক্সেপশন হ্যান্ডলিং ও মাল্টিথ্রেডিং (116-145)
  3.6: জাভা কালেকশন ফ্রেমওয়ার্ক ও ফাইল আই/ও (146-175)
  3.7: জিইউআই ডেভেলপমেন্ট ও ডেটাবেস সংযোগ (176-200)
"""

sub3_questions_part2 = []

# ==============================================================================
# অধ্যায় ৩.৪: জাভায় ক্লাস, মেথড ও ইনহেরিটেন্স (Questions 86 to 115)
# ==============================================================================
topic_3_4 = "অধ্যায় ৩.৪: জাভায় ক্লাস, মেথড ও ইনহেরিটেন্স (Classes, Methods & Inheritance)"

sub3_questions_part2.append({
    "id": 86,
    "topic": topic_3_4,
    "question": "জাভায় `Student s = new Student();` স্টেটমেন্টে অবজেক্টটি মেমরির কোন অংশে তৈরি হয়?",
    "options": [
        "হিপ মেমরিতে (Heap Memory); আর রেফারেন্স ভ্যারিয়েবল 's' থাকে স্ট্যাক মেমরিতে (Stack)",
        "সম্পূর্ণটি স্ট্যাক মেমরিতে",
        "সম্পূর্ণটি কোড মেমরিতে",
        "সিপিইউ রেজিস্টারে"
    ],
    "answer": "ক",
    "explanation": "জাভায় `new` অপারেটর দিয়ে তৈরি সকল অবজেক্ট রান-টাইমে হিপ মেমরিতে বরাদ্দ পায় এবং তার পয়েন্টার/রেফারেন্স স্ট্যাকে থাকে।"
})

sub3_questions_part2.append({
    "id": 87,
    "topic": topic_3_4,
    "question": "একই ক্লাসে এক কনস্ট্রাক্টর থেকে অন্য কনস্ট্রাক্টর কল করাকে (Constructor Chaining) কী বলে?",
    "options": ["this() কনস্ট্রাক্টর কল", "super() কল", "clone() কল", "new() কল"],
    "answer": "ক",
    "explanation": "`this(...)` মেথড কনস্ট্রাক্টরের বডির একদম প্রথম লাইনে লিখে অন্য ওভারলোডেড কনস্ট্রাক্টরকে কল করতে হয়।"
})

sub3_questions_part2.append({
    "id": 88,
    "topic": topic_3_4,
    "question": "জাভায় মেথড ওভারলোডিং (Method Overloading) এর ক্ষেত্রে নিচের কোনটি সত্য?",
    "options": [
        "প্যারামিটারের সংখ্যা বা ডেটা টাইপ অবশ্যই ভিন্ন হতে হবে; শুধুমাত্র রিটার্ন টাইপ ভিন্ন করে ওভারলোডিং সম্ভব নয়",
        "শুধুমাত্র রিটার্ন টাইপ পরিবর্তন করলেই ওভারলোডিং হয়ে যায়",
        "মেথডের নাম ভিন্ন হতে হবে",
        "মেথডটি প্রাইভেট হতে হবে"
    ],
    "answer": "ক",
    "explanation": "কম্পাইলার মেথডের আর্গুমেন্ট তালিকা দেখে ওভারলোড রিজলভ করে; রিটার্ন টাইপ মেথড সিগনেচারের অংশ নয়।"
})

sub3_questions_part2.append({
    "id": 89,
    "topic": topic_3_4,
    "question": "জাভা ৫ এ প্রবর্তিত ভ্যারিয়েবল আর্গুমেন্ট (Varargs) ঘোষণার সঠিক সিনট্যাক্স কোনটি?",
    "options": ["public void display(int... numbers)", "public void display(int numbers...)", "public void display(...int numbers)", "public void display(var int numbers)"],
    "answer": "ক",
    "explanation": "ডেটা টাইপের পর তিনটি ডট (`...`) দিয়ে ভ্যারিয়েবল আর্গুমেন্ট ঘোষণা করা হয় এবং এটি মেথড প্যারামিটারের সর্বশেষ আর্গুমেন্ট হতে হয়।"
})

sub3_questions_part2.append({
    "id": 90,
    "topic": topic_3_4,
    "question": "জাভায় স্বয়ংক্রিয় মেমরি ব্যবস্থাপনার জন্য ব্যবহৃত ব্যাকগ্রাউন্ড প্রসেস কোনটি?",
    "options": ["গার্বেজ কালেক্টর (Garbage Collector - GC)", "মেমরি ডিফ্র্যাগমেন্টার", "টাস্ক ম্যানেজার", "জেআইটি কম্পাইলার"],
    "answer": "ক",
    "explanation": "গার্বেজ কালেক্টর হিপ মেমরি স্ক্যান করে যেসব অবজেক্টের কোনো অ্যাক্টিভ রেফারেন্স নেই তাদের মেমরি স্বয়ংক্রিয়ভাবে মুক্ত করে।"
})

sub3_questions_part2.append({
    "id": 91,
    "topic": topic_3_4,
    "question": "কোনো অবজেক্ট মেমরি থেকে গার্বেজ কালেকশনে ধ্বংস হওয়ার ঠিক পূর্ব মুহূর্তে কোন মেথডটি কল হয়?",
    "options": ["finalize() মেথড", "destroy() মেথড", "delete() মেথড", "clean() মেথড"],
    "answer": "ক",
    "explanation": "`Object` ক্লাসের `finalize()` মেথড অবজেক্ট ক্লিনআপের জন্য GC কর্তৃক অবজেক্ট ধ্বংসের ঠিক পূর্বে নির্বাহিত হয়।"
})

sub3_questions_part2.append({
    "id": 92,
    "topic": topic_3_4,
    "question": "জাভায় একটি ক্লাস অন্য একটি ক্লাসকে ইনহেরিট করতে কোন কীওয়ার্ড ব্যবহার করে?",
    "options": ["extends", "implements", "inherits", "subclass"],
    "answer": "ক",
    "explanation": "ক্লাস ইনহেরিট্যান্সের জন্য `extends` এবং ইন্টারফেস বাস্তবায়নের জন্য `implements` কীওয়ার্ড ব্যবহৃত হয়।"
})

sub3_questions_part2.append({
    "id": 93,
    "topic": topic_3_4,
    "question": "জাভা ক্লাসের ক্ষেত্রে কেন সরাসরি একাধিক প্যারেন্ট ক্লাস থেকে মাল্টিপল ইনহেরিটেন্স সমর্থন করে না?",
    "options": [
        "ডায়মন্ড সমস্যা ও মেথড অ্যাম্বিগুয়িটি (দ্ব্যর্থতা) দূর করে ভাষাটিকে সহজ ও সুরক্ষিত রাখতে",
        "জাভায় একাধিক ক্লাস তৈরি করা যায় না",
        "JVM-এর মেমরি কম বলে",
        "এটি সি++ এর কপিরাইট বলে"
    ],
    "answer": "ক",
    "explanation": "একাধিক প্যারেন্টে একই মেথড থাকলে চাইল্ড ক্লাসে কোনটি কল হবে সেই জটিলতা (Diamond Problem) এড়াতে জাভায় ক্লাসের মাল্টিপল ইনহেরিটেন্স নিষিদ্ধ।"
})

sub3_questions_part2.append({
    "id": 94,
    "topic": topic_3_4,
    "question": "প্যারেন্ট ক্লাসের কোনো মেথডকে চাইল্ড ক্লাসে হুবহু একই নামে ও একই সিগনেচারে নতুনভাবে বাস্তবায়ন করাকে কী বলে?",
    "options": ["মেথড ওভাররাইডিং (Method Overriding)", "মেথড ওভারলোডিং", "মেথড হাইডিং", "মেথড রিকার্শন"],
    "answer": "ক",
    "explanation": "সাবক্লাসে প্যারেন্ট মেথডের নতুন রূপদানই মেথড ওভাররাইডিং, যা ডায়নামিক মেথড ডিসপ্যাচ বা রান-টাইম পলিমরফিজম ঘটায়।"
})

sub3_questions_part2.append({
    "id": 95,
    "topic": topic_3_4,
    "question": "চাইল্ড ক্লাসের ভেতর থেকে প্যারেন্ট ক্লাসের কনস্ট্রাক্টর কল করার সিনট্যাক্স কোনটি?",
    "options": ["super();", "parent();", "base();", "this.super();"],
    "answer": "ক",
    "explanation": "`super()` কলটি সাবক্লাস কনস্ট্রাক্টরের সর্বপ্রথম স্টেটমেন্ট হতে হয় যা প্যারেন্ট কনস্ট্রাক্টর কার্যকর করে।"
})

sub3_questions_part2.append({
    "id": 96,
    "topic": topic_3_4,
    "question": "জাভায় প্যারেন্ট ক্লাসের কোনো ওভাররিডেন মেথড চাইল্ড ক্লাসের ভেতর থেকে কল করার উপায় কোনটি?",
    "options": ["super.methodName()", "parent.methodName()", "base.methodName()", "this.super.methodName()"],
    "answer": "ক",
    "explanation": "`super` কীওয়ার্ড দিয়ে প্যারেন্ট ক্লাসের আড়াল হওয়া ভ্যারিয়েবল ও মেথড অ্যাক্সেস করা যায়।"
})

sub3_questions_part2.append({
    "id": 97,
    "topic": topic_3_4,
    "question": "কোনো ক্লাসকে `final` ঘোষণা করলে (`public final class A`) কী ঘটবে?",
    "options": [
        "ক্লাসটিকে অন্য কোনো ক্লাস ইনহেরিট (extends) করতে পারবে না",
        "ক্লাসটির অবজেক্ট তৈরি করা যাবে না",
        "ক্লাসটির কোনো মেথড থাকবে না",
        "ক্লাসটি মেমরি থেকে মুছে যাবে"
    ],
    "answer": "ক",
    "explanation": "`final` ক্লাস কখনো সাবক্লাস বা ইনহেরিট করা যায় না (যেমন: `java.lang.String` একটি final ক্লাস)।"
})

sub3_questions_part2.append({
    "id": 98,
    "topic": topic_3_4,
    "question": "কোনো মেথডকে `final` ঘোষণা করলে তার ফলাফল কী?",
    "options": [
        "মেথডটিকে চাইল্ড ক্লাসে ওভাররাইড (Override) করা সম্পূর্ণ নিষিদ্ধ হয়ে যায়",
        "মেথডটি কল করা যায় না",
        "মেথডটি কোনো আর্গুমেন্ট নিতে পারে না",
        "মেথডটি প্রাইভেট হয়ে যায়"
    ],
    "answer": "ক",
    "explanation": "সাবক্লাসে নিরাপত্তা বা লজিক অপরিবর্তিত রাখতে প্যারেন্ট ক্লাসের মেথডকে `final` করা হয় যাতে ওভাররাইড বন্ধ থাকে।"
})

sub3_questions_part2.append({
    "id": 99,
    "topic": topic_3_4,
    "question": "জাভায় অ্যাবস্ট্রাক্ট মেথড (Abstract Method) ঘোষণার বৈশিষ্ট্য কোনটি?",
    "options": [
        "মেথডটির কেবল ডিক্লারেশন বা প্রোটোটাইপ থাকে, কিন্তু কোনো মেথড বডি বা দ্বিতীয় বন্ধনী `{ }` থাকে না",
        "মেথডটিতে সর্বদা কোড বডি থাকে",
        "মেথডটি শুধু প্রাইভেট হতে পারে",
        "মেথডটি অবজেক্ট ছাড়া কল করা যায়"
    ],
    "answer": "ক",
    "explanation": "`abstract void draw();` মেথডে কোনো বডি থাকে না এবং শেষে সেমিকোলন থাকে; সাবক্লাস এটি বাধ্যতামূলকভাবে ইমপ্লিমেন্ট করে।"
})

sub3_questions_part2.append({
    "id": 100,
    "topic": topic_3_4,
    "question": "জাভায় অ্যাবস্ট্রাক্ট ক্লাস (Abstract Class) সম্পর্কে নিচের কোনটি সঠিক?",
    "options": [
        "`new` অপারেটর দিয়ে সরাসরি অ্যাবস্ট্রাক্ট ক্লাসের অবজেক্ট তৈরি করা যায় না",
        "অ্যাবস্ট্রাক্ট ক্লাসে কোনো নন-অ্যাবস্ট্রাক্ট কনক্রিট মেথড থাকতে পারে না",
        "অ্যাবস্ট্রাক্ট ক্লাসে কনস্ট্রাক্টর থাকতে পারে না",
        "অ্যাবস্ট্রাক্ট ক্লাসের রেফারেন্স ভ্যারিয়েবল তৈরি করা যায় না"
    ],
    "answer": "ক",
    "explanation": "অ্যাবস্ট্রাক্ট ক্লাসের সরাসরি অবজেক্ট তৈরি অবৈধ, তবে তার রেফারেন্স তৈরি করে সাবক্লাসের অবজেক্ট পয়েন্ট করা যায়।"
})

sub3_questions_part2.append({
    "id": 101,
    "topic": topic_3_4,
    "question": "জাভায় ইন্টারফেস (Interface) বাস্তবায়ন করতে ক্লাস কোন কীওয়ার্ড ব্যবহার করে?",
    "options": ["implements", "extends", "inherits", "interface_of"],
    "answer": "ক",
    "explanation": "ইন্টারফেস বাস্তবায়নে `class MyClass implements MyInterface` সিনট্যাক্স ব্যবহৃত হয়।"
})

sub3_questions_part2.append({
    "id": 102,
    "topic": topic_3_4,
    "question": "জাভায় একটি ক্লাস একই সাথে একাধিক ইন্টারফেস বাস্তবায়ন করতে পারে কি?",
    "options": [
        "হ্যাঁ, কমা দিয়ে একাধিক ইন্টারফেস বাস্তবায়ন করা যায় (যেমন: class C implements A, B)",
        "না, সর্বোচ্চ একটি ইন্টারফেস নেওয়া যায়",
        "শুধুমাত্র abstract ক্লাসে সম্ভব",
        "জাভায় ইন্টারফেস মাল্টিপল সাপোর্ট করে না"
    ],
    "answer": "ক",
    "explanation": "জাভায় ক্লাসের ক্ষেত্রে মাল্টিপল ইনহেরিটেন্স না থাকলেও ইন্টারফেসের মাধ্যমে পূর্ণাঙ্গ মাল্টিপল ইনহেরিটেন্সের সুবিধা অর্জন করা যায়।"
})

sub3_questions_part2.append({
    "id": 103,
    "topic": topic_3_4,
    "question": "জাভা ইন্টারফেসে ঘোষিত সকল ভ্যারিয়েবল স্বয়ংক্রিয়ভাবে কী ধরনের হয়?",
    "options": ["public static final", "private static", "protected final", "volatile transient"],
    "answer": "ক",
    "explanation": "ইন্টারফেসের সমস্ত ফিল্ড ডিফল্টভাবেই ধ্রুবক কনস্ট্যান্ট, অর্থাৎ `public static final`।"
})

sub3_questions_part2.append({
    "id": 104,
    "topic": topic_3_4,
    "question": "জাভা ৮ থেকে ইন্টারফেসে কোড বডি সহ মেথড লেখার জন্য কোন দুটি মেকানিজম যুক্ত করা হয়েছে?",
    "options": ["default মেথড এবং static মেথড", "final মেথড এবং native মেথড", "abstract মেথড", "private constructor"],
    "answer": "ক",
    "explanation": "বিদ্যমান কোড না ভেঙে ইন্টারফেস আপগ্রেড করার জন্য জাভা ৮-এ `default` ও `static` মেথড যোগ করা হয়।"
})

sub3_questions_part2.append({
    "id": 105,
    "topic": topic_3_4,
    "question": "যে ইন্টারফেসে কোনো মেথড বা ফিল্ড থাকে না, কেবল JVM-কে বিশেষ বার্তা দেয় তাকে কী বলে?",
    "options": ["মার্কার ইন্টারফেস (Marker / Tag Interface)", "ফাংশনাল ইন্টারফেস", "অ্যাবস্ট্রাক্ট ইন্টারফেস", "এম্পটি ক্লাস"],
    "answer": "ক",
    "explanation": "যেমন `Serializable`, `Cloneable` হলো মার্কার ইন্টারফেস যা JVM কে অবজেক্টের বিশেষ সামর্থ্য সম্পর্কে অবগত করে।"
})

sub3_questions_part2.append({
    "id": 106,
    "topic": topic_3_4,
    "question": "যে ইন্টারফেসে কেবল একটিমাত্র অ্যাবস্ট্রাক্ট মেথড (Single Abstract Method - SAM) থাকে তাকে কী বলে?",
    "options": ["ফাংশনাল ইন্টারফেস (Functional Interface)", "মার্কার ইন্টারফেস", "ডিফল্ট ইন্টারফেস", "সিঙ্গেল ইন্টারফেস"],
    "answer": "ক",
    "explanation": "SAM ইন্টারফেসকে `@FunctionalInterface` বলে (যেমন: `Runnable`), যা ল্যাম্বডা এক্সপ্রেশন (Lambda) দিয়ে কল করা যায়।"
})

sub3_questions_part2.append({
    "id": 107,
    "topic": topic_3_4,
    "question": "জাভায় সম্পর্কিত ক্লাস ও ইন্টারফেসসমূহকে একটি একক ডিরেক্টরি কাঠামোয় বিন্যস্ত করাকে কী বলে?",
    "options": ["প্যাকেজ (Package)", "মডিউল", "লাইব্রেরি", "ফ্রেমওয়ার্ক"],
    "answer": "ক",
    "explanation": "নেমস্পেস সংঘাত এড়াতে এবং কোড মডুলার রাখতে `package packagename;` ব্যবহার করা হয়।"
})

sub3_questions_part2.append({
    "id": 108,
    "topic": topic_3_4,
    "question": "জাভার কোন প্যাকেজটি প্রতিটি জাভা ফাইলে স্বয়ংক্রিয়ভাবে ইমপোর্ট (Implicitly Imported) হয়ে থাকে?",
    "options": ["java.lang", "java.util", "java.io", "java.net"],
    "answer": "ক",
    "explanation": "`java.lang` প্যাকেজে মৌলিক ক্লাসগুলো (System, String, Object ইত্যাদি) থাকায় এটি স্বয়ংক্রিয়ভাবে ইমপোর্ট হয়।"
})

sub3_questions_part2.append({
    "id": 109,
    "topic": topic_3_4,
    "question": "জাভায় `protected` মেম্বারদের অ্যাক্সেস পরিধি (Scope) কতটুকু?",
    "options": [
        "একই প্যাকেজের সকল ক্লাস এবং ভিন্ন প্যাকেজের কেবল চাইল্ড সাবক্লাসসমূহে অ্যাক্সেসযোগ্য",
        "বিশ্বের যেকোনো প্যাকেজ থেকে সম্পূর্ণ উন্মুক্ত",
        "শুধুমাত্র নিজস্ব ক্লাসে সীমাবদ্ধ",
        "শুধুমাত্র একই ফাইলে"
    ],
    "answer": "ক",
    "explanation": "`protected` মেম্বার প্যাকেজের মধ্যে ফ্রেন্ডলি এবং প্যাকেজের বাইরে ইনহেরিটেন্স সূত্রের মাধ্যমে সাবক্লাসে অ্যাক্সেস পায়।"
})

sub3_questions_part2.append({
    "id": 110,
    "topic": topic_3_4,
    "question": "জাভায় কোনো ক্লাসের মেম্বারের আগে কোনো অ্যাক্সেস মডিফায়ার না লিখলে ডিফল্ট অ্যাক্সেস কী হয়?",
    "options": ["ডিফল্ট বা প্যাকেজ-প্রাইভেট (Package-Private)", "public", "private", "protected"],
    "answer": "ক",
    "explanation": "কোনো কিওয়ার্ড না দিলে তা ডিফল্ট (Package-Private) থাকে, যা কেবল একই প্যাকেজের ক্লাসগুলো দেখতে পায়।"
})

sub3_questions_part2.append({
    "id": 111,
    "topic": topic_3_4,
    "question": "কোনো ক্লাসের অবজেক্ট তৈরি না করেই ক্লাসের নাম দিয়ে সরাসরি মেথড কল করতে চাইলে মেথডটি কী হতে হবে?",
    "options": ["static মেথড", "final মেথড", "synchronized মেথড", "abstract মেথড"],
    "answer": "ক",
    "explanation": "`Math.sqrt()` এর মতো স্ট্যাটিক মেথড ক্লাস মেমোরিতে থাকে এবং অবজেক্ট ছাড়াই `ClassName.methodName()` দ্বারা কল হয়।"
})

sub3_questions_part2.append({
    "id": 112,
    "topic": topic_3_4,
    "question": "স্ট্যাটিক মেথডের ভেতর থেকে নন-স্ট্যাটিক (ইনস্ট্যান্স) ভ্যারিয়েবল সরাসরি অ্যাক্সেস করলে কী ঘটে?",
    "options": ["কম্পাইল এরর প্রদর্শন করে", "স্বয়ংক্রিয়ভাবে ভ্যালু ০ হয়", "রান-টাইমে ক্র্যাশ করে", "কোনো সমস্যা হয় না"],
    "answer": "ক",
    "explanation": "স্ট্যাটিক কনটেক্সটে কোনো অবজেক্ট বা `this` পয়েন্টার সক্রিয় থাকে না, তাই নন-স্ট্যাটিক মেম্বার সরাসরি অ্যাক্সেস অবৈধ।"
})

sub3_questions_part2.append({
    "id": 113,
    "topic": topic_3_4,
    "question": "ক্লাস লোড হওয়ার সময় স্ট্যাটিক ভ্যারিয়েবল ইনিশিয়ালাইজ করার জন্য স্বয়ংক্রিয়ভাবে রান হওয়া ব্লক কোনটি?",
    "options": ["স্ট্যাটিক ব্লক (static { ... })", "ইনস্ট্যান্স ব্লক", "কনস্ট্রাক্টর", "ফাইনাল ব্লক"],
    "answer": "ক",
    "explanation": "ক্লাস মেমরিতে লোড হওয়ার সাথে সাথে মেইন মেথডেরও আগে `static` ব্লক এক্সিকিউট হয়।"
})

sub3_questions_part2.append({
    "id": 114,
    "topic": topic_3_4,
    "question": "জাভায় ডায়নামিক মেথড ডিসপ্যাচ (Dynamic Method Dispatch) কখন ঘটে?",
    "options": [
        "যখন সুপার ক্লাসের রেফারেন্স ভ্যারিয়েবল সাবক্লাসের অবজেক্ট নির্দেশ করে এবং ওভাররিডেন মেথড কল করা হয়",
        "কনস্ট্রাক্টর ওভারলোড করার সময়",
        "স্ট্যাটিক মেথড কল করার সময়",
        "ক্লাস ইমপোর্ট করার সময়"
    ],
    "answer": "ক",
    "explanation": "`SuperClass obj = new SubClass(); obj.show();` এখানে রান টাইমে সাবক্লাসের `show()` কল হওয়াকে ডায়নামিক ডিসপ্যাচ বলে।"
})

sub3_questions_part2.append({
    "id": 115,
    "topic": topic_3_4,
    "question": "জাভায় অন্য ক্লাসের অভ্যন্তরে সংজ্ঞায়িত ক্লাসকে কী বলা হয়?",
    "options": ["নেস্টেড বা ইনার ক্লাস (Nested / Inner Class)", "সাবক্লাস", "সুপারক্লাস", "ডেরিভেটিভ ক্লাস"],
    "answer": "ক",
    "explanation": "কোনো ক্লাসের পেটে অন্য ক্লাস লিখলে তাকে নেস্টেড বা ইনার ক্লাস বলে, যা লজিক্যাল গ্রুপিং উন্নত করে।"
})

# ==============================================================================
# অধ্যায় ৩.৫: এক্সেপশন হ্যান্ডলিং ও মাল্টিথ্রেডিং (Questions 116 to 145)
# ==============================================================================
topic_3_5 = "অধ্যায় ৩.৫: এক্সেপশন হ্যান্ডলিং ও মাল্টিথ্রেডিং (Exception Handling & Multithreading)"

sub3_questions_part2.append({
    "id": 116,
    "topic": topic_3_5,
    "question": "জাভায় এক্সেপশন ও এরর সংক্রান্ত সকল ক্লাসের মূল প্যারেন্ট সুপারক্লাস কোনটি?",
    "options": ["java.lang.Throwable", "java.lang.Exception", "java.lang.Error", "java.lang.Object"],
    "answer": "ক",
    "explanation": "`Throwable` হলো শীর্ষ ক্লাস, যার দুটি মূল শাখা: `Error` এবং `Exception`।"
})

sub3_questions_part2.append({
    "id": 117,
    "topic": topic_3_5,
    "question": "জাভায় চেকড এক্সেপশন (Checked Exception) এবং আনচেকড এক্সেপশনের মধ্যে মূল পার্থক্য কী?",
    "options": [
        "চেকড এক্সেপশন কম্পাইল সময়েই হ্যান্ডল বা ডিক্লেয়ার করতে হয়, আর আনচেকড রান-টাইমে ঘটে",
        "আনচেকড এক্সেপশন কম্পাইল সময়ে ধরা পড়ে",
        "চেকড এক্সেপশন কখনো হ্যান্ডল করা যায় না",
        "উভয়ের মধ্যে কোনো প্রযুক্তিগত পার্থক্য নেই"
    ],
    "answer": "ক",
    "explanation": "কম্পাইলার চেকড এক্সেপশন (যেমন IOException) হ্যান্ডেল করা হয়েছে কিনা কম্পাইল সময়েই বাধ্য করে; `RuntimeException` হলো আনচেকড।"
})

sub3_questions_part2.append({
    "id": 118,
    "topic": topic_3_5,
    "question": "নিচের কোনটি জাভায় একটি আনচেকড এক্সেপশন (Unchecked Exception)?",
    "options": ["NullPointerException", "IOException", "SQLException", "ClassNotFoundException"],
    "answer": "ক",
    "explanation": "`NullPointerException` হলো `RuntimeException` এর সাবক্লাস, যা রান-টাইমে নাল রেফারেন্স অ্যাক্সেস করলে ঘটে।"
})

sub3_questions_part2.append({
    "id": 119,
    "topic": topic_3_5,
    "question": "জাভায় যে কোডে সম্ভাব্য কোনো ত্রুটি বা এক্সেপশন ঘটার ঝুঁকি থাকে তা কোন ব্লকে রাখা হয়?",
    "options": ["try ব্লক", "catch ব্লক", "finally ব্লক", "throw ব্লক"],
    "answer": "ক",
    "explanation": "ঝুঁকিপূর্ণ কোড `try` ব্লকে আবদ্ধ করা হয় এবং ত্রুটি ধরা পড়লে তা সংশ্লিষ্ট `catch` ব্লকে স্থানান্তরিত হয়।"
})

sub3_questions_part2.append({
    "id": 120,
    "topic": topic_3_5,
    "question": "এক্সেপশন ঘটুক বা না ঘটুক, ক্লিনআপ কোড রান করতে কোন ব্লকটি সর্বদা নিশ্চিতভাবে এক্সিকিউট হয়?",
    "options": ["finally ব্লক", "catch ব্লক", "try ব্লক", "throw ব্লক"],
    "answer": "ক",
    "explanation": "`finally` ব্লকের ভেতরের কোড (যেমন ডেটাবেস সংযোগ বা ফাইল বন্ধ করা) যেকোনো পরিস্থিতিতে এক্সিকিউট হওয়া নিশ্চিত।"
})

sub3_questions_part2.append({
    "id": 121,
    "topic": topic_3_5,
    "question": "জাভায় প্রোগ্রামারের কোড থেকে ম্যানুয়ালি কোনো এক্সেপশন অবজেক্ট নিক্ষেপ করতে কোন কীওয়ার্ড ব্যবহৃত হয়?",
    "options": ["throw", "throws", "catch", "try"],
    "answer": "ক",
    "explanation": "`throw new ArithmeticException(\"Invalid\");` সিনট্যাক্সে একক এক্সেপশন নিক্ষেপ করা হয়।"
})

sub3_questions_part2.append({
    "id": 122,
    "topic": topic_3_5,
    "question": "কোনো মেথড তার ভেতর থেকে চেকড এক্সেপশন ছুঁড়তে পারে তা কলার মেথডকে আগাম সতর্ক করতে মেথড হেডারে কী ব্যবহৃত হয়?",
    "options": ["throws কীওয়ার্ড", "throw কীওয়ার্ড", "try কীওয়ার্ড", "catch কীওয়ার্ড"],
    "answer": "ক",
    "explanation": "মেথড সিগনেচারে `void readFile() throws IOException` লিখে সম্ভাব্য এক্সেপশন ডিক্লেয়ার করা হয়।"
})

sub3_questions_part2.append({
    "id": 123,
    "topic": topic_3_5,
    "question": "একাধিক `catch` ব্লক ব্যবহারের ক্ষেত্রে সঠিক নিয়ম কোনটি?",
    "options": [
        "নির্দিষ্ট সাবক্লাস এক্সেপশন আগে এবং সাধারণ সুপারক্লাস (Exception) সবার শেষে রাখতে হবে",
        "সুপারক্লাস এক্সেপশন সবার প্রথমে দিতে হবে",
        "যেকোনো ক্রমে দেওয়া যায়",
        "কেবলমাত্র একটি ক্যাচ ব্লক অনুমোদিত"
    ],
    "answer": "ক",
    "explanation": "প্যারেন্ট ক্লাস `Exception` আগে দিলে আনরিচেবল কোড (Unreachable catch block) এরর দেখায়।"
})

sub3_questions_part2.append({
    "id": 124,
    "topic": topic_3_5,
    "question": "জাভা ৭ এ প্রবর্তিত Try-with-resources স্টেটমেন্টের প্রধান সুবিধা কী?",
    "options": [
        "স্টেটমেন্ট শেষে স্বয়ংক্রিয়ভাবে ওপেনকৃত ফাইল বা স্ট্রিম ক্লোজ করে দেয় (AutoCloseable)",
        "গতি দ্বিগুণ করে",
        "ক্যাচ ব্লক লিখতে হয় না",
        "মেমরি ডিলিট করে"
    ],
    "answer": "ক",
    "explanation": "Try-with-resources বন্ধনীতে থাকা রিসোর্স কাজ শেষে ম্যানুয়াল ক্লোজ ছাড়াই অটো ক্লোজ নিশ্চিত করে।"
})

sub3_questions_part2.append({
    "id": 125,
    "topic": topic_3_5,
    "question": "জাভায় নিজস্ব কাস্টম এক্সেপশন তৈরি করতে হলে ক্লাসটিকে কার সাবক্লাস হতে হয়?",
    "options": ["Exception ক্লাস (বা RuntimeException)", "Object ক্লাস", "Error ক্লাস", "Thread ক্লাস"],
    "answer": "ক",
    "explanation": "`class MyCustomException extends Exception` লিখে ব্যবহারকারী-সংজ্ঞায়িত এক্সেপশন তৈরি করা হয়।"
})

sub3_questions_part2.append({
    "id": 126,
    "topic": topic_3_5,
    "question": "কম্পিউটারে অপারেটিং সিস্টেমের একটি প্রসেস (Process) এবং থ্রেডের (Thread) মধ্যে পার্থক্য কী?",
    "options": [
        "প্রসেস হলো ভারী ও পৃথক মেমরিযুক্ত স্বতন্ত্র প্রোগ্রাম; থ্রেড হলো একই প্রসেসের ভেতরের হালকা ও মেমরি শেয়ারকারী একক",
        "থ্রেড বেশি ভারী",
        "প্রসেসে কোনো মেমরি থাকে না",
        "উভয়ই হুবহু এক"
    ],
    "answer": "ক",
    "explanation": "থ্রেডকে লাইটওয়েট সাব-প্রসেস বলা হয় যা একই প্রসেসের অ্যাড্রেস স্পেস ও ফাইল রিসোর্স শেয়ার করে দ্রুত কাজ করে।"
})

sub3_questions_part2.append({
    "id": 127,
    "topic": topic_3_5,
    "question": "জাভায় একটি থ্রেড তৈরি করার দুটি স্ট্যান্ডার্ড উপায় কী কী?",
    "options": [
        "`Thread` ক্লাস ইনহেরিট করা অথবা `Runnable` ইন্টারফেস বাস্তবায়ন করা",
        "`Process` ক্লাস ব্যবহার করা",
        "`Object` ক্লাস ক্লোন করা",
        "`System` মেথড কল করা"
    ],
    "answer": "ক",
    "explanation": "জাভায় থ্রেড তৈরিতে `extends Thread` অথবা `implements Runnable` ব্যবহার করা হয়।"
})

sub3_questions_part2.append({
    "id": 128,
    "topic": topic_3_5,
    "question": "কোন পদ্ধতিতে থ্রেড তৈরি করা ওওপি ডিজাইনের জন্য সর্বাধিক সুপারিশকৃত ও নমনীয়?",
    "options": [
        "`Runnable` ইন্টারফেস বাস্তবায়ন (কারণ জাভায় অন্য ক্লাস ইনহেরিট করার সুযোগ বহাল থাকে)",
        "`Thread` ক্লাস ইনহেরিট করা",
        "উভয় পদ্ধতি সমান ক্ষতিকর",
        "কোনোটিই নয়"
    ],
    "answer": "ক",
    "explanation": "যেহেতু জাভা মাল্টিপল ক্লাস ইনহেরিটেন্স সমর্থন করে না, তাই Runnable ইন্টারফেস ব্যবহার করলে অন্য যেকোনো ক্লাস ইনহেরিট করার স্বাধীনতা থাকে।"
})

sub3_questions_part2.append({
    "id": 129,
    "topic": topic_3_5,
    "question": "একটি থ্রেডের কাজ শুরু করতে কোন মেথডটি কল করতে হয়?",
    "options": ["start() মেথড", "run() মেথড", "init() মেথড", "execute() মেথড"],
    "answer": "ক",
    "explanation": "`thread.start()` মেথড নতুন কল স্ট্যাক তৈরি করে এবং JVM কর্তৃক অ্যাসিনক্রোনাসলি `run()` মেথডকে এক্সিকিউট করায়।"
})

sub3_questions_part2.append({
    "id": 130,
    "topic": topic_3_5,
    "question": "সরাসরি `thread.run()` কল করলে কী সমস্যা হয়?",
    "options": [
        "নতুন কোনো থ্রেড তৈরি হয় না; এটি বর্তমান মূল থ্রেডেই সাধারণ মেথডের মতো কল হয়ে যায়",
        "কম্পাইল এরর প্রদর্শন করে",
        "প্রোগ্রাম বন্ধ হয়ে যায়",
        "সিপিইউ নষ্ট হয়"
    ],
    "answer": "ক",
    "explanation": "`run()` সরাসরি কল করলে মাল্টিথ্রেডিং হয় না, কারেন্ট থ্রেডেই কোড রান করে। থ্রেড শুরু করতে `start()` আবশ্যক।"
})

sub3_questions_part2.append({
    "id": 131,
    "topic": topic_3_5,
    "question": "চলমান কোনো থ্রেডকে নির্দিষ্ট মিলি-সেকেন্ডের জন্য সাময়িক বিরতি দেওয়ার মেথড কোনটি?",
    "options": ["Thread.sleep(milliseconds)", "Thread.wait()", "Thread.pause()", "Thread.stop()"],
    "answer": "ক",
    "explanation": "`Thread.sleep(1000)` থ্রেডকে ১ সেকেন্ডের জন্য স্লিপ বা টাইমড ওয়েটিং স্টেটে রাখে।"
})

sub3_questions_part2.append({
    "id": 132,
    "topic": topic_3_5,
    "question": "কোনো নির্দিষ্ট থ্রেডের কাজ পুরোপুরি শেষ না হওয়া পর্যন্ত বর্তমান থ্রেডকে অপেক্ষা করাতে কোন মেথড কল করতে হয়?",
    "options": ["thread.join()", "thread.wait()", "thread.hold()", "thread.sync()"],
    "answer": "ক",
    "explanation": "`t1.join()` কল করলে t1 থ্রেড সমাপ্ত না হওয়া পর্যন্ত পরবর্তী থ্রেড বা মেইন থ্রেড অপেক্ষা করে।"
})

sub3_questions_part2.append({
    "id": 133,
    "topic": topic_3_5,
    "question": "জাভায় থ্রেডের ডিফল্ট স্বাভাবিক অগ্রাধিকার (Norm Priority) মান কত?",
    "options": ["5 (রেঞ্জ ১ থেকে ১০)", "1", "10", "0"],
    "answer": "ক",
    "explanation": "থ্রেড প্রায়োরিটি ১ (`MIN_PRIORITY`) থেকে ১০ (`MAX_PRIORITY`) পর্যন্ত হয়; ডিফল্ট মান হলো ৫ (`NORM_PRIORITY`)।"
})

sub3_questions_part2.append({
    "id": 134,
    "topic": topic_3_5,
    "question": "একাধিক থ্রেড যখন একই শেয়ার্ড ডেটা সমান্তরালে পরিবর্তন করার চেষ্টা করে ত্রুটিপূর্ণ ফলাফল তৈরি করে তখন তাকে কী বলে?",
    "options": ["রেস কন্ডিশন (Race Condition)", "ডেডলক", "স্টারভেশন", "লাইভলক"],
    "answer": "ক",
    "explanation": "শেয়ার্ড রিসোর্সে অনিয়ন্ত্রিত অ্যাক্সেসের সংঘাতকে Race Condition বলা হয়।"
})

sub3_questions_part2.append({
    "id": 135,
    "topic": topic_3_5,
    "question": "রেস কন্ডিশন রোধে এবং একবারে একটিমাত্র থ্রেডকে ক্রিটিক্যাল সেকশনে প্রবেশের অনুমতি দিতে কোন কীওয়ার্ড ব্যবহৃত হয়?",
    "options": ["synchronized", "volatile", "atomic", "locked"],
    "answer": "ক",
    "explanation": "`synchronized` মেথড বা ব্লক অবজেক্ট মনিটর লক ব্যবহার করে থ্রেড-সেফটি নিশ্চিত করে।"
})

sub3_questions_part2.append({
    "id": 136,
    "topic": topic_3_5,
    "question": "দুটি বা ততোধিক থ্রেড যখন পরস্পরের দখলকৃত রিসোর্সের জন্য চিরতরে অপেক্ষমাণ অবস্থায় আটকে থাকে তখন তাকে কী বলে?",
    "options": ["ডেডলক (Deadlock)", "রেস কন্ডিশন", "থ্রেড পুল", "ইনফাইনাইট লুপ"],
    "answer": "ক",
    "explanation": "সার্কুলার ডিপেন্ডেন্সির কারণে থ্রেডসমূহ অনির্দিষ্টকালের জন্য আটকে থাকাই হলো ডেডলক।"
})

sub3_questions_part2.append({
    "id": 137,
    "topic": topic_3_5,
    "question": "জাভায় ইন্টার-থ্রেড কমিউনিকেশনের মেথডসমূহ (`wait()`, `notify()`, `notifyAll()`) কোন ক্লাসে সংজ্ঞায়িত?",
    "options": ["java.lang.Object ক্লাসে", "java.lang.Thread ক্লাসে", "java.lang.Runnable ইন্টারফেসে", "java.util.concurrent প্যাকেজে"],
    "answer": "ক",
    "explanation": "যেহেতু লক বা মনিটর প্রতিটি অবজেক্টের সাথে যুক্ত থাকে, তাই এই মেথডগুলো `Thread` এ নয় বরং শীর্ষ `Object` ক্লাসে সংজ্ঞায়িত।"
})

sub3_questions_part2.append({
    "id": 138,
    "topic": topic_3_5,
    "question": "`wait()` এবং `notify()` মেথডগুলো কোন ধরনের ব্লকের ভেতর থেকে কল করা বাধ্যতামূলক?",
    "options": ["synchronized ব্লকের ভেতর থেকে", "try-catch ব্লকে", "static ব্লকে", "যেকোনো সাধারণ ব্লকে"],
    "answer": "ক",
    "explanation": "অবজেক্টের মনিটর লক ছাড়া `wait()` কল করলে রান-টাইমে `IllegalMonitorStateException` ঘটে।"
})

sub3_questions_part2.append({
    "id": 139,
    "topic": topic_3_5,
    "question": "জাভায় ব্যাকগ্রাউন্ড সাপোর্ট সার্ভিস দেওয়ার জন্য ব্যবহৃত থ্রেডকে (যেমন গার্বেজ কালেক্টর) কী বলে?",
    "options": ["ডেমোন থ্রেড (Daemon Thread)", "ইউজার থ্রেড", "মেইন থ্রেড", "ফরগ্রাউন্ড থ্রেড"],
    "answer": "ক",
    "explanation": "ডেমোন থ্রেড হলো কম অগ্রাধিকারের ব্যাকগ্রাউন্ড থ্রেড; সকল ইউজার থ্রেড শেষ হলে JVM স্বয়ংক্রিয়ভাবে বন্ধ হয়ে যায়।"
})

sub3_questions_part2.append({
    "id": 140,
    "topic": topic_3_5,
    "question": "একটি থ্রেডকে ডেমোন থ্রেড বানাতে কোন মেথডটি `start()` কলের আগেই ডাকতে হয়?",
    "options": ["thread.setDaemon(true)", "thread.makeDaemon()", "thread.daemon = true", "thread.initDaemon()"],
    "answer": "ক",
    "explanation": "থ্রেড চালু করার পর `setDaemon()` কল করলে `IllegalThreadStateException` ঘটে।"
})

sub3_questions_part2.append({
    "id": 141,
    "topic": topic_3_5,
    "question": "জাভায় `volatile` কীওয়ার্ড ফিল্ডের সাথে ব্যবহারের মূল উদ্দেশ্য কী?",
    "options": [
        "ভেরিয়েবলের মান কোনো থ্রেড ক্যাশে সংরক্ষণ না করে সরাসরি মূল মেমরি (RAM) থেকে পড়তে ও লিখতে বাধ্য করা",
        "ভেরিয়েবলকে কনস্ট্যান্ট করা",
        "ভেরিয়েবলকে প্রাইভেট করা",
        "মেমরি সেভ করা"
    ],
    "answer": "ক",
    "explanation": "`volatile` নিশ্চিত করে যে এক থ্রেড কর্তৃক করা মান পরিবর্তন অন্যান্য সকল থ্রেড তাৎক্ষণিক দেখতে পায় (Visibility guarantee)।"
})

sub3_questions_part2.append({
    "id": 142,
    "topic": topic_3_5,
    "question": "জাভায় একটি থ্রেড তার জীবদ্দশায় কয়টি মৌলিক অবস্থা (Life Cycle States) অতিক্রম করতে পারে?",
    "options": ["৬টি (NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED)", "৩টি", "৪টি", "৮টি"],
    "answer": "ক",
    "explanation": "জাভা থ্রেডের স্টেটগুলো `Thread.State` এনামে মোট ৬টি সুনির্দিষ্ট অবস্থায় সংজ্ঞায়িত।"
})

sub3_questions_part2.append({
    "id": 143,
    "topic": topic_3_5,
    "question": "জাভা কনকারেন্সি ইউটিলিটিতে বারবার নতুন থ্রেড তৈরি করার ওভারহেড কমাতে কী ব্যবহৃত হয়?",
    "options": ["থ্রেড পুল (Thread Pool - ExecutorService)", "সিঙ্গেল থ্রেড", "রিকার্সিভ থ্রেড", "অ্যারে থ্রেড"],
    "answer": "ক",
    "explanation": "`ExecutorService` পূর্বে তৈরিকৃত থ্রেড পুনঃব্যবহার করে টাস্ক এক্সিকিউট করে, ফলে রিসোর্স সাশ্রয় হয়।"
})

sub3_questions_part2.append({
    "id": 144,
    "topic": topic_3_5,
    "question": "কোনো মেথডে `System.exit(0)` এক্সিকিউট হলে `finally` ব্লক কি কার্যকর হবে?",
    "options": [
        "না, JVM সরাসরি বন্ধ হয়ে যাওয়ায় finally ব্লক রান করে না",
        "হ্যাঁ, সর্বদা রান করবে",
        "কম্পাইল এরর হবে",
        "অনিশ্চিত"
    ],
    "answer": "ক",
    "explanation": "`System.exit()` হলো একমাত্র বিরল ব্যতিক্রম যখন JVM তাৎক্ষণিক টার্মিনেট হওয়ায় finally ব্লকও চলে না।"
})

sub3_questions_part2.append({
    "id": 145,
    "topic": topic_3_5,
    "question": "জাভায় থ্রেডের বর্তমান রেফারেন্স জানতে কোন স্ট্যাটিক মেথড কল করতে হয়?",
    "options": ["Thread.currentThread()", "Thread.getThread()", "this.getThread()", "System.getThread()"],
    "answer": "ক",
    "explanation": "`Thread.currentThread()` বর্তমানে চলমান থ্রেড অবজেক্টটির রেফারেন্স রিটার্ন করে।"
})

# ==============================================================================
# অধ্যায় ৩.৬: জাভা কালেকশন ফ্রেমওয়ার্ক ও ফাইল আই/ও (Questions 146 to 175)
# ==============================================================================
topic_3_6 = "অধ্যায় ৩.৬: জাভা কালেকশন ফ্রেমওয়ার্ক ও ফাইল আই/ও (Collections & I/O)"

sub3_questions_part2.append({
    "id": 146,
    "topic": topic_3_6,
    "question": "জাভা কালেকশন ফ্রেমওয়ার্কের (Collection Framework) রুট ইন্টারফেস কোনটি?",
    "options": ["java.lang.Iterable (যার চাইল্ড হলো Collection)", "java.util.Map", "java.util.List", "java.lang.Object"],
    "answer": "ক",
    "explanation": "`Iterable` হলো শীর্ষ ইন্টারফেস যা for-each লুপ সমর্থন করে; এর নিচে রয়েছে `Collection` ইন্টারফেস।"
})

sub3_questions_part2.append({
    "id": 147,
    "topic": topic_3_6,
    "question": "নিচের কোনটি জাভায় `Collection` ইন্টারফেসের সরাসরি সাব-ইন্টারফেস নয়?",
    "options": ["Map", "List", "Set", "Queue"],
    "answer": "ক",
    "explanation": "`Map` কালেকশন ফ্রেমওয়ার্কের অংশ হলেও এটি কি-ভ্যালু জোড়া ধারণ করায় `Collection` ইন্টারফেস ইনহেরিট করে না।"
})

sub3_questions_part2.append({
    "id": 148,
    "topic": topic_3_6,
    "question": "জাভায় `ArrayList` এবং `LinkedList` এর মধ্যে মূল পারফরম্যান্সগত পার্থক্য কী?",
    "options": [
        "`ArrayList` র্যান্ডম অ্যাক্সেসে ($O(1)$) দ্রুততর, কিন্তু `LinkedList` উপাদান সংযোজন বা বিয়োজনে ($O(1)$) দ্রুততর",
        "`LinkedList` এ ইনডেক্স দিয়ে দ্রুত পড়া যায়",
        "`ArrayList` ডুপ্লিকেট রাখতে পারে না",
        "উভয়ের অভ্যন্তরীণ গঠন একই"
    ],
    "answer": "ক",
    "explanation": "ArrayList ডায়নামিক অ্যারে ভিত্তিক হওয়ায় র্যান্ডম অ্যাক্সেস ফাস্ট; LinkedList ডাবল লিঙ্কড লিস্ট হওয়ায় ইনসার্শন/ডিলিশন ফাস্ট।"
})

sub3_questions_part2.append({
    "id": 149,
    "topic": topic_3_6,
    "question": "জাভায় কোনো ডুপ্লিকেট উপাদান সংরক্ষণ করতে না দিলে কোন কালেকশন ইন্টারফেস ব্যবহার করতে হয়?",
    "options": ["Set ইন্টারফেস", "List ইন্টারফেস", "Queue ইন্টারফেস", "Vector ইন্টারফেস"],
    "answer": "ক",
    "explanation": "`Set` ইন্টারফেসে (যেমন `HashSet`, `TreeSet`) কোনো উপাদান দুইবার প্রবেশ করানো যায় না (No duplicates allowed)।"
})

sub3_questions_part2.append({
    "id": 150,
    "topic": topic_3_6,
    "question": "উপাদানসমূহকে স্বয়ংক্রিয়ভাবে স্বাভাবিক ক্রমানুসারে (Sorted Order) সংরক্ষণ করার Set ক্লাস কোনটি?",
    "options": ["TreeSet (Red-Black Tree ভিত্তিক)", "HashSet", "LinkedHashSet", "ArrayList"],
    "answer": "ক",
    "explanation": "`TreeSet` সেলফ-ব্যালেন্সিং রেড-ব্ল্যাক ট্রি ব্যবহার করে উপাদানগুলোকে সর্বদা সর্টেড অর্ডারে সাজিয়ে রাখে ($O(\\log N)$)।"
})

sub3_questions_part2.append({
    "id": 151,
    "topic": topic_3_6,
    "question": "হ্যাশিং টেকনোলজি ব্যবহার করে $O(1)$ টাইম কমপ্লেক্সিটিতে উপাদান সংরক্ষণ ও সন্ধানের Set ক্লাস কোনটি?",
    "options": ["HashSet", "TreeSet", "Vector", "LinkedList"],
    "answer": "ক",
    "explanation": "`HashSet` হ্যাশম্যাপের অভ্যন্তরীণ মেকানিজমে কাজ করে অত্যন্ত দ্রুতগতিতে উপাদান প্রসেস করে।"
})

sub3_questions_part2.append({
    "id": 152,
    "topic": topic_3_6,
    "question": "জাভায় কি-ভ্যালু (Key-Value) জোড়া সংরক্ষণের জন্য বহুল ব্যবহৃত নন-সিনক্রোনাইজড ক্লাস কোনটি?",
    "options": ["HashMap", "Hashtable", "TreeMap", "ArrayList"],
    "answer": "ক",
    "explanation": "`HashMap` দ্রুতগতির কি-ভ্যালু সংরক্ষণ ক্লাস যা একটি নাল কি (Null key) এবং একাধিক নাল ভ্যালু সমর্থন করে।"
})

sub3_questions_part2.append({
    "id": 153,
    "topic": topic_3_6,
    "question": "`HashMap` এবং লিগ্যাসি `Hashtable` ক্লাসের মধ্যে পার্থক্য কোনটি?",
    "options": [
        "`HashMap` নন-সিনক্রোনাইজড ও দ্রুত এবং নাল অনুমোদন করে; `Hashtable` সিনক্রোনাইজড এবং নাল অনুমোদন করে না",
        "`Hashtable` দ্রুত কাজ করে",
        "উভয়ই নাল কি গ্রহণ করে",
        "কোনো পার্থক্য নেই"
    ],
    "answer": "ক",
    "explanation": "মাল্টিথ্রেডিং নিরাপত্তার জন্য পুরনো `Hashtable` এর মেথডগুলো সিনক্রোনাইজড কিন্তু ধীরগতির।"
})

sub3_questions_part2.append({
    "id": 154,
    "topic": topic_3_6,
    "question": "জাভায় কালেকশন উপাদানগুলোকে সামনের দিকে ক্রমান্বয়ে ট্রাভার্স করার ইউনিভার্সাল ইন্টারফেস কোনটি?",
    "options": ["Iterator (hasNext(), next(), remove())", "ListIterator", "Enumeration", "ForLoop"],
    "answer": "ক",
    "explanation": "`Iterator` ইন্টারফেস যেকোনো Collection অবজেক্ট ট্রাভার্স করার জন্য স্ট্যান্ডার্ড মেথড প্রদান করে।"
})

sub3_questions_part2.append({
    "id": 155,
    "topic": topic_3_6,
    "question": "উভয়মুখী (সামনে ও পেছনে - Bidirectional) ট্রাভার্সাল সমর্থন করে কোন ইটারেটরটি?",
    "options": ["ListIterator", "Iterator", "Spliterator", "Enumeration"],
    "answer": "ক",
    "explanation": "`ListIterator` কেবল `List` এর জন্য প্রযোজ্য এবং এটি `hasPrevious()` ও `previous()` সমর্থন করে।"
})

sub3_questions_part2.append({
    "id": 156,
    "topic": topic_3_6,
    "question": "জাভা জেনেরিক্সের (Generics) মূল উদ্দেশ্য কোনটি?",
    "options": [
        "কম্পাইল-টাইম টাইপ সেফটি নিশ্চিত করা এবং বারবার টাইপ কাস্টিংয়ের ঝামেলা দূর করা",
        "ফাইলের সাইজ কমানো",
        "প্রোগ্রাম স্বয়ংক্রিয়ভাবে রান করা",
        "পাসওয়ার্ড এনক্রিপ্ট করা"
    ],
    "answer": "ক",
    "explanation": "`List<String> list = new ArrayList<>();` জেনেরিক্স ভুল ডেটা টাইপ ঢোকানো কম্পাইল সময়েই আটকে দেয়।"
})

sub3_questions_part2.append({
    "id": 157,
    "topic": topic_3_6,
    "question": "জাভায় কাস্টম অবজেক্ট সর্ট করতে ন্যাচারাল অর্ডারিংয়ের জন্য কোন ইন্টারফেস ইমপ্লিমেন্ট করতে হয়?",
    "options": ["Comparable ইন্টারফেস (compareTo মেথড)", "Comparator ইন্টারফেস (compare মেথড)", "Cloneable", "Serializable"],
    "answer": "ক",
    "explanation": "একক মূল ক্লাসের ভেতর ন্যাচারাল সর্টিং লজিক লিখতে `Comparable<T>` এর `compareTo()` বাস্তবায়ন করতে হয়।"
})

sub3_questions_part2.append({
    "id": 158,
    "topic": topic_3_6,
    "question": "একাধিক ভিন্ন ভিন্ন মানদণ্ডের ভিত্তিতে (যেমন কখনো নাম, কখনো বয়স দিয়ে) সর্ট করতে কোনটি ব্যবহৃত হয়?",
    "options": ["Comparator ইন্টারফেস (compare(o1, o2) মেথড)", "Comparable ইন্টারফেস", "Iterator", "Sorter"],
    "answer": "ক",
    "explanation": "মূল ক্লাসে হাত না দিয়ে বাহ্যিক ক্লাসে একাধিক কাস্টম সর্টিং লজিক লিখতে `Comparator` ব্যবহৃত হয়।"
})

sub3_questions_part2.append({
    "id": 159,
    "topic": topic_3_6,
    "question": "জাভায় বাইট স্ট্রিম (Byte Stream) পরিচালনার মূল সুপারক্লাস দুটি কোনটি?",
    "options": ["InputStream এবং OutputStream", "Reader এবং Writer", "FileInputStream এবং FileOutputStream", "DataInputStream"],
    "answer": "ক",
    "explanation": "কাঁচা বাইট ডেটা (ছবি, অডিও ইত্যাদি) প্রসেস করতে ৮-বিট বাইট স্ট্রিম `InputStream`/`OutputStream` ব্যবহৃত হয়।"
})

sub3_questions_part2.append({
    "id": 160,
    "topic": topic_3_6,
    "question": "জাভায় ক্যারেক্টার স্ট্রিম (Character Stream) পরিচালনার মূল সুপারক্লাস দুটি কোনটি?",
    "options": ["Reader এবং Writer", "InputStream এবং OutputStream", "FileReader এবং FileWriter", "Scanner"],
    "answer": "ক",
    "explanation": "১৬-বিট ইউনিকোড টেক্সট ফাইল পরিচালনার জন্য `Reader` এবং `Writer` ক্লাসদ্বয় ব্যবহৃত হয়।"
})

sub3_questions_part2.append({
    "id": 161,
    "topic": topic_3_6,
    "question": "টেক্সট ফাইল থেকে দ্রুতগতির লাইন-বাই-লাইন (`readLine()`) পড়ার জনপ্রিয় ক্লাস কোনটি?",
    "options": ["BufferedReader", "FileReader", "FileInputStream", "Scanner"],
    "answer": "ক",
    "explanation": "`BufferedReader` বাফার ব্যবহার করে দক্ষভাবে পুরো লাইন একসাথে পড়ে।"
})

sub3_questions_part2.append({
    "id": 162,
    "topic": topic_3_6,
    "question": "মেমরির কোনো চলমান জাভা অবজেক্টকে বাইট স্ট্রিমে রূপান্তর করে ফাইলে সংরক্ষণের প্রক্রিয়াকে কী বলে?",
    "options": ["অবজেক্ট সিরিয়ালাইজেশন (Serialization)", "ডি-সিরিয়ালাইজেশন", "টাইপ কাস্টিং", "অবজেক্ট ক্লোনিং"],
    "answer": "ক",
    "explanation": "নেটওয়ার্কে প্রেরণ বা ডিস্কে স্থায়ীভাবে রাখতে অবজেক্ট স্টেটকে বাইটে পরিণত করাকে Serialization বলে।"
})

sub3_questions_part2.append({
    "id": 163,
    "topic": topic_3_6,
    "question": "সংরক্ষিত বাইট স্ট্রিম থেকে পুনরায় মূল জাভা অবজেক্ট পুনর্গঠন করার প্রক্রিয়াকে কী বলে?",
    "options": ["ডি-সিরিয়ালাইজেশন (Deserialization)", "সিরিয়ালাইজেশন", "ইনস্ট্যানশিয়েশন", "কম্পাইলেশন"],
    "answer": "ক",
    "explanation": "`ObjectInputStream.readObject()` মেথডের মাধ্যমে বাইট থেকে মেমরিতে অবজেক্ট ফিরিয়ে আনা হয়।"
})

sub3_questions_part2.append({
    "id": 164,
    "topic": topic_3_6,
    "question": "কোনো ক্লাসকে সিরিয়ালাইজেবল করতে হলে কোন ইন্টারফেসটি ইমপ্লিমেন্ট করা আবশ্যক?",
    "options": ["java.io.Serializable", "java.io.Externalizable", "java.lang.Cloneable", "java.util.Collection"],
    "answer": "ক",
    "explanation": "`Serializable` একটি মার্কার ইন্টারফেস যা ক্লাসকে সিরিয়ালাইজেশন সক্ষম করে তোলে।"
})

sub3_questions_part2.append({
    "id": 165,
    "topic": topic_3_6,
    "question": "সিরিয়ালাইজেশনের সময় ক্লাসের কোনো সংবেদনশীল ডেটা মেম্বার (যেমন পাসওয়ার্ড) সংরক্ষণ থেকে বাদ দিতে কীওয়ার্ড কোনটি?",
    "options": ["transient", "volatile", "private", "final"],
    "answer": "ক",
    "explanation": "`transient` ফিল্ড সিরিয়ালাইজেশনে অংশ নেয় না; ডি-সিরিয়ালাইজেশনের সময় এটি ডিফল্ট মান (যেমন null বা 0) পায়।"
})

sub3_questions_part2.append({
    "id": 166,
    "topic": topic_3_6,
    "question": "সিরিয়ালাইজড ক্লাসের সংস্করণ সামঞ্জস্যতা নিশ্চিত করতে কোন আইডি ঘোষণা করা হয়?",
    "options": ["serialVersionUID", "versionID", "classUID", "hashCode"],
    "answer": "ক",
    "explanation": "`private static final long serialVersionUID = 1L;` ডি-সিরিয়ালাইজেশনে ক্লাস ভার্সন অমিলজনিত ত্রুটি রোধ করে।"
})

sub3_questions_part2.append({
    "id": 167,
    "topic": topic_3_6,
    "question": "জাভায় `Collections.sort()` মেথড মূলত কোন সর্টিং অ্যালগরিদম ব্যবহার করে?",
    "options": ["TimSort (Merge Sort এবং Insertion Sort এর সংমিশ্রণ)", "QuickSort", "Bubble Sort", "Heap Sort"],
    "answer": "ক",
    "explanation": "জাভায় অবজেক্ট কালেকশন সর্ট করার জন্য টিম পিটার্স উদ্ভাবিত উচ্চ ক্ষমতাসম্পন্ন হাইব্রিড TimSort ব্যবহৃত হয়।"
})

sub3_questions_part2.append({
    "id": 168,
    "topic": topic_3_6,
    "question": "জাভায় একটি থ্রেড-সেফ ডায়নামিক লিস্ট পেতে কোনটি ব্যবহৃত হয়?",
    "options": ["CopyOnWriteArrayList অথবা Collections.synchronizedList()", "ArrayList", "LinkedList", "TreeSet"],
    "answer": "ক",
    "explanation": "মাল্টিথ্রেডেড পরিবেশে কনকারেন্ট অ্যাক্সেসের জন্য `CopyOnWriteArrayList` আদর্শ।"
})

sub3_questions_part2.append({
    "id": 169,
    "topic": topic_3_6,
    "question": "জাভায় `PriorityQueue` উপাদানগুলোকে কোন ডেটা স্ট্রাকচারের নিয়মে সাজায়?",
    "options": ["বাইনারি হিপ (Min-Heap ডিফল্টভাবে)", "অ্যারে", "স্ট্যাক", "বৃত্তাকার কিউ"],
    "answer": "ক",
    "explanation": "`PriorityQueue` ডিফল্টভাবে মিন-হিপ ব্যবহার করে সর্বনিম্ন উপাদানকে রুটে রাখে।"
})

sub3_questions_part2.append({
    "id": 170,
    "topic": topic_3_6,
    "question": "জাভায় ফাইল ও ডিরেক্টরি সম্পর্কিত তথ্য ও পথ পরিচালনার জন্য `java.io.File` এর আধুনিক বিকল্প কোনটি?",
    "options": ["java.nio.file.Path এবং java.nio.file.Files (Java 7+ NIO.2)", "java.io.FileReader", "java.util.File", "java.nio.Buffer"],
    "answer": "ক",
    "explanation": "NIO.2 প্যাকেজের `Path` এবং `Files` ক্লাস আধুনিক প্ল্যাটফর্ম-স্বাধীন ফাইল অপারেশনের জন্য উন্নত ও দ্রুত।"
})

sub3_questions_part2.append({
    "id": 171,
    "topic": topic_3_6,
    "question": "জাভায় কালেকশন অবজেক্টকে অপরিবর্তনীয় (Unmodifiable / Immutable) করার পদ্ধতি কোনটি?",
    "options": ["Collections.unmodifiableList(list)", "list.makeFinal()", "list.lock()", "list.immutable()"],
    "answer": "ক",
    "explanation": "`Collections.unmodifiableList()` দিয়ে তৈরি লিস্টে কোনো নতুন উপাদান যোগ বা মুছতে গেলে এক্সেপশন ঘটে।"
})

sub3_questions_part2.append({
    "id": 172,
    "topic": topic_3_6,
    "question": "জাভায় `Stack` ক্লাস কোন ডেটা স্ট্রাকচার প্রিন্সিপাল অনুসরণ করে?",
    "options": ["LIFO (Last-In-First-Out)", "FIFO (First-In-First-Out)", "Priority", "Random"],
    "answer": "ক",
    "explanation": "স্ট্যাকের মৌলিক অপারেশন `push()` ও `pop()` LIFO নীতি মেনে কাজ করে।"
})

sub3_questions_part2.append({
    "id": 173,
    "topic": topic_3_6,
    "question": "জাভা কালেকশনে একই কী-তে বারবার নতুন ভ্যালু পুট (`map.put(key, value)`) করলে কী ঘটে?",
    "options": [
        "পূর্ববর্তী ভ্যালুটি ওভাররাইট হয়ে নতুন ভ্যালু বসে এবং আগের ভ্যালুটি রিটার্ন হয়",
        "কম্পাইল এরর প্রদর্শন করে",
        "ডুপ্লিকেট কি তৈরি হয়",
        "ম্যাপ ক্র্যাশ করে"
    ],
    "answer": "ক",
    "explanation": "ম্যাপে কি অনন্য (Unique); বিদ্যমান কী-তে নতুন মান দিলে তা পূর্বের মানকে প্রতিস্থাপন করে।"
})

sub3_questions_part2.append({
    "id": 174,
    "topic": topic_3_6,
    "question": "জাভায় ফাইল ডিরেক্টরির ফাইল তালিকা পাওয়ার মেথড কোনটি?",
    "options": ["file.listFiles()", "file.getFiles()", "file.allFiles()", "file.readDir()"],
    "answer": "ক",
    "explanation": "`File.listFiles()` ডিরেক্টরির ভেতরের সমস্ত ফাইল ও ফোল্ডারের `File[]` অ্যারে প্রদান করে।"
})

sub3_questions_part2.append({
    "id": 175,
    "topic": topic_3_6,
    "question": "জাভায় প্রিন্ট রাইটার ক্লাসের (`PrintWriter`) প্রধান সুবিধা কী?",
    "options": [
        "ফরম্যাটেড টেক্সট আউটপুট লেখা যায় (`printf()`, `println()`) এবং এটি স্বয়ংক্রিয়ভাবে কোনো এক্সেপশন থ্রো করে না",
        "ছবি প্রসেস করতে পারে",
        "ফাইল এনক্রিপ্ট করে",
        "এটি মেমরি ব্যবহার করে না"
    ],
    "answer": "ক",
    "explanation": "`PrintWriter` টেক্সট ফাইলে সহজে লেখার সুবিধা দেয় এবং `checkError()` দিয়ে এরর যাচাই করা যায়।"
})

# ==============================================================================
# অধ্যায় ৩.৭: জিইউআই ডেভেলপমেন্ট ও ডেটাবেস সংযোগ (Questions 176 to 200)
# ==============================================================================
topic_3_7 = "অধ্যায় ৩.৭: জিইউআই ডেভেলপমেন্ট ও ডেটাবেস সংযোগ (Java GUI & JDBC)"

sub3_questions_part2.append({
    "id": 176,
    "topic": topic_3_7,
    "question": "জাভায় AWT (Abstract Window Toolkit) এবং Swing-এর মধ্যে প্রধান পার্থক্য কী?",
    "options": [
        "AWT হলো প্ল্যাটফর্ম-নির্ভর হেভিওয়েট কম্পোনেন্ট; Swing হলো ১০০% খাঁটি জাভায় তৈরি লাইটওয়েট ও প্ল্যাটফর্ম-স্বাধীন কম্পোনেন্ট",
        "Swing প্ল্যাটফর্ম-নির্ভর",
        "AWT তে বেশি উপাদান রয়েছে",
        "উভয়ের মধ্যে কোনো প্রযুক্তিগত পার্থক্য নেই"
    ],
    "answer": "ক",
    "explanation": "সুইং উপাদানগুলো ওএস নেটিভ কোড ব্যবহার করে না, ফলে সব অপারেটিং সিস্টেমে দেখতে একই রকম (Pluggable Look and Feel) হয়।"
})

sub3_questions_part2.append({
    "id": 177,
    "topic": topic_3_7,
    "question": "জাভা সুইং প্যাকেজের শীর্ষ উইন্ডো ফ্রেম তৈরি করার ক্লাস কোনটি?",
    "options": ["javax.swing.JFrame", "javax.swing.JPanel", "java.awt.Window", "javax.swing.JDialog"],
    "answer": "ক",
    "explanation": "`JFrame` হলো সুইং অ্যাপ্লিকেশনের প্রধান উইন্ডো যা টাইটেলবার, মিনিমাইজ ও ক্লোজ বাটন ধারণ করে।"
})

sub3_questions_part2.append({
    "id": 178,
    "topic": topic_3_7,
    "question": "কোনো `JFrame` উইন্ডোর ক্লোজ বাটনে (X) চাপলে পুরো প্রোগ্রাম বন্ধ করতে কোন মেথড কল করতে হয়?",
    "options": [
        "frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);",
        "frame.close();",
        "frame.terminate();",
        "frame.exit();"
    ],
    "answer": "ক",
    "explanation": "`EXIT_ON_CLOSE` কনস্ট্যান্ট সেট করলে উইন্ডো কাটার সাথে সাথে সম্পূর্ণ প্রোগ্রাম প্রসেস সমাপ্ত হয়।"
})

sub3_questions_part2.append({
    "id": 179,
    "topic": topic_3_7,
    "question": "জাভায় `JFrame`-এর ডিফল্ট লেআউট ম্যানেজার কোনটি?",
    "options": ["BorderLayout (North, South, East, West, Center)", "FlowLayout", "GridLayout", "CardLayout"],
    "answer": "ক",
    "explanation": "`JFrame` এর কন্টেন্ট পেনের ডিফল্ট লেআউট হলো `BorderLayout`, যা ৫টি জোনে উপাদান রাখে।"
})

sub3_questions_part2.append({
    "id": 180,
    "topic": topic_3_7,
    "question": "জাভায় `JPanel`-এর ডিফল্ট লেআউট ম্যানেজার কোনটি?",
    "options": ["FlowLayout", "BorderLayout", "GridLayout", "BoxLayout"],
    "answer": "ক",
    "explanation": "`JPanel` ডিফল্টভাবে `FlowLayout` ব্যবহার করে, যেখানে উপাদানগুলো বাম থেকে ডানে সারিবদ্ধভাবে বসে।"
})

sub3_questions_part2.append({
    "id": 181,
    "topic": topic_3_7,
    "question": "সমস্ত উপাদানকে সমান আকারের সারি ও কলামের গ্রিডে ভাগ করে সাজানোর লেআউট কোনটি?",
    "options": ["GridLayout", "FlowLayout", "BorderLayout", "CardLayout"],
    "answer": "ক",
    "explanation": "`GridLayout(rows, cols)` উইন্ডোকে সমান চতুর্ভুজাকৃতি ঘরে ভাগ করে উপাদান সাজায়।"
})

sub3_questions_part2.append({
    "id": 182,
    "topic": topic_3_7,
    "question": "জাভায় বাটন ক্লিকের ইভেন্ট হ্যান্ডল করতে কোন ইন্টারফেসটি বাস্তবায়ন করতে হয়?",
    "options": ["ActionListener (actionPerformed মেথড)", "MouseListener", "KeyListener", "WindowListener"],
    "answer": "ক",
    "explanation": "`button.addActionListener(this);` দিয়ে `actionPerformed(ActionEvent e)` মেথডে ক্লিকের লজিক লিখতে হয়।"
})

sub3_questions_part2.append({
    "id": 183,
    "topic": topic_3_7,
    "question": "জাভায় ইউজার পাসওয়ার্ড ইনপুট নেওয়ার জন্য টেক্সট গোপন রাখার বিশেষ সুইং কম্পোনেন্ট কোনটি?",
    "options": ["JPasswordField (getPassword() মেথড)", "JTextField", "JTextArea", "JHiddenField"],
    "answer": "ক",
    "explanation": "`JPasswordField` ইনপুট করা অক্ষরগুলোকে ডট বা এস্টারিস্ক দিয়ে স্ক্রিনে ঢেকে রাখে।"
})

sub3_questions_part2.append({
    "id": 184,
    "topic": topic_3_7,
    "question": "জেডিবিসি (JDBC)-এর পূর্ণরূপ কী?",
    "options": [
        "Java Database Connectivity",
        "Java Data Binding Connection",
        "Java Direct Business Controller",
        "Joint Database Connector"
    ],
    "answer": "ক",
    "explanation": "JDBC হলো জাভা প্রোগ্রাম থেকে রিলেশনাল ডেটাবেসে সংযোগ ও এসকিউএল কুয়েরি পরিচালনার স্ট্যান্ডার্ড এপিআই।"
})

sub3_questions_part2.append({
    "id": 185,
    "topic": topic_3_7,
    "question": "জেডিবিসি ড্রাইভারগুলোর মধ্যে ১০০% খাঁটি জাভায় তৈরি সরাসরি ডেটাবেস প্রটোকলে কথা বলা টাইপ কোনটি?",
    "options": ["Type 4 Driver (Thin Driver - Direct Network to DB)", "Type 1 Driver (JDBC-ODBC Bridge)", "Type 2 Driver (Native API)", "Type 3 Driver (Network Protocol)"],
    "answer": "ক",
    "explanation": "টাইপ ৪ ড্রাইভার কোনো ক্লায়েন্ট লাইব্রেরি ছাড়াই সরাসরি ডেটাবেস প্রোটোকলে যোগাযোগ করে এবং সর্বাধিক ব্যবহৃত হয়।"
})

sub3_questions_part2.append({
    "id": 186,
    "topic": topic_3_7,
    "question": "জেডিবিসিতে ডেটাবেস সংযোগ স্থাপনের প্রথম ধাপে ড্রাইভার ক্লাস মেমরিতে লোড করতে কোন মেথড ব্যবহৃত হয়?",
    "options": ["Class.forName(\"driver_class_name\")", "DriverManager.load()", "Connection.start()", "new Driver()"],
    "answer": "ক",
    "explanation": "`Class.forName(\"com.mysql.cj.jdbc.Driver\")` ক্লাসটিকে ডাইনামিকালি লোড ও রেজিস্টার করে।"
})

sub3_questions_part2.append({
    "id": 187,
    "topic": topic_3_7,
    "question": "ডেটাবেস সংযোগ অবজেক্ট (`Connection`) রিটার্ন করে কোন মেথডটি?",
    "options": [
        "DriverManager.getConnection(url, user, password)",
        "Connection.create(url)",
        "Database.open(url)",
        "Class.getConnection(url)"
    ],
    "answer": "ক",
    "explanation": "`DriverManager.getConnection()` ইউআরএল, ইউজারনেম ও পাসওয়ার্ড দিয়ে ডেটাবেস কানেকশন তৈরি করে।"
})

sub3_questions_part2.append({
    "id": 188,
    "topic": topic_3_7,
    "question": "এসকিউএল ইনজেকশন (SQL Injection) আক্রমণ প্রতিরোধ করতে কোন স্টেটমেন্ট ব্যবহার করা বাধ্যতামূলক?",
    "options": [
        "PreparedStatement (প্যারামিটারাইজড কুয়েরি '?' সহ)",
        "Statement",
        "CallableStatement",
        "SimpleStatement"
    ],
    "answer": "ক",
    "explanation": "`PreparedStatement` এসকিউএল কুয়েরি আগে থেকেই প্রি-কম্পাইল করে এবং ব্যবহারকারী ইনপুটকে কোড হিসেবে রান করতে দেয় না।"
})

sub3_questions_part2.append({
    "id": 189,
    "topic": topic_3_7,
    "question": "জেডিবিসিতে ডেটাবেস স্টোর্ড প্রসিডিউর (Stored Procedures) এক্সিকিউট করতে কোনটি ব্যবহৃত হয়?",
    "options": ["CallableStatement", "PreparedStatement", "Statement", "ProcedureStatement"],
    "answer": "ক",
    "explanation": "`CallableStatement` ডেটাবেসের স্টোর্ড প্রসিডিউর এবং ফাংশন কল করতে ব্যবহৃত হয়।"
})

sub3_questions_part2.append({
    "id": 190,
    "topic": topic_3_7,
    "question": "ডাটাবেসে `SELECT` কুয়েরি চালিয়ে ডেটা ফেচ বা পড়ার জন্য কোন মেথডটি কল করতে হয়?",
    "options": ["executeQuery() (যা ResultSet রিটার্ন করে)", "executeUpdate()", "execute()", "fetch()"],
    "answer": "ক",
    "explanation": "`SELECT` কুয়েরির ফলাফল একটি `ResultSet` টেবিল অবজেক্ট আকারে ফিরে আসে `executeQuery()` কলের মাধ্যমে।"
})

sub3_questions_part2.append({
    "id": 191,
    "topic": topic_3_7,
    "question": "ডেটাবেসে `INSERT`, `UPDATE`, বা `DELETE` কুয়েরি এক্সিকিউট করতে কোন মেথড ব্যবহৃত হয়?",
    "options": [
        "executeUpdate() (কতটি রো প্রভাবিত হয়েছে সেই int সংখ্যা রিটার্ন করে)",
        "executeQuery()",
        "executeSelect()",
        "commitQuery()"
    ],
    "answer": "ক",
    "explanation": "`executeUpdate()` ডেটা ম্যানিপুলেশন কুয়েরি রান করে এবং কতটি রেকর্ড পরিবর্তিত হয়েছে তা রিটার্ন করে।"
})

sub3_questions_part2.append({
    "id": 192,
    "topic": topic_3_7,
    "question": "জেডিবিসি `ResultSet` থেকে পরবর্তী রেকর্ডে কার্সর সরাতে কোন মেথড ব্যবহৃত হয়?",
    "options": ["rs.next()", "rs.forward()", "rs.moveToNext()", "rs.hasNext()"],
    "answer": "ক",
    "explanation": "`rs.next()` পরবর্তী রো-তে যায় এবং রো বিদ্যমান থাকলে `true` দেয়; ফলে `while(rs.next())` দিয়ে লুপ চলে।"
})

sub3_questions_part2.append({
    "id": 193,
    "topic": topic_3_7,
    "question": "ডেটাবেস ট্রানজেকশনে সকল পরিবর্তন স্থায়ীভাবে সংরক্ষণ নিশ্চিত করতে কোন মেথড কল করা হয়?",
    "options": ["connection.commit()", "connection.save()", "connection.persist()", "connection.flush()"],
    "answer": "ক",
    "explanation": "`setAutoCommit(false)` করার পর সকল কুয়েরি সফল হলে `commit()` দিয়ে স্থায়ী করতে হয়।"
})

sub3_questions_part2.append({
    "id": 194,
    "topic": topic_3_7,
    "question": "ট্রানজেকশনে কোনো একটি অপারেশন ব্যর্থ হলে পূর্বের সকল পরিবর্তন বাতিল করে ডেটাবেসকে আগের অবস্থায় ফেরাতে কী করতে হয়?",
    "options": ["connection.rollback()", "connection.undo()", "connection.revert()", "connection.cancel()"],
    "answer": "ক",
    "explanation": "`rollback()` মেথড ট্রানজেকশনের অসম্পূর্ণ বা ত্রুটিপূর্ণ পরিবর্তনগুলো বাতিল করে ডেটাবেসের সামঞ্জস্য রক্ষা করে।"
})

sub3_questions_part2.append({
    "id": 195,
    "topic": topic_3_7,
    "question": "জেডিবিসিতে ডেটাবেসের টেবিল কলামের নাম ও ডেটা টাইপ ইত্যাদি মেটাডেটা জানতে কোনটি ব্যবহৃত হয়?",
    "options": ["ResultSetMetaData (rs.getMetaData())", "DatabaseMetaData", "TableMetaData", "ColumnInfo"],
    "answer": "ক",
    "explanation": "`ResultSetMetaData` থেকে কলাম সংখ্যা, কলাম নাম, ডেটা টাইপ ইত্যাদি জানা যায়।"
})

sub3_questions_part2.append({
    "id": 196,
    "topic": topic_3_7,
    "question": "জেডিবিসিতে ডেটাবেসের নাম, ভার্সন ও ড্রাইভার তথ্য জানতে কোন অবজেক্ট ব্যবহৃত হয়?",
    "options": ["DatabaseMetaData (conn.getMetaData())", "ResultSetMetaData", "SystemInfo", "DriverInfo"],
    "answer": "ক",
    "explanation": "`DatabaseMetaData` ডেটাবেস সার্ভারের সামগ্রিক কনফিগারেশন তথ্য প্রদান করে।"
})

sub3_questions_part2.append({
    "id": 197,
    "topic": topic_3_7,
    "question": "জেডিবিসিতে ডেটাবেস সংযোগের জন্য ব্যবহৃত স্ট্যান্ডার্ড URL ফরম্যাট কোনটি?",
    "options": ["jdbc:subprotocol:subname (যেমন jdbc:mysql://localhost:3306/db)", "http://localhost:3306/db", "db://localhost/mysql", "sql:mysql://localhost"],
    "answer": "ক",
    "explanation": "জেডিবিসি ইউআরএল সর্বদা `jdbc:` প্রটোকল দিয়ে শুরু হয়, তারপর সাব-প্রটোকল (যেমন mysql, oracle) থাকে।"
})

sub3_questions_part2.append({
    "id": 198,
    "topic": topic_3_7,
    "question": "জেডিবিসি রিসোর্স যেমন `ResultSet`, `Statement` ও `Connection` ব্যবহারের পর কী করা বাধ্যতামূলক?",
    "options": [
        "close() মেথড দিয়ে মেমরি ও ডেটাবেস সংযোগ মুক্ত করা",
        "কম্পিউটার রিস্টার্ট করা",
        "delete() কল করা",
        "কোনো কিছু করার প্রয়োজন নেই"
    ],
    "answer": "ক",
    "explanation": "সংযোগ খোলা রাখলে ডেটাবেস সার্ভারে কানেকশন লিক ঘটে এবং সার্ভার ক্র্যাশ করতে পারে।"
})

sub3_questions_part2.append({
    "id": 199,
    "topic": topic_3_7,
    "question": "এন্টারপ্রাইজ অ্যাপ্লিকেশনে বারবার সংযোগ তৈরি না করে পূর্বের সংযোগ পুনঃব্যবহার করতে কী প্রযুক্তি ব্যবহৃত হয়?",
    "options": ["কানেকশন পুলিং (Connection Pooling - যেমন HikariCP, DBCP)", "সিঙ্গেল কানেকশন", "স্ট্যাটিক কানেকশন", "থ্রেড লক"],
    "answer": "ক",
    "explanation": "কানেকশন পুলিং আগে থেকেই প্রস্তুত করা সংযোগের পুল বজায় রেখে সিস্টেমের গতি নাটকীয়ভাবে বৃদ্ধি করে।"
})

sub3_questions_part2.append({
    "id": 200,
    "topic": topic_3_7,
    "question": "জাভা সুইং অ্যাপ্লিকেশন তৈরি করার সময় থ্রেড-সেফটি বজায় রাখতে জিইউআই আপডেট কোন থ্রেডে রান করাতে হয়?",
    "options": [
        "ইভেন্ট ডিসপ্যাচ থ্রেড (Event Dispatch Thread - EDT via SwingUtilities.invokeLater)",
        "মেইন থ্রেড (Main Thread)",
        "গার্বেজ কালেক্টর থ্রেড",
        "ব্যাকগ্রাউন্ড ডেমোন থ্রেড"
    ],
    "answer": "ক",
    "explanation": "সুইং কম্পোনেন্টগুলো থ্রেড-সেফ নয়; তাই যেকোনো জিইউআই পরিবর্তন EDT থ্রেডের মাধ্যমে সম্পন্ন করতে হয়।"
})

print(f"Generated Subject 3 Part 2: {len(sub3_questions_part2)} questions")
