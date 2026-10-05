# -*- coding: utf-8 -*-
import json
import os

questions_part1 = [
    # Subtopic 1: File Systems vs DBMS & Data Modeling Architecture (1-15)
    {
        "id": 1,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "ট্রেডিশনাল ফাইল প্রসেসিং সিস্টেমের (File Processing System) প্রধান অসুবিধা কোনটি?",
        "options": [
            "ক) ডেটা রিডান্ড্যান্সি (Redundancy) ও ডেটা ইনকনসিস্টেন্সি (Inconsistency)",
            "খ) মেমরির অতিরিক্ত অপচয় রোধ",
            "গ) উচ্চমানের মাল্টি-ইউজার কনকারেন্সি কন্ট্রোল",
            "ঘ) স্বয়ংক্রিয় ব্যাকআপ ব্যবস্থা"
        ],
        "answer": "ক",
        "explanation": "ফাইল প্রসেসিং সিস্টেমে একই ডেটা বিভিন্ন ফাইলে বারবার সংরক্ষিত হয় যাকে ডেটা রিডান্ড্যান্সি বলে। এর ফলে ডেটা আপডেট করার সময় বিভিন্ন স্থানে ভিন্ন মান থেকে যায়, যা ডেটা ইনকনসিস্টেন্সি তৈরি করে। DBMS এই সমস্যা দূর করে।"
    },
    {
        "id": 2,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "DBMS-এর ত্রি-স্তর বিশিষ্ট আর্কিটেকচারে (Three-Schema Architecture) কোন স্তরটি ডেটা বাস্তবে হার্ডডিস্কে কীভাবে সংরক্ষিত থাকে তা নির্দেশ করে?",
        "options": [
            "ক) ভিউ লেভেল (View/External Level)",
            "খ) কনসেপচুয়াল বা লজিক্যাল লেভেল (Conceptual/Logical Level)",
            "গ) ইন্টারনাল বা ফিজিক্যাল লেভেল (Internal/Physical Level)",
            "ঘ) ইউজার ইন্টারফেস লেভেল"
        ],
        "answer": "গ",
        "explanation": "ANSI-SPARC থ্রি-স্কিমা আর্কিটেকচারে ইন্টারনাল বা ফিজিক্যাল লেভেল ডেটা মেমরি বা স্টোরেজে কীভাবে বাইনারি/ব্লক আকারে সংরক্ষিত আছে (ডাটা স্ট্রাকচার, ইনডেক্সিং ইত্যাদি) তা নির্দিষ্ট করে।"
    },
    {
        "id": 3,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "লজিক্যাল স্কিমা পরিবর্তন না করে ফিজিক্যাল স্কিমা পরিবর্তনের সামর্থ্যকে কী বলা হয়?",
        "options": [
            "ক) Logical Data Independence",
            "খ) Physical Data Independence",
            "গ) Data Isolation",
            "ঘ) Schema Redundancy"
        ],
        "answer": "খ",
        "explanation": "ফিজিক্যাল স্টোরেজ গঠন বা ইনডেক্স পরিবর্তন করার পরেও যদি কনসেপচুয়াল/লজিক্যাল স্কিমায় কোনো প্রভাব না পড়ে, তবে তাকে Physical Data Independence বলা হয়।"
    },
    {
        "id": 4,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "কনসেপচুয়াল স্কিমা পরিবর্তন করার পরেও ইউজার ভিউ বা অ্যাপ্লিকেশনে পরিবর্তন না হওয়ার সুবিধাকে কী বলে?",
        "options": [
            "ক) Physical Data Independence",
            "খ) Logical Data Independence",
            "গ) Data Integrity",
            "ঘ) Concurrency"
        ],
        "answer": "খ",
        "explanation": "কনসেপচুয়াল স্কিমার পরিবর্তন (যেমন নতুন টেবিল বা অ্যাট্রিবিউট যোগ করা) বাহ্যিক ভিউ বা অ্যাপ্লিকেশনের ওপর প্রভাব না ফেললে তাকে Logical Data Independence বলে।"
    },
    {
        "id": 5,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "ডেটাবেজের সামগ্রিক নকশা বা কাঠামোকে (Overall Design) কী বলা হয়?",
        "options": [
            "ক) Database Instance",
            "খ) Database Schema",
            "গ) Snapshot",
            "ঘ) Relation Extension"
        ],
        "answer": "খ",
        "explanation": "ডেটাবেজের সামগ্রিক লজিক্যাল ডিজাইন বা ব্লুপ্রিন্টকে 'Database Schema' বলা হয়। আর কোনো নির্দিষ্ট মুহূর্তে ডেটাবেজে থাকা মূল ডেটার সংগ্রহকে 'Instance' বলা হয়।"
    },
    {
        "id": 6,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "কোনো নির্দিষ্ট মুহূর্তে ডেটাবেজে সংগৃহীত বাস্তব ডেটার সেটকে কী বলা হয়?",
        "options": [
            "ক) Database Schema",
            "খ) Database Instance বা State",
            "গ) Metadata",
            "ঘ) Domain"
        ],
        "answer": "খ",
        "explanation": "কোনো নির্দিষ্ট সময়ে ডেটাবেজের মধ্যে বিদ্যমান তথ্যের অবস্থাকে Database Instance বা Snapshot বা Database State বলা হয়।"
    },
    {
        "id": 7,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "DBMS-এ ডেটা ডিকশনারি (Data Dictionary) বা সিস্টেম ক্যাটালগে কী সংরক্ষিত থাকে?",
        "options": [
            "ক) শুধুমাত্র ইউজার টেবিলের ডেটা",
            "খ) মেটাডেটা (Metadata - ডেটা সম্পর্কে ডেটা, যেমন স্কিমা, কনস্ট্রেইন্ট ইত্যাদি)",
            "গ) অপারেটিং সিস্টেমের বুট ফাইল",
            "ঘ) নেটওয়ার্ক প্যাকেট লগ"
        ],
        "answer": "খ",
        "explanation": "Data Dictionary বা System Catalog হলো একটি স্বয়ংক্রিয় ডেটাবেজ যা মেটাডেটা (Metadata) সংরক্ষণ করে—যেমন টেবিলের নাম, অ্যাট্রিবিউটের ধরন, ইনডেক্স, অথোরাইজেশন ও ইন্টিগ্রিটি কনস্ট্রেইন্ট।"
    },
    {
        "id": 8,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "DDL কম্পাইলার দ্বারা জেনারেট করা টেবিল কাঠামোর ডেটা কোথায় সেভ হয়?",
        "options": [
            "ক) Data Dictionary-তে",
            "খ) Log Buffer-এ",
            "গ) RAM-এর ক্যাশ মেমরিতে স্থায়ীভাবে",
            "ঘ) Application Source কোডে"
        ],
        "answer": "ক",
        "explanation": "DDL স্টেটমেন্ট (CREATE, ALTER ইত্যাদি) এক্সিকিউট হলে তার স্কিমা ডেটা সরাসরি Data Dictionary (সিস্টেম ক্যাটালগ)-তে স্টোর বা আপডেট হয়।"
    },
    {
        "id": 9,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "নিচের কোনটি DML (Data Manipulation Language)-এর উদাহরণ?",
        "options": [
            "ক) CREATE",
            "খ) ALTER",
            "গ) INSERT",
            "ঘ) DROP"
        ],
        "answer": "গ",
        "explanation": "INSERT, UPDATE, DELETE হলো DML স্টেটমেন্ট যা টেবিলের মধ্যকার ডেটা ম্যানিপুলেট করতে ব্যবহৃত হয়। CREATE, ALTER, DROP হলো DDL।"
    },
    {
        "id": 10,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "নিচের কোনটি DCL (Data Control Language)-এর অন্তর্ভুক্ত?",
        "options": [
            "ক) GRANT ও REVOKE",
            "খ) COMMIT ও ROLLBACK",
            "গ) SELECT ও WHERE",
            "ঘ) CREATE ও ALTER"
        ],
        "answer": "ক",
        "explanation": "GRANT এবং REVOKE হলো DCL কমান্ড যা ইউজার পারমিশন এবং অ্যাক্সেস কন্ট্রোল নিয়ন্ত্রণ করতে ব্যবহৃত হয়।"
    },
    {
        "id": 11,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "নিচের কোন কমান্ডগুলো TCL (Transaction Control Language)-এর অংশ?",
        "options": [
            "ক) INSERT, UPDATE",
            "খ) COMMIT, ROLLBACK, SAVEPOINT",
            "গ) GRANT, REVOKE",
            "ঘ) DROP, TRUNCATE"
        ],
        "answer": "খ",
        "explanation": "ট্রানজ্যাকশনের স্থায়িত্ব এবং রোলব্যাক ব্যবস্থাপনার জন্য COMMIT, ROLLBACK এবং SAVEPOINT ব্যবহৃত হয়, যা TCL।"
    },
    {
        "id": 12,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "ডেটাবেজ অ্যাডমিনিস্ট্রেটরের (DBA) প্রধান দায়িত্বের মধ্যে কোনটি পড়ে না?",
        "options": [
            "ক) স্কিমা সংজ্ঞা ও ফিজিক্যাল স্টোরেজ কাঠামো নির্ধারণ",
            "খ) ব্যবহারকারীদের অথোরাইজেশন ও নিরাপত্তা প্রদান",
            "গ) অ্যাপ্লিকেশনের ব্যবসায়িক লজিক কোডিং (Frontend UI Development)",
            "ঘ) ব্যাকআপ ও রিকভারি নিশ্চিত করা"
        ],
        "answer": "গ",
        "explanation": "ফ্রন্টএন্ড বা বিজনেস লজিক কোডিং অ্যাপ্লিকেশন প্রোগ্রামার বা সফটওয়্যার ইঞ্জিনিয়ারের কাজ; DBA ডেটাবেজের ডিজাইন, পারমিশন, ব্যাকআপ ও পারফরম্যান্স ম্যানেজ করেন।"
    },
    {
        "id": 13,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "DBMS-এর ক্লায়েন্ট-সার্ভার টু-টিয়ার (2-tier) আর্কিটেকচারে অ্যাপ্লিকেশন প্রোগ্রাম কোথায় চলে?",
        "options": [
            "ক) ডাটাবেজ ইঞ্জিনের ভেতরে",
            "খ) ক্লায়েন্ট মেশিনে (User side)",
            "গ) কোনো অ্যাপ সার্ভার থাকে না, সরাসরি হার্ডওয়্যারে",
            "ঘ) ক্লাউড প্রক্সিতে"
        ],
        "answer": "খ",
        "explanation": "2-tier আর্কিটেকচারে ক্লায়েন্ট মেশিনে ইউজার ইন্টারফেস এবং বিজনেস অ্যাপ্লিকেশন রান করে, যা ODBC/JDBC-এর মাধ্যমে সরাসরি ডেটাবেজ সার্ভারের সাথে যোগাযোগ করে।"
    },
    {
        "id": 14,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "3-tier ক্লায়েন্ট-সার্ভার ডেটাবেজ আর্কিটেকচারে মাঝের লেয়ারটি (Intermediate layer) কী?",
        "options": [
            "ক) Presentation Layer",
            "খ) Application Server / Web Server (Business Logic Layer)",
            "গ) Database Server",
            "ঘ) Disk Storage Controller"
        ],
        "answer": "খ",
        "explanation": "3-tier আর্কিটেকচারে ৩টি স্তর থাকে: Client Tier (Presentation), Application Tier (Business Logic), এবং Database Tier।"
    },
    {
        "id": 15,
        "topic": "File Processing vs DBMS & Database Architecture",
        "question": "ডেটাবেজের 'Data Abstraction'-এর সর্বোচ্চ লেভেল কোনটি যা সাধারণ ব্যবহারকারীদের দেখানো হয়?",
        "options": [
            "ক) Physical level",
            "খ) Logical level",
            "গ) View level (External level)",
            "ঘ) Storage level"
        ],
        "answer": "গ",
        "explanation": "View Level বা External Level হলো সর্বোচ্চ লেভেল যেখানে জটিল কাঠামো লুকিয়ে রেখে ব্যবহারকারীকে কেবল প্রয়োজনীয় ভিউ দেখানো হয়।"
    },

    # Subtopic 2: Entity-Relationship (ER) & Extended ER (EER) Modeling (16-35)
    {
        "id": 16,
        "topic": "ER and EER Modeling",
        "question": "ER ডায়াগ্রামে এনটিটি (Entity) এবং অ্যাট্রিবিউট (Attribute) কোন কোন জ্যামিতিক চিত্র দিয়ে প্রকাশ করা হয়?",
        "options": [
            "ক) এনটিটি: ডায়মন্ড, অ্যাট্রিবিউট: আয়তক্ষেত্র",
            "খ) এনটিটি: আয়তক্ষেত্র (Rectangle), অ্যাট্রিবিউট: উপবৃত্ত (Ellipse/Oval)",
            "গ) এনটিটি: উপবৃত্ত, অ্যাট্রিবিউট: বৃত্ত",
            "ঘ) এনটিটি: সামান্তরিক, অ্যাট্রিবিউট: আয়তক্ষেত্র"
        ],
        "answer": "খ",
        "explanation": "ER মডেলের প্রচলিত স্বরলিপিতে (Peter Chen's Notation) সত্তা বা এনটিটিকে আয়তক্ষেত্র (Rectangle) এবং বৈশিষ্ট্য বা অ্যাট্রিবিউটকে উপবৃত্ত (Ellipse) দ্বারা দেখানো হয়।"
    },
    {
        "id": 17,
        "topic": "ER and EER Modeling",
        "question": "ER ডায়াগ্রামে রিলেশনশিপ সেট (Relationship Set) কোন প্রতীক দিয়ে নির্দেশ করা হয়?",
        "options": [
            "ক) বৃত্ত (Circle)",
            "খ) রম্বস বা ডায়মন্ড (Diamond)",
            "গ) ত্রিভুজ (Triangle)",
            "ঘ) ডবল ওভাল (Double Oval)"
        ],
        "answer": "খ",
        "explanation": "ER ডায়াগ্রামে দুটি বা ততোধিক এনটিটির মধ্যকার সম্পর্ক (Relationship) রম্বস বা ডায়মন্ড বক্স দ্বারা উপস্থাপন করা হয়।"
    },
    {
        "id": 18,
        "topic": "ER and EER Modeling",
        "question": "যে অ্যাট্রিবিউটকে একাধিক ক্ষুদ্র মৌলিক অংশে ভাগ করা যায় (যেমন- Name কে First Name, Last Name) তাকে কী বলে?",
        "options": [
            "ক) Simple Attribute",
            "খ) Composite Attribute",
            "গ) Multivalued Attribute",
            "ঘ) Derived Attribute"
        ],
        "answer": "খ",
        "explanation": "কম্পোজিট অ্যাট্রিবিউট হলো এমন বৈশিষ্ট্য যা একাধিক ছোট উপ-অ্যাট্রিবিউট নিয়ে গঠিত। যেমন: Address (Street, City, Zip)।"
    },
    {
        "id": 19,
        "topic": "ER and EER Modeling",
        "question": "কোনো একজন ব্যক্তির একাধিক ফোন নম্বর বা ইমেইল থাকলে তা ER মডেলে কোন ধরণের অ্যাট্রিবিউট?",
        "options": [
            "ক) Derived Attribute",
            "খ) Multivalued Attribute (বহুমানসম্পন্ন)",
            "গ) Key Attribute",
            "ঘ) Composite Attribute"
        ],
        "answer": "খ",
        "explanation": "কোনো এনটিটির জন্য একটি অ্যাট্রিবিউটের একাধিক মান থাকলে তাকে Multivalued Attribute বলে, যা ER ডায়াগ্রামে ডাবল উপবৃত্ত (Double Oval) দিয়ে দেখানো হয়।"
    },
    {
        "id": 20,
        "topic": "ER and EER Modeling",
        "question": "জন্মতারিখ (Date of Birth) থেকে বয়স (Age) গণনা করা হলে 'Age' কোন ধরণের অ্যাট্রিবিউট?",
        "options": [
            "ক) Derived Attribute (লব্ধ অ্যাট্রিবিউট)",
            "খ) Primary Attribute",
            "গ) Multivalued Attribute",
            "ঘ) Atomic Attribute"
        ],
        "answer": "ক",
        "explanation": "যে অ্যাট্রিবিউটের মান সরাসরি সংরক্ষণ না করে অন্য কোনো অ্যাট্রিবিউট থেকে গণনা করা যায় তাকে Derived Attribute বলে। এটি ড্যাশড উপবৃত্ত (Dashed Oval) দ্বারা দেখানো হয়।"
    },
    {
        "id": 21,
        "topic": "ER and EER Modeling",
        "question": "যে এনটিটি সেটের নিজস্ব প্রাইমারি কি গঠনের মতো পর্যাপ্ত অ্যাট্রিবিউট নেই তাকে কী বলে?",
        "options": [
            "ক) Strong Entity Set",
            "খ) Weak Entity Set (দুর্বল এনটিটি)",
            "গ) Associative Entity",
            "ঘ) Super Entity"
        ],
        "answer": "খ",
        "explanation": "Weak Entity Set-এর নিজস্ব কোনো প্রাইমারি কি থাকে না। এটি তার অস্তিত্বের জন্য একটি Identifying বা Strong Entity-এর ওপর নির্ভর করে। একে ডবল আয়তক্ষেত্র দিয়ে দেখানো হয়।"
    },
    {
        "id": 22,
        "topic": "ER and EER Modeling",
        "question": "Weak Entity Set-এর টাপলগুলোকে চিহ্নিত করতে Identifying Entity-র প্রাইমারি কি-এর সাথে কোন কি ব্যবহার করা হয়?",
        "options": [
            "ক) Candidate Key",
            "খ) Partial Key বা Discriminator",
            "গ) Alternate Key",
            "ঘ) Super Key"
        ],
        "answer": "খ",
        "explanation": "Weak Entity-র টাপলগুলোকে স্বাতন্ত্র্য দিতে Discriminator বা Partial Key ব্যবহার করা হয়। ডায়াগ্রামে একে ড্যাশড আন্ডারলাইন (Dashed Underline) দ্বারা নির্দেশ করা হয়।"
    },
    {
        "id": 23,
        "topic": "ER and EER Modeling",
        "question": "যদি এনটিটি সেট $A$-র প্রতিটি উপাদান এনটিটি সেট $B$-র সাথে সম্পর্কের ক্ষেত্রে বাধ্যতামূলকভাবে যুক্ত থাকে, তবে সেই পার্টিসিপেশনকে কী বলে?",
        "options": [
            "ক) Partial Participation",
            "খ) Total Participation (Existence Dependency)",
            "গ) Semi Participation",
            "ঘ) Binary Participation"
        ],
        "answer": "খ",
        "explanation": "টোটাল পার্টিসিপেশনে এনটিটি সেটের প্রতিটি সত্তা অন্তত একটি সম্পর্কে অংশ নিতেই হবে। ER চিত্রে এটি ডবল লাইন (Double Line) দ্বারা নির্দেশ করা হয়।"
    },
    {
        "id": 24,
        "topic": "ER and EER Modeling",
        "question": "একটি রিলেশনশিপে কয়টি এনটিটি সেট অংশগ্রহণ করেছে তার সংখ্যাকে কী বলা হয়?",
        "options": [
            "ক) Cardinality",
            "খ) Degree of Relationship",
            "গ) Modality",
            "ঘ) Domain"
        ],
        "answer": "খ",
        "explanation": "একটি সম্পর্কে অংশগ্রহণকারী এনটিটি সেটের সংখ্যাকে Degree of Relationship বলে। যেমন: ১টি হলে Unary/Recursive, ২টি হলে Binary, ৩টি হলে Ternary।"
    },
    {
        "id": 25,
        "topic": "ER and EER Modeling",
        "question": "একজন শিক্ষক একাধিক কোর্স পড়াতে পারেন এবং একটি কোর্স কেবল একজন শিক্ষক পড়ান—এটি কোন কার্ডিনালিটি রেশিও?",
        "options": [
            "ক) One-to-One (1:1)",
            "খ) One-to-Many (1:N)",
            "গ) Many-to-One (N:1)",
            "ঘ) Many-to-Many (M:N)"
        ],
        "answer": "খ",
        "explanation": "শিক্ষক থেকে কোর্সের সম্পর্ক 1:N (One-to-Many), কারণ একজন শিক্ষকের সাথে সম্পর্কিত হতে পারে একাধিক কোর্স।"
    },
    {
        "id": 26,
        "topic": "ER and EER Modeling",
        "question": "ER মডেলের Many-to-Many (M:N) সম্পর্ককে রিলেশনাল টেবিলে রূপান্তরের জন্য কী প্রয়োজন?",
        "options": [
            "ক) যেকোনো একটি টেবিলে Foreign Key যোগ করলেই হয়",
            "খ) একটি পৃথক সংযোগকারী টেবিল (Junction / Bridge / Associative Table) তৈরি করতে হয়",
            "গ) টেবিল দুটিকে একত্রিত করে একটি ফাইলে রাখা",
            "ঘ) কোনো রূপান্তর সম্ভব নয়"
        ],
        "answer": "খ",
        "explanation": "M:N সম্পর্ক রূপান্তরে উভয় টেবিলের Primary Key-র সমন্বয়ে একটি নতুন টেবিল তৈরি করতে হয় যার composite primary key তৈরি হয়।"
    },
    {
        "id": 27,
        "topic": "ER and EER Modeling",
        "question": "বর্ধিত ER মডেলের (EER) 'স্পেশালাইজেশন' (Specialization) প্রক্রিয়াটি কোন অ্যাপ্রোচ অনুসরণ করে?",
        "options": [
            "ক) Bottom-Up Approach",
            "খ) Top-Down Approach",
            "গ) Hybrid Approach",
            "ঘ) Horizontal Approach"
        ],
        "answer": "খ",
        "explanation": "স্পেশালাইজেশন হলো একটি Top-Down প্রক্রিয়া যেখানে একটি উচ্চস্তরের উচ্চতর সাধারণ সত্তাকে তার বৈশিষ্ট্যের ভিত্তিতে একাধিক নিম্নস্তরের সাবক্লাসে বিভক্ত করা হয়।"
    },
    {
        "id": 28,
        "topic": "ER and EER Modeling",
        "question": "একাধিক নিম্নস্তরের এনটিটির সাধারণ বৈশিষ্ট্যগুলোকে নিয়ে একটি উচ্চস্তরের সুপারক্লাস গঠনের প্রক্রিয়াকে কী বলে?",
        "options": [
            "ক) Generalization (সাধারণীকরণ)",
            "খ) Specialization",
            "গ) Aggregation",
            "ঘ) Normalization"
        ],
        "answer": "ক",
        "explanation": "Generalization হলো একটি Bottom-Up প্রক্রিয়া যেখানে একাধিক এনটিটি (যেমন কার, ট্রাক) সমন্বয়ে উচ্চস্তরের সুপারক্লাস (যেমন Vehicle) গঠিত হয়।"
    },
    {
        "id": 29,
        "topic": "ER and EER Modeling",
        "question": "যখন একটি সম্পর্ক নিজেই অন্য আরেকটি সম্পর্কের সাথে যুক্ত হওয়ার প্রয়োজন পড়ে, তখন EER-এ কোন ধারণাটি ব্যবহৃত হয়?",
        "options": [
            "ক) Generalization",
            "খ) Aggregation",
            "গ) Specialization",
            "ঘ) Cardinality"
        ],
        "answer": "খ",
        "explanation": "Aggregation হলো একটি অ্যাবস্ট্রাকশন যেখানে একটি সম্পর্ক এবং তার সাথে জড়িত এনটিটিগুলোকে সামগ্রিকভাবে একটি একক উচ্চস্তরের এনটিটি হিসেবে গণ্য করা হয়।"
    },
    {
        "id": 30,
        "topic": "ER and EER Modeling",
        "question": "EER মডেলে যদি একজন ব্যক্তি একই সাথে 'Student' এবং 'Employee' সাবক্লাস উভয়েরই সদস্য হতে পারে, তবে সেই স্পেশালাইজেশনকে কী বলে?",
        "options": [
            "ক) Disjoint Specialization",
            "খ) Overlapping Specialization",
            "গ) Total Specialization",
            "ঘ) Partial Disjoint"
        ],
        "answer": "খ",
        "explanation": "Overlapping স্পেশালাইজেশনে একটি এনটিটি একই সময়ে একাধিক সাবক্লাসের সদস্য হতে পারে। আর Disjoint-এ সর্বোচ্চ একটির সদস্য হতে পারে।"
    },
    {
        "id": 31,
        "topic": "ER and EER Modeling",
        "question": "ER মডেলে কী-অ্যাট্রিবিউট (Key Attribute বা Primary Key)-কে কীভাবে নির্দেশ করা হয়?",
        "options": [
            "ক) উপবৃত্তের ভেতরের লেখায় আন্ডারলাইন (Underline) দিয়ে",
            "খ) উপবৃত্তকে ডাবল লাইন দিয়ে",
            "গ) উপবৃত্তের চারপাশে ড্যাশড লাইন দিয়ে",
            "ঘ) গাঢ় রঙের শেড দিয়ে"
        ],
        "answer": "ক",
        "explanation": "Primary Key বা মূল কী অ্যাট্রিবিউট নির্দেশ করতে উপবৃত্তের ভেতরে নামের নিচে সলিড আন্ডারলাইন দেওয়া হয়।"
    },
    {
        "id": 32,
        "topic": "ER and EER Modeling",
        "question": "যদি কোনো দুর্বল সত্তা সেটের নিজস্ব ডিসক্রিমিনেটর $d$ এবং শনাক্তকারী শক্তিশালী সত্তার প্রাইমারি কি $k$ হয়, তবে দুর্বল সত্তা টেবিলের প্রাইমারি কি কী হবে?",
        "options": [
            "ক) কেবল $d$",
            "খ) কেবল $k$",
            "গ) $k$ এবং $d$ এর যৌথ সমন্বয় ($k, d$)",
            "ঘ) কোনো প্রাইমারি কি থাকবে না"
        ],
        "answer": "গ",
        "explanation": "Weak Entity-র রিলেশনাল স্কিমায় শক্তিশালী সত্তার প্রাইমারি কি ($k$) এবং দুর্বল সত্তার আংশিক কি ($d$) উভয়ে মিলে কম্পোজিট প্রাইমারি কি গঠন করে।"
    },
    {
        "id": 33,
        "topic": "ER and EER Modeling",
        "question": "একটি প্রতিষ্ঠানে কর্মী তার ম্যানেজারের অধীনে কাজ করেন এবং ম্যানেজার নিজেও একজন কর্মী। এই রিলেশনশিপকে কী বলা হয়?",
        "options": [
            "ক) Ternary Relationship",
            "খ) Recursive বা Unary Relationship",
            "গ) Composite Relationship",
            "ঘ) Cyclic Relationship"
        ],
        "answer": "খ",
        "explanation": "যখন একই এনটিটি সেট কোনো রিলেশনশিপে ভিন্ন ভিন্ন ভূমিকায় (Role) একাধিকবার অংশগ্রহণ করে, তাকে Recursive বা Unary রিলেশনশিপ বলে।"
    },
    {
        "id": 34,
        "topic": "ER and EER Modeling",
        "question": "মিনিমাম-ম্যাক্সিমাম কনস্ট্রেইন্ট $(min, max)$ যদি $(0, 1)$ হয়, তবে তার অর্থ কী?",
        "options": [
            "ক) অংশগ্রহণ বাধ্যতামূলক এবং সর্বোচ্চ ১টি",
            "খ) অংশগ্রহণ ঐচ্ছিক (Optional/Partial) এবং সর্বোচ্চ ১টিতে অংশ নিতে পারে",
            "গ) অন্তত ১টি এবং সর্বোচ্চ বহু",
            "ঘ) কোনো অংশগ্রহণ সম্ভব নয়"
        ],
        "answer": "খ",
        "explanation": "min=0 মানে হলো পার্টিসিপেশন আংশিক বা ঐচ্ছিক (কোনো সম্পর্কে নাও থাকতে পারে) এবং max=1 মানে সর্বোচ্চ একটি সম্পর্কে জড়াতে পারে।"
    },
    {
        "id": 35,
        "topic": "ER and EER Modeling",
        "question": "কোনো সুপারক্লাসের সমস্ত বৈশিষ্ট্য ও মেথড সাবক্লাস কর্তৃক স্বয়ংক্রিয়ভাবে প্রাপ্ত হওয়ার নীতিকে কী বলে?",
        "options": [
            "ক) Polymorphism",
            "খ) Attribute Inheritance",
            "গ) Encapsulation",
            "ঘ) Normalization"
        ],
        "answer": "খ",
        "explanation": "স্পেশালাইজেশন বা জেনারেলাইজেশন হায়ারার্কিতে সাবক্লাসগুলো তাদের সুপারক্লাস থেকে অ্যাট্রিবিউট ও রিলেশনশিপ উত্তরাধিকার সূত্রে পায়, যাকে Attribute Inheritance বলে।"
    },

    # Subtopic 3: Relational Model & Relational Algebra / Calculus (36-55)
    {
        "id": 36,
        "topic": "Relational Model & Relational Algebra",
        "question": "রিলেশনাল মডেলের প্রবক্তা কে এবং এটি কত সালে প্রস্তাব করা হয়েছিল?",
        "options": [
            "ক) Alan Turing, 1950",
            "খ) E. F. Codd (Edgar Frank Codd), 1970",
            "গ) Charles Bachman, 1965",
            "ঘ) Dennis Ritchie, 1972"
        ],
        "answer": "খ",
        "explanation": "আইবিএম গবেষক ড. ই এফ কড (E. F. Codd) ১৯৭০ সালে 'A Relational Model of Data for Large Shared Data Banks' গবেষণাপত্রে রিলেশনাল ডেটাবেজের ভিত্তি স্থাপন করেন।"
    },
    {
        "id": 37,
        "topic": "Relational Model & Relational Algebra",
        "question": "রিলেশনাল ডেটাবেজে একটি টেবিলের সারি (Row) এবং কলামকে (Column) তাত্ত্বিকভাবে যথাক্রমে কী বলা হয়?",
        "options": [
            "ক) Attribute এবং Tuple",
            "খ) Tuple এবং Attribute",
            "গ) Relation এবং Domain",
            "ঘ) Record এবং File"
        ],
        "answer": "খ",
        "explanation": "রিলেশনাল মডেলে প্রতিটি অনুভূমিক সারিকে টাপল (Tuple) এবং প্রতিটি উল্লম্ব কলামকে অ্যাট্রিবিউট (Attribute) বলা হয়।"
    },
    {
        "id": 38,
        "topic": "Relational Model & Relational Algebra",
        "question": "একটি রিলেশনে টাপলের (Row) মোট সংখ্যাকে কী বলা হয়?",
        "options": [
            "ক) Degree",
            "খ) Cardinality",
            "গ) Domain",
            "ঘ) Order"
        ],
        "answer": "খ",
        "explanation": "একটি রিলেশনের মোট সারির সংখ্যাকে Cardinality এবং মোট কলামের (অ্যাট্রিবিউট) সংখ্যাকে Degree বা Arity বলা হয়।"
    },
    {
        "id": 39,
        "topic": "Relational Model & Relational Algebra",
        "question": "একটি টেবিলে ৫টি কলাম এবং ১০০টি সারি থাকলে টেবিলটির Degree এবং Cardinality কত?",
        "options": [
            "ক) Degree = 100, Cardinality = 5",
            "খ) Degree = 5, Cardinality = 100",
            "গ) Degree = 500, Cardinality = 5",
            "ঘ) Degree = 5, Cardinality = 500"
        ],
        "answer": "খ",
        "explanation": "কলামের সংখ্যা = Degree = 5; সারির সংখ্যা = Cardinality = 100।"
    },
    {
        "id": 40,
        "topic": "Relational Model & Relational Algebra",
        "question": "Entity Integrity Constraint অনুযায়ী প্রাইমারি কি-র ক্ষেত্রে নিচের কোনটি সত্য?",
        "options": [
            "ক) প্রাইমারি কি-র কোনো উপাদান NULL হতে পারবে না",
            "খ) প্রাইমারি কি অবশ্যই স্ট্রিং হতে হবে",
            "গ) প্রাইমারি কি-র মান নেতিবাচক হতে পারবে না",
            "ঘ) প্রাইমারি কি টেবিলের যেকোনো কলাম হতে পারে"
        ],
        "answer": "ক",
        "explanation": "Entity Integrity নিয়মে বলা হয়েছে কোনো প্রাইমারি কি-র মান কখনো NULL (অজ্ঞাত বা অনুপস্থিত) হতে পারে না এবং এটি ইউনিক হতে হবে।"
    },
    {
        "id": 41,
        "topic": "Relational Model & Relational Algebra",
        "question": "Referential Integrity Constraint মূলত কোন দুটির মধ্যকার সম্পর্কের নিশ্চয়তা দেয়?",
        "options": [
            "ক) Primary Key এবং Candidate Key",
            "খ) Foreign Key এবং Referenced Primary Key",
            "গ) Super Key এবং Composite Key",
            "ঘ) Check Constraint এবং Unique Key"
        ],
        "answer": "খ",
        "explanation": "রেফারেন্সিয়াল ইন্টিগ্রিটি অনুযায়ী, চাইল্ড টেবিলের Foreign Key-র প্রতিটি মান প্যারেন্ট টেবিলের Primary Key-তে উপস্থিত থাকতে হবে অথবা মানটি সম্পূর্ণ NULL হতে হবে।"
    },
    {
        "id": 42,
        "topic": "Relational Model & Relational Algebra",
        "question": "রিলেশনাল অ্যালজেবরায় টাপল বা সারি ফিল্টার/সিলেক্ট করার জন্য কোন অপারেটর ব্যবহৃত হয়?",
        "options": [
            "ক) $\\Pi$ (Pi - Projection)",
            "খ) $\\sigma$ (Sigma - Selection)",
            "গ) $\\rho$ (Rho - Rename)",
            "ঘ) $\\bowtie$ (Join)"
        ],
        "answer": "খ",
        "explanation": "সিগমা ($\\\\sigma$) হলো সিলেকশন অপারেটর যা শর্ত পূরণকারী রো বা টাপল নির্বাচন করে (SQL এর WHERE ক্লজের অনুরূপ)।"
    },
    {
        "id": 43,
        "topic": "Relational Model & Relational Algebra",
        "question": "রিলেশনাল অ্যালজেবরায় নির্দিষ্ট কলাম বা অ্যাট্রিবিউট বাছাই করার প্রজেকশন অপারেটর কোনটি?",
        "options": [
            "ক) $\\sigma$ (Sigma)",
            "খ) $\\Pi$ (Pi)",
            "গ) $\\times$ (Cartesian Product)",
            "ঘ) $\\cap$ (Intersection)"
        ],
        "answer": "খ",
        "explanation": "পাই ($\\\\Pi$) হলো প্রজেকশন অপারেটর যা টেবিল থেকে কাঙ্ক্ষিত কলামগুলো নির্বাচন করে এবং স্বয়ংক্রিয়ভাবে ডুপ্লিকেট টাপল বাদ দেয়।"
    },
    {
        "id": 44,
        "topic": "Relational Model & Relational Algebra",
        "question": "দুটি রিলেশন $R$ (যার টাপল সংখ্যা $m$) এবং $S$ (যার টাপল সংখ্যা $n$) এর কার্টেশিয়ান গুণনের ($R \\times S$) টাপল সংখ্যা কত?",
        "options": [
            "ক) $m + n$",
            "খ) $m \\times n$",
            "গ) $m^n$",
            "ঘ) $m / n$"
        ],
        "answer": "খ",
        "explanation": "Cross Product বা Cartesian Product-এ প্রথম টেবিলের প্রতিটি রো দ্বিতীয় টেবিলের প্রতিটি রো-র সাথে যুক্ত হয়, ফলে মোট রো হয় $m \\times n$।"
    },
    {
        "id": 45,
        "topic": "Relational Model & Relational Algebra",
        "question": "ন্যাচারাল জয়েন (Natural Join, $\\bowtie$) সম্পাদনের জন্য দুটি রিলেশনের মধ্যে কী আবশ্যক?",
        "options": [
            "ক) কোনো সাধারণ কলাম থাকা যাবে না",
            "খ) অন্তত একটি অভিন্ন নামের ও সমজাতীয় ডোমেইনের কলাম থাকতে হবে",
            "গ) দুটি টেবিলের ডিগ্রি সমান হতে হবে",
            "ঘ) প্রাইমারি কি একই হতে হবে"
        ],
        "answer": "খ",
        "explanation": "ন্যাচারাল জয়েন উভয় টেবিলের সমনামের কলামের মানের সমতার ভিত্তিতে জয়েন করে এবং ফলাফল থেকে ডুপ্লিকেট কলাম বাদ দিয়ে একটি কলাম রাখে।"
    },
    {
        "id": 46,
        "topic": "Relational Model & Relational Algebra",
        "question": "রিলেশনাল অ্যালজেবরায় সেট অপারেশন (Union, Intersection, Set Difference) করার জন্য টেবিল দুটিকে কী হতে হয়?",
        "options": [
            "ক) Primary Compatible",
            "খ) Union Compatible (একই ডিগ্রি ও সমজাতীয় ডোমেইন)",
            "গ) Cardinality Compatible",
            "ঘ) Normalized"
        ],
        "answer": "খ",
        "explanation": "Union Compatibility-র শর্ত হলো দুটি রিলেশনের অ্যাট্রিবিউটের সংখ্যা (Degree) সমান হতে হবে এবং অনুরূপ কলামগুলোর ডেটা টাইপ বা ডোমেইন এক হতে হবে।"
    },
    {
        "id": 47,
        "topic": "Relational Model & Relational Algebra",
        "question": "লেফট আউটার জয়েন (Left Outer Join, $\\leftouterjoin$) এর বৈশিষ্ট্য কোনটি?",
        "options": [
            "ক) শুধুমাত্র ম্যাচ করা টাপল ফিরিয়ে দেয়",
            "খ) বাম টেবিলের সব টাপল রাখে, ডান টেবিলের সাথে ম্যাচ না করলে NULL বসায়",
            "গ) ডান টেবিলের সব টাপল রাখে এবং বাম টেবিল বাদ দেয়",
            "ঘ) সব টাপল বাদ দেয়"
        ],
        "answer": "খ",
        "explanation": "লেফট আউটার জয়েন বাম টেবিলের সমস্ত রেকর্ড প্রদর্শন করে এবং ডান টেবিল থেকে শর্ত মেলানো রেকর্ড আনে; ডান টেবিলে কোনো মিল না থাকলে সেখানে NULL প্রদর্শন করে।"
    },
    {
        "id": 48,
        "topic": "Relational Model & Relational Algebra",
        "question": "রিলেশনাল অ্যালজেবরায় রিলেশন বা অ্যাট্রিবিউটের নাম পরিবর্তনের (Rename) জন্য কোন প্রতীক ব্যবহৃত হয়?",
        "options": [
            "ক) $\\theta$ (Theta)",
            "খ) $\\rho$ (Rho)",
            "গ) $\\gamma$ (Gamma)",
            "ঘ) $\\delta$ (Delta)"
        ],
        "answer": "খ",
        "explanation": "রো ($\\\\rho$) অপারেটর রিলেশন বা অ্যাট্রিবিউটের পুনঃনামকরণ করতে ব্যবহৃত হয়। যেমন: $\\\\rho_{S}(R)$।"
    },
    {
        "id": 49,
        "topic": "Relational Model & Relational Algebra",
        "question": "একটি প্রতিষ্ঠানে 'সকল প্রকল্পে' (All projects) কর্মরত কর্মীদের খুঁজে পেতে রিলেশনাল অ্যালজেবরার কোন অপারেটরটি সবচেয়ে উপযোগী?",
        "options": [
            "ক) Cartesian Product ($\\times$)",
            "খ) Division Operator ($\\div$)",
            "গ) Theta Join ($\\bowtie_\\theta$)",
            "ঘ) Intersection ($\\cap$)"
        ],
        "answer": "খ",
        "explanation": "'For all' বা 'সবগুলোতেই অংশ নেওয়া' সম্পর্কিত কুয়েরি বাস্তবায়নে ডিভিশন অপারেটর ($R \\\\div S$) ব্যবহৃত হয়।"
    },
    {
        "id": 50,
        "topic": "Relational Model & Relational Algebra",
        "question": "রিলেশনাল অ্যালজেবরা এবং রিলেশনাল ক্যালকুলাসের মধ্যে প্রধান পার্থক্য কী?",
        "options": [
            "ক) অ্যালজেবরা হলো ডিক্লারেটিভ, ক্যালকুলাস হলো প্রসিডিউরাল",
            "খ) অ্যালজেবরা হলো প্রসিডিউরাল (কীভাবে বের করতে হবে), ক্যালকুলাস হলো নন-প্রসিডিউরাল/ডিক্লারেটিভ (কী চাই)",
            "গ) উভয়েই একই সিনট্যাক্স ব্যবহার করে",
            "ঘ) ক্যালকুলাসে কোনো ম্যাথমেটিক্যাল লজিক নেই"
        ],
        "answer": "খ",
        "explanation": "Relational Algebra নির্দেশ করে কীভাবে ফলাফল পেতে হবে (Procedural), আর Relational Calculus (TRC/DRC) নির্দেশ করে কী ফলাফল প্রয়োজন, কীভাবে তা নয় (Declarative)।"
    },
    {
        "id": 51,
        "topic": "Relational Model & Relational Algebra",
        "question": "টাপল রিলেশনাল ক্যালকুলাস (TRC)-এ কুয়েরির সাধারণ রূপ কোনটি?",
        "options": [
            "ক) $\\{ t \\mid P(t) \\}$",
            "খ) $\\sigma_{P}(t)$",
            "গ) $\\Pi_{P}(t)$",
            "ঘ) $f(t) \\to P$"
        ],
        "answer": "ক",
        "explanation": "TRC এক্সপ্রেশনের সাধারণ রূপ হলো $\\\\{ t \\\\mid P(t) \\\\}$, যার অর্থ হলো এমন সকল টাপল $t$ এর সেট যার জন্য প্রেডিকেট $P(t)$ সত্য।"
    },
    {
        "id": 52,
        "topic": "Relational Model & Relational Algebra",
        "question": "যদি কোনো কুয়েরি ভাষা দিয়ে রিলেশনাল অ্যালজেবরার সমান শক্তিশালী সকল এক্সপ্রেশন প্রকাশ করা যায়, তবে সেই ভাষাকে কী বলে?",
        "options": [
            "ক) Turing Complete",
            "খ) Relationally Complete",
            "গ) Algebraically Closed",
            "ঘ) Functionally Complete"
        ],
        "answer": "খ",
        "explanation": "কড-এর সংজ্ঞানুযায়ী, একটি ভাষা যদি বেসিক রিলেশনাল অ্যালজেবরা দ্বারা প্রকাশিত যেকোনো কুয়েরি প্রকাশ করতে সক্ষম হয়, তাকে Relationally Complete বলা হয়।"
    },
    {
        "id": 53,
        "topic": "Relational Model & Relational Algebra",
        "question": "Super Key এবং Candidate Key-র মধ্যে মূল পার্থক্য কোনটি?",
        "options": [
            "ক) Super Key সবসময় একক কলাম হয়",
            "খ) Candidate Key হলো মিনিমাল সুপার কি (Minimal Super Key)",
            "গ) Candidate Key-তে ডুপ্লিকেট মান থাকতে পারে",
            "ঘ) এদের মধ্যে কোনো পার্থক্য নেই"
        ],
        "answer": "খ",
        "explanation": "একটি রিলেশনের যেকোনো অ্যাট্রিবিউট সেট যা টাপলকে ইউনিকলি শনাক্ত করতে পারে তা Super Key। এর মধ্যে থেকে অপ্রয়োজনীয় অ্যাট্রিবিউট বাদ দিলে যে ক্ষুদ্রতম সেট পাওয়া যায় তা Candidate Key।"
    },
    {
        "id": 54,
        "topic": "Relational Model & Relational Algebra",
        "question": "একটি টেবিলে একাধিক ক্যান্ডিডেট কি থাকলে যেটিকে মূল শনাক্তকারী হিসেবে বাছাই করা হয় তাকে কী বলে?",
        "options": [
            "ক) Foreign Key",
            "খ) Primary Key",
            "গ) Alternate Key",
            "ঘ) Secondary Key"
        ],
        "answer": "খ",
        "explanation": "ডেটাবেজ ডিজাইনার ক্যান্ডিডেট কি-গুলোর মধ্যে থেকে একটিকে প্রাইমারি কি হিসেবে নির্বাচন করেন। বাকি ক্যান্ডিডেট কি-গুলোকে Alternate Key বলা হয়।"
    },
    {
        "id": 55,
        "topic": "Relational Model & Relational Algebra",
        "question": "নিচের কোনটি রিলেশনাল মডেলের মৌলিক ইন্টিগ্রিটি রুল নয়?",
        "options": [
            "ক) Entity Integrity",
            "খ) Referential Integrity",
            "গ) Domain Integrity",
            "ঘ) Operating System Integrity"
        ],
        "answer": "ঘ",
        "explanation": "রিলেশনাল মডেলের তিনটি কোর ইন্টিগ্রিটি নিয়ম হলো: Entity Integrity, Referential Integrity এবং Domain Integrity।"
    },

    # Subtopic 4: Functional Dependencies & Normalization (56-80)
    {
        "id": 56,
        "topic": "Functional Dependencies & Normalization",
        "question": "যদি একটি রিলেশনে $X$-এর প্রতিটি মানের জন্য $Y$-এর ঠিক একটিই মান নির্ধারিত থাকে, তবে ফাংশনাল ডিপেন্ডেন্সি কীভাবে লেখা হয়?",
        "options": [
            "ক) $Y \\to X$",
            "খ) $X \\to Y$ ($X$ functionally determines $Y$)",
            "গ) $X \\leftrightarrow Y$",
            "ঘ) $X \\subset Y$"
        ],
        "answer": "খ",
        "explanation": "$X \\\\to Y$ নির্দেশ করে যে অ্যাট্রিবিউট $X$ দ্বারা $Y$ কার্যকরীভাবে নির্ধারিত (Functionally Determined) হয়। এখানে $X$ হলো নির্ণায়ক (Determinant)।"
    },
    {
        "id": 57,
        "topic": "Functional Dependencies & Normalization",
        "question": "আর্মস্ট্রং-এর স্বতঃসিদ্ধের (Armstrong's Axioms) 'ট্রানজিটিভিটি রুল' (Transitivity Rule) কোনটি?",
        "options": [
            "ক) If $X \\to Y$, then $XZ \\to YZ$",
            "খ) If $Y \\subseteq X$, then $X \\to Y$",
            "গ) If $X \\to Y$ and $Y \\to Z$, then $X \\to Z$",
            "ঘ) If $X \\to Y$ and $X \\to Z$, then $X \\to YZ$"
        ],
        "answer": "গ",
        "explanation": "যদি $X$ থেকে $Y$ এবং $Y$ থেকে $Z$ নির্ধারিত হয়, তবে স্বাভাবিকভাবেই $X$ থেকে $Z$ নির্ধারিত হবে ($X \\\\to Z$); এটি Transitivity Rule।"
    },
    {
        "id": 58,
        "topic": "Functional Dependencies & Normalization",
        "question": "আর্মস্ট্রং-এর অগমেন্টেশন রুল (Augmentation Rule) কোনটি নির্দেশ করে?",
        "options": [
            "ক) If $X \\to Y$, then $XZ \\to YZ$",
            "খ) If $X \\to YZ$, then $X \\to Y$",
            "গ) If $X \\to Y$, then $Y \\to X$",
            "ঘ) If $XY \\to Z$, then $X \\to Z$"
        ],
        "answer": "ক",
        "explanation": "উভয় পাশে যেকোনো অ্যাট্রিবিউট সেট $Z$ যুক্ত করলে ডিপেন্ডেন্সি বজায় থাকে: $X \\\\to Y \\\\implies XZ \\\\to YZ$।"
    },
    {
        "id": 59,
        "topic": "Functional Dependencies & Normalization",
        "question": "যদি $Y \\subseteq X$ হয়, তবে $X \\to Y$ ডিপেন্ডেন্সিকে কী বলা হয়?",
        "options": [
            "ক) Non-trivial Functional Dependency",
            "খ) Trivial Functional Dependency (তুচ্ছ নির্ভরতা)",
            "গ) Partial Dependency",
            "ঘ) Transitive Dependency"
        ],
        "answer": "খ",
        "explanation": "ডানপাশের অ্যাট্রিবিউট যদি বামপাশের অ্যাট্রিবিউট সেটের একটি সাবসেট হয় (যেমন: $AB \\\\to A$), তবে তাকে সর্বদা সত্য বা Trivial Functional Dependency বলে।"
    },
    {
        "id": 60,
        "topic": "Functional Dependencies & Normalization",
        "question": "একটি রিলেশন ফার্স্ট নরমাল ফর্মে (1NF) থাকার প্রধান শর্ত কোনটি?",
        "options": [
            "ক) কোনো ট্রানজিটিভ ডিপেন্ডেন্সি থাকা যাবে না",
            "খ) প্রতিটি কলামের মান অবশ্যই অ্যাটমিক (Atomic / অবিভাজ্য) হতে হবে এবং কোনো রিপিটিং গ্রুপ থাকা যাবে না",
            "গ) সমস্ত কলামকে প্রাইমারি কি হতে হবে",
            "ঘ) BCNF মেনে চলতে হবে"
        ],
        "answer": "খ",
        "explanation": "1NF নিশ্চিত করে যে টেবিলে কোনো মাল্টি-ভ্যালুড অ্যাট্রিবিউট বা কম্পোজিট অ্যাট্রিবিউট বা নেস্টেড টেবিল থাকবে না; প্রতিটি সেলে কেবল একটি একক অ্যাটমিক মান থাকবে।"
    },
    {
        "id": 61,
        "topic": "Functional Dependencies & Normalization",
        "question": "সেকেন্ড নরমাল ফর্মে (2NF) উত্তীর্ণ হওয়ার জন্য রিলেশনটিতে কোন ধরণের নির্ভরতা থাকা যাবে না?",
        "options": [
            "ক) আংশিক নির্ভরতা (Partial Dependency)",
            "খ) ট্রানজিটিভ নির্ভরতা (Transitive Dependency)",
            "গ) মাল্টি-ভ্যালুড নির্ভরতা (Multivalued Dependency)",
            "ঘ) ট্রাইভিয়াল নির্ভরতা"
        ],
        "answer": "ক",
        "explanation": "2NF-এ থাকার শর্ত: টেবিলটি 1NF-এ থাকবে এবং কোনো নন-প্রাইম অ্যাট্রিবিউট কম্পোজিট ক্যান্ডিডেট কি-র কোনো অংশের ওপর আংশিকভাবে নির্ভরশীল (Partial Dependency) হতে পারবে না।"
    },
    {
        "id": 62,
        "topic": "Functional Dependencies & Normalization",
        "question": "নন-প্রাইম অ্যাট্রিবিউট (Non-prime attribute) বলতে কী বোঝায়?",
        "options": [
            "ক) যে অ্যাট্রিবিউটটি কোনো ক্যান্ডিডেট কি-র অংশ নয়",
            "খ) যে অ্যাট্রিবিউটে মৌলিক সংখ্যা নেই",
            "গ) Foreign Key অ্যাট্রিবিউট",
            "ঘ) কেবল NULL মান ধারণকারী কলাম"
        ],
        "answer": "ক",
        "explanation": "যে অ্যাট্রিবিউটগুলো কোনো ক্যান্ডিডেট কি (Candidate Key)-র অন্তর্ভুক্ত থাকে সেগুলোকে Prime Attribute এবং বাকিগুলোকে Non-prime Attribute বলে।"
    },
    {
        "id": 63,
        "topic": "Functional Dependencies & Normalization",
        "question": "থার্ড নরমাল ফর্মের (3NF) মূল উদ্দেশ্য কোনটি দূর করা?",
        "options": [
            "ক) Partial Dependency",
            "খ) Transitive Dependency (পরোক্ষ বা সংক্রামক নির্ভরতা)",
            "গ) Multivalued Dependency",
            "ঘ) Join Dependency"
        ],
        "answer": "খ",
        "explanation": "3NF-এ কোনো নন-প্রাইম অ্যাট্রিবিউট অন্য কোনো নন-প্রাইম অ্যাট্রিবিউটের ওপর নির্ভরশীল হতে পারে না ($X \\\\to Y$ হলে $X$ কে অবশ্যই Super Key হতে হবে অথবা $Y$ কে Prime Attribute হতে হবে)।"
    },
    {
        "id": 64,
        "topic": "Functional Dependencies & Normalization",
        "question": "BCNF (Boyce-Codd Normal Form)-এর কঠোর শর্ত কোনটি?",
        "options": [
            "ক) প্রতিটি নন-ট্রিভিয়াল $X \\to Y$ ডিপেন্ডেন্সিতে $X$ কে অবশ্যই একটি Super Key হতে হবে",
            "খ) $Y$ কে অবশ্যই একটি প্রাইম অ্যাট্রিবিউট হতে হবে",
            "গ) টেবিলে সর্বোচ্চ ৩টি কলাম থাকতে পারবে",
            "ঘ) কেবল 1NF মানলেই BCNF হবে"
        ],
        "answer": "ক",
        "explanation": "BCNF-এ প্রতিটি নন-ট্রিভিয়াল ফাংশনাল ডিপেন্ডেন্সি $X \\\\to Y$-এর জন্য বামপাশের নির্ধারক $X$ কে অবশ্যই সুপার কি হতে হবে। 3NF-এর শিথিলতা ($Y$ প্রাইম হওয়ার সুযোগ) BCNF-এ নেই।"
    },
    {
        "id": 65,
        "topic": "Functional Dependencies & Normalization",
        "question": "3NF এবং BCNF-এর সম্পর্কের ক্ষেত্রে নিচের কোন উক্তিটি সর্বদাই সত্য?",
        "options": [
            "ক) প্রতিটি 3NF রিলেশনই BCNF",
            "খ) প্রতিটি BCNF রিলেশনই 3NF, কিন্তু সকল 3NF রিলেশন BCNF নাও হতে পারে",
            "গ) BCNF এবং 3NF সম্পূর্ণ বিপরীত ধারণার",
            "ঘ) 3NF সর্বদা লসলেস হয় না"
        ],
        "answer": "খ",
        "explanation": "BCNF হলো 3NF-এর চেয়েও কঠোর একটি রূপ। তাই যেকোনো রিলেশন BCNF হলে তা স্বয়ংক্রিয়ভাবে 3NF হবে, তবে বিপরীতটি সর্বদা সত্য নয়।"
    },
    {
        "id": 66,
        "topic": "Functional Dependencies & Normalization",
        "question": "ফোর্থ নরমাল ফর্ম (4NF) কোন ধরণের নির্ভরতা নিরসনের সাথে সম্পর্কিত?",
        "options": [
            "ক) Partial Dependency",
            "খ) Transitive Dependency",
            "গ) Multivalued Dependency (MVD, $X \\twoheadrightarrow Y$)",
            "ঘ) Join Dependency"
        ],
        "answer": "গ",
        "explanation": "4NF মাল্টি-ভ্যালুড ডিপেন্ডেন্সি (MVD) নিরসন করে। যখন একটি টেবিলে দুটি সম্পূর্ণ স্বাধীন বহুমানসম্পন্ন অ্যাট্রিবিউট থাকে তখন ডেটা অপ্রয়োজনীয়ভাবে বৃদ্ধি পায়।"
    },
    {
        "id": 67,
        "topic": "Functional Dependencies & Normalization",
        "question": "ফিফথ নরমাল ফর্ম (5NF) অন্য কোন নামে পরিচিত?",
        "options": [
            "ক) Boyce-Codd Normal Form",
            "খ) Project-Join Normal Form (PJ/NF)",
            "গ) Domain-Key Normal Form (DKNF)",
            "ঘ) Strict Normal Form"
        ],
        "answer": "খ",
        "explanation": "5NF কে Project-Join Normal Form (PJNF) বলা হয়, যা Join Dependency নিরসন করে।"
    },
    {
        "id": 68,
        "topic": "Functional Dependencies & Normalization",
        "question": "একটি রিলেশন $R(A, B, C)$-কে $R_1(A, B)$ এবং $R_2(B, C)$-তে ডিকম্পোজ করা হলে এটি Lossless-Join হওয়ার প্রয়োজনীয় ও পর্যাপ্ত শর্ত কী?",
        "options": [
            "ক) $R_1 \\cap R_2 \\to R_1$ অথবা $R_1 \\cap R_2 \\to R_2$ সত্য হতে হবে",
            "খ) $R_1$ এবং $R_2$ তে কোনো সাধারণ অ্যাট্রিবিউট থাকা যাবে না",
            "গ) $R_1$ এবং $R_2$ এর সারি সংখ্যা সমান হতে হবে",
            "ঘ) $A \\to C$ হতে হবে"
        ],
        "answer": "ক",
        "explanation": "দুটি সাব-রিলেশনে লসলেস জয়েনের শর্ত হলো তাদের সাধারণ অ্যাট্রিবিউট সেট ($R_1 \\\\cap R_2 = B$) অন্তত একটি সাব-রিলেশনের সুপার কি হতে হবে।"
    },
    {
        "id": 69,
        "topic": "Functional Dependencies & Normalization",
        "question": "ডিকম্পোজিশনের পর মূল টেবিলের সকল ফাংশনাল ডিপেন্ডেন্সি সাব-টেবিলগুলোর এফডি থেকে যাচাই করা সম্ভব হলে তাকে কী বলে?",
        "options": [
            "ক) Lossless Decomposition",
            "খ) Dependency Preservation",
            "গ) Redundant Decomposition",
            "ঘ) Minimal Coverage"
        ],
        "answer": "খ",
        "explanation": "Dependency Preservation নিশ্চিত করে যে ডিকম্পোজিশনের পরেও মূল টেবিলের সমস্ত FD সংরক্ষিত আছে এবং কোনো জয়েন ছাড়াই ইন্টিগ্রিটি চেক করা সম্ভব।"
    },
    {
        "id": 70,
        "topic": "Functional Dependencies & Normalization",
        "question": "3NF ডিকম্পোজিশন সর্বদা কোন দুটি বৈশিষ্ট্য গ্যারান্টি দেয়?",
        "options": [
            "ক) কেবল Lossless-Join",
            "খ) Lossless-Join এবং Dependency Preservation উভয়ই",
            "গ) কোনোটিই নয়",
            "ঘ) কেবল BCNF রূপান্তর"
        ],
        "answer": "খ",
        "explanation": "যেকোনো রিলেশন স্কিমাকে সর্বদা এমনভাবে 3NF-এ ডিকম্পোজ করা সম্ভব যা একই সাথে Lossless-Join এবং Dependency Preserving উভয়ই বজায় রাখে।"
    },
    {
        "id": 71,
        "topic": "Functional Dependencies & Normalization",
        "question": "BCNF ডিকম্পোজিশন সর্বদা কোনটি গ্যারান্টি দেয় কিন্তু কখনো কখনো অপরটি হারাতে পারে?",
        "options": [
            "ক) Lossless-Join নিশ্চিত করে কিন্তু Dependency Preservation বজায় নাও থাকতে পারে",
            "খ) Dependency Preservation নিশ্চিত করে কিন্তু Lossless নাও হতে পারে",
            "গ) উভয়ই হারায়",
            "ঘ) কোনো পরিবর্তন হয় না"
        ],
        "answer": "ক",
        "explanation": "BCNF ডিকম্পোজিশন সবসময় Lossless-Join নিশ্চিত করতে পারে, কিন্তু অনেক সময় Dependency Preservation অর্জন করা অসম্ভব হয়ে পড়ে।"
    },
    {
        "id": 72,
        "topic": "Functional Dependencies & Normalization",
        "question": "অ্যাট্রিবিউট ক্লোজার (Attribute Closure, $X^+$) বলতে কী বোঝায়?",
        "options": [
            "ক) কেবলমাত্র $X$-এর নিজস্ব মান",
            "খ) $X$ দ্বারা ফাংশনালি নির্ধারিত হতে পারে এমন সমস্ত অ্যাট্রিবিউটের সেট",
            "গ) $X$-এর প্রাইমারি কি তালিকা",
            "ঘ) $X$ কলামের সর্বোচ্চ মান"
        ],
        "answer": "খ",
        "explanation": "$X^+$ হলো এমন সমস্ত অ্যাট্রিবিউটের সেট যা প্রদত্ত FD সেটের সাহায্যে $X$ থেকে বের করা সম্ভব।"
    },
    {
        "id": 73,
        "topic": "Functional Dependencies & Normalization",
        "question": "যদি কোনো অ্যাট্রিবিউট সেট $X$-এর ক্লোজার $X^+$ পুরো রিলেশনের সকল অ্যাট্রিবিউট ধারণ করে, তবে $X$ অবশ্যই একটি কী?",
        "options": [
            "ক) Foreign Key",
            "খ) Super Key",
            "গ) Non-prime attribute",
            "ঘ) Nullable Key"
        ],
        "answer": "খ",
        "explanation": "যেহেতু $X$ রিলেশনের সকল অ্যাট্রিবিউট নির্ধারণ করতে পারে, তাই সংজ্ঞা অনুযায়ী $X$ একটি Super Key।"
    },
    {
        "id": 74,
        "topic": "Functional Dependencies & Normalization",
        "question": "ক্যানোনিকাল কভার (Canonical Cover বা Minimal Cover) $F_c$-এর বৈশিষ্ট্য কোনটি?",
        "options": [
            "ক) এতে কোনো অতিরিক্ত (Extraneous) অ্যাট্রিবিউট বা অপ্রয়োজনীয় FD থাকে না",
            "খ) প্রতিটি FD-র ডানপাশে ঠিক একটি অ্যাট্রিবিউট থাকে",
            "গ) এর ক্লোজার মূল সেট $F$-এর ক্লোজারের সমান ($F_c^+ = F^+$)",
            "ঘ) উপরের সবগুলো"
        ],
        "answer": "ঘ",
        "explanation": "ক্যানোনিকাল কভার হলো মূল FD সেটের একটি ন্যূনতম সমতুল্য রূপ যাতে কোনো অপ্রয়োজনীয় নির্ভরতা বা অতিরিক্ত অ্যাট্রিবিউট থাকে না।"
    },
    {
        "id": 75,
        "topic": "Functional Dependencies & Normalization",
        "question": "একটি রিলেশনে ইনসার্ট, ডিলিট বা আপডেটের সময় অসঙ্গতি দেখা দিলে তাকে কী বলা হয়?",
        "options": [
            "ক) Normalization",
            "খ) Modification Anomaly (অ্যানোমালি)",
            "গ) Deadlock",
            "ঘ) Serialization"
        ],
        "answer": "খ",
        "explanation": "খারাপ ডেটাবেজ ডিজাইনের কারণে ডেটা ঢুকানো, মোছা বা সংশোধনের সময় তৈরি হওয়া ত্রুটিকে যথাক্রমে Insertion, Deletion এবং Update Anomaly বলে।"
    },
    {
        "id": 76,
        "topic": "Functional Dependencies & Normalization",
        "question": "উচ্চস্তরের নরমালাইজেশনের প্রধান অপূর্ণতা বা ট্রেড-অফ (Trade-off) কোনটি?",
        "options": [
            "ক) ডেটা রিডান্ড্যান্সি বৃদ্ধি পায়",
            "খ) কুয়েরি করার সময় অতিরিক্ত Join অপারেশন প্রয়োজন হওয়ায় কুয়েরি এক্সিকিউশন ধীর হতে পারে",
            "গ) ডেটা ইনকনসিস্টেন্সি বেড়ে যায়",
            "ঘ) স্টোরেজ ক্ষমতা কমে যায়"
        ],
        "answer": "খ",
        "explanation": "নরমালাইজেশনের ফলে টেবিল ভেঙে ছোট ছোট একাধিক টেবিলে পরিণত হয়, যার ফলে রিড কুয়েরির সময় অনেক টেবিল JOIN করতে হয় এবং পারফরম্যান্স ধীর হতে পারে।"
    },
    {
        "id": 77,
        "topic": "Functional Dependencies & Normalization",
        "question": "কুয়েরি পারফরম্যান্স ও রিড স্পিড বাড়ানোর লক্ষ্যে ইচ্ছাকৃতভাবে কিছুটা রিডান্ড্যান্সি রাখার প্রক্রিয়াকে কী বলে?",
        "options": [
            "ক) Denormalization (ডিনরমালাইজেশন)",
            "খ) De-indexing",
            "গ) Regression",
            "ঘ) Over-normalization"
        ],
        "answer": "ক",
        "explanation": "Data Warehouse বা OLAP সিস্টেমে দ্রুত পড়ার সুবিধার জন্য নরমালাইজড টেবিলগুলোকে আবার একত্রিত করাকে Denormalization বলে।"
    },
    {
        "id": 78,
        "topic": "Functional Dependencies & Normalization",
        "question": "ধরা যাক $R(A, B, C, D)$ এবং $FD = \\{A \\to B, B \\to C, C \\to D\\}$। এখানে $A \\to D$ কোন নিয়মে সত্য?",
        "options": [
            "ক) Reflexivity",
            "খ) Augmentation",
            "গ) Transitivity",
            "ঘ) Decomposition"
        ],
        "answer": "গ",
        "explanation": "$A \\\\to B$ এবং $B \\\\to C$ থেকে $A \\\\to C$ পাওয়া যায়, আবার $A \\\\to C$ এবং $C \\\\to D$ থেকে $A \\\\to D$ পাওয়া যায়—এটি Transitivity।"
    },
    {
        "id": 79,
        "topic": "Functional Dependencies & Normalization",
        "question": "একটি টেবিলে যদি কেবল একটিই ক্যান্ডিডেট কি থাকে এবং সেটি একক (Non-composite) অ্যাট্রিবিউট হয়, তবে টেবিলটি 1NF হলে স্বয়ংক্রিয়ভাবে কোন নর্মাল ফর্মে থাকবে?",
        "options": [
            "ক) 2NF",
            "খ) BCNF",
            "গ) 4NF",
            "ঘ) 5NF"
        ],
        "answer": "ক",
        "explanation": "ক্যান্ডিডেট কি একক অ্যাট্রিবিউট হলে কোনো আংশিক নির্ভরতা (Partial Dependency) থাকা গাণিতিকভাবে অসম্ভব, ফলে টেবিলটি 1NF হলে অবধারিতভাবেই 2NF হবে।"
    },
    {
        "id": 80,
        "topic": "Functional Dependencies & Normalization",
        "question": "নিচের কোন নরমাল ফর্মটিকে ডোমেইন এবং কি ভিত্তিক চূড়ান্ত রূপ (Domain-Key Normal Form) বলা হয়?",
        "options": [
            "ক) 3NF",
            "খ) BCNF",
            "গ) DKNF",
            "ঘ) 4NF"
        ],
        "answer": "গ",
        "explanation": "DKNF (Domain-Key Normal Form)-এ সমস্ত সীমাবদ্ধতা কেবলমাত্র ডোমেইন এবং কি কনস্ট্রেইন্টের সাহায্যে প্রকাশ করা হয়; এটি তাত্ত্বিক সর্বোচ্চ নরমাল ফর্ম।"
    },

    # Subtopic 5: SQL (DDL, DML, DCL, TCL, Subqueries, Joins, Triggers, Views) (81-100)
    {
        "id": 81,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ কোনো টেবিলের গঠন পুরোপুরি মুছে ফেলতে কোন DDL কমান্ডটি ব্যবহৃত হয়?",
        "options": [
            "ক) DELETE TABLE",
            "খ) DROP TABLE",
            "গ) TRUNCATE TABLE",
            "ঘ) REMOVE TABLE"
        ],
        "answer": "খ",
        "explanation": "DROP TABLE কমান্ড দিয়ে টেবিলের স্কিমা, স্ট্রাকচার ও ডেটা সম্পূর্ণভাবে ডেটা ডিকশনারি থেকে মুছে ফেলা হয়। TRUNCATE বা DELETE কেবল ভেতরের ডেটা মুছে স্ট্রাকচার ঠিক রাখে।"
    },
    {
        "id": 82,
        "topic": "SQL & Relational Database Systems",
        "question": "DELETE এবং TRUNCATE কমান্ডের মধ্যে মূল পার্থক্য কী?",
        "options": [
            "ক) TRUNCATE হলো DDL কমান্ড, এটি রো-বাই-রো লগ রাখে না এবং DELETE-এর চেয়ে অনেক দ্রুত",
            "খ) DELETE টেবিলে কোনো WHERE ক্লজ নেয় না",
            "গ) TRUNCATE রোলব্যাক করা অনেক সহজ",
            "ঘ) তাদের মধ্যে কোনো পার্থক্য নেই"
        ],
        "answer": "ক",
        "explanation": "TRUNCATE হলো DDL অপারেশন যা সম্পূর্ণ পেজ ডিলিকেট করে একবারে টেবিল খালি করে ফেলে, এটি লগ কম তৈরি করে এবং অনেক দ্রুত। DELETE হলো DML যা প্রতি রো-র জন্য লগ লেখে।"
    },
    {
        "id": 83,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL এগ্রিগেট ফাংশন ব্যবহারের পর গ্রুপকৃত ডেটার ওপর শর্ত প্রয়োগ করতে কোন ক্লজ ব্যবহৃত হয়?",
        "options": [
            "ক) WHERE",
            "খ) HAVING",
            "গ) ORDER BY",
            "ঘ) GROUP FILTER"
        ],
        "answer": "খ",
        "explanation": "WHERE ক্লজ ব্যক্তিগত রো-র ওপর শর্ত আরোপ করে, আর GROUP BY-এর মাধ্যমে তৈরি হওয়া গ্রুপের এগ্রিগেট ফলের ওপর শর্ত দিতে HAVING ক্লজ ব্যবহৃত হয়।"
    },
    {
        "id": 84,
        "topic": "SQL & Relational Database Systems",
        "question": "নিচের কোন এগ্রিগেট ফাংশনটি NULL মানকে উপেক্ষা (Ignore) করে না?",
        "options": [
            "ক) AVG(column_name)",
            "খ) COUNT(*)",
            "গ) SUM(column_name)",
            "ঘ) MAX(column_name)"
        ],
        "answer": "খ",
        "explanation": "COUNT(*) টেবিলের মোট রো সংখ্যা গণনা করে যাতে NULL মান থাকা সারিও অন্তর্ভুক্ত হয়। বাকি সব এগ্রিগেট ফাংশন কলামের NULL মান বাদ দিয়ে হিসাব করে।"
    },
    {
        "id": 85,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ স্ট্রিং প্যাটার্ন ম্যাচিংয়ের জন্য কোন অপারেটর এবং ওয়াইল্ডকার্ড ব্যবহার করা হয়?",
        "options": [
            "ক) MATCH এবং *",
            "খ) LIKE এবং %, _",
            "গ) EQUALS এবং ?",
            "ঘ) REGEX এবং #"
        ],
        "answer": "খ",
        "explanation": "SQL-এ LIKE অপারেটরে '%' শূন্য বা ততোধিক অক্ষরের জন্য এবং '_' ঠিক একটি নির্দিষ্ট অক্ষরের জন্য ওয়াইল্ডকার্ড হিসেবে ব্যবহৃত হয়।"
    },
    {
        "id": 86,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ একটি ভার্চুয়াল টেবিল তৈরি করার স্টেটমেন্ট কোনটি?",
        "options": [
            "ক) CREATE TABLE ...",
            "খ) CREATE VIEW ... AS SELECT ...",
            "গ) CREATE TEMPORARY ...",
            "ঘ) CREATE SNAPSHOT ..."
        ],
        "answer": "খ",
        "explanation": "View হলো একটি সংরক্ষিত SQL কুয়েরি ভিত্তিক ভার্চুয়াল টেবিল যা ফিজিক্যালি ডেটা স্টোর করে না কিন্তু টেবিলের মতো অ্যাক্সেস করা যায়।"
    },
    {
        "id": 87,
        "topic": "SQL & Relational Database Systems",
        "question": "নিচের কোন ধরণের সাবকুয়েরিটি আউটার কুয়েরির প্রতিটি রো-র জন্য বারবার এক্সিকিউট হয়?",
        "options": [
            "ক) Non-correlated Subquery",
            "খ) Correlated Subquery",
            "গ) Scalar Subquery",
            "ঘ) Static Subquery"
        ],
        "answer": "খ",
        "explanation": "Correlated Subquery আউটার কুয়েরির কলাম রেফারেন্স ব্যবহার করে, ফলে আউটার কুয়েরির প্রতিটি সারির জন্য সাবকুয়েরিটি পুনরাবৃত্তভাবে এক্সিকিউট হয়।"
    },
    {
        "id": 88,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ 'EXISTS' অপারেটর কখন TRUE রিটার্ন করে?",
        "options": [
            "ক) যদি সাবকুয়েরিটি অন্তত একটি রো রিটার্ন করে",
            "খ) যদি সাবকুয়েরিটি খালি থাকে",
            "গ) যদি সাবকুয়েরিটি কেবল সংখ্যা দেয়",
            "ঘ) যদি কোনো এরর না হয়"
        ],
        "answer": "ক",
        "explanation": "EXISTS অপারেটর সাবকুয়েরিতে অন্তত একটি রো পাওয়া গেলেই TRUE রিটার্ন করে এবং সাথে সাথে তল্লাশি বন্ধ করে, যা কুয়েরি দ্রুত করে।"
    },
    {
        "id": 89,
        "topic": "SQL & Relational Database Systems",
        "question": "ডেটাবেজে নির্দিষ্ট কোনো ঘটনা (যেমন INSERT, UPDATE, DELETE) ঘটলে স্বয়ংক্রিয়ভাবে কার্যকর হওয়া স্পেশাল প্রসিডিউরকে কী বলে?",
        "options": [
            "ক) Stored Procedure",
            "খ) Database Trigger",
            "গ) Cursor",
            "ঘ) Index"
        ],
        "answer": "খ",
        "explanation": "Trigger হলো ডেটাবেজের সাথে যুক্ত একটি প্রোগ্রাম যা কোনো নির্দিষ্ট DML বা DDL ইভেন্ট ঘটার পূর্বে (BEFORE) বা পরে (AFTER) স্বয়ংক্রিয়ভাবে সক্রিয় (Fire) হয়।"
    },
    {
        "id": 90,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ প্যারেন্ট টেবিলের কোনো রো ডিলিট হলে চাইল্ড টেবিলের সংশ্লিষ্ট রেফারেন্সিং রো-গুলো স্বয়ংক্রিয়ভাবে মুছে যাওয়ার ক্লজ কোনটি?",
        "options": [
            "ক) ON DELETE SET NULL",
            "খ) ON DELETE CASCADE",
            "গ) ON DELETE RESTRICT",
            "ঘ) ON DELETE NO ACTION"
        ],
        "answer": "খ",
        "explanation": "Foreign Key সংজ্ঞায় ON DELETE CASCADE ব্যবহার করলে প্যারেন্ট রেকর্ড ডিলিট হলে রেফারেন্স করা সমস্ত চাইল্ড রেকর্ড স্বয়ংক্রিয়ভাবে মুছে যায়।"
    },
    {
        "id": 91,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ Three-Valued Logic-এ NULL-এর সাথে কোনো তুলনার ফলাফল কী হয়?",
        "options": [
            "ক) TRUE",
            "খ) FALSE",
            "গ) UNKNOWN",
            "ঘ) ERROR"
        ],
        "answer": "গ",
        "explanation": "SQL-এ বুলিয়ান লজিক তিনটি মান গ্রহণ করে: TRUE, FALSE এবং UNKNOWN। NULL-এর সাথে কোনো তুলনা ($=, <, >$) করলে ফলাফল UNKNOWN হয়।"
    },
    {
        "id": 92,
        "topic": "SQL & Relational Database Systems",
        "question": "কোনো কলামের মান NULL কিনা তা পরীক্ষা করার সঠিক SQL সিনট্যাক্স কোনটি?",
        "options": [
            "ক) WHERE salary = NULL",
            "খ) WHERE salary IS NULL",
            "গ) WHERE salary == NULL",
            "ঘ) WHERE salary EQUALS NULL"
        ],
        "answer": "খ",
        "explanation": "NULL কোনো বাস্তব মান নয় বরং মানের অনুপস্থিতি। তাই `= NULL` কাজ করে না, `IS NULL` বা `IS NOT NULL` ব্যবহার করতে হয়।"
    },
    {
        "id": 93,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ UNION এবং UNION ALL-এর মধ্যে পার্থক্য কী?",
        "options": [
            "ক) UNION ডুপ্লিকেট সারি স্বয়ংক্রিয়ভাবে বাদ দেয়, কিন্তু UNION ALL সকল ডুপ্লিকেট সারি রেখে দেয়",
            "খ) UNION ALL দ্রুত কাজ করতে পারে না",
            "গ) UNION শুধুমাত্র একটি টেবিলে চলে",
            "ঘ) এদের মধ্যে কোনো পার্থক্য নেই"
        ],
        "answer": "ক",
        "explanation": "UNION দুটি কুয়েরির ফলাফল একত্রিত করে ডুপ্লিকেট বাদ দেয় (যার জন্য সর্টিং প্রয়োজন হয়), আর UNION ALL কোনো ডুপ্লিকেট ফিল্টার ছাড়াই সরাসরি যুক্ত করে এবং অনেক দ্রুত।"
    },
    {
        "id": 94,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ কলামের মান একটি নির্দিষ্ট সীমার ভেতরে আছে কিনা তা পরীক্ষা করতে কোন অপারেটর ব্যবহৃত হয়?",
        "options": [
            "ক) IN",
            "খ) BETWEEN ... AND ...",
            "গ) RANGE",
            "ঘ) LIMIT"
        ],
        "answer": "খ",
        "explanation": "BETWEEN min_val AND max_val অপারেটর মান অন্তর্ভুক্তমূলকভাবে (inclusive) নির্দিষ্ট রেঞ্জে আছে কিনা পরীক্ষা করে।"
    },
    {
        "id": 95,
        "topic": "SQL & Relational Database Systems",
        "question": "নিচের কোন SQL জয়েনটি দুটি টেবিলের কার্টেশিয়ান গুণন (Cartesian Product) ফিরিয়ে দেয়?",
        "options": [
            "ক) INNER JOIN",
            "খ) CROSS JOIN",
            "গ) LEFT JOIN",
            "ঘ) FULL OUTER JOIN"
        ],
        "answer": "খ",
        "explanation": "CROSS JOIN দুটি টেবিলের প্রতিটি সারির সাথে প্রতিটি সারির সংযোগ ঘটিয়ে কার্টেশিয়ান গুণফল প্রদান করে।"
    },
    {
        "id": 96,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ 'Self Join' বলতে কী বোঝায়?",
        "options": [
            "ক) ডেটাবেজ নিজে থেকে যে জয়েন করে",
            "খ) একটি টেবিল যখন নিজের সাথেই Join অপারেশনে অংশ নেয়",
            "গ) প্রাইমারি কি ছাড়া জয়েন",
            "ঘ) দুটি অভিন্ন নামের টেবিলের জয়েন"
        ],
        "answer": "খ",
        "explanation": "যখন একই টেবিল ভিন্ন ভিন্ন অ্যালিয়াস (Alias) ব্যবহার করে নিজের সাথে জয়েন করা হয় (যেমন কর্মচারী ও ম্যানেজারের সম্পর্ক বের করতে), তখন তাকে Self Join বলে।"
    },
    {
        "id": 97,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ সংরক্ষিত কোড ব্লক যা ইনপুট প্যারামিটার নিয়ে কাজ করতে পারে এবং বারবার কল করা যায় তাকে কী বলে?",
        "options": [
            "ক) Stored Procedure",
            "খ) View",
            "গ) Index",
            "ঘ) Schema"
        ],
        "answer": "ক",
        "explanation": "Stored Procedure হলো ডেটাবেজে সংকলিত ও সংরক্ষিত এক বা একাধিক SQL স্টেটমেন্টের গ্রুপ যা প্যারামিটার গ্রহণ করতে পারে এবং অ্যাপ্লিকেশন থেকে সহজেই এক্সিকিউট করা যায়।"
    },
    {
        "id": 98,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL ইনজেকশন (SQL Injection) আক্রমণ প্রতিহত করার সর্বোত্তম উপায় কোনটি?",
        "options": [
            "ক) ডাইনামিক স্ট্রিং কনক্যাটেনেশন ব্যবহার করা",
            "খ) প্যারামিটারাইজড কুয়েরি বা প্রিপেয়ার্ড স্টেটমেন্ট (Prepared Statements) ব্যবহার করা",
            "গ) ডেটাবেজ পাসওয়ার্ড ছোট রাখা",
            "ঘ) পোর্টেবল ডেটাবেজ ব্যবহার করা"
        ],
        "answer": "খ",
        "explanation": "Prepared Statement বা Parameterized Query ডেটা এবং কোডকে আলাদা রাখে, ফলে ব্যবহারকারীর ক্ষতিকর ইনপুট এক্সিকিউটেবল কোড হিসেবে রান করতে পারে না।"
    },
    {
        "id": 99,
        "topic": "SQL & Relational Database Systems",
        "question": "একটি SQL কুয়েরির ফলাফল থেকে শীর্ষ ৫টি রো দেখার জন্য স্ট্যান্ডার্ড ক্লজ কোনটি?",
        "options": [
            "ক) TOP 5 অথবা LIMIT 5",
            "খ) MAX 5",
            "গ) FIRST 5",
            "ঘ) STOP 5"
        ],
        "answer": "ক",
        "explanation": "MySQL/PostgreSQL-এ `LIMIT 5` এবং SQL Server-এ `SELECT TOP 5` ব্যবহার করে নির্দিষ্ট সংখ্যক সারি আনা হয়।"
    },
    {
        "id": 100,
        "topic": "SQL & Relational Database Systems",
        "question": "SQL-এ ডেটাবেজের কোনো কলামের উপর বিশেষ শর্ত (যেমন age >= 18) আরোপ করতে কোন কনস্ট্রেইন্ট ব্যবহৃত হয়?",
        "options": [
            "ক) DEFAULT",
            "খ) CHECK",
            "গ) UNIQUE",
            "ঘ) FOREIGN KEY"
        ],
        "answer": "খ",
        "explanation": "CHECK কনস্ট্রেইন্ট কোনো কলামে প্রবেশের সময় নির্দিষ্ট লজিক্যাল এক্সপ্রেশন বা শর্ত পূরণ নিশ্চিত করে।"
    }
]

out_dir = "NTRCA 452 - AI"
os.makedirs(out_dir, exist_ok=True)
filename = os.path.join(out_dir, "অধ্যায়- ৬. Database Management System.json")

with open(filename, "w", encoding="utf-8") as f:
    json.dump(questions_part1, f, ensure_ascii=False, indent=2)

print(f"Saved Part 1 with {len(questions_part1)} questions successfully.")
