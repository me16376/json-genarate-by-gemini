# -*- coding: utf-8 -*-
import json
import os

questions_part2 = [
    # Subtopic 6: Object-Oriented Database (OODB) & Object-Relational (ORDBMS) (101-115)
    {
        "id": 101,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "অবজেক্ট-ওরিয়েন্টেড ডেটাবেজে (OODBMS) প্রতিটি অবজেক্টকে সিস্টেম-ব্যাপী স্বতন্ত্রভাবে শনাক্ত করার জন্য কী ব্যবহৃত হয়?",
        "options": [
            "ক) Primary Key",
            "খ) Object Identifier (OID)",
            "গ) Foreign Key",
            "ঘ) Surrogate Key"
        ],
        "answer": "খ",
        "explanation": "OODBMS-এ প্রতিটি অবজেক্টের একটি ইউনিক, ইমিউটেবল এবং সিস্টেম-জেনারেটেড শনাক্তকারী থাকে যাকে OID (Object Identifier) বলা হয়। এটি অবজেক্টের ভেতরের ডেটা মানের ওপর নির্ভর করে না।"
    },
    {
        "id": 102,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "রিলেশনাল মডেলের তুলনায় অবজেক্ট-ওরিয়েন্টেড মডেলের প্রধান সুবিধা কোনটি?",
        "options": [
            "ক) জটিল ও নেস্টেড ডেটা স্ট্রাকচার (যেমন CAD, GIS, মাল্টিমিডিয়া) সহজেই হ্যান্ডেল করা যায়",
            "খ) রিলেশনাল মডেলের চেয়ে গাণিতিক ভিত্তি সহজ",
            "গ) কোনো কুয়েরি ভাষার প্রয়োজন হয় না",
            "ঘ) টেবিলে কোনো রো থাকে না"
        ],
        "answer": "ক",
        "explanation": "OODBMS জটিল অবজেক্ট, হায়ারার্কিক্যাল সম্পর্ক এবং নন-অ্যাটমিক ডেটা সহজে সাপোর্ট করে যা ট্রেডিশনাল RDBMS-এর ফার্স্ট নরমাল ফর্মের সীমাবদ্ধতায় কঠিন।"
    },
    {
        "id": 103,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "অবজেক্ট-ওরিয়েন্টেড ডেটাবেজে ডেটা এবং সেই ডেটা ম্যানিপুলেট করার ফাংশন/মেথড একসাথে ক্যাপসুল আকারে রাখার নীতিকে কী বলে?",
        "options": [
            "ক) Inheritance",
            "খ) Polymorphism",
            "গ) Encapsulation",
            "ঘ) Persistence"
        ],
        "answer": "গ",
        "explanation": "Encapsulation অবজেক্টের অভ্যন্তরীণ গঠন লুকিয়ে রাখে এবং শুধুমাত্র অনুমোদিত মেথডের মাধ্যমে স্টেট পরিবর্তনের সুযোগ দেয়।"
    },
    {
        "id": 104,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "ঐতিহ্যবাহী রিলেশনাল ডেটাবেজের উপর অবজেক্ট-ওরিয়েন্টেড ফিচার (যেমন ইউজার-ডিফাইন্ড টাইপ, ইনহেরিটেন্স) যুক্ত করে তৈরি করা হাইব্রিড সিস্টেমকে কী বলে?",
        "options": [
            "ক) Network DBMS",
            "খ) Object-Relational DBMS (ORDBMS)",
            "গ) Hierarchical DBMS",
            "ঘ) Flat File System"
        ],
        "answer": "খ",
        "explanation": "ORDBMS (যেমন PostgreSQL, Oracle) হলো এমন একটি ব্যবস্থা যা রিলেশনাল মডেলের টেবিল ও SQL-এর সুবিধাকে অবজেক্ট-ওরিয়েন্টেড ক্ষমতার সাথে সমন্বিত করে।"
    },
    {
        "id": 105,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "SQL:1999 স্ট্যান্ডার্ডে জটিল অবজেক্ট সাপোর্ট করার জন্য নিচের কোন স্ট্রাকচার্ড কালেকশন টাইপ অন্তর্ভুক্ত করা হয়েছে?",
        "options": [
            "ক) ARRAY এবং MULTISET",
            "খ) POINTER এবং STACK",
            "গ) TREE এবং GRAPH",
            "ঘ) QUEUE এবং HEAP"
        ],
        "answer": "ক",
        "explanation": "SQL:1999 এবং পরবর্তী সংস্করণে নন-অ্যাটমিক কালেকশন হিসেবে ARRAY এবং MULTISET টাইপ যুক্ত করে অবজেক্ট-রিলেশনাল মডেল সমৃদ্ধ করা হয়েছে।"
    },
    {
        "id": 106,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "অবজেক্ট ডেটাবেজ ম্যানেজমেন্ট গ্রুপ (ODMG) কর্তৃক প্রস্তাবিত কুয়েরি ভাষার নাম কী?",
        "options": [
            "ক) OQL (Object Query Language)",
            "খ) OOPL",
            "গ) O-SQL",
            "ঘ) ODQL"
        ],
        "answer": "ক",
        "explanation": "ODMG স্ট্যান্ডার্ড অনুযায়ী অবজেক্ট-ওরিয়েন্টেড ডেটাবেজে কুয়েরি করার জন্য OQL (Object Query Language) ডিজাইন করা হয়েছিল যা SQL-এর সমতুল্য।"
    },
    {
        "id": 107,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "ডেটাবেজ অবজেক্টের 'Persistence' বলতে কী বোঝায়?",
        "options": [
            "ক) প্রোগ্রাম চলাকালীন মেমরিতে দ্রুত ডেটা পাঠানো",
            "খ) প্রোগ্রাম বা প্রসেস টার্মিনেট হওয়ার পরেও ডিস্কে অবজেক্টের অস্তিত্ব অক্ষুণ্ণ থাকা",
            "গ) অবজেক্টের নাম পরিবর্তন না হওয়া",
            "ঘ) ইনডেক্স তৈরি না করা"
        ],
        "answer": "খ",
        "explanation": "Persistence নির্দেশ করে যে অবজেক্টটি যে প্রোগ্রাম তৈরি করেছিল তা বন্ধ হয়ে গেলেও অবজেক্টটির স্টেট স্থায়ী ডিস্কে সংরক্ষিত থাকে।"
    },
    {
        "id": 108,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "অবজেক্ট-ওরিয়েন্টেড ডেটাবেজে টাইপ হায়ারার্কিতে (Type Hierarchy) একটি সাব-টাইপ তার সুপার-টাইপ থেকে বৈশিষ্ট্য পাওয়ার প্রক্রিয়াকে কী বলে?",
        "options": [
            "ক) Specialization / Inheritance",
            "খ) Serialization",
            "গ) Partitioning",
            "ঘ) De-normalization"
        ],
        "answer": "ক",
        "explanation": "Inheritance-এর মাধ্যমে সাব-টাইপ তার অভিভাবক ক্লাসের সমস্ত অ্যাট্রিবিউট ও মেথড স্বয়ংক্রিয়ভাবে লাভ করে এবং অতিরিক্ত নিজস্ব বৈশিষ্ট্য যুক্ত করতে পারে।"
    },
    {
        "id": 109,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "রিলেশনাল ডেটাবেজের সাথে অবজেক্ট প্রোগ্রামিংয়ের অমিলকে কম্পিউটার বিজ্ঞানে কী সমস্যা বলা হয়?",
        "options": [
            "ক) Object-Relational Impedance Mismatch",
            "খ) Thread Contention",
            "গ) Normalization Bottleneck",
            "ঘ) Schema Drift"
        ],
        "answer": "ক",
        "explanation": "অবজেক্ট মডেল (ক্লাস, পয়েন্টার, মেথড) এবং রিলেশনাল মডেলের (টেবিল, রো, ফরেন কি) মধ্যে ধারণাগত অমিলকে Impedance Mismatch বলা হয়, যা মেটাতে Hibernate, JPA-র মতো ORM ব্যবহৃত হয়।"
    },
    {
        "id": 110,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "ORDBMS-এ রেফারেন্স টাইপ (Reference Type - REF) মূলত কী কাজে ব্যবহৃত হয়?",
        "options": [
            "ক) অন্য কোনো অবজেক্টের OID নির্দেশ বা লিংক করতে",
            "খ) ভ্যালু কপি করতে",
            "গ) ডিস্ক পার্টিশন ফরম্যাট করতে",
            "ঘ) পাসওয়ার্ড এনক্রিপ্ট করতে"
        ],
        "answer": "ক",
        "explanation": "SQL/ORDBMS-এ `REF` টাইপ একটি নির্দিষ্ট টাইপড টেবিলের অবজেক্টের লজিক্যাল OID ধারণ করে রিলেশনাল পয়েন্টারের মতো কাজ করে।"
    },
    {
        "id": 111,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "ODMG অবজেক্ট মডেলে 'Literal' এবং 'Object'-এর মধ্যে প্রধান পার্থক্য কী?",
        "options": [
            "ক) Literal-এর নিজস্ব কোনো OID থাকে না, কেবল ভ্যালু থাকে",
            "খ) Object-এর কোনো টাইপ থাকে না",
            "গ) Literal কখনো মেমরিতে সংরক্ষিত হয় না",
            "ঘ) Object কোনো মেথড সাপোর্ট করে না"
        ],
        "answer": "ক",
        "explanation": "ODMG-তে Object-এর একটি অনন্য আইডেন্টিফায়ার (OID) থাকে, কিন্তু Literal (যেমন পূর্ণসংখ্যা, স্ট্রিং) হলো অপরিবর্তনীয় মান যার কোনো স্বতন্ত্র OID থাকে না।"
    },
    {
        "id": 112,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "পোস্টগ্রেসকুয়েল (PostgreSQL)-এ ইউজার চাইলে নিজস্ব ডেটা টাইপ এবং ফাংশন তৈরি করতে পারে। এটি কোন মডেলের প্রমাণ?",
        "options": [
            "ক) Pure RDBMS",
            "খ) Object-Relational DBMS (ORDBMS)",
            "গ) Flat File",
            "ঘ) Hierarchical DBMS"
        ],
        "answer": "খ",
        "explanation": "PostgreSQL একটি উন্নত ওপেন সোর্স ORDBMS যা কাস্টম টাইপ, ইনহেরিটেন্স, অপারেটর ওভারলোডিং এবং মেথড সাপোর্ট করে।"
    },
    {
        "id": 113,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "XML এবং JSON ডেটা স্টোর ও কুয়েরি করার ক্ষমতা কোন ধরণের ডেটাবেজ এক্সটেনশনে বেশি ব্যবহৃত হয়?",
        "options": [
            "ক) আধুনিক ORDBMS এবং NoSQL/Document স্টোর",
            "খ) প্রথম প্রজন্মের ফাইল সিস্টেম",
            "গ) নেটওয়ার্ক মডেল",
            "ঘ) কেবল অ্যাসেম্বলি ল্যাঙ্গুয়েজ সিস্টেমে"
        ],
        "answer": "ক",
        "explanation": "আধুনিক ORDBMS (যেমন PostgreSQL-এর JSONB) এবং ডকুমেন্ট স্টোর সেমি-স্ট্রাকচার্ড ডেটা প্রক্রিয়াকরণে ব্যবহৃত হয়।"
    },
    {
        "id": 114,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "OODBMS-এ একাধিক বিভিন্ন ক্লাসের অবজেক্টে একই নামের মেথড কল করলে ভিন্ন ভিন্ন আচরণ করার ক্ষমতাকে কী বলে?",
        "options": [
            "ক) Polymorphism",
            "খ) Inheritance",
            "গ) Encapsulation",
            "ঘ) Normalization"
        ],
        "answer": "ক",
        "explanation": "Polymorphism (বহুরূপতা) রানটাইমে সঠিক মেথড ডিসপ্যাচ করে বিভিন্ন অবজেক্টের জন্য উপযুক্ত কাজ সম্পাদন করে।"
    },
    {
        "id": 115,
        "topic": "Object-Oriented & Object-Relational Databases",
        "question": "OQL (Object Query Language)-এ নেস্টেড স্ট্রাকচারের অ্যাট্রিবিউট অ্যাক্সেস করার জন্য কোন অপারেটর ব্যবহৃত হয়?",
        "options": [
            "ক) ডট (.) বা অ্যারো (->) অপারেটর",
            "খ) হ্যাশ (#)",
            "গ) কোলন (:)",
            "ঘ) ডলার ($)"
        ],
        "answer": "ক",
        "explanation": "অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিংয়ের মতোই OQL-এ পাথ এক্সপ্রেশনে ডট (.) বা অ্যারো (->) ব্যবহার করে অবজেক্টের অভ্যন্তরীণ অ্যাট্রিবিউট বা সম্পর্কিত অবজেক্টে পৌঁছানো হয়।"
    },

    # Subtopic 7: Indexing & Hashing (B-Tree, B+ Tree, Static & Dynamic Hashing) (116-135)
    {
        "id": 116,
        "topic": "Indexing & Hashing",
        "question": "ডেটা ফাইলের প্রতি রেকর্ডের জন্য ইনডেক্স ফাইলে একটি করে এন্ট্রি থাকলে সেই ইনডেক্সকে কী বলা হয়?",
        "options": [
            "ক) Sparse Index (বিরল ইনডেক্স)",
            "খ) Dense Index (ঘন ইনডেক্স)",
            "গ) Secondary Index",
            "ঘ) Hash Index"
        ],
        "answer": "খ",
        "explanation": "Dense Index-এ মূল ফাইলের প্রতিটি সার্চ কি মানের জন্য ইনডেক্স টেবিলে আলাদা এন্ট্রি থাকে। আর Sparse Index-এ কেবল প্রতিটি ব্লকের প্রথম রেকর্ডের এন্ট্রি থাকে।"
    },
    {
        "id": 117,
        "topic": "Indexing & Hashing",
        "question": "মূল ডেটা ফাইলটি যে সার্চ-কি অর্ডারে ফিজিক্যালি ডিস্কে সাজানো থাকে, সেই কি-র ওপর তৈরি ইনডেক্সকে কী বলে?",
        "options": [
            "ক) Clustering Index বা Primary Index",
            "খ) Non-clustering Index",
            "গ) Secondary Index",
            "ঘ) Bitmap Index"
        ],
        "answer": "ক",
        "explanation": "যে ইনডেক্স সার্চ-কি মূল ডেটা ফাইলের ফিজিক্যাল সিকোয়েন্সের সাথে হুবহু মিলে যায় তাকে ক্লাস্টারিং বা প্রাইমারি ইনডেক্স বলে। একটি টেবিলে সর্বোচ্চ একটিই ক্লাস্টার্ড ইনডেক্স থাকতে পারে।"
    },
    {
        "id": 118,
        "topic": "Indexing & Hashing",
        "question": "B+ Tree ডেটা স্ট্রাকচার ডেটাবেজ ইনডেক্সিংয়ের জন্য B-Tree-র চেয়ে বেশি জনপ্রিয় হওয়ার প্রধান কারণ কোনটি?",
        "options": [
            "ক) সমস্ত বাস্তব ডেটা পয়েন্টার কেবল লিফ নোডে (Leaf Nodes) থাকে এবং লিফ নোডগুলো পরস্পরের সাথে লিংকড লিস্ট দ্বারা যুক্ত থাকায় রেঞ্জ কুয়েরি অত্যন্ত দ্রুত হয়",
            "খ) B+ Tree-তে কোনো রুট নোড থাকে না",
            "গ) B+ Tree-র উচ্চতা B-Tree-র চেয়ে অনেক বেশি হয়",
            "ঘ) B+ Tree-তে কোনো ব্যালেন্সিং প্রয়োজন হয় না"
        ],
        "answer": "ক",
        "explanation": "B+ Tree-র অভ্যন্তরীণ নোডে কেবল সার্চ কি থাকে (ডেটা রেকর্ড থাকে না), ফলে ফ্যান-আউট বেশি হয় এবং গাছ কম গভীর হয়। লিফ নোডগুলো ডাবল-লিংকড লিস্ট দিয়ে যুক্ত থাকায় রেঞ্জ কুয়েরি ($k_1 \\le x \\le k_2$) অত্যন্ত দক্ষ।"
    },
    {
        "id": 119,
        "topic": "Indexing & Hashing",
        "question": "অর্ডার $p$ বিশিষ্ট একটি B+ Tree-র প্রতিটি নন-রুট অভ্যন্তরীণ নোডে সর্বনিম্ন কতগুলো চাইল্ড পয়েন্টার থাকতে হবে?",
        "options": [
            "ক) $1$",
            "খ) $\\lceil p/2 \\rceil$",
            "গ) $p-1$",
            "ঘ) $p/4$"
        ],
        "answer": "খ",
        "explanation": "B+ Tree-তে প্রতিটি নন-রুট ইন্টারনাল নোডে ন্যূনতম চাইল্ড সংখ্যা $\\\\lceil p/2 \\\\rceil$ এবং সর্বোচ্চ $p$ টি চাইল্ড থাকতে পারে। এটি ট্রি-র ব্যালেন্স বজায় রাখে।"
    },
    {
        "id": 120,
        "topic": "Indexing & Hashing",
        "question": "একটি B+ Tree-তে $N$ সংখ্যক রেকর্ড থাকলে যেকোনো রেকর্ড খোঁজার সময় জটিলতা (Search Time Complexity) কত?",
        "options": [
            "ক) $O(N)$",
            "খ) $O(1)$",
            "গ) $O(\\log_B N)$",
            "ঘ) $O(N \\log N)$"
        ],
        "answer": "গ",
        "explanation": "B+ Tree সম্পূর্ণ ব্যালেন্সড ট্রি এবং এর ব্রাঞ্চিং ফ্যাক্টর (ফ্যান-আউট) $B$ অনেক বড় হওয়ায় এর অনুসন্ধান সময় $O(\\\\log_B N)$, যা সাধারণ বাইনারি ট্রির চেয়ে অনেক দ্রুত।"
    },
    {
        "id": 121,
        "topic": "Indexing & Hashing",
        "question": "স্ট্যাটিক হ্যাশিংয়ে (Static Hashing) যদি একটি বাকেটে (Bucket) নতুন রেকর্ড ঢোকানোর জায়গা না থাকে, তখন কী ঘটে?",
        "options": [
            "ক) Bucket Overflow (ওভারফ্লো চেইনিং প্রয়োজন হয়)",
            "খ) স্বয়ংক্রিয়ভাবে পুরো ডেটাবেজ ফরম্যাট হয়ে যায়",
            "গ) হ্যাশ ফাংশন বদলে যায়",
            "ঘ) রেকর্ডটি বাদ পড়ে যায়"
        ],
        "answer": "ক",
        "explanation": "বাকেট ধারণক্ষমতা অতিক্রম করলে বাকেট ওভারফ্লো ঘটে, যা সামলাতে ওভারফ্লো বাকেট লিঙ্ক করা হয় (Overflow Chaining)।"
    },
    {
        "id": 122,
        "topic": "Indexing & Hashing",
        "question": "এক্সটেন্ডিবল হ্যাশিং (Extendible Hashing)-এ বাকেট বিভাজনের সময় বাকেটের কোন প্যারামিটারটি ১ বৃদ্ধি পায়?",
        "options": [
            "ক) Global Depth",
            "খ) Local Depth ($d'$)",
            "গ) Hash Index Factor",
            "ঘ) Modulo Count"
        ],
        "answer": "খ",
        "explanation": "এক্সটেন্ডিবল হ্যাশিংয়ে ওভারফ্লো হওয়া বাকেটের Local Depth এক বাড়ে ($d' + 1$)। যদি নতুন লোকাল ডেপথ গ্লোবাল ডেপথ ($d$) এর চেয়ে বড় হয়ে যায়, তবে ডিরেক্টরি দ্বিগুণ হয়ে গ্লোবাল ডেপথও বৃদ্ধি পায়।"
    },
    {
        "id": 123,
        "topic": "Indexing & Hashing",
        "question": "এক্সটেন্ডিবল হ্যাশিং ডিরেক্টরির গ্লোবাল ডেপথ $d$ হলে ডিরেক্টরিতে মোট এন্ট্রির সংখ্যা কত?",
        "options": [
            "ক) $d$",
            "খ) $2^d$",
            "গ) $d^2$",
            "ঘ) $2 \\times d$"
        ],
        "answer": "খ",
        "explanation": "গ্লোবাল ডেপথ $d$ নির্দেশ করে হ্যাশ ভ্যালুর প্রথম $d$-টি বিট ডিরেক্টরি ইনডেক্সিংয়ে ব্যবহৃত হচ্ছে, ফলে মোট ডিরেক্টরি সাইজ হয় $2^d$।"
    },
    {
        "id": 124,
        "topic": "Indexing & Hashing",
        "question": "লিনিয়ার হ্যাশিং (Linear Hashing) এবং এক্সটেন্ডিবল হ্যাশিংয়ের মধ্যে মূল পার্থক্য কোনটি?",
        "options": [
            "ক) লিনিয়ার হ্যাশিংয়ে কোনো অতিরিক্ত ডিরেক্টরি (Directory-less) লাগে না এবং বাকেটগুলো ক্রমানুসারে বিভক্ত হয়",
            "খ) এক্সটেন্ডিবল হ্যাশিংয়ে হ্যাশ ফাংশন লাগে না",
            "গ) লিনিয়ার হ্যাশিং রেঞ্জ কুয়েরি সাপোর্ট করে",
            "ঘ) এদের মধ্যে কোনো পার্থক্য নেই"
        ],
        "answer": "ক",
        "explanation": "লিনিয়ার হ্যাশিং একটি ডিরেক্টরিবিহীন ডাইনামিক হ্যাশিং কৌশল যেখানে ওভারফ্লো বাকেট যুক্ত হলে একটি নির্দিষ্ট পয়েন্টার ($p$) অনুযায়ী ক্রমান্বয়ে পরবর্তী বাকেট বিভক্ত হয়।"
    },
    {
        "id": 125,
        "topic": "Indexing & Hashing",
        "question": "হ্যাশ ইনডেক্সিং কোন ধরণের কুয়েরির জন্য অত্যন্ত কার্যকরী কিন্তু কোন ধরণের কুয়েরির জন্য অকার্যকর?",
        "options": [
            "ক) রেঞ্জ কুয়েরির জন্য সেরা, কিন্তু পয়েন্ট কুয়েরিতে অকার্যকর",
            "খ) পয়েন্ট কুয়েরি (Exact match, $key = val$) এর জন্য $O(1)$ সেরা, কিন্তু রেঞ্জ কুয়েরির ($k_1 \\le x \\le k_2$) জন্য সম্পূর্ণ অকার্যকর",
            "গ) উভয় কুয়েরির জন্যই সমান কার্যকরী",
            "ঘ) সর্টিং করার জন্য সেরা"
        ],
        "answer": "খ",
        "explanation": "হ্যাশিং গাণিতিক সূত্রে সরাসরি ঠিকানা বের করে তাই সমতার কুয়েরিতে $O(1)$ গতি দেয়। তবে ডেটা ক্রমানুসারে সাজানো থাকে না বলে রেঞ্জ কুয়েরিতে ফুল টেবিল স্ক্যান করতে হয়।"
    },
    {
        "id": 126,
        "topic": "Indexing & Hashing",
        "question": "মাল্টি-লেভেল ইনডেক্সিংয়ের সবচেয়ে ভেতরের বা নিচের লেভেলটি সাধারণত কী ধরণের ইনডেক্স হয়?",
        "options": [
            "ক) Primary Sparse Index",
            "খ) Primary Dense Index",
            "গ) Secondary Non-key Index",
            "ঘ) B+ Tree Root"
        ],
        "answer": "খ",
        "explanation": "মাল্টিলেভেল ইনডেক্সে প্রথম স্তরটি সাধারণত বেস ডেটা ফাইলের ওপর Dense Index থাকে এবং পরবর্তী উচ্চ স্তরগুলো Sparse Index হিসেবে সেই ইনডেক্স ফাইলের ওপর কাজ করে।"
    },
    {
        "id": 127,
        "topic": "Indexing & Hashing",
        "question": "বিটম্যাপ ইনডেক্সিং (Bitmap Indexing) কোন ধরণের কলামের জন্য সবচেয়ে বেশি উপযোগী?",
        "options": [
            "ক) অত্যন্ত উচ্চ কার্ডিনালিটি বিশিষ্ট কলাম (যেমন ন্যাশনাল আইডি, ফোন নম্বর)",
            "খ) নিম্ন কার্ডিনালিটি বিশিষ্ট কলাম (Low Cardinality, যেমন জেন্ডার, বৈবাহিক অবস্থা, রক্তের গ্রুপ)",
            "গ) দীর্ঘ টেক্সট বা প্যারাগ্রাফ কলাম",
            "ঘ) ভাসমান দশমিক সংখ্যা"
        ],
        "answer": "খ",
        "explanation": "যেসব কলামে মাত্র কয়েকটি স্বতন্ত্র মান থাকে (Low Cardinality), সেগুলোতে বিট অ্যারে (০ এবং ১) দিয়ে তৈরি Bitmap Index অত্যন্ত কম জায়গা নেয় এবং দ্রুত বিটওয়াইজ AND/OR কুয়েরি সম্পন্ন করে।"
    },
    {
        "id": 128,
        "topic": "Indexing & Hashing",
        "question": "একটি টেবিলের একাধিক কলামের ওপর যৌথভাবে তৈরি করা ইনডেক্সকে কী বলা হয়?",
        "options": [
            "ক) Composite Index বা Concatenated Index",
            "খ) Clustered Index",
            "গ) Sparse Index",
            "ঘ) Hash Index"
        ],
        "answer": "ক",
        "explanation": "যখন দুটি বা ততোধিক কলামকে একসাথে নিয়ে একটি ইনডেক্স তৈরি করা হয় (যেমন `CREATE INDEX idx ON emp(dept_id, salary)`), তাকে Composite বা Compound Index বলে।"
    },
    {
        "id": 129,
        "topic": "Indexing & Hashing",
        "question": "B-Tree-র প্রতিটি নোডে কি এবং চাইল্ড পয়েন্টারের সংখ্যার সম্পর্ক কী?",
        "options": [
            "ক) নোডে $k$ টি কি থাকলে চাইল্ড পয়েন্টার থাকবে $k+1$ টি",
            "খ) নোডে $k$ টি কি থাকলে চাইল্ড পয়েন্টার থাকবে $k$ টি",
            "গ) নোডে $k$ টি কি থাকলে চাইল্ড পয়েন্টার থাকবে $2k$ টি",
            "ঘ) কোনো নির্দিষ্ট সম্পর্ক নেই"
        ],
        "answer": "ক",
        "explanation": "সার্চ কি ভ্যালুগুলো চাইল্ড পয়েন্টারগুলোর মাঝখানে বিভাজক হিসেবে থাকে, তাই $k$ টি কী-র জন্য ঠিক $k+1$ টি সাব-ট্রি পয়েন্টার থাকে।"
    },
    {
        "id": 130,
        "topic": "Indexing & Hashing",
        "question": "হ্যাশ ফাংশনের আদর্শ বৈশিষ্ট্য কোনটি?",
        "options": [
            "ক) সমস্ত কি-কে একই বাকেটে পাঠানো",
            "খ) কি-গুলোকে সমস্ত বাকেটের মধ্যে সমানভাবে (Uniform Distribution) ও দৈবচয়নভাবে (Random Distribution) বণ্টন করা",
            "গ) প্রতিটি কলের জন্য আলাদা ফল দেওয়া",
            "ঘ) আউটপুট সাইজ সীমাহীন বড় হওয়া"
        ],
        "answer": "খ",
        "explanation": "একটি ভালো হ্যাশ ফাংশন সমস্ত সার্চ কি ভ্যালুকে বাকেট রেঞ্জের ওপর সমানভাবে ও সুষমভাবে ছড়িয়ে দেয় যেন বাকেট ওভারফ্লো ও কোলিশন সর্বনিম্ন থাকে।"
    },
    {
        "id": 131,
        "topic": "Indexing & Hashing",
        "question": "সেকেন্ডারি ইনডেক্স (Secondary Index) সর্বদা কোন ধরণের ইনডেক্স হতে বাধ্য?",
        "options": [
            "ক) Sparse Index",
            "খ) Dense Index",
            "গ) Dynamic Hash Index",
            "ঘ) Non-unique Index"
        ],
        "answer": "খ",
        "explanation": "যেহেতু সেকেন্ডারি ইনডেক্সের কি অনুযায়ী ডেটা ফাইল ফিজিক্যালি সর্ট করা থাকে না, তাই প্রতিটি রেকর্ডের সঠিক অবস্থান নিশ্চিত করতে এটি অবশ্যই Dense Index হতে হয়।"
    },
    {
        "id": 132,
        "topic": "Indexing & Hashing",
        "question": "B+ Tree-তে নতুন কি ইনসার্ট করার সময় লিফ নোড পূর্ণ থাকলে কী ঘটে?",
        "options": [
            "ক) নোডটি স্প্লিট (Split) হয়ে দুটি নোডে বিভক্ত হয় এবং মাঝের কী-র কপি প্যারেন্ট নোডে পাঠানো হয়",
            "খ) ইনসার্ট অপারেশন বন্ধ হয়ে যায়",
            "গ) পুরোনো কি স্বয়ংক্রিয়ভাবে ডিলিট হয়ে যায়",
            "ঘ) ট্রি-র উচ্চতা প্রতিবার দ্বিগুণ হয়"
        ],
        "answer": "ক",
        "explanation": "নোড পূর্ণ হলে নোডটিকে অর্ধেক করে দুটি নতুন নোড তৈরি করা হয় এবং বিভক্তকারী কী-র একটি কপি প্যারেন্ট নোডে পুশ আপ করা হয়।"
    },
    {
        "id": 133,
        "topic": "Indexing & Hashing",
        "question": "কোনো কুয়েরি যদি টেবিলের ডেটা ব্লকে না গিয়ে কেবলমাত্র ইনডেক্স থেকেই সমস্ত কাঙ্ক্ষিত কলামের উত্তর দিয়ে দিতে পারে, তবে সেই ইনডেক্সকে কী বলে?",
        "options": [
            "ক) Covering Index",
            "খ) Dense Index",
            "গ) Primary Index",
            "ঘ) Bitmap Index"
        ],
        "answer": "ক",
        "explanation": "Covering Index এমন একটি ইনডেক্স যাতে কুয়েরির SELECT এবং WHERE ক্লজের সমস্ত কলাম বিদ্যমান থাকে, ফলে মূল টেবিলে ডিস্ক I/O এক্সেসের প্রয়োজন হয় না।"
    },
    {
        "id": 134,
        "topic": "Indexing & Hashing",
        "question": "অতিরিক্ত ইনডেক্স তৈরির প্রধান নেতিবাচক দিক (Drawback) কোনটি?",
        "options": [
            "ক) SELECT কুয়েরি ধীর হয়",
            "খ) INSERT, UPDATE, DELETE অপারেশনের সময় প্রতিবার ইনডেক্স আপডেট করতে হয় বিধায় রাইট পারফরম্যান্স কমে যায় এবং অতিরিক্ত ডিস্ক স্পেস লাগে",
            "গ) ডেটাবেজ লক হয়ে যায়",
            "ঘ) ব্যাকআপ নেওয়া অসম্ভব হয়ে পড়ে"
        ],
        "answer": "খ",
        "explanation": "ইনডেক্স রিড অপারেশন দ্রুত করলেও প্রতিবার ডেটা মডিফিকেশনের (DML) সময় সংশ্লিষ্ট সকল ইনডেক্স ট্রি আপডেট ও রি-ব্যালেন্স করতে হয়, যা রাইট পারফরম্যান্সে ওভারহেড তৈরি করে।"
    },
    {
        "id": 135,
        "topic": "Indexing & Hashing",
        "question": "একটি B+ Tree-র উচ্চতা (Height) বৃদ্ধি পায় কখন?",
        "options": [
            "ক) প্রতিবার যেকোনো লিফ নোড বিভক্ত হলে",
            "খ) যখন রুট নোডটি স্প্লিট হয়ে দুটি নোড তৈরি করে এবং তাদের উপরে একটি নতুন রুট নোড যুক্ত হয়",
            "গ) যখন ডেটা ডিলিট করা হয়",
            "ঘ) প্রতি ১০০টি ইনসার্টেশনের পর"
        ],
        "answer": "খ",
        "explanation": "B+ Tree সর্বদা নিচ থেকে উপরের দিকে বৃদ্ধি পায়। যখন সর্বোচ্চ রুট নোড উপচে গিয়ে স্প্লিট হয়, তখনই কেবল ট্রি-র উচ্চতা ১ স্তর বৃদ্ধি পায়।"
    },

    # Subtopic 8: Query Processing & Optimization (Cost estimation, selection/join algorithms) (136-150)
    {
        "id": 136,
        "topic": "Query Processing & Optimization",
        "question": "DBMS-এ কুয়েরি প্রসেসিংয়ের প্রধান তিনটি ধাপের সঠিক ক্রম কোনটি?",
        "options": [
            "ক) Optimization -> Parsing -> Execution",
            "খ) Parsing and Translation -> Query Optimization -> Query Execution (Evaluation)",
            "গ) Evaluation -> Optimization -> Parsing",
            "ঘ) Translation -> Indexing -> Scanning"
        ],
        "answer": "খ",
        "explanation": "প্রথমে SQL পার্স ও সিনট্যাক্স চেক করে রিলেশনাল অ্যালজেবরা এক্সপ্রেশনে রূপান্তর করা হয়, তারপর অপটিমাইজার সবচেয়ে কম খরচের এক্সিকিউশন প্ল্যান তৈরি করে এবং পরিশেষে ইঞ্জিন তা রান করে।"
    },
    {
        "id": 137,
        "topic": "Query Processing & Optimization",
        "question": "হিউরিস্টিক কুয়েরি অপটিমাইজেশনের (Heuristic Optimization) সবচেয়ে গুরুত্বপূর্ণ সোনালী নিয়ম কোনটি?",
        "options": [
            "ক) Selection ($\\sigma$) এবং Projection ($\\Pi$) অপারেশনগুলোকে এক্সপ্রেশন ট্রির যতদূর সম্ভব নিচের দিকে পুশ করা (Perform Selection/Projection Early)",
            "খ) কার্টেশিয়ান প্রোডাক্ট সবার আগে করা",
            "গ) সমস্ত জয়েন শেষে ফিল্টারিং করা",
            "ঘ) কোনো ইনডেক্স ব্যবহার না করা"
        ],
        "answer": "ক",
        "explanation": "শুরুতেই Selection এবং Projection প্রয়োগ করলে মধ্যবর্তী রিলেশনের আকার (টাপল ও কলাম সংখ্যা) বহুলাংশে হ্রাস পায়, যার ফলে পরবর্তী ব্যয়বহুল জয়েন অপারেশনের খরচ নাটকীয়ভাবে কমে যায়।"
    },
    {
        "id": 138,
        "topic": "Query Processing & Optimization",
        "question": "কুয়েরি অপটিমাইজার বিভিন্ন এক্সিকিউশন প্ল্যানের খরচ পরিমাপে মূলত কোন বিষয়টিকে প্রধান উপাদান হিসেবে বিবেচনা করে?",
        "options": [
            "ক) ইন্টারনেট ব্রাউজারের স্পিড",
            "খ) ডিস্ক ব্লক এক্সেসের সংখ্যা (Number of Disk Block I/O Operations)",
            "গ) কুয়েরির অক্ষরের দৈর্ঘ্য",
            "ঘ) ইউজারের পাসওয়ার্ড লেন্থ"
        ],
        "answer": "খ",
        "explanation": "যেহেতু মেমরির তুলনায় সেকেন্ডারি স্টোরেজ (ডিস্ক) এক্সেস হাজার গুণ ধীর, তাই কুয়েরি অপটিমাইজেশন খরচের প্রধানতম মেট্রিক হলো মোট ডিস্ক ব্লক রিড/রাইট সংখ্যা।"
    },
    {
        "id": 139,
        "topic": "Query Processing & Optimization",
        "question": "রিলেশন $R$ (যার ব্লক সংখ্যা $B_r$) এবং $S$ (যার ব্লক সংখ্যা $B_s$)। সাধারণ নেস্টেড-লুপ জয়েনে (Nested-Loop Join) সবচেয়ে খারাপ ক্ষেত্রে ডিস্ক ব্লক I/O খরচ কত?",
        "options": [
            "ক) $B_r + B_s$",
            "খ) $B_r + |R| \\times B_s$ (যেখানে $|R|$ হলো $R$-এর টাপল সংখ্যা)",
            "গ) $B_r \\times B_s$",
            "ঘ) $\\log (B_r + B_s)$"
        ],
        "answer": "খ",
        "explanation": "সাধারণ টাপল-বেসড নেস্টেড লুপে আউটার রিলেশনের প্রতিটি সারির জন্য পুরো ইনার রিলেশন ডিস্ক থেকে পড়তে হয়, ফলে মোট খরচ দাঁড়ায় $B_r + |R| \\\\times B_s$।"
    },
    {
        "id": 140,
        "topic": "Query Processing & Optimization",
        "question": "ব্লক নেস্টেড-লুপ জয়েনে (Block Nested-Loop Join) বাফার মেমরির সুবিধা নিয়ে ব্লক I/O খরচ কমিয়ে কত করা যায়?",
        "options": [
            "ক) $B_r + B_r \\times B_s$",
            "খ) $B_r + B_s$",
            "গ) $B_r + \\lceil B_r / (M - 2) \\rceil \\times B_s$ (যেখানে $M$ হলো বাফার ফ্রেম সংখ্যা)",
            "ঘ) $M \\times (B_r + B_s)$"
        ],
        "answer": "গ",
        "explanation": "ব্লক নেস্টেড লুপে আউটার টেবিলের $M-2$ টি ব্লক একবারে মেমরিতে ক্যাশ করে ইনার টেবিলের সাথে মেলানো হয়, ফলে ইনার টেবিল স্ক্যান করার সংখ্যা বহুলাংশে কমে যায়।"
    },
    {
        "id": 141,
        "topic": "Query Processing & Optimization",
        "question": "দুটি রিলেশন যদি তাদের জয়েন অ্যাট্রিবিউটের ওপর পূর্ব থেকেই সর্ট করা থাকে, তবে সবচেয়ে দ্রুততম জয়েন অ্যালগরিদম কোনটি?",
        "options": [
            "ক) Nested-Loop Join",
            "খ) Sort-Merge Join",
            "গ) Hash Join",
            "ঘ) Cartesian Join"
        ],
        "answer": "খ",
        "explanation": "উভয় টেবিল যদি জয়েন কলামের ওপর সাজানো থাকে, তবে Sort-Merge Join প্রতিটি টেবিলকে একবার স্ক্যান করেই ($O(B_r + B_s)$ খরচে) সমস্ত মিল খুঁজে বের করতে পারে।"
    },
    {
        "id": 142,
        "topic": "Query Processing & Optimization",
        "question": "অত্যন্ত বৃহৎ টেবিলের ক্ষেত্রে ন্যাচারাল বা ইকুই-জয়েন সম্পন্ন করতে আধুনিক RDBMS-এ কোন অ্যালগরিদমটি সর্বাধিক ব্যবহৃত হয়?",
        "options": [
            "ক) Grace Hash Join",
            "খ) Bubble Join",
            "গ) Linear Scan",
            "ঘ) Brute Force"
        ],
        "answer": "ক",
        "explanation": "Hash Join (বিশেষ করে Grace Hash Join) উভয় টেবিলের জয়েন কি-র ওপর একই হ্যাশ ফাংশন চালিয়ে পার্টিশনে বিভক্ত করে এবং মেমরিতে বাকেট ধরে জয়েন করে অত্যন্ত দ্রুত ফলাফল দেয়।"
    },
    {
        "id": 143,
        "topic": "Query Processing & Optimization",
        "question": "কুয়েরি কস্ট অনুমানে সিস্টেম ক্যাটালগ থেকে কোন পরিসংখ্যানগত তথ্য (Catalog Statistics) ব্যবহৃত হয়?",
        "options": [
            "ক) টাপলের মোট সংখ্যা ($n_r$), ব্লকের সংখ্যা ($b_r$), কলামের ডিস্ট্রিবিউশন ও ইউনিক মানের সংখ্যা ($V(A, r)$)",
            "খ) ইউজারের জন্মতারিখ",
            "গ) মনিটরের রেজোলিউশন",
            "ঘ) নেটওয়ার্ক ম্যাক অ্যাড্রেস"
        ],
        "answer": "ক",
        "explanation": "অপটিমাইজার প্রতিটি অপারেশনের সিলেক্টিভিটি (Selectivity factor) হিসাব করতে ক্যাটালগে থাকা সাইজ, ডিস্ক ব্লক, স্বতন্ত্র মানের সংখ্যা এবং হিস্টোগ্রাম ব্যবহার করে।"
    },
    {
        "id": 144,
        "topic": "Query Processing & Optimization",
        "question": "রিলেশনাল অ্যালজেবরায় জয়েন অপারেশনের কোন গাণিতিক বৈশিষ্ট্য কুয়েরি ট্রির পুনর্বিন্যাসে অপটিমাইজার ব্যবহার করে?",
        "options": [
            "ক) জয়েন অপারেশন Commutative এবং Associative উভয়ই ($R \\bowtie S = S \\bowtie R$ এবং $(R \\bowtie S) \\bowtie T = R \\bowtie (S \\bowtie T)$)",
            "খ) জয়েন অপারেশন শুধুমাত্র Distributive",
            "গ) জয়েন কখনো রিভার্স করা যায় না",
            "ঘ) জয়েন কেবল একটি টেবিলে হয়"
        ],
        "answer": "ক",
        "explanation": "জয়েন বিনিময়যোগ্য (Commutative) এবং সংযোগী (Associative) হওয়ায় অপটিমাইজার টেবিলগুলোর জয়েন অর্ডার পরিবর্তন করে সবচেয়ে ছোট আকারের মধ্যবর্তী টেবিল আগে তৈরি করতে পারে।"
    },
    {
        "id": 145,
        "topic": "Query Processing & Optimization",
        "question": "কুয়েরি অপটিমাইজারে 'Pipelining' বলতে কী বোঝায়?",
        "options": [
            "ক) ইন্টারমিডিয়েট ফলাফল ডিস্কে সংরক্ষণ না করে একটি অপারেশনের আউটপুট সরাসরি পরবর্তী অপারেশনে স্ট্রিম আকারে পাঠানো",
            "খ) সম্পূর্ণ টেবিল হার্ডডিস্কে ডাম্প করা",
            "গ) ফাইল কম্প্রেস করা",
            "ঘ) একাধিক কুয়েরি বাতিল করা"
        ],
        "answer": "ক",
        "explanation": "Pipelining-এ অন্তর্বর্তী ফলাফল ডিস্কে না লিখে মেমরি পাইপের মধ্য দিয়ে সরাসরি পরবর্তী অপারেশনে পাঠানো হয়, যা ডিস্ক I/O এবং মেমরি ব্যবহার বাঁচায়।"
    },
    {
        "id": 146,
        "topic": "Query Processing & Optimization",
        "question": "Materialization কৌশলের বৈশিষ্ট্য কোনটি?",
        "options": [
            "ক) কোনো মেমরি ব্যবহার করে না",
            "খ) অপারেশনের মধ্যবর্তী ফলাফলকে ডিস্কে একটি অস্থায়ী রিলেশন হিসেবে সম্পূর্ণরূপে তৈরি ও সংরক্ষণ করে পরবর্তী অপারেশনে ইনপুট দেওয়া হয়",
            "গ) এটি পাইপলাইনিংয়ের চেয়ে সর্বদাই দ্রুত",
            "ঘ) এটি কেবল সিলেকশনে চলে"
        ],
        "answer": "খ",
        "explanation": "Materialization পদ্ধতিতে প্রতিটি সাব-অপারেশনের ফলাফল সম্পূর্ণরূপে একটি অস্থায়ী টেবিলে ডিস্কে তৈরি (Materialized) করা হয় এবং পরবর্তী অপারেটর তা রিড করে।"
    },
    {
        "id": 147,
        "topic": "Query Processing & Optimization",
        "question": "একটি কলাম $A$-র ওপর সমতা শর্তে সিলেকশন $\\sigma_{A=v}(r)$ এর সিলেক্টিভিটি ফ্যাক্টর (Selectivity Factor) কত ধরা হয়, যদি মানের সুষম বণ্টন (Uniform distribution) থাকে?",
        "options": [
            "ক) $1 / V(A, r)$",
            "খ) $V(A, r) / n_r$",
            "গ) $n_r$",
            "ঘ) $1 / n_r^2$"
        ],
        "answer": "ক",
        "explanation": "যদি কলামে $V(A, r)$ সংখ্যক স্বতন্ত্র মান থাকে এবং সেগুলো সমভাবে বণ্টিত থাকে, তবে যেকোনো একটি মানের জন্য ম্যাচ করার সম্ভাবনা বা সিলেক্টিভিটি হলো $1 / V(A, r)$।"
    },
    {
        "id": 148,
        "topic": "Query Processing & Optimization",
        "question": "একটি SQL কুয়েরির এক্সিকিউশন প্ল্যান (Execution Plan) দেখার জন্য স্ট্যান্ডার্ড ডেটাবেজ কমান্ড কোনটি?",
        "options": [
            "ক) SHOW PLAN বা EXPLAIN SELECT ...",
            "খ) DEBUG QUERY",
            "গ) PRINT EXECUTION",
            "ঘ) LOG QUERY"
        ],
        "answer": "ক",
        "explanation": "SQL-এ `EXPLAIN` বা `EXPLAIN ANALYZE` কমান্ড ব্যবহার করে অপটিমাইজারের নির্বাচিত এক্সিকিউশন প্ল্যান, ইনডেক্স স্ক্যান, জয়েন মেথড এবং কস্ট দেখা যায়।"
    },
    {
        "id": 149,
        "topic": "Query Processing & Optimization",
        "question": "ইন্ডেক্স স্ক্যান (Index Scan) কখন ফুল টেবিল স্ক্যানের (Full Table Scan) চেয়ে ধীর হতে পারে?",
        "options": [
            "ক) যখন টেবিলটি অত্যন্ত ছোট হয় অথবা সিলেকশনে টেবিলের অধিকাংশ (> 20-30%) রো রিটার্ন করে",
            "খ) যখন টেবিলে কোনো প্রাইমারি কি থাকে না",
            "গ) যখন মেমরি অনেক বেশি থাকে",
            "ঘ) ইনডেক্স স্ক্যান কখনো ধীর হতে পারে না"
        ],
        "answer": "ক",
        "explanation": "যদি কুয়েরিতে টেবিলের বিশাল অংশের রো প্রয়োজন হয়, তবে ইনডেক্স থেকে বারবার আন-ক্লাস্টার্ড ডেটা পেজে জাম্প করার চেয়ে সিকোয়েনশিয়াল ফুল টেবিল স্ক্যান অনেক দ্রুত হয়।"
    },
    {
        "id": 150,
        "topic": "Query Processing & Optimization",
        "question": "ডাইনামিক প্রোগ্রামিং ভিত্তিক System-R অপটিমাইজেশন অ্যালগরিদমে কোন আকারের জয়েন ট্রি বিবেচনা করে স্পেস কমানো হয়?",
        "options": [
            "ক) Left-deep Join Tree",
            "খ) Bushy Tree",
            "গ) Right-deep Tree",
            "ঘ) Star Tree"
        ],
        "answer": "ক",
        "explanation": "সিস্টেম-আর স্টাইলের অপটিমাইজার মূলত Left-deep Join Trees বিবেচনা করে, যার ফলে পাইপলাইনিং কার্যকর করা সহজ হয় এবং সার্চ স্পেস পরিমিত থাকে।"
    },

    # Subtopic 9: Transactions & Concurrency Control (ACID, Serializability, 2PL, Deadlock) (151-170)
    {
        "id": 151,
        "topic": "Transactions & Concurrency Control",
        "question": "ডেটাবেজ ট্রানজ্যাকশনের ACID প্রোপার্টিজ কোন চারটি বৈশিষ্ট্য নিয়ে গঠিত?",
        "options": [
            "ক) Accuracy, Consistency, Integrity, Durability",
            "খ) Atomicity, Consistency, Isolation, Durability",
            "গ) Authentication, Concurrency, Isolation, Distribution",
            "ঘ) Availability, Consistency, Isolation, Diversity"
        ],
        "answer": "খ",
        "explanation": "ACID হলো ডেটাবেজ লেনদেনের মূল ভিত্তি: Atomicity (সব বা কিছুই না), Consistency (নিয়ম মেনে চলা), Isolation (পরস্পর বিচ্ছিন্নতা) এবং Durability (স্থায়িত্ব)।"
    },
    {
        "id": 152,
        "topic": "Transactions & Concurrency Control",
        "question": "'একটি ট্রানজ্যাকশনের সমস্ত অপারেশন সফলভাবে সম্পন্ন হবে, নয়তো কোনো পরিবর্তনই ডেটাবেজে সংরক্ষিত হবে না (All or Nothing)'—এটি কোন বৈশিষ্ট্য?",
        "options": [
            "ক) Atomicity (পরমাণুতা)",
            "খ) Consistency",
            "গ) Isolation",
            "ঘ) Durability"
        ],
        "answer": "ক",
        "explanation": "Atomicity নিশ্চিত করে ট্রানজ্যাকশনটি একটি অবিভাজ্য একক হিসেবে কাজ করে। মাঝপথে ফেইল করলে সম্পূর্ণ কাজ রোলব্যাক (Rollback/Abort) হয়ে আগের অবস্থায় ফিরে যায়।"
    },
    {
        "id": 153,
        "topic": "Transactions & Concurrency Control",
        "question": "ট্রানজ্যাকশন সফলভাবে COMMIT হওয়ার পর সিস্টেম ক্র্যাশ করলেও তার ডেটা ডিস্কে সুরক্ষিত ও স্থায়ী থাকার নিশ্চয়তা কে দেয়?",
        "options": [
            "ক) Durability",
            "খ) Isolation",
            "গ) Atomicity",
            "ঘ) Availability"
        ],
        "answer": "ক",
        "explanation": "Durability নিশ্চিত করে যে একবার ট্রানজ্যাকশন সফলভাবে কমিক হয়ে গেলে বিদ্যুৎ চলে গেলেও বা ওএস ক্র্যাশ করলেও ডেটা নষ্ট হবে না।"
    },
    {
        "id": 154,
        "topic": "Transactions & Concurrency Control",
        "question": "ট্রানজ্যাকশনের লাইফসাইকেলে স্টেটগুলোর সঠিক ক্রম কোনটি?",
        "options": [
            "ক) Active -> Partially Committed -> Committed",
            "খ) Committed -> Active -> Failed",
            "গ) Failed -> Partially Committed -> Active",
            "ঘ) Aborted -> Committed -> Active"
        ],
        "answer": "ক",
        "explanation": "ট্রানজ্যাকশন শুরু হলে Active স্টেটে থাকে, শেষ স্টেটমেন্টের পর Partially Committed হয়, এবং ডিস্কে লগ রাইট সফল হলে Committed স্টেটে পৌঁছায়। ব্যর্থ হলে Failed এবং পরে Aborted হয়।"
    },
    {
        "id": 155,
        "topic": "Transactions & Concurrency Control",
        "question": "একটি ট্রানজ্যাকশন চলাকালীন অপর ট্রানজ্যাকশনের অসম্পূর্ণ/আনকমিটেড ডেটা রিড করার ফলে তৈরি হওয়া ত্রুটিকে কী বলে?",
        "options": [
            "ক) Lost Update Problem",
            "খ) Dirty Read Problem (বা Temporary Update)",
            "গ) Inconsistent Analysis",
            "ঘ) Phantom Read"
        ],
        "answer": "খ",
        "explanation": "Dirty Read ঘটে যখন $T_1$ একটি ডেটা পরিবর্তন করে কিন্তু এখনো Commit করেনি, এবং সেই মুহূর্তে $T_2$ সেই মানটি রিড করে। পরে $T_1$ রোলব্যাক করলে $T_2$-র রিড করা ডেটা অবৈধ হয়ে যায়।"
    },
    {
        "id": 156,
        "topic": "Transactions & Concurrency Control",
        "question": "দুটি অপারেশনের মধ্যে কনফ্লিক্ট (Conflict) হওয়ার শর্ত কোনটি?",
        "options": [
            "ক) অপারেশন দুটি ভিন্ন ট্রানজ্যাকশনের হতে হবে, একই ডেটা আইটেমের ওপর হতে হবে এবং অন্তত একটি অপারেশন WRITE হতে হবে",
            "খ) উভয় অপারেশন READ হতে হবে",
            "গ) দুটি ভিন্ন ডেটা আইটেমের হতে হবে",
            "ঘ) একই ট্রানজ্যাকশনের হতে হবে"
        ],
        "answer": "ক",
        "explanation": "Read-Write ($R_1(A), W_2(A)$), Write-Read ($W_1(A), R_2(A)$) অথবা Write-Write ($W_1(A), W_2(A)$) কনফ্লিক্ট তৈরি করে যদি তারা ভিন্ন ট্রানজ্যাকশন কর্তৃক একই ডেটায় ঘটে।"
    },
    {
        "id": 157,
        "topic": "Transactions & Concurrency Control",
        "question": "একটি শিডিউল কনফ্লিক্ট সিরিয়ালাইজেবল (Conflict Serializable) কিনা তা পরীক্ষা করার সবচেয়ে নির্ভরযোগ্য পদ্ধতি কোনটি?",
        "options": [
            "ক) বাবল সর্টিং",
            "খ) প্রেসিডেন্স গ্রাফ (Precedence Graph বা Conflict Graph)-এ কোনো সাইকেল (Cycle) আছে কিনা তা পরীক্ষা করা",
            "গ) ডেটাবেজ সাইজ মাপা",
            "ঘ) লক কাউন্ট করা"
        ],
        "answer": "খ",
        "explanation": "Precedence Graph-এ প্রতিটি ট্রানজ্যাকশন একটি নোড এবং কনফ্লিক্টিং অপারেশনের জন্য এজ ($T_i \\to T_j$) টানা হয়। গ্রাফটি যদি Directed Acyclic Graph (DAG) হয় অর্থাৎ কোনো চক্র (Cycle) না থাকে, তবে শিডিউলটি Conflict Serializable।"
    },
    {
        "id": 158,
        "topic": "Transactions & Concurrency Control",
        "question": "যে শিডিউল কনফ্লিক্ট সিরিয়ালাইজেবল নয়, কিন্তু কোনো ব্লাইন্ড রাইট (Blind Write) থাকার কারণে সিরিয়াল শিডিউলের সমতুল্য ফলাফল দেয় তাকে কী বলে?",
        "options": [
            "ক) View Serializable Schedule",
            "খ) Strict Schedule",
            "গ) Cascadeless Schedule",
            "ঘ) Recoverable Schedule"
        ],
        "answer": "ক",
        "explanation": "View Serializability হলো সিরিয়ালাইজেবিলিটির একটি বিস্তৃত রূপ। প্রতিটি কনফ্লিক্ট সিরিয়ালাইজেবল শিডিউলই ভিউ সিরিয়ালাইজেবল, কিন্তু বিপরীতটি সর্বদা সত্য নয়।"
    },
    {
        "id": 159,
        "topic": "Transactions & Concurrency Control",
        "question": "টু-ফেজ লকিং (2PL) প্রোটোকলের গ্রোয়িং ফেজ (Growing Phase) এবং শ্রিঙ্কিং ফেজ (Shrinking Phase)-এর নিয়ম কী?",
        "options": [
            "ক) গ্রোয়িং ফেজে কেবল লক অর্জন (Acquire) করা যায় কিন্তু কোনো লক ছাড়া যায় না, আর শ্রিঙ্কিং ফেজে লক রিলিজ করা যায় কিন্তু কোনো নতুন লক নেওয়া যায় না",
            "খ) যে কোনো সময় লক নেওয়া ও ছাড়া যায়",
            "গ) কোনো লক রিলিজ করা যায় না",
            "ঘ) ট্রানজ্যাকশন শুরুর আগেই সব লক ছাড়তে হয়"
        ],
        "answer": "ক",
        "explanation": "2PL নিশ্চিত করে যে ট্রানজ্যাকশন একবার কোনো লক রিলিজ করা শুরু করলে (Shrinking phase) সে আর কখনো নতুন কোনো লক নিতে পারবে না। এটি Conflict Serializability নিশ্চিত করে।"
    },
    {
        "id": 160,
        "topic": "Transactions & Concurrency Control",
        "question": "ক্যাসকেডিং অ্যাবোর্ট (Cascading Abort বা ক্যাসকেডিং রোলব্যাক) এড়াতে কোন ধরণের 2PL ব্যবহার করা হয়?",
        "options": [
            "ক) Basic 2PL",
            "খ) Strict 2PL (যেখানে সমস্ত Exclusive Lock ট্রানজ্যাকশন COMMIT বা ABORT না হওয়া পর্যন্ত ধরে রাখা হয়)",
            "গ) Dynamic 2PL",
            "ঘ) Optimistic 2PL"
        ],
        "answer": "খ",
        "explanation": "Strict 2PL নিশ্চিত করে যে কোনো ট্রানজ্যাকশন তার সমস্ত এক্সক্লুসিভ লক শেষ না হওয়া (Commit/Abort) পর্যন্ত ধরে রাখবে, ফলে কেউ ডার্টি ডেটা রিড করতে পারে না এবং ক্যাসকেডিং রোলব্যাক বন্ধ হয়।"
    },
    {
        "id": 161,
        "topic": "Transactions & Concurrency Control",
        "question": "রিগোরাস টু-ফেজ লকিং (Rigorous 2PL) এর ক্ষেত্রে কোনটি সত্য?",
        "options": [
            "ক) শুধুমাত্র Shared লক ধরে রাখা হয়",
            "খ) Shared (S) এবং Exclusive (X) উভয় ধরণের সমস্ত লকই ট্রানজ্যাকশন শেষ (Commit/Abort) না হওয়া পর্যন্ত ধরে রাখা হয়",
            "গ) কোনো লক নেওয়া হয় না",
            "ঘ) ডেডলক সম্পূর্ণ অসম্ভব"
        ],
        "answer": "খ",
        "explanation": "Rigorous 2PL হলো সবচেয়ে কঠোর লকিং যেখানে ট্রানজ্যাকশনের সমাপ্তি পর্যন্ত সকল প্রকার (রিড ও রাইট) লক ধরে রাখা হয়, যা সিরিয়ালাইজেশন অর্ডারকে কমিট অর্ডারের সমান করে দেয়।"
    },
    {
        "id": 162,
        "topic": "Transactions & Concurrency Control",
        "question": "লক-বেসড কনকারেন্সিতে ডেডলক প্রতিরোধের 'Wait-Die' স্কিমের নীতি কোনটি?",
        "options": [
            "ক) নন-প্রিম্পটিভ: যদি বয়স্ক ট্রানজ্যাকশন ($T_{old}$) কনিষ্ঠের ($T_{young}$) ধরে রাখা লক চায় তবে $T_{old}$ অপেক্ষা করবে (Wait); কিন্তু $T_{young}$ বয়স্কের লক চাইলে সে নিজে মরে যাবে/রোলব্যাক হবে (Die)",
            "খ) বয়স্ক ট্রানজ্যাকশন সবসময় তরুণকে হত্যা করবে",
            "গ) সবাই অনির্দিষ্টকাল অপেক্ষা করবে",
            "ঘ) কোনো ট্রানজ্যাকশন রোলব্যাক হবে না"
        ],
        "answer": "ক",
        "explanation": "Wait-Die হলো নন-প্রিম্পটিভ টাইমস্ট্যাম্প স্কিম: $TS(T_i) < TS(T_j)$ হলে $T_i$ অপেক্ষা করতে পারে, কিন্তু বিপরীত হলে $T_i$ ডাই (অ্যাবোর্ট) হয়। এটি ডেডলক সাইকেল তৈরি হতে দেয় না।"
    },
    {
        "id": 163,
        "topic": "Transactions & Concurrency Control",
        "question": "ডেডলক প্রতিরোধের 'Wound-Wait' স্কিম কোন ধরণের স্কিম?",
        "options": [
            "ক) প্রিম্পটিভ স্কিম (Preemptive Scheme): যেখানে বয়স্ক ট্রানজ্যাকশন কনিষ্ঠের কাছ থেকে জোরপূর্বক রিসোর্স ছিনিয়ে নিয়ে তাকে আহত বা বাতিল (Wound/Abort) করে",
            "খ) নন-প্রিম্পটিভ স্কিম",
            "গ) কোনো টাইমস্ট্যাম্প ব্যবহার করে না",
            "ঘ) র্যান্ডম রোলব্যাক স্কিম"
        ],
        "answer": "ক",
        "explanation": "Wound-Wait প্রিম্পটিভ নীতি অনুসরণ করে: $TS(T_i) < TS(T_j)$ হলে $T_i$ তরুণ ট্রানজ্যাকশন $T_j$-কে উন্ড (অ্যাবোর্ট) করে রিসোর্স দখল করে, নয়তো অপেক্ষা করে।"
    },
    {
        "id": 164,
        "topic": "Transactions & Concurrency Control",
        "question": "চলমান সিস্টেমে ডেডলক শনাক্ত করতে (Deadlock Detection) ডেটাবেজ সিস্টেম কোন গ্রাফ তৈরি ও পর্যবেক্ষণ করে?",
        "options": [
            "ক) B-Tree",
            "খ) Wait-For Graph (WFG)",
            "গ) Precedence Graph",
            "ঘ) Flowchart"
        ],
        "answer": "খ",
        "explanation": "Wait-For Graph-এ এজ $T_i \\to T_j$ নির্দেশ করে যে ট্রানজ্যাকশন $T_i$ অন্য ট্রানজ্যাকশন $T_j$-র মুক্ত করার অপেক্ষায় রয়েছে। এই গ্রাফে চক্র (Cycle) তৈরি হলে ডেডলক নিশ্চিত হয়।"
    },
    {
        "id": 165,
        "topic": "Transactions & Concurrency Control",
        "question": "টাইমস্ট্যাম্প-বেসড কনকারেন্সি প্রোটোকলে 'টমাস রাইট রুল' (Thomas' Write Rule) কোন সুবিধা প্রদান করে?",
        "options": [
            "ক) অপ্রয়োজনীয় ও পুরোনো রাইট অপারেশন উপেক্ষা (Ignore/Discard) করে অধিকতর কনকারেন্সি প্রদান করে",
            "খ) সমস্ত রিড অপারেশন বন্ধ করে দেয়",
            "গ) লক ছাড়া ডেটা ডিলিট করে",
            "ঘ) ক্যাসকেডিং অ্যাবোর্ট বৃদ্ধি করে"
        ],
        "answer": "ক",
        "explanation": "টমাস রাইট রুলে যদি কোনো লেট রাইট আসে ($TS(T) < W\\_TS(Q)$), তবে ট্রানজ্যাকশনটি অ্যাবোর্ট না করে কেবল সেই পুরোনো রাইট অপারেশনটিকে বাতিল/উপেক্ষা করে এগিয়ে যায়।"
    },
    {
        "id": 166,
        "topic": "Transactions & Concurrency Control",
        "question": "মাল্টিপল গ্র্যানুলারিটি লকিংয়ে (Multiple Granularity Locking) নিচের স্তরে লক নেওয়ার পূর্বে উপরের স্তরে কোন লক নিতে হয়?",
        "options": [
            "ক) Intention Lock (যেমন IS বা IX)",
            "খ) Exclusive Lock",
            "গ) Deadlock",
            "ঘ) Read Lock"
        ],
        "answer": "ক",
        "explanation": "হায়ারার্কির নোডে সরাসরি লক না নিয়ে তার পূর্বপুরুষ (Ancestor) নোডগুলোতে ইনটেনশন লক (Intent Shared - IS বা Intent Exclusive - IX) স্থাপন করে নিচের স্তরে লকিং সহজ করা হয়।"
    },
    {
        "id": 167,
        "topic": "Transactions & Concurrency Control",
        "question": "অপটিমিস্টিক কনকারেন্সি কন্ট্রোলে (Optimistic Concurrency Control) তিনটি ধাপ কী কী?",
        "options": [
            "ক) Lock Phase -> Execute Phase -> Free Phase",
            "খ) Read Phase -> Validation Phase -> Write Phase",
            "গ) Start Phase -> Sleep Phase -> Commit Phase",
            "ঘ) Write Phase -> Read Phase -> Log Phase"
        ],
        "answer": "খ",
        "explanation": "অপটিমিস্টিক কন্ট্রোলে ধরে নেওয়া হয় সংঘাত কম হবে। প্রথমে রিড করে লোকাল ভেরিয়েবলে কাজ হয় (Read Phase), তারপর কোনো সংঘাত হয়েছে কিনা যাচাই করা হয় (Validation Phase), এবং সবশেষে ডেটাবেজে লেখা হয় (Write Phase)।"
    },
    {
        "id": 168,
        "topic": "Transactions & Concurrency Control",
        "question": "SQL ট্রানজ্যাকশনের সর্বোচ্চ আইসোলেশন লেভেল (Highest Isolation Level) কোনটি?",
        "options": [
            "ক) READ UNCOMMITTED",
            "খ) READ COMMITTED",
            "গ) REPEATABLE READ",
            "ঘ) SERIALIZABLE"
        ],
        "answer": "ঘ",
        "explanation": "SERIALIZABLE হলো সর্বোচ্চ আইসোলেশন লেভেল যা Dirty Read, Non-repeatable Read এবং Phantom Read—সকল ত্রুটি সম্পূর্ণরূপে দূর করে সমান্তরাল কাজকে ধারাবাহিক রূপ দেয়।"
    },
    {
        "id": 169,
        "topic": "Transactions & Concurrency Control",
        "question": "একই ট্রানজ্যাকশনে একই কুয়েরি দুইবার চালালে দ্বিতীয়বারে অন্য ট্রানজ্যাকশন কর্তৃক ইনসার্ট করা নতুন সারির উপস্থিতি পাওয়ার সমস্যাকে কী বলে?",
        "options": [
            "ক) Dirty Read",
            "খ) Phantom Read",
            "গ) Lost Update",
            "ঘ) Starvation"
        ],
        "answer": "খ",
        "explanation": "Phantom Read ঘটে যখন রেঞ্জ কুয়েরির মাঝে অন্য কেউ নতুন রো INSERT করে এবং আগের ট্রানজ্যাকশন একই শর্তে পুনরায় কুয়েরি চালিয়ে 'ভৌতিক' নতুন রেকর্ড দেখতে পায়।"
    },
    {
        "id": 170,
        "topic": "Transactions & Concurrency Control",
        "question": "ডেডলক রিকভারির সময় যে ট্রানজ্যাকশনকে বাতিল বা রোলব্যাক করার জন্য বাছাই করা হয় তাকে কী বলা হয়?",
        "options": [
            "ক) Coordinator",
            "খ) Victim Transaction (শিকার ট্রানজ্যাকশন)",
            "গ) Orphan Transaction",
            "ঘ) Zombie Transaction"
        ],
        "answer": "খ",
        "explanation": "ডেডলক ভাঙতে সাইকেল থেকে ন্যূনতম খরচের কোনো একটি ট্রানজ্যাকশনকে 'Victim' হিসেবে নির্বাচন করে রোলব্যাক করা হয় এবং তার রিসোর্স মুক্ত করা হয়।"
    },

    # Subtopic 10: Recovery System (Log-based, WAL, Checkpoints, ARIES) (171-180)
    {
        "id": 171,
        "topic": "Recovery System",
        "question": "Write-Ahead Logging (WAL) প্রোটোকলের প্রধান নিয়ম কোনটি?",
        "options": [
            "ক) ডেটাবেজ বাফার থেকে মূল ডেটা পেজ ডিস্কে লেখার আগেই সংশ্লিষ্ট লগ রেকর্ডটি স্থায়ী ডিস্কে রাইট হতে হবে",
            "খ) লগ সবশেষে লেখা হবে",
            "গ) কোনো লগ রাখা যাবে না",
            "ঘ) লগ কেবল মেমরিতে থাকবে"
        ],
        "answer": "ক",
        "explanation": "WAL নিশ্চিত করে যে ডেটাবেজের কোনো ডিস্ক পরিবর্তন স্থায়ী হওয়ার আগে অবশ্যই তার Undo/Redo লগ রেকর্ড নন-ভোলাটাইল ডিস্ক স্টোরেজে লেখা সম্পন্ন হতে হবে।"
    },
    {
        "id": 172,
        "topic": "Recovery System",
        "question": "ডিফার্ড ডেটাবেজ মডিফিকেশন (Deferred Database Modification) কৌশলে ক্র্যাশের পর রিকভারি করতে কোনটি প্রয়োজন হয় না?",
        "options": [
            "ক) UNDO অপারেশনের প্রয়োজন হয় না, কেবল REDO প্রয়োজন হয়",
            "খ) REDO প্রয়োজন হয় না",
            "গ) কোনো লগ রেকর্ড প্রয়োজন হয় না",
            "ঘ) চেকপয়েন্ট লাগে না"
        ],
        "answer": "ক",
        "explanation": "Deferred Modification-এ ট্রানজ্যাকশন সম্পূর্ণরূপে Commit না হওয়া পর্যন্ত মূল ডেটাবেজ ফাইলে কোনো রাইট হয় না, ফলে ক্র্যাশ করলে কখনো UNDO করার দরকার পড়ে না।"
    },
    {
        "id": 173,
        "topic": "Recovery System",
        "question": "ইমিডিয়েট ডেটাবেজ মডিফিকেশন (Immediate Database Modification) কৌশলে সিস্টেম রিকভারির জন্য কোন দুটি অপারেশন প্রয়োজন?",
        "options": [
            "ক) কেবল REDO",
            "খ) UNDO এবং REDO উভয়ই",
            "গ) কেবল Rollback",
            "ঘ) Commit এবং Terminate"
        ],
        "answer": "খ",
        "explanation": "Immediate Modification-এ ট্রানজ্যাকশন চলাকালীনই ডিস্কে পরিবর্তন লেখা হতে পারে, তাই আনকমিটেড ট্রানজ্যাকশনকে UNDO এবং কমিটেড ট্রানজ্যাকশনকে REDO করতে হয়।"
    },
    {
        "id": 174,
        "topic": "Recovery System",
        "question": "ডেটাবেজ রিকভারিতে 'চেকপয়েন্ট' (Checkpoint)-এর প্রধান সুবিধা কী?",
        "options": [
            "ক) এটি পুরো লগ ফাইলের শুরু থেকে স্ক্যান করার প্রয়োজনীয়তা দূর করে রিকভারির সময় বহুগুণ কমিয়ে আনে",
            "খ) এটি সকল পাসওয়ার্ড মুছে দেয়",
            "গ) এটি ডিস্কের সাইজ বাড়িয়ে দেয়",
            "ঘ) এটি টেবিল ড্রপ করে"
        ],
        "answer": "ক",
        "explanation": "চেকপয়েন্টের সময় সমস্ত মডিফায়েড মেমরি পেজ ফিজিক্যাল ডিস্কে জোরপূর্বক ফ্লাশ করে নিশ্চিত করা হয়। ফলে ক্র্যাশ রিকভারির সময় চেকপয়েন্টের পূর্ববর্তী সফল লেনদেনগুলোকে আর রিডো করতে হয় না।"
    },
    {
        "id": 175,
        "topic": "Recovery System",
        "question": "আইবিএম কর্তৃক উদ্ভাবিত আধুনিক ডেটাবেজ রিকভারি অ্যালগরিদম ARIES-এর তিনটি পর্যায় কোনগুলো?",
        "options": [
            "ক) Scan, Sort, Merge",
            "খ) Analysis Phase, Redo Phase (Repeating history), Undo Phase",
            "গ) Lock, Execute, Unlock",
            "ঘ) Read, Write, Commit"
        ],
        "answer": "খ",
        "explanation": "ARIES তিনটি ধাপে কাজ করে: Analysis (সিস্টেমের অবস্থা বিশ্লেষণ), Redo (ক্র্যাশের আগ পর্যন্ত সমস্ত হিস্ট্রি রিপিট করা), এবং Undo (অসম্পূর্ণ ট্রানজ্যাকশন রোলব্যাক করা)।"
    },
    {
        "id": 176,
        "topic": "Recovery System",
        "question": "শ্যাডো পেজিং (Shadow Paging) রিকভারি টেকনিকে ডেটাবেজ ডিরেক্টরির কয়টি কপি রাখা হয়?",
        "options": [
            "ক) ১টি",
            "খ) ২টি (Current Page Table এবং Shadow Page Table)",
            "গ) ৩টি",
            "ঘ) ৪টি"
        ],
        "answer": "খ",
        "explanation": "Shadow Paging-এ দুটি পেজ টেবিল থাকে। ট্রানজ্যাকশন চলাকালীন সমস্ত পরিবর্তন Current Page Table-এ হয় এবং ক্র্যাশ হলে কোনো লগ ছাড়াই Shadow Page Table পুনরুদ্ধার করে রোলব্যাক করা যায়।"
    },
    {
        "id": 177,
        "topic": "Recovery System",
        "question": "কম্পিউটার বিজ্ঞানে এমন স্টোরেজ যা কোনো অবস্থাতেই ডেটা হারায় না (তাত্ত্বিকভাবে শতভাগ নির্ভরযোগ্য) তাকে কী বলে?",
        "options": [
            "ক) Volatile Storage",
            "খ) Non-volatile Storage",
            "গ) Stable Storage",
            "ঘ) Optical Storage"
        ],
        "answer": "গ",
        "explanation": "Stable Storage হলো একাধিক নন-ভোলাটাইল মিডিয়াতে (যেমন মিরর ডিস্ক/RAID) প্রতিলিপি তৈরি করে নির্মিত ধারণাগত স্টোরেজ যা সকল ফেইলিওর সত্ত্বেও ডেটা অক্ষত রাখে।"
    },
    {
        "id": 178,
        "topic": "Recovery System",
        "question": "লগ ফাইলে ট্রানজ্যাকশন $T_i$ এর জন্য $\\langle T_i, \\text{start} \\rangle$ আছে কিন্তু কোনো $\\langle T_i, \\text{commit} \\rangle$ বা $\\langle T_i, \\text{abort} \\rangle$ নেই। ক্র্যাশের পর রিকভারি ম্যানেজার কী করবে?",
        "options": [
            "ক) ট্রানজ্যাকশনটিকে REDO করবে",
            "খ) ট্রানজ্যাকশনটিকে UNDO (রোলব্যাক) করবে",
            "গ) ট্রানজ্যাকশনটিকে Commit ঘোষণা করবে",
            "ঘ) কিছুই করবে না"
        ],
        "answer": "খ",
        "explanation": "যেসব ট্রানজ্যাকশন ক্র্যাশের আগ পর্যন্ত কমিট হতে পারেনি তাদের সম্পূর্ণ কাজ UNDO করে ডেটাবেজকে আবার সামঞ্জস্যপূর্ণ অবস্থায় নিয়ে আসা হয়।"
    },
    {
        "id": 179,
        "topic": "Recovery System",
        "question": "লগ ফাইলে প্রতিটি লগ রেকর্ডের একটি অনন্য ক্রমবর্ধমান শনাক্তকারী সংখ্যা থাকে, যাকে কী বলা হয়?",
        "options": [
            "ক) Log Sequence Number (LSN)",
            "খ) Transaction ID",
            "গ) Block Number",
            "ঘ) Sector Key"
        ],
        "answer": "ক",
        "explanation": "প্রতিটি লগ এন্ট্রিকে LSN (Log Sequence Number) দিয়ে চিহ্নিত করা হয়। প্রতিটি ডেটা পেজেও তার সর্বশেষ আপডেটের PageLSN লেখা থাকে যা রিকভারিতে ব্যবহৃত হয়।"
    },
    {
        "id": 180,
        "topic": "Recovery System",
        "question": "রোলব্যাক করার সময় লগ ফাইলে ক্ষতিপূরণমূলক যে বিশেষ লগ রেকর্ড লেখা হয় তাকে কী বলে?",
        "options": [
            "ক) Checkpoint Record",
            "খ) Compensation Log Record (CLR)",
            "গ) Abort Signal",
            "ঘ) Redo Token"
        ],
        "answer": "খ",
        "explanation": "ARIES অ্যালগরিদমে UNDO চলাকালীন প্রতিটি বিপরীত পরিবর্তনের জন্য Compensation Log Record (CLR) লেখা হয় যেন রিকভারি চলাকালীন পুনরায় ক্র্যাশ হলেও ইনফিনিট লুপ না ঘটে।"
    },

    # Subtopic 11: Data Mining & Data Warehousing (OLAP, Decision Tree, Bayes, K-Means, Apriori) (181-190)
    {
        "id": 181,
        "topic": "Data Mining & Data Warehousing",
        "question": "OLTP (Online Transaction Processing) এবং OLAP (Online Analytical Processing)-এর মধ্যে মূল পার্থক্য কোনটি?",
        "options": [
            "ক) OLTP দৈনন্দিন ট্রানজ্যাকশন ও দ্রুত ইনসার্ট/আপডেটের জন্য অপটিমাইজড, আর OLAP ঐতিহাসিক ডেটা বিশ্লেষণ ও জটিল ব্যবসায়িক রিপোর্টিংয়ের জন্য অপটিমাইজড",
            "খ) OLAP কোনো কুয়েরি সাপোর্ট করে না",
            "গ) OLTP কেবলমাত্র ডেটা ওয়্যারহাউজে চলে",
            "ঘ) এদের মধ্যে কোনো পার্থক্য নেই"
        ],
        "answer": "ক",
        "explanation": "OLTP পরিচালিত হয় রিয়েল-টাইম অপারেশনাল কাজের জন্য (3NF নরমালাইজড), আর OLAP পরিচালিত হয় ডিসিশন সাপোর্ট ও ব্যবসায়িক বুদ্ধিমত্তার (BI) জন্য (ডিনরমালাইজড স্টার স্কিমা)।"
    },
    {
        "id": 182,
        "topic": "Data Mining & Data Warehousing",
        "question": "ডেটা ওয়্যারহাউজের কোন স্কিমাতে একটি সেন্ট্রাল ফ্যাক্ট টেবিল (Fact Table) সরাসরি একাধিক ডিমেনশন টেবিলের (Dimension Tables) সাথে যুক্ত থাকে?",
        "options": [
            "ক) Snowflake Schema",
            "খ) Star Schema (তারকা স্কিমা)",
            "গ) Fact Constellation",
            "ঘ) Network Schema"
        ],
        "answer": "খ",
        "explanation": "Star Schema হলো ডেটা ওয়্যারহাউজের সবচেয়ে সহজ ও জনপ্রিয় মডেল যেখানে কেন্দ্রে একটি ফ্যাক্ট টেবিল থাকে এবং তার চারপাশে অ-নরমালাইজড ডিমেনশন টেবিলগুলো তারার মতো বিন্যস্ত থাকে।"
    },
    {
        "id": 183,
        "topic": "Data Mining & Data Warehousing",
        "question": "Snowflake Schema কীভাবে Star Schema থেকে আলাদা?",
        "options": [
            "ক) Snowflake স্কিমাতে ডিমেনশন টেবিলগুলোকে আরও নরমালাইজড করে একাধিক উপ-টেবিলে বিভক্ত করা হয়",
            "খ) Snowflake স্কিমাতে কোনো ফ্যাক্ট টেবিল থাকে না",
            "গ) Snowflake স্কিমাতে কোনো জয়েন করা যায় না",
            "ঘ) এটি স্টার স্কিমার চেয়ে সহজ"
        ],
        "answer": "ক",
        "explanation": "স্নোফ্লেক স্কিমাতে রিডান্ড্যান্সি কমাতে ডিমেনশন টেবিলগুলোকে নরমালাইজ করে আরও শাখা-প্রশাখায় ভাগ করা হয় যা দেখতে স্নো-ফ্লেকের মতো দেখায়।"
    },
    {
        "id": 184,
        "topic": "Data Mining & Data Warehousing",
        "question": "OLAP অপারেশনে সামগ্রিক ডেটা থেকে ক্রমান্বয়ে গভীর বিস্তারিত তথ্যের দিকে যাওয়ার (যেমন: বছর -> মাস -> দিন) প্রক্রিয়াকে কী বলে?",
        "options": [
            "ক) Roll-up (বা Drill-up)",
            "খ) Drill-down",
            "গ) Slice and Dice",
            "ঘ) Pivot"
        ],
        "answer": "খ",
        "explanation": "Drill-down কম বিস্তারিত থেকে অধিকতর বিস্তারিত তথ্যের গভীরে প্রবেশ করায়। এর বিপরীত হলো Roll-up (যা ডেটাকে এগ্রিগেট করে সংক্ষেপ করে)।"
    },
    {
        "id": 185,
        "topic": "Data Mining & Data Warehousing",
        "question": "ডিসিশন ট্রি ক্লাসিফিকেশনের (Decision Tree) ID3 অ্যালগরিদমে সেরা স্প্লিটিং অ্যাট্রিবিউট বাছাই করতে কোনটি পরিমাপ করা হয়?",
        "options": [
            "ক) Euclidean Distance",
            "খ) Information Gain এবং Entropy (এনট্রপি)",
            "গ) Gini Impurity",
            "ঘ) Support and Confidence"
        ],
        "answer": "খ",
        "explanation": "ID3 অ্যালগরিদম প্রতিটি অ্যাট্রিবিউটের এনট্রপি পরিবর্তনের মাধ্যমে Information Gain হিসাব করে এবং যে অ্যাট্রিবিউটে ইনফরমেশন গেইন সর্বোচ্চ হয় তাকে নোড হিসেবে স্প্লিট করে।"
    },
    {
        "id": 186,
        "topic": "Data Mining & Data Warehousing",
        "question": "CART (Classification and Regression Trees) অ্যালগরিদম নোড স্প্লিট করার জন্য কোন মেট্রিকটি ব্যবহার করে?",
        "options": [
            "ক) Information Gain",
            "খ) Gini Index / Gini Impurity",
            "গ) Silhouette Score",
            "ঘ) Cosine Similarity"
        ],
        "answer": "খ",
        "explanation": "CART অ্যালগরিদমে ডেটাসেটের অবিশুদ্ধতা পরিমাপ করতে Gini Index ব্যবহার করা হয়। জিনি ইনডেক্স যত কম হয়, স্প্লিট তত নিখুঁত হয়।"
    },
    {
        "id": 187,
        "topic": "Data Mining & Data Warehousing",
        "question": "নেভ বায়েস ক্লাসিফায়ার (Naive Bayes Classifier) কোন মৌলিক অনুমানের ওপর ভিত্তি করে কাজ করে?",
        "options": [
            "ক) সমস্ত ফিচার একে অপরের সাথে গভীরভাবে যুক্ত",
            "খ) ক্লাসের প্রেক্ষিতে সকল ফিচার পরস্পরের থেকে সম্পূর্ণ স্বাধীন (Conditional Independence)",
            "গ) কোনো প্রোবাবিলিটি ব্যবহার করে না",
            "ঘ) ডেটাসেট অবশ্যই লিনিয়ার হতে হবে"
        ],
        "answer": "খ",
        "explanation": "বায়েস থিওরেম প্রয়োগের সুবিধার জন্য এটি ধরে নেয় যে একটি ফিচারের উপস্থিতি অন্য ফিচারের থেকে স্বাধীন, এই সরলীকরণের জন্যই একে 'Naive' বলা হয়।"
    },
    {
        "id": 188,
        "topic": "Data Mining & Data Warehousing",
        "question": "অ্যাসোসিয়েশন রুল মাইনিংয়ে (Association Rule Mining, যেমন মার্কেট বাস্কেট এনালাইসিস) কোন দুটি প্রধান মেট্রিক ব্যবহৃত হয়?",
        "options": [
            "ক) Precision এবং Recall",
            "খ) Support এবং Confidence",
            "গ) Entropy এবং Variance",
            "ঘ) Mean এবং Median"
        ],
        "answer": "খ",
        "explanation": "একটি রুল $X \\to Y$ কতটা জনপ্রিয় তা মাপে Support (মোট ট্রানজ্যাকশনে $X$ ও $Y$ একসাথে থাকার অনুপাত) এবং কতটা নির্ভরযোগ্য তা মাপে Confidence ($X$ ঘটলে $Y$ ঘটার সম্ভাবনা)।"
    },
    {
        "id": 189,
        "topic": "Data Mining & Data Warehousing",
        "question": "ফ্রিকোয়েন্ট আইটেমসেট (Frequent Itemset) খোঁজার জন্য বহুল ব্যবহৃত প্রুনিং অ্যালগরিদম কোনটি?",
        "options": [
            "ক) Apriori Algorithm",
            "খ) Dijkstra Algorithm",
            "গ) Kruskal Algorithm",
            "ঘ) Round Robin"
        ],
        "answer": "ক",
        "explanation": "Apriori অ্যালগরিদম এই নীতির ওপর চলে যে: 'যদি কোনো আইটেমসেট ফ্রিকোয়েন্ট হয়, তবে তার সমস্ত সাবসেটও অবশ্যই ফ্রিকোয়েন্ট হবে।' এর ফলে অপ্রয়োজনীয় কম্বিনেশন প্রুন করা সম্ভব হয়।"
    },
    {
        "id": 190,
        "topic": "Data Mining & Data Warehousing",
        "question": "K-Means অ্যালগরিদম ডেটা মাইনিংয়ের কোন প্রধান শাখার অন্তর্ভুক্ত?",
        "options": [
            "ক) সুপারভাইজড ক্লাসিফিকেশন",
            "খ) আন-সুপারভাইজড ক্লাস্টারিং (Unsupervised Clustering)",
            "গ) রিগ্রেশন মডেলিং",
            "ঘ) সিকোয়েন্স প্রেডিকশন"
        ],
        "answer": "খ",
        "explanation": "K-Means কোনো পূর্ব-নির্ধারিত লেবেল ছাড়াই দূরত্বের (Centroid distance) ওপর ভিত্তি করে ডেটাকে স্বয়ংক্রিয়ভাবে $K$-টি ক্লাস্টারে ভাগ করে, যা একটি আন-সুপারভাইজড পদ্ধতি।"
    },

    # Subtopic 12: Parallel & Distributed Databases, Database Tuning & Security (191-200)
    {
        "id": 191,
        "topic": "Parallel and Distributed Databases & Security",
        "question": "প্যারালাল ডেটাবেজ আর্কিটেকচারে কোন মডেলটি সবচেয়ে বেশি স্কেলেবল (Scalable) এবং ফল্ট-টলারেন্ট?",
        "options": [
            "ক) Shared Memory",
            "খ) Shared Disk",
            "গ) Shared Nothing Architecture",
            "ঘ) Shared Cache"
        ],
        "answer": "গ",
        "explanation": "Shared-Nothing আর্কিটেকচারে প্রতিটি নোডের নিজস্ব প্রসেসর, মেমরি ও ডিস্ক থাকে এবং নোডগুলো উচ্চগতির নেটওয়ার্কে যুক্ত থাকে। ফলে এতে কোনো সেন্ট্রাল বটলনেক থাকে না এবং এটি সবচেয়ে স্কেলেবল।"
    },
    {
        "id": 192,
        "topic": "Parallel and Distributed Databases & Security",
        "question": "প্যারালাল ডেটাবেজে রাউন্ড-রবিন পার্টিশনিংয়ের (Round-robin partitioning) নিয়ম কী?",
        "options": [
            "ক) প্রতিটি টাপলকে পর্যায়ক্রমে ক্রমানুসারে পরবর্তী ডিস্কে পাঠিয়ে সকল ডিস্কে সমানভাবে ডেটা বণ্টন করা",
            "খ) হ্যাশ ফাংশন দিয়ে ডিস্ক নির্ধারণ করা",
            "গ) একটি নির্দিষ্ট রেঞ্জ দেখে ডিস্কে পাঠানো",
            "ঘ) সমস্ত ডেটা কেবল প্রথম ডিস্কে রাখা"
        ],
        "answer": "ক",
        "explanation": "রাউন্ড-রবিনে টাপলগুলোকে চক্রাকারে $D_0, D_1, D_2, \\dots$ ডিস্কে বণ্টন করা হয় যা সব ডিস্কে সমান আকারের ডেটা বিস্তার নিশ্চিত করে।"
    },
    {
        "id": 193,
        "topic": "Parallel and Distributed Databases & Security",
        "question": "একটি টেবিলের কিছু নির্দিষ্ট সারি (Rows) এক সাইটে এবং বাকি সারি অন্য সাইটে সংরক্ষণ করাকে কোন ধরণের ফ্র্যাগমেন্টেশন বলে?",
        "options": [
            "ক) Vertical Fragmentation",
            "খ) Horizontal Fragmentation (অনুভূমিক খণ্ডায়ন)",
            "গ) Mixed Fragmentation",
            "ঘ) Derived Fragmentation"
        ],
        "answer": "খ",
        "explanation": "Selection ($\\\\sigma$) অপারেশনের মাধ্যমে টেবিলের অনুভূমিক সারিগুলোকে বিভিন্ন সাইটে ভাগ করাকে Horizontal Fragmentation বলে। কলামগুলোকে ভাগ করলে Vertical Fragmentation হয়।"
    },
    {
        "id": 194,
        "topic": "Parallel and Distributed Databases & Security",
        "question": "ডিস্ট্রিবিউটেড ডেটাবেজে পরমাণুতা (Atomicity) নিশ্চিত করার স্ট্যান্ডার্ড প্রোটোকল কোনটি?",
        "options": [
            "ক) Two-Phase Commit Protocol (2PC)",
            "খ) Sliding Window Protocol",
            "গ) Two-Phase Locking",
            "ঘ) Stop and Wait"
        ],
        "answer": "ক",
        "explanation": "2PC প্রোটোকলে কো-অর্ডিনেটর প্রথমে সমস্ত সাইটকে প্রস্তুতির জন্য ভোট পাঠায় (Prepare Phase) এবং সকল সাইট রাজি হলে ফাইনাল কমিট পাঠায় (Commit Phase), নয়তো বাতিল করে।"
    },
    {
        "id": 195,
        "topic": "Parallel and Distributed Databases & Security",
        "question": "ডিস্ট্রিবিউটেড সিস্টেমের CAP থিওরেম অনুযায়ী কোন তিনটি বৈশিষ্ট্যের মধ্যে সর্বোচ্চ দুটি একসাথে পূর্ণ অর্জন করা সম্ভব?",
        "options": [
            "ক) Consistency, Availability, Partition Tolerance",
            "খ) Concurrency, Accuracy, Performance",
            "গ) Confidentiality, Authentication, Privacy",
            "ঘ) Capacity, Adaptability, Persistence"
        ],
        "answer": "ক",
        "explanation": "এরিক ব্রিউয়ারের CAP উপপাদ্য অনুযায়ী নেটওয়ার্ক পার্টিশনের ($P$) উপস্থিতিতে একটি ডিস্ট্রিবিউটেড সিস্টেম একই সাথে Consistency ($C$) এবং Availability ($A$) উভয়টি অর্জন করতে পারে না।"
    },
    {
        "id": 196,
        "topic": "Parallel and Distributed Databases & Security",
        "question": "ডেটাবেজ সিকিউরিটিতে Discretionary Access Control (DAC) কীভাবে প্রয়োগ করা হয়?",
        "options": [
            "ক) ওএস কার্নেল লেভেলে",
            "খ) SQL এর GRANT এবং REVOKE স্টেটমেন্টের মাধ্যমে ব্যবহারকারীদের সুযোগ ও পারমিশন নির্ধারণ করে",
            "গ) শুধুমাত্র ফায়ারওয়াল দিয়ে",
            "ঘ) ব্যবহারকারীর আইপি ব্লক করে"
        ],
        "answer": "খ",
        "explanation": "DAC মডেলে ডেটার মালিক নিজেই সিদ্ধান্ত নেন কে কোন টেবিল বা কলাম পড়তে বা লিখতে পারবে, যা SQL-এ `GRANT` এবং `REVOKE` কমান্ড দ্বারা পরিচালিত হয়।"
    },
    {
        "id": 197,
        "topic": "Parallel and Distributed Databases & Security",
        "question": "Mandatory Access Control (MAC) মডেলে ডেটা এক্সেস নিয়ন্ত্রণের ভিত্তি কী?",
        "options": [
            "ক) ইউজারের ক্লিয়ারেন্স লেভেল এবং ডেটা অবজেক্টের সিকিউরিটি ক্লাসিফিকেশন লেভেল (যেমন: Top Secret, Secret, Confidential)",
            "খ) টেবিলের আকার",
            "গ) ইনডেক্সের সংখ্যা",
            "ঘ) ফাইল ফরম্যাট"
        ],
        "answer": "ক",
        "explanation": "MAC মডেলে সিস্টেম সেন্ট্রালি কঠোর নীতি প্রয়োগ করে। Bell-LaPadula মডেল (No Read-Up, No Write-Down) অনুযায়ী নিরাপত্তা স্তর যাচাই করে ডেটা প্রবেশাধিকার দেওয়া হয়।"
    },
    {
        "id": 198,
        "topic": "Parallel and Distributed Databases & Security",
        "question": "Role-Based Access Control (RBAC)-এর মূল ধারণা কোনটি?",
        "options": [
            "ক) প্রতিটি ব্যবহারকারীকে সরাসরি আলাদা আলাদা শত শত অনুমতি দেওয়া",
            "খ) অনুমতি বা পারমিশনগুলোকে নির্দিষ্ট রোলে (যেমন: Admin, Manager, Cashier) অর্পণ করা এবং ব্যবহারকারীদের সেই রোলে যুক্ত করা",
            "গ) কোনো পাসওয়ার্ড না রাখা",
            "ঘ) কেবল রুট ইউজার দিয়ে কাজ করা"
        ],
        "answer": "খ",
        "explanation": "RBAC-এ অনুমতি দেওয়া হয় পদের বা রোলের (Role) ভিত্তিতে, যা বৃহৎ প্রতিষ্ঠানে ব্যবহারকারী অধিকার ব্যবস্থাপনা অত্যন্ত সহজ ও সুসংহত করে তোলে।"
    },
    {
        "id": 199,
        "topic": "Parallel and Distributed Databases & Security",
        "question": "SQL Injection প্রতিরোধে অ্যাপ্লিকেশনে ইনপুট ডেটা যাচাই করার পাশাপাশি কোন কৌশলটি বাধ্যতামূলক?",
        "options": [
            "ক) Parameterized Queries বা PreparedStatement ব্যবহার করা",
            "খ) কন্টেইনারে ডেটা রাখা",
            "গ) ডেটাবেজ সাইট বন্ধ রাখা",
            "ঘ) কেবল GET রিকোয়েস্ট ব্যবহার করা"
        ],
        "answer": "ক",
        "explanation": "প্যারামিটারাইজড কুয়েরিতে ইউজার ইনপুটকে সরাসরি কুয়েরি কোডের সাথে জোড়া না লাগিয়ে আলাদা প্যারামিটার হিসেবে ডেটাবেজে পাঠানো হয়, ফলে ইনপুট কোনো নির্দেশ হিসেবে রান করার সুযোগ পায় না।"
    },
    {
        "id": 200,
        "topic": "Parallel and Distributed Databases & Security",
        "question": "ডেটাবেজ টিউনিংয়ের (Database Performance Tuning) সবচেয়ে সাধারণ ও কার্যকর প্রাথমিক পদক্ষেপ কোনটি?",
        "options": [
            "ক) ঘন ঘন ব্যবহৃত WHERE এবং JOIN কলামের ওপর যথাযথ ইনডেক্স তৈরি করা এবং ধীরগতির কুয়েরিগুলোর এক্সিকিউশন প্ল্যান বিশ্লেষণ করা",
            "খ) সমস্ত টেবিল মুছে ফেলা",
            "গ) সকল ফরেন কি তুলে দেওয়া",
            "ঘ) হার্ডডিস্ক বদলে ফেলা"
        ],
        "answer": "ক",
        "explanation": "পারফরম্যান্স টিউনিংয়ের শুরুতেই স্লো কুয়েরি লগ ও এক্সিকিউশন প্ল্যান (EXPLAIN) দেখে অপ্রয়োজনীয় ফুল টেবিল স্ক্যান বাদ দিয়ে সঠিক ক্লাস্টার্ড/সেকেন্ডারি ইনডেক্স তৈরি করা হয়।"
    }
]

out_dir = "NTRCA 452 - AI"
os.makedirs(out_dir, exist_ok=True)
filename = os.path.join(out_dir, "অধ্যায়- ৬. Database Management System.json")

# Load existing part 1
with open(filename, "r", encoding="utf-8") as f:
    existing = json.load(f)

# Merge
all_questions = existing + questions_part2
# Sort by id to be certain
all_questions = sorted(all_questions, key=lambda x: x["id"])

with open(filename, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated Chapter 6 with exactly {len(all_questions)} MCQs!")
