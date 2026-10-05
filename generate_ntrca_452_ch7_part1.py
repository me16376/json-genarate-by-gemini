# -*- coding: utf-8 -*-
import json
import os

questions_part1 = [
    # Subtopic 1: Internet, Network Edge, Core & Protocol Layers (1-25)
    {
        "id": 1,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "কম্পিউটার নেটওয়ার্কে এন্ড সিস্টেম (End Systems) বা হোস্ট (Hosts) কোনগুলো?",
        "options": [
            "ক) রাউটার ও সুইচ",
            "খ) কম্পিউটার, স্মার্টফোন, সার্ভার ও আইওটি ডিভাইস",
            "গ) ফাইবার অপটিক ক্যাবল ও রিপিটার",
            "ঘ) কেবল ডিএনএস সার্ভার"
        ],
        "answer": "খ",
        "explanation": "নেটওয়ার্কের প্রান্তে (Network Edge) সংযুক্ত যেসকল ডিভাইসে ব্যবহারকারীর অ্যাপ্লিকেশন সফটওয়্যার রান করে (যেমন পিসি, সার্ভার, মোবাইল) সেগুলোকে End Systems বা Hosts বলা হয়।"
    },
    {
        "id": 2,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "প্যাকেট সুইচিং (Packet Switching) এবং সার্কিট সুইচিং (Circuit Switching)-এর মধ্যে মূল পার্থক্য কোনটি?",
        "options": [
            "ক) সার্কিট সুইচিংয়ে যোগাযোগের পূর্বে একটি ডেডিকেটেড ফিজিক্যাল পাথ বা ব্যান্ডউইথ রিজার্ভ করা হয়, আর প্যাকেট সুইচিংয়ে কোনো ডেডিকেটেড পাথ ছাড়াই প্যাকেটগুলো স্বাধীনভাবে রাউট হয়",
            "খ) প্যাকেট সুইচিং শুধুমাত্র অ্যানালগ সিগন্যালে চলে",
            "গ) সার্কিট সুইচিংয়ে কোনো সংযোগ স্থাপন করতে হয় না",
            "ঘ) ইন্টারনেট সার্কিট সুইচিং ব্যবহার করে"
        ],
        "answer": "ক",
        "explanation": "ঐতিহ্যবাহী টেলিফোন নেটওয়ার্কে Circuit Switching ব্যবহৃত হতো যেখানে সম্পূর্ণ চ্যানেল সংরক্ষিত থাকে। বিপরীতে ইন্টারনেট Packet Switching (Store-and-Forward) ব্যবহার করে ব্যান্ডউইথের সর্বোচ্চ সদ্ব্যবহার করে।"
    },
    {
        "id": 3,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "একটি প্যাকেটের দৈর্ঘ্য $L$ বিট এবং লিঙ্কের ট্রান্সমিশন রেট $R$ bps হলে ট্রান্সমিশন ডিলে (Transmission Delay) কত?",
        "options": [
            "ক) $L \\times R$",
            "খ) $L / R$",
            "গ) $R / L$",
            "ঘ) $d / s$"
        ],
        "answer": "খ",
        "explanation": "ট্রান্সমিশন ডিলে হলো প্যাকেটের সমস্ত বিট লিঙ্কে পুশ করতে প্রয়োজনীয় সময়, যার সূত্র $d_{trans} = L / R$।"
    },
    {
        "id": 4,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "দুটি রাউটারের মধ্যবর্তী দূরত্ব $d$ এবং সিগন্যালের গতি $s$ (প্রায় $2 \\times 10^8$ m/s) হলে প্রোপাগেশন ডিলে (Propagation Delay) কত?",
        "options": [
            "ক) $L / R$",
            "খ) $d / s$",
            "গ) $d \\times s$",
            "ঘ) $s / d$"
        ],
        "answer": "খ",
        "explanation": "প্রোপাগেশন ডিলে হলো ফিজিক্যাল মাধ্যমে একটি বিটের এক প্রান্ত থেকে অন্য প্রান্তে পৌঁছানোর সময়, যার সূত্র $d_{prop} = d / s$।"
    },
    {
        "id": 5,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "রাউটারের বাফারে যখন প্যাকেটের আগমন হার ট্রান্সমিশন হারের চেয়ে বেশি হয়, তখন কোন বিলম্ব বা ক্ষতি ঘটে?",
        "options": [
            "ক) কিউয়িং ডিলে (Queuing Delay) এবং প্যাকেট লস (Packet Loss / Drop)",
            "খ) প্রোপাগেশন ডিলে বৃদ্ধি পায়",
            "গ) আলোর গতি কমে যায়",
            "ঘ) রাউটারের হার্ডওয়্যার পুড়ে যায়"
        ],
        "answer": "ক",
        "explanation": "বাফার ভরে গেলে প্যাকেটকে কিউতে অপেক্ষা করতে হয় (Queuing delay) এবং বাফার উপচে পড়লে নতুন প্যাকেট ড্রপ হয় যা Packet Loss হিসেবে পরিচিত।"
    },
    {
        "id": 6,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "নোডাল প্রসেসিং ডিলে (Processing Delay) মূলত কীসের সাথে জড়িত?",
        "options": [
            "ক) তারের মধ্য দিয়ে বিট চলাচলের সময়",
            "খ) প্যাকেটের হেডার পরীক্ষা করা, বিট এরর চেক করা এবং আউটপুট লিঙ্ক নির্ধারণের সময়",
            "গ) ডিস্কে ফাইল সেভ করার সময়",
            "ঘ) ব্রাউজার রেন্ডারিং সময়"
        ],
        "answer": "খ",
        "explanation": "Processing delay হলো রাউটারের প্রসেসর কর্তৃক প্যাকেটের হেডার পড়া, চেকসাম ভেরিফাই করা এবং রাউটিং টেবিল দেখে পরবর্তী লিঙ্ক বাছাইয়ের সময়।"
    },
    {
        "id": 7,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "OSI মডেলের ৭টি লেয়ারের নিচের দিক থেকে উপরের দিকের সঠিক ক্রম কোনটি?",
        "options": [
            "ক) Physical -> Data Link -> Network -> Transport -> Session -> Presentation -> Application",
            "খ) Application -> Presentation -> Session -> Transport -> Network -> Data Link -> Physical",
            "গ) Physical -> Network -> Data Link -> Transport -> Session -> Presentation -> Application",
            "ঘ) Data Link -> Physical -> Transport -> Network -> Application -> Session -> Presentation"
        ],
        "answer": "ক",
        "explanation": "OSI (Open Systems Interconnection) মডেলের স্তরগুলো হলো: ১. Physical, ২. Data Link, ৩. Network, ৪. Transport, ৫. Session, ৬. Presentation, এবং ৭. Application।"
    },
    {
        "id": 8,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "TCP/IP প্রোটোকল স্যুটের ৫-স্তর বিশিষ্ট আর্কিটেকচারে কোন স্তর দুটিকে অ্যাপ্লিকেশন লেয়ারের মধ্যে একীভূত করা হয়েছে?",
        "options": [
            "ক) Session এবং Presentation লেয়ার",
            "খ) Data Link এবং Network লেয়ার",
            "গ) Transport এবং Network লেয়ার",
            "ঘ) Physical এবং Data Link লেয়ার"
        ],
        "answer": "ক",
        "explanation": "TCP/IP মডেলে OSI-এর Session এবং Presentation লেয়ারের কার্যকারিতা সরাসরি Application লেয়ারের ভেতরেই সম্পাদন করা হয়।"
    },
    {
        "id": 9,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "বিভিন্ন স্তরে প্রোটোকল ডেটা ইউনিটের (PDU) সঠিক মিল কোনটি?",
        "options": [
            "ক) Application: Message, Transport: Segment, Network: Datagram/Packet, Data Link: Frame, Physical: Bits",
            "খ) Transport: Packet, Network: Segment",
            "গ) Data Link: Packet, Network: Frame",
            "ঘ) Application: Frame, Data Link: Bits"
        ],
        "answer": "ক",
        "explanation": "লেয়ার অনুযায়ী PDU-এর নাম: Application-এ Message, Transport-এ Segment, Network-এ Datagram/Packet, Data Link-এ Frame এবং Physical-এ Bits।"
    },
    {
        "id": 10,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "প্রেরক প্রান্তে উচ্চ স্তর থেকে নিম্ন স্তরে নামার সময় প্রতিটি স্তরে হেডার যুক্ত হওয়ার প্রক্রিয়াকে কী বলে?",
        "options": [
            "ক) Decapsulation",
            "খ) Encapsulation (এনক্যাপসুলেশন)",
            "গ) Segmentation",
            "ঘ) Multiplexing"
        ],
        "answer": "খ",
        "explanation": "Encapsulation হলো এমন এক প্রক্রিয়া যাতে প্রতিটি প্রোটোকল লেয়ার উচ্চতর লেয়ার থেকে পাওয়া ডেটার সাথে নিজস্ব কন্ট্রোল হেডার যোগ করে নিচের স্তরে পাঠায়।"
    },
    {
        "id": 11,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "গ্রাহক প্রান্তে ফিজিক্যাল লেয়ার থেকে ডেটা উপরে ওঠার সময় হেডার খুলে ফেলার প্রক্রিয়াকে কী বলে?",
        "options": [
            "ক) Encapsulation",
            "খ) Decapsulation (ডিক্যাপসুলেশন)",
            "গ) Buffering",
            "ঘ) Routing"
        ],
        "answer": "খ",
        "explanation": "Decapsulation হলো প্রতিটি স্তরে সংশ্লিষ্ট হেডারটি পরীক্ষা ও অপসরণ করে মূল পে-লোডটি উপরের স্তরে হস্তান্তর করার প্রক্রিয়া।"
    },
    {
        "id": 12,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "হোম ব্রডব্যান্ডে ব্যবহৃত DSL (Digital Subscriber Line) প্রযুক্তিতে ডেটা স্থানান্তরের মাধ্যম কোনটি?",
        "options": [
            "ক) প্রচলিত কপার টেলিফোন লাইন (Twisted-pair telephone wire)",
            "খ) কো-অ্যাক্সিয়াল ক্যাবল টিভি তার",
            "গ) স্যাটেলাইট লিঙ্ক",
            "ঘ) পাওয়ার গ্রিড"
        ],
        "answer": "ক",
        "explanation": "DSL বিদ্যমান টেলিফোন লাইনের উচ্চ ফ্রিকোয়েন্সি স্পেকট্রাম ব্যবহার করে ভয়েস ও ডেটা সিগন্যাল একই সাথে প্রেরণ করে।"
    },
    {
        "id": 13,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "HFC (Hybrid Fiber-Coaxial) ক্যাবল ইন্টারনেট অ্যাক্সেস কোন ধরণের মিডিয়া ব্যবহার করে?",
        "options": [
            "ক) ক্যাবল হেডএন্ড পর্যন্ত ফাইবার অপটিক এবং গ্রাহকের বাড়ি পর্যন্ত কো-অ্যাক্সিয়াল ক্যাবল",
            "খ) শুধুমাত্র টুইস্টেড পেয়ার তার",
            "গ) ইনফ্রারেড রশ্মি",
            "ঘ) মাইক্রোওয়েভ লিঙ্ক"
        ],
        "answer": "ক",
        "explanation": "ক্যাবল নেটওয়ার্কে ফাইবার ব্যাকবোন এবং বাড়িগুলোর সংযোগে কো-অ্যাক্সিয়াল ক্যাবল সমন্বিত থাকায় একে Hybrid Fiber-Coaxial (HFC) বলে।"
    },
    {
        "id": 14,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "সার্কিট সুইচিং নেটওয়ার্কে মাল্টিপ্লেক্সিংয়ের দুটি বহুল ব্যবহৃত কৌশল কী কী?",
        "options": [
            "ক) FDM (Frequency-Division Multiplexing) এবং TDM (Time-Division Multiplexing)",
            "খ) TCP এবং UDP",
            "গ) HTTP এবং DNS",
            "ঘ) CSMA/CD এবং CSMA/CA"
        ],
        "answer": "ক",
        "explanation": "সার্কিট সুইচিংয়ে চ্যানেল শেয়ার করতে ফ্রিকোয়েন্সি ভাগ করা (FDM) অথবা সময়কে টাইম-স্লটে ভাগ করা (TDM) ব্যবহৃত হয়।"
    },
    {
        "id": 15,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "নেটওয়ার্ক বটলনেক লিঙ্ক (Bottleneck Link) বলতে কী বোঝায়?",
        "options": [
            "ক) এন্ড-টু-এন্ড পাথের যে লিঙ্কের ট্রান্সমিশন থ্রুপুট সর্বনিম্ন",
            "খ) সবচেয়ে দীর্ঘ ক্যাবল লিঙ্ক",
            "গ) সবচেয়ে দামি রাউটার",
            "ঘ) ওয়্যারলেস অ্যান্টেনা"
        ],
        "answer": "ক",
        "explanation": "একটি নেটওয়ার্ক সংযোগের সামগ্রিক থ্রুপুট নির্ধারিত হয় পাথের সর্বনিম্ন ক্যাপাসিটির লিঙ্ক দ্বারা, যাকে Bottleneck Link বলে।"
    },
    {
        "id": 16,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "ফিজিক্যাল লেয়ারের প্রধান দায়িত্ব কোনটি?",
        "options": [
            "ক) র বিট স্ট্রিমকে (0 এবং 1) ফিজিক্যাল মাধ্যমে ইলেকট্রিক্যাল, অপটিক্যাল বা রেডিও সিগন্যালে রূপান্তর ও স্থানান্তর",
            "খ) আইপি অ্যাড্রেসিং নির্ধারণ",
            "গ) প্রসেস-টু-প্রসেস সংযোগ স্থাপন",
            "ঘ) এইচটিটিপি মেমোরি ক্যাশ রাখা"
        ],
        "answer": "ক",
        "explanation": "Physical Layer ফিজিক্যাল মিডিয়া (ক্যাবল/এয়ার)-র মধ্য দিয়ে বৈদ্যুতিক ভোল্টেজ বা আলোর স্পন্দন আকারে বিট পাঠানো ও গ্রহণ করার জন্য দায়ী।"
    },
    {
        "id": 17,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "ডাটা লিঙ্ক লেয়ারের প্রধান কাজগুলোর মধ্যে কোনটি অন্তর্ভুক্ত?",
        "options": [
            "ক) একই লিঙ্কে নোড-টু-নোড বা হপ-টু-হপ ফ্রেম ডেলিভারি, ফ্রেমিং, ম্যাক অ্যাড্রেসিং এবং এরর ডিটেকশন (CRC)",
            "খ) গ্লোবাল রাউটিং অ্যালগরিদম চালানো",
            "গ) ইউজার ইন্টারফেস ডিজাইন",
            "ঘ) ডোমেইন নেম রেজোলিউশন"
        ],
        "answer": "ক",
        "explanation": "Data Link Layer সংলগ্ন দুটি নোডের মধ্যে নির্ভরযোগ্য ডেটা ফ্রেম বিনিময়, মিডিয়া অ্যাক্সেস কন্ট্রোল (MAC) এবং লিঙ্ক-লেভেল ত্রুটি শনাক্ত করে।"
    },
    {
        "id": 18,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "নেটওয়ার্ক লেয়ারের মূল কাজ কোনটি?",
        "options": [
            "ক) হোস্ট-টু-হোস্ট ডেলিভারি, লজিক্যাল অ্যাড্রেসিং (IP Addressing) এবং রাউটিং",
            "খ) প্রসেস-টু-প্রসেস ডেটা ট্রান্সফার",
            "গ) টেক্সট কম্প্রেশন",
            "ঘ) অ্যাপ্লিকেশন রেন্ডারিং"
        ],
        "answer": "ক",
        "explanation": "Network Layer সোর্স হোস্ট থেকে ডেস্টিনেশন হোস্টে প্যাকেট পৌঁছে দেওয়ার জন্য লজিক্যাল আইপি অ্যাড্রেসিং এবং রাউটিং রুট নির্বাচন পরিচালনা করে।"
    },
    {
        "id": 19,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "ট্রান্সপোর্ট লেয়ারের মূল লক্ষ্য কোনটি?",
        "options": [
            "ক) এক হোস্টের নির্দিষ্ট অ্যাপ প্রসেসের সাথে অন্য হোস্টের অ্যাপ প্রসেসের যোগাযোগ (Process-to-Process Delivery)",
            "খ) ফিজিক্যাল ক্যাবল সংযোগ",
            "গ) রাউটারের বাফার মেমরি ক্লিন করা",
            "ঘ) ম্যাক অ্যাড্রেস নির্ধারণ"
        ],
        "answer": "ক",
        "explanation": "Transport Layer হোস্টের নির্দিষ্ট অ্যাপ্লিকেশন প্রসেসগুলোর মধ্যে এন্ড-টু-এন্ড যোগাযোগ, পোর্ট অ্যাড্রেসিং, মাল্টিপ্লেক্সিং ও নির্ভরযোগ্যতা নিশ্চিত করে।"
    },
    {
        "id": 20,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "OSI মডেলের প্রেজেন্টেশন লেয়ারের (Presentation Layer) প্রধান কাজ কোনটি?",
        "options": [
            "ক) ডেটা ট্রান্সলেশন, ক্যারেক্টার এনকোডিং (ASCII/Unicode), ডেটা এনক্রিপশন ও কম্প্রেশন",
            "খ) প্যাকেট রাউটিং",
            "গ) বিট সিনক্রোনাইজেশন",
            "ঘ) ফিজিক্যাল টপোলজি তৈরি"
        ],
        "answer": "ক",
        "explanation": "Presentation Layer ডেটার বিন্যাস ও সিনট্যাক্স হ্যান্ডেল করে; যার মধ্যে ডেটা রূপান্তর, এনক্রিপশন/ডিক্রিপশন এবং কম্প্রেশন অন্তর্ভুক্ত।"
    },
    {
        "id": 21,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "OSI সেশন লেয়ারের (Session Layer) প্রধান কাজ কী?",
        "options": [
            "ক) দুটি ডিভাইসের মধ্যে ডায়ালগ কন্ট্রোল, সেশন প্রতিষ্ঠা, রক্ষণাবেক্ষণ ও সিনক্রোনাইজেশন চেকপয়েন্ট স্থাপন",
            "খ) প্যাকেট ড্রপ রোধ",
            "গ) আইপি সাবনেটিং",
            "ঘ) সিআরসি চেক"
        ],
        "answer": "ক",
        "explanation": "Session Layer যোগাযোগকারী অ্যাপ্লিকেশনের মধ্যে ডায়ালগ শুরু, শেষ এবং কোনো ত্রুটি হলে পূর্বের চেকপয়েন্ট থেকে রিকভারি পরিচালনা করে।"
    },
    {
        "id": 22,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "ইন্টারনেটের মূল চালিকাশক্তি 'Best-effort delivery' সার্ভিস মডেল কোন লেয়ারের অন্তর্গত?",
        "options": [
            "ক) Network Layer (IP Protocol)",
            "খ) Application Layer",
            "গ) Session Layer",
            "ঘ) Presentation Layer"
        ],
        "answer": "ক",
        "explanation": "ইন্টারনেট প্রোটোকল (IP) একটি Best-effort সার্ভিস, যার অর্থ এটি প্যাকেট পৌঁছানোর শতভাগ গ্যারান্টি, সঠিক অর্ডার বা বিলম্বহীনতার নিশ্চয়তা দেয় না।"
    },
    {
        "id": 23,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "Layer-2 ডিভাইস এবং Layer-3 ডিভাইসের যথোপযুক্ত উদাহরণ কোনটি?",
        "options": [
            "ক) Layer-2: ইথারনেট সুইচ (Switch), Layer-3: রাউটার (Router)",
            "খ) Layer-2: হাব, Layer-3: ক্যাবল",
            "গ) Layer-2: রাউটার, Layer-3: সুইচ",
            "ঘ) Layer-2: রিপিটার, Layer-3: হাব"
        ],
        "answer": "ক",
        "explanation": "সাধারণ সুইচ ম্যাক অ্যাড্রেসের ভিত্তিতে লেয়ার-২ (Data Link)-এ কাজ করে, আর রাউটার আইপি অ্যাড্রেস দেখে লেয়ার-৩ (Network)-এ কাজ করে।"
    },
    {
        "id": 24,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "কম্পিউটার নেটওয়ার্কে 'থ্রুপুট' (Throughput) বলতে কী বোঝায়?",
        "options": [
            "ক) প্রতি একক সময়ে গ্রাহক প্রান্তে সফলভাবে পৌঁছানো বাস্তব ডেটা বিটের হার (Rate)",
            "খ) ক্যাবলের মোট দৈর্ঘ্য",
            "গ) রাউটারের মেমরি ধারণক্ষমতা",
            "ঘ) আইপি অ্যাড্রেসের সংখ্যা"
        ],
        "answer": "ক",
        "explanation": "Throughput হলো কোনো নির্দিষ্ট সময়ে নেটওয়ার্কের এক প্রান্ত থেকে অন্য প্রান্তে সফলভাবে স্থানান্তরিত তথ্যের কার্যকরী হার (সাধারণত bps বা Mbps এককে)।"
    },
    {
        "id": 25,
        "topic": "Network Edge, Core & Protocol Layers",
        "question": "একটি কম্পিউটার নেটওয়ার্কে ডস বা ডিডস (DoS/DDoS) আক্রমণের মূল উদ্দেশ্য কী?",
        "options": [
            "ক) অতিরিক্ত কৃত্রিম ট্রাফিক পাঠিয়ে সার্ভার বা নেটওয়ার্ক রিসোর্সকে ক্র্যাশ করিয়ে বৈধ গ্রাহকদের সেবা থেকে বঞ্চিত করা",
            "খ) ইউজারের পাসওয়ার্ড চুরি করা",
            "গ) হার্ডডিস্ক চুরি করা",
            "ঘ) ক্যাবল কেটে ফেলা"
        ],
        "answer": "ক",
        "explanation": "Denial of Service (DoS/DDoS) আক্রমণে বটনেট ব্যবহার করে টার্গেট সিস্টেমে প্লাডিং ঘটিয়ে সার্ভারকে আনরেসপনসিভ বা ওভারলোড করে দেওয়া হয়।"
    },

    # Subtopic 2: Application Layer (HTTP, FTP, SMTP, DNS, P2P) (26-55)
    {
        "id": 26,
        "topic": "Application Layer Protocols",
        "question": "ক্লায়েন্ট-সার্ভার (Client-Server) আর্কিটেকচার এবং পিয়ার-টু-পিয়ার (P2P) আর্কিটেকচারের প্রধান পার্থক্য কোনটি?",
        "options": [
            "ক) ক্লায়েন্ট-সার্ভারে সর্বদা সক্রিয় একটি কেন্দ্রীয় সার্ভার থাকে, আর P2P-তে যেকোনো পিয়ার ডিভাইস একই সাথে ক্লায়েন্ট ও সার্ভার উভয় হিসেবে কাজ করে",
            "খ) P2P-তে কোনো ইন্টারনেট লাগে না",
            "গ) ক্লায়েন্ট-সার্ভারে কোনো ডেটাবেজ থাকে না",
            "ঘ) উভয়েই সম্পূর্ণ অভিন্ন"
        ],
        "answer": "ক",
        "explanation": "P2P আর্কিটেকচারে (যেমন BitTorrent) প্রতিটি নোড (Peer) সরাসরি একে অপরের সাথে ডেটা শেয়ার করে, ফলে এটি স্বয়ংক্রিয়ভাবে অত্যন্ত স্কেলেবল (Self-scalability)।"
    },
    {
        "id": 27,
        "topic": "Application Layer Protocols",
        "question": "নেটওয়ার্ক অ্যাপ্লিকেশনে 'সকেট' (Socket) বলতে কী বোঝায়?",
        "options": [
            "ক) অ্যাপ্লিকেশন লেয়ার এবং ট্রান্সপোর্ট লেয়ারের মধ্যবর্তী সফটওয়্যার ইন্টারফেস বা ডোরওয়ে (Doorway)",
            "খ) মাদারবোর্ডের প্রসেসর বসানোর স্লট",
            "গ) ক্যাবলের আরজে-৪৫ কানেক্টর",
            "ঘ) ব্রাউজারের বুকমার্ক"
        ],
        "answer": "ক",
        "explanation": "সকেট হলো অ্যাপ্লিকেশন প্রসেস এবং আন্ডারলাইং নেটওয়ার্কের মধ্যে প্রোগ্রাম্যাটিক ইন্টারফেস যার মাধ্যমে প্রসেস নেটওয়ার্কে ডেটা পাঠায় ও গ্রহণ করে।"
    },
    {
        "id": 28,
        "topic": "Application Layer Protocols",
        "question": "HTTP প্রোটোকলকে 'Stateless Protocol' বলা হয় কেন?",
        "options": [
            "ক) সার্ভার অতীতের ক্লায়েন্ট রিকোয়েস্ট সম্পর্কে কোনো স্টেট বা তথ্য স্মৃতিতে সংরক্ষণ করে রাখে না",
            "খ) এটি কোনো সিকিউরিটি দেয় না",
            "গ) এটি ক্যাশে কাজ করে না",
            "ঘ) এতে কোনো ছবি দেখা যায় না"
        ],
        "answer": "ক",
        "explanation": "HTTP প্রতিটি রিকোয়েস্টকে সম্পূর্ণ স্বাধীন ও নতুন হিসেবে বিবেচনা করে এবং আগের কোনো ট্রানজ্যাকশন মনে রাখে না। এজন্যই ক্লায়েন্ট সেশন ধরে রাখতে Cookies ব্যবহৃত হয়।"
    },
    {
        "id": 29,
        "topic": "Application Layer Protocols",
        "question": "Non-persistent HTTP এবং Persistent HTTP-র মধ্যে প্রধান পার্থক্য কোনটি?",
        "options": [
            "ক) Non-persistent-এ প্রতি অবজেক্টের জন্য নতুন TCP কানেকশন খোলা ও বন্ধ হয়, Persistent-এ একটি একক TCP কানেকশনেই একাধিক ওয়েব অবজেক্ট পাঠানো যায়",
            "খ) Non-persistent অনেক দ্রুত",
            "গ) Persistent-এ UDP ব্যবহৃত হয়",
            "ঘ) এদের মধ্যে কোনো পার্থক্য নেই"
        ],
        "answer": "ক",
        "explanation": "HTTP/1.0 ছিল Non-persistent (প্রতি অবজেক্টে 2 RTT ওভারহেড)। HTTP/1.1 এ Persistent Connection ডিফল্ট করা হয় যাতে একই সকেটে পাইপলাইনিংয়ের সুবিধা পাওয়া যায়।"
    },
    {
        "id": 30,
        "topic": "Application Layer Protocols",
        "question": "একটি ছোট প্যাকেট ক্লায়েন্ট থেকে সার্ভারে গিয়ে ফিরে আসতে যে সময় নেয় তাকে কী বলা হয়?",
        "options": [
            "ক) RTT (Round Trip Time)",
            "খ) MTU (Maximum Transmission Unit)",
            "গ) TTL (Time To Live)",
            "ঘ) MSS (Maximum Segment Size)"
        ],
        "answer": "ক",
        "explanation": "Round-Trip Time (RTT) হলো ডেটার একপ্রান্ত থেকে অন্যপ্রান্তে পৌঁছানো এবং তার স্বীকৃতি (ACK) ফিরে আসার মোট সময়।"
    },
    {
        "id": 31,
        "topic": "Application Layer Protocols",
        "question": "HTTP স্ট্যাটাস কোড '200 OK' এবং '404 Not Found'-এর অর্থ কী?",
        "options": [
            "ক) 200: অনুরোধ সফল হয়েছে, 404: কাঙ্ক্ষিত রিসোর্স সার্ভারে পাওয়া যায়নি",
            "খ) 200: পেজ ডিলিট হয়েছে, 404: সফল",
            "গ) 200: সার্ভার ক্র্যাশ, 404: রিডাইরেক্ট",
            "ঘ) উভয়ই এরর কোড"
        ],
        "answer": "ক",
        "explanation": "HTTP স্ট্যাটাস কোডে 2xx মানে সাফল্য (Success) এবং 4xx মানে ক্লায়েন্ট এরর (Client Error)।"
    },
    {
        "id": 32,
        "topic": "Application Layer Protocols",
        "question": "HTTP স্ট্যাটাস কোড 301, 400 এবং 500 যথাক্রমে কী নির্দেশ করে?",
        "options": [
            "ক) 301: Moved Permanently, 400: Bad Request, 500: Internal Server Error",
            "খ) 301: OK, 400: Gateway Timeout, 500: Unauthorized",
            "গ) 301: Forbidden, 400: Created, 500: OK",
            "ঘ) 301: Found, 400: Server Busy, 500: Success"
        ],
        "answer": "ক",
        "explanation": "3xx হলো রিডাইরেকশন (Moved Permanently), 400 হলো ক্লায়েন্টের অবৈধ সিনট্যাক্স (Bad Request), এবং 500 হলো সার্ভার সাইডের ক্র্যাশ বা এরর।"
    },
    {
        "id": 33,
        "topic": "Application Layer Protocols",
        "question": "ওয়েব ক্যাশিং (Web Caching বা Proxy Server) ব্যবহারের প্রধান সুবিধা কোনটি?",
        "options": [
            "ক) ক্লায়েন্টের রেসপন্স টাইম নাটকীয়ভাবে কমে এবং প্রতিষ্ঠানের অ্যাক্সেস লিঙ্কের ট্রাফিক হ্রাস পায়",
            "খ) ব্রাউজারের র‍্যাম বৃদ্ধি পায়",
            "গ) আইপি অ্যাড্রেস স্থায়ী হয়",
            "ঘ) কোনো ইন্টারনেটের প্রয়োজন হয় না"
        ],
        "answer": "ক",
        "explanation": "প্রক্সি ক্যাশ সার্ভার লোকাল নেটওয়ার্কে ঘন ঘন অনুরোধকৃত ওয়েব পেজ সেভ রাখে, ফলে বারবার দূরবর্তী অরিজিন সার্ভারে যেতে হয় না।"
    },
    {
        "id": 34,
        "topic": "Application Layer Protocols",
        "question": "ক্যাশ সার্ভারে থাকা অবজেক্ট অরিজিন সার্ভারের চেয়ে পুরোনো বা পরিবর্তিত হয়েছে কিনা তা যাচাই করতে কোন HTTP হেডার ব্যবহৃত হয়?",
        "options": [
            "ক) Conditional GET (If-Modified-Since)",
            "খ) User-Agent",
            "গ) Content-Type",
            "ঘ) Accept-Language"
        ],
        "answer": "ক",
        "explanation": "ক্যাশ সার্ভার `If-Modified-Since` হেডার দিয়ে অরিজিন সার্ভারে চেক করে। যদি পরিবর্তন না হয়, তবে সার্ভার '304 Not Modified' পাঠায়, যা নতুন করে বডি পাঠানো বন্ধ করে ব্যান্ডউইথ বাঁচায়।"
    },
    {
        "id": 35,
        "topic": "Application Layer Protocols",
        "question": "HTTP/2 প্রোটোকলের প্রধান উন্নতি কোনটি ছিল?",
        "options": [
            "ক) একই TCP কানেকশনে বাইনারি ফ্রেমিং এবং মাল্টিপ্লেক্সিং (Multiplexing) এর মাধ্যমে Head-of-Line Blocking দূর করা",
            "খ) UDP প্রোটোকলে রূপান্তর",
            "গ) টেক্সট ফরম্যাট বাধ্যতামূলক করা",
            "ঘ) কোনো সিকিউরিটি না রাখা"
        ],
        "answer": "ক",
        "explanation": "HTTP/2单一 TCP কানেকশনে একাধিক রিকোয়েস্ট ও রেসপন্স স্ট্রিমকে প্যারালালে ইন্টারলিভ করে আদান-প্রদান করতে পারে।"
    },
    {
        "id": 36,
        "topic": "Application Layer Protocols",
        "question": "HTTP/3 প্রোটোকল ট্রান্সপোর্ট লেয়ারে TCP-র বদলে কোন প্রোটোকল ব্যবহার করে?",
        "options": [
            "ক) QUIC (UDP ভিত্তিক)",
            "খ) ICMP",
            "গ) OSPF",
            "ঘ) IGMP"
        ],
        "answer": "ক",
        "explanation": "HTTP/3 গুগল উদ্ভাবিত QUIC প্রোটোকল ব্যবহার করে যা UDP-র উপর নির্মিত এবং TCP-র হ্যান্ডশেক ডিলে ও ট্রান্সপোর্ট লেভেলের HOL ব্লকিং দূর করে।"
    },
    {
        "id": 37,
        "topic": "Application Layer Protocols",
        "question": "FTP (File Transfer Protocol) একই সাথে দুটি প্যারালাল সংযোগ ব্যবহার করে। সেগুলো কী কী এবং তাদের ডিফল্ট পোর্ট কত?",
        "options": [
            "ক) কন্ট্রোল সংযোগ (Control: Port 21) এবং ডেটা সংযোগ (Data: Port 20)",
            "খ) রিড সংযোগ (Port 80) এবং রাইট সংযোগ (Port 443)",
            "গ) ফাইল পোর্ট 25 এবং কমান্ড পোর্ট 53",
            "ঘ) সিঙ্গেল পোর্ট 22"
        ],
        "answer": "ক",
        "explanation": "FTP 'Out-of-band' কন্ট্রোল ব্যবহার করে। কমান্ড আদান-প্রদানে পোর্ট ২১ এবং বাস্তব ফাইল ডেটা ট্রান্সফারে পোর্ট ২০ ব্যবহৃত হয়।"
    },
    {
        "id": 38,
        "topic": "Application Layer Protocols",
        "question": "ইলেকট্রনিক মেইল পাঠাতে ক্লায়েন্ট থেকে মেল সার্ভারে কোন প্রোটোকল ব্যবহৃত হয়?",
        "options": [
            "ক) SMTP (Simple Mail Transfer Protocol - Port 25)",
            "খ) POP3",
            "গ) IMAP",
            "ঘ) SNMP"
        ],
        "answer": "ক",
        "explanation": "SMTP হলো একটি পুশ প্রোটোকল যা মেইল পাঠানো বা সার্ভার টু সার্ভার মেইল ফরোয়ার্ডিংয়ে ব্যবহৃত হয় (ডিফল্ট পোর্ট ২৫/৫৮৭)।"
    },
    {
        "id": 39,
        "topic": "Application Layer Protocols",
        "question": "মেইল সার্ভার থেকে ক্লায়েন্ট ডিভাইসে ইমেইল ডাউনলোড/অ্যাক্সেস করার দুটি প্রধান প্রোটোকল কোনগুলো?",
        "options": [
            "ক) POP3 (Post Office Protocol 3) এবং IMAP (Internet Message Access Protocol)",
            "খ) SMTP এবং HTTP",
            "গ) FTP এবং TFTP",
            "ঘ) DNS এবং DHCP"
        ],
        "answer": "ক",
        "explanation": "মেইল রিড করার জন্য POP3 (পোর্ট ১১০) এবং IMAP (পোর্ট ১৪৩) ব্যবহৃত হয়। IMAP সার্ভারে মেইল সিঙ্ক রাখে যা একাধিক ডিভাইস থেকে অ্যাক্সেসে সুবিধাজনক।"
    },
    {
        "id": 40,
        "topic": "Application Layer Protocols",
        "question": "নন-টেক্সট মাল্টিমিডিয়া ফাইল (যেমন ছবি, অডিও, পিডিএফ) ইমেইলের সাথে সংযুক্ত করার জন্য কোন স্ট্যান্ডার্ড ব্যবহৃত হয়?",
        "options": [
            "ক) MIME (Multipurpose Internet Mail Extensions)",
            "খ) ASCII 7-bit",
            "গ) BASE16",
            "ঘ) HTML5"
        ],
        "answer": "ক",
        "explanation": "MIME ঐতিহ্যবাহী 7-bit ASCII মেইল ব্যবস্থাকে প্রসারিত করে বাইনারি ফাইল ও মাল্টিমিডিয়া অ্যাটাচমেন্ট ট্রান্সমিট করার সুযোগ দেয়।"
    },
    {
        "id": 41,
        "topic": "Application Layer Protocols",
        "question": "ডোমেইন নেম সিস্টেমের (DNS) প্রধান কাজ কোনটি এবং এটি কোন ট্রান্সপোর্ট প্রোটোকল ও পোর্ট ব্যবহার করে?",
        "options": [
            "ক) মানুষের পাঠযোগ্য হোস্টনেমকে (যেমন www.google.com) আইপি অ্যাড্রেসে (যেমন 142.250.x.x) রূপান্তর করা; UDP পোর্ট 53 ব্যবহার করে",
            "খ) ফাইল ডাউনলোড করা; TCP পোর্ট 21",
            "গ) রাউটার কনফিগার করা; TCP পোর্ট 23",
            "ঘ) ওয়েবসাইট হোস্টিং করা; পোর্ট 80"
        ],
        "answer": "ক",
        "explanation": "DNS ইন্টারনেটের ডিরেক্টরি সার্ভিস যা হোস্টনেম টু আইপি রেজোলিউশন করে। দ্রুততার জন্য স্ট্যান্ডার্ড কুয়েরিতে UDP পোর্ট ৫৩ ব্যবহৃত হয়।"
    },
    {
        "id": 42,
        "topic": "Application Layer Protocols",
        "question": "DNS-এর হায়ারার্কিক্যাল ডেটাবেজের স্তরগুলোর সঠিক ক্রম কোনটি?",
        "options": [
            "ক) Root DNS Servers -> TLD (Top-Level Domain) Servers -> Authoritative DNS Servers",
            "খ) Local DNS -> Root DNS -> TLD",
            "গ) TLD -> Root -> Local",
            "ঘ) Authoritative -> Root -> TLD"
        ],
        "answer": "ক",
        "explanation": "DNS ট্রি কাঠামোতে সবার উপরে থাকে Root Servers, তার নিচে TLD (যেমন .com, .org, .bd), এবং সর্বশেষে নির্দিষ্ট ডোমেইনের Authoritative DNS Servers।"
    },
    {
        "id": 43,
        "topic": "Application Layer Protocols",
        "question": "DNS রিসোর্স রেকর্ডে (Resource Record - RR) হোস্টনেমের আইপি অ্যাড্রেস সংরক্ষণের টাইপ কোনটি?",
        "options": [
            "ক) Type A (IPv4 এর জন্য) এবং Type AAAA (IPv6 এর জন্য)",
            "খ) Type NS",
            "গ) Type CNAME",
            "ঘ) Type MX"
        ],
        "answer": "ক",
        "explanation": "Type A রেকর্ড হোস্টনেমের IPv4 অ্যাড্রেস এবং Type AAAA রেকর্ড IPv6 অ্যাড্রেস সংরক্ষণ করে।"
    },
    {
        "id": 44,
        "topic": "Application Layer Protocols",
        "question": "DNS রেকর্ডে একটি মেইল সার্ভারের নাম নির্দেশ করতে কোন রেকর্ড টাইপ ব্যবহৃত হয়?",
        "options": [
            "ক) MX (Mail Exchange)",
            "খ) CNAME",
            "গ) PTR",
            "ঘ) TXT"
        ],
        "answer": "ক",
        "explanation": "MX রেকর্ড ডোমেইনের ইনকামিং ইমেইল পরিচালনার দায়িত্বে নিয়োজিত মেইল সার্ভারকে নির্দেশ করে।"
    },
    {
        "id": 45,
        "topic": "Application Layer Protocols",
        "question": "DNS-এ কোনো হোস্টনেমের জন্য ক্যানোনিকাল বা আসল নামের অপর একটি অ্যালিয়াস (Alias) নাম নির্দেশ করতে কোন রেকর্ড ব্যবহৃত হয়?",
        "options": [
            "ক) CNAME (Canonical Name)",
            "খ) A Record",
            "গ) SOA",
            "ঘ) NS"
        ],
        "answer": "ক",
        "explanation": "CNAME রেকর্ড একটি অ্যালিয়াস ডোমেইনকে তার আসল ক্যানোনিকাল ডোমেইনের সাথে ম্যাপ করে।"
    },
    {
        "id": 46,
        "topic": "Application Layer Protocols",
        "question": "DNS কুয়েরিতে রিকার্সিভ (Recursive) এবং ইটারেটিভ (Iterative) কুয়েরির মধ্যে পার্থক্য কী?",
        "options": [
            "ক) রিকার্সিভ কুয়েরিতে সার্ভার নিজে পরবর্তী সার্ভারগুলো থেকে উত্তর খুঁজে ক্লায়েন্টকে দেয়, আর ইটারেটিভে সার্ভার ক্লায়েন্টকে পরবর্তী রেফারেল সার্ভারের ঠিকানা দেয়",
            "খ) রিকার্সিভ কুয়েরি কখনোই উত্তর দেয় না",
            "গ) ইটারেটিভ কুয়েরি ব্রাউজারে হয় না",
            "ঘ) উভয়েই সম্পূর্ণ একই"
        ],
        "answer": "ক",
        "explanation": "ক্লায়েন্ট পিসি লোকাল DNS সার্ভারকে সাধারণত Recursive কুয়েরি পাঠায়, আর লোকাল DNS সার্ভার Root, TLD এবং Authoritative সার্ভারগুলোতে Iterative কুয়েরি চালায়।"
    },
    {
        "id": 47,
        "topic": "Application Layer Protocols",
        "question": "DNS কুয়েরির রেসপন্স ক্লায়েন্ট ও লোকাল সার্ভারে কতক্ষণ সংরক্ষিত থাকবে তা কোন ফিল্ড নির্ধারণ করে?",
        "options": [
            "ক) TTL (Time To Live)",
            "খ) MTU",
            "গ) Window Size",
            "ঘ) Checksum"
        ],
        "answer": "ক",
        "explanation": "TTL মান সেকেন্ড এককে নির্দেশ করে ডিএনএস ক্যাশে রেকর্ডটি কতক্ষণ সতেজ থাকবে। TTL শেষ হলে পুনরায় মূল সার্ভারে কুয়েরি করা হয়।"
    },
    {
        "id": 48,
        "topic": "Application Layer Protocols",
        "question": "টেলনেট (Telnet) এবং এসএসএইচ (SSH)-এর মধ্যে নিরাপত্তার ক্ষেত্রে প্রধান পার্থক্য কী?",
        "options": [
            "ক) Telnet সমতল টেক্সটে (Plaintext - Unencrypted) পাসওয়ার্ড পাঠায়, আর SSH সম্পূর্ণ ট্রাফিক ক্রিপ্টোগ্রাফিকভাবে এনক্রিপ্ট করে পাঠায়",
            "খ) Telnet অনেক সুরক্ষিত",
            "গ) SSH কোনো টার্মিনাল দেয় না",
            "ঘ) Telnet পোর্ট 22 ব্যবহার করে"
        ],
        "answer": "ক",
        "explanation": "Telnet (পোর্ট ২৩) অনিরাপদ কারণ এতে পাসওয়ার্ড স্নাইফ করা যায়। SSH (Secure Shell - পোর্ট ২২) সুরক্ষিত এনক্রিপ্টেড রিমোট লগইন প্রদান করে।"
    },
    {
        "id": 49,
        "topic": "Application Layer Protocols",
        "question": "DHCP (Dynamic Host Configuration Protocol) নেটওয়ার্কে কী কাজ করে?",
        "options": [
            "ক) ক্লায়েন্ট কম্পিউটারগুলোকে স্বয়ংক্রিয়ভাবে ডায়নামিক IP অ্যাড্রেস, সাবনেট মাস্ক, ডিফল্ট গেটওয়ে ও DNS সার্ভারের ঠিকানা বরাদ্দ করে",
            "খ) হার্ডডিস্ক ফরম্যাট করে",
            "গ) ভাইরাস স্ক্যান করে",
            "ঘ) ওয়েবসাইট ব্লক করে"
        ],
        "answer": "ক",
        "explanation": "DHCP একটি নেটওয়ার্ক ম্যানেজমেন্ট প্রোটোকল যা DORA (Discover, Offer, Request, Acknowledge) প্রক্রিয়ায় স্বয়ংক্রিয়ভাবে আইপি কনফিগারেশন প্রদান করে।"
    },
    {
        "id": 50,
        "topic": "Application Layer Protocols",
        "question": "DHCP প্রক্রিয়ার সঠিক ৪টি ধাপের ক্রম (DORA) কোনটি?",
        "options": [
            "ক) Discover -> Offer -> Request -> Acknowledge",
            "খ) Demand -> Order -> Receive -> Accept",
            "গ) Data -> Open -> Read -> Action",
            "ঘ) Direct -> Option -> Route -> Assign"
        ],
        "answer": "ক",
        "explanation": "DHCP ক্লায়েন্ট প্রথমে DHCPDISCOVER ব্রডকাস্ট করে, সার্ভার DHCPOFFER দেয়, ক্লায়েন্ট DHCPREQUEST পাঠায় এবং সার্ভার DHCPACK দিয়ে আইপি নিশ্চিত করে।"
    },
    {
        "id": 51,
        "topic": "Application Layer Protocols",
        "question": "নেটওয়ার্ক ডিভাইস (যেমন রাউটার, সুইচ) মনিটরিং ও পরিচালনার জন্য আদর্শ প্রোটোকল কোনটি?",
        "options": [
            "ক) SNMP (Simple Network Management Protocol)",
            "খ) SMTP",
            "গ) IMAP",
            "ঘ) RIP"
        ],
        "answer": "ক",
        "explanation": "SNMP প্রোটোকল নেটওয়ার্ক অ্যাডমিনিস্ট্রেটরদের বিভিন্ন ডিভাইসের পারফরম্যান্স ও ত্রুটি ট্র্যাক করতে (MIB ডেটাবেজের মাধ্যমে) ব্যবহৃত হয়।"
    },
    {
        "id": 52,
        "topic": "Application Layer Protocols",
        "question": "HTTP সিকিউর (HTTPS) কোন ক্রিপ্টোগ্রাফিক প্রোটোকল ব্যবহার করে ট্রাফিক এনক্রিপ্ট করে এবং এর ডিফল্ট পোর্ট কত?",
        "options": [
            "ক) TLS/SSL (Transport Layer Security); Port 443",
            "খ) IPsec; Port 80",
            "গ) WEP; Port 21",
            "ঘ) DES; Port 25"
        ],
        "answer": "ক",
        "explanation": "HTTPS হলো HTTP-র একটি এনক্রিপ্টেড সংস্করণ যা TLS/SSL প্রোটোকলের মাধ্যমে কাজ করে এবং ডিফল্টভাবে TCP পোর্ট 443 ব্যবহার করে।"
    },
    {
        "id": 53,
        "topic": "Application Layer Protocols",
        "question": "ক্লায়েন্ট সাইডে ব্যবহারকারীর ট্র্যাকিং, শপিং কার্ট এবং লগইন সেশন মনে রাখার জন্য কোন মেকানিজম বহুল ব্যবহৃত হয়?",
        "options": [
            "ক) Cookies (কুকিজ)",
            "খ) Proxy",
            "গ) DNS CNAME",
            "ঘ) Gateway"
        ],
        "answer": "ক",
        "explanation": "HTTP রেসপন্সে সার্ভার `Set-Cookie` হেডার পাঠায় এবং পরবর্তীতে ক্লায়েন্ট প্রতি রিকোয়েস্টে `Cookie` হেডারে সেশন আইডি পাঠায়।"
    },
    {
        "id": 54,
        "topic": "Application Layer Protocols",
        "question": "কন্টেন্ট ডেলিভারি নেটওয়ার্কের (CDN) প্রধান উদ্দেশ্য কোনটি?",
        "options": [
            "ক) বিশ্বব্যাপী ছড়িয়ে থাকা এজ-সার্ভারে কনটেন্ট ক্যাশ রেখে ব্যবহারকারীর ভৌগোলিক দূরত্বের নিকটতম সার্ভার থেকে দ্রুত ওয়েবসাইট লোড নিশ্চিত করা",
            "খ) অরিজিন সার্ভারের সিপিইউ পরিবর্তন করা",
            "গ) ব্রাউজার তৈরি করা",
            "ঘ) ক্লায়েন্টের ইন্টারনেট বিল কমানো"
        ],
        "answer": "ক",
        "explanation": "CDN (যেমন Cloudflare, Akamai) স্ট্যাটিক ও ডাইনামিক কনটেন্টকে ইউজারের কাছাকাছি এজ সার্ভারে ক্যাশ করে ল্যাটেন্সি কমায় এবং সার্ভারের ট্রাফিক চাপ দূর করে।"
    },
    {
        "id": 55,
        "topic": "Application Layer Protocols",
        "question": "BitTorrent প্রোটোকলে 'Choking' এবং 'Tit-for-Tat' অ্যালগরিদমের উদ্দেশ্য কী?",
        "options": [
            "ক) যেসকল পিয়ার সর্বোচ্চ আপলোড রেটে ডেটা সরবরাহ করে কেবল তাদেরকেই ডেটা ডাউনলোড করতে দেওয়া (ফ্রি-রাইডার রোধ করা)",
            "খ) সব সংযোগ বন্ধ করে দেওয়া",
            "গ) সকল ফাইল এনক্রিপ্ট করা",
            "ঘ) সার্ভার বন্ধ রাখা"
        ],
        "answer": "ক",
        "explanation": "Tit-for-Tat নীতি নিশ্চিত করে যে একজন পিয়ার যত বেশি আপলোড করবে, সে তত বেশি ডাউনলোড ব্যান্ডউইথ পাবে; ফলে নেটওয়ার্কে স্বার্থপর ফ্রি-লোডারদের দৌরাত্ম্য বন্ধ হয়।"
    },

    # Subtopic 3: Transport Layer (UDP, TCP, Reliable Transfer, Congestion Control) (56-80)
    {
        "id": 56,
        "topic": "Transport Layer Protocols & Services",
        "question": "ট্রান্সপোর্ট লেয়ারে মাল্টিপ্লেক্সিং (Multiplexing) এবং ডিমাল্টিপ্লেক্সিং (Demultiplexing) মূলত কোন তথ্যের ওপর ভিত্তি করে পরিচালিত হয়?",
        "options": [
            "ক) সোর্স পোর্ট নম্বর এবং ডেস্টিনেশন পোর্ট নম্বর (Port Numbers)",
            "খ) ম্যাক অ্যাড্রেস",
            "গ) কেবল তারের দৈর্ঘ্য",
            "ঘ) ওয়েব ব্রাউজারের ভার্সন"
        ],
        "answer": "ক",
        "explanation": "ট্রান্সপোর্ট লেয়ার প্যাকেটগুলোকে সঠিক অ্যাপ্লিকেশন সকেটে পৌঁছে দিতে সেগমেন্ট হেডারের পোর্ট নম্বর (Port Number) ব্যবহার করে।"
    },
    {
        "id": 57,
        "topic": "Transport Layer Protocols & Services",
        "question": "ওয়েল-নোন পোর্ট নম্বরের (Well-known Ports) সীমা কত?",
        "options": [
            "ক) 0 থেকে 1023",
            "খ) 1024 থেকে 49151",
            "গ) 49152 থেকে 65535",
            "ঘ) 1 থেকে 255"
        ],
        "answer": "ক",
        "explanation": "IANA দ্বারা নির্ধারিত: 0-1023 হলো Well-known ports (স্ট্যান্ডার্ড সার্ভিসের জন্য যেমন HTTP: 80, SSH: 22); 1024-49151 হলো Registered; এবং 49152-65535 হলো Dynamic/Private ports।"
    },
    {
        "id": 58,
        "topic": "Transport Layer Protocols & Services",
        "question": "UDP (User Datagram Protocol)-এর প্রধান বৈশিষ্ট্য কোনটি?",
        "options": [
            "ক) এটি কানেকশনলেস (Connectionless), অনির্ভরযোগ্য (Unreliable), কোনো কনজেশন বা ফ্লো কন্ট্রোল নেই কিন্তু ন্যূনতম ওভারহেড বিশিষ্ট",
            "খ) এটি শতভাগ ডেটা গ্যারান্টি দেয়",
            "গ) এতে ৩-ওয়ে হ্যান্ডশেক হয়",
            "ঘ) এর হেডার সাইজ ২০ বাইট"
        ],
        "answer": "ক",
        "explanation": "UDP কোনো সংযোগ স্থাপন ছাড়াই সরাসরি সেগমেন্ট পাঠায়। এর কোনো রিট্রান্সমিশন মেকানিজম নেই বিধায় এটি অত্যন্ত দ্রুত এবং রিয়েল-টাইম স্ট্রিমিং ও ডিএনএসের জন্য উপযুক্ত।"
    },
    {
        "id": 59,
        "topic": "Transport Layer Protocols & Services",
        "question": "UDP হেডারের আকার কত বাইট এবং এতে কয়টি ফিল্ড থাকে?",
        "options": [
            "ক) ৮ বাইট (৪টি ফিল্ড: Source Port, Destination Port, Length, Checksum)",
            "খ) ২০ বাইট",
            "গ) ৪০ বাইট",
            "ঘ) ৪ বাইট"
        ],
        "answer": "ক",
        "explanation": "UDP হেডার অত্যন্ত সংক্ষিপ্ত (মাত্র ৮ বাইট), যাতে প্রতিটি ২ বাইট করে মোট ৪টি ফিল্ড থাকে: সোর্স পোর্ট, ডেস্টিনেশন পোর্ট, মোট দৈর্ঘ্য এবং এরর চেকসাম।"
    },
    {
        "id": 60,
        "topic": "Transport Layer Protocols & Services",
        "question": "ইন্টারনেট চেকসাম (Checksum) গণনায় বিটগুলো কীভাবে যোগ করা হয়?",
        "options": [
            "ক) ১৬-বিট পূর্ণসংখ্যাগুলোর 1's Complement যোগফল নিয়ে তার বিপরীত (Inversion) করা হয়",
            "খ) সাধারণ XOR অপারেশন",
            "গ) 2's Complement গুণফল",
            "ঘ) CRC-32 ম্যাট্রিক্স"
        ],
        "answer": "ক",
        "explanation": "ইন্টারনেট চেকসামে হেডারের সমস্ত ১৬-বিট শব্দ 1's complement নিয়মে যোগ করা হয় এবং ফলাফলের 1's complement নিয়ে চেকসাম ফিল্ডে বসানো হয়।"
    },
    {
        "id": 61,
        "topic": "Transport Layer Protocols & Services",
        "question": "রিয়েল-টাইম ভিডিও কনফারেন্সিং বা অনলাইন গেমিংয়ে TCP-র চেয়ে UDP বেশি পছন্দের কারণ কোনটি?",
        "options": [
            "ক) হ্যান্ডশেক ডিলে নেই এবং প্যাকেট হারালেও রিট্রান্সমিশনের জন্য পুরো স্ট্রিমকে আটকে রাখে না (No retransmission delay)",
            "খ) UDP সকল প্যাকেট খুঁজে দেয়",
            "গ) UDP ডেটা কম্প্রেস করে",
            "ঘ) TCP-র চেয়ে ধীরগতির"
        ],
        "answer": "ক",
        "explanation": "লাইভ ভিডিওতে হারানো ফ্রেম পুনরায় পাঠানোর চেয়ে সময়মতো পরবর্তী ফ্রেম দেখানো গুরুত্বপূর্ণ। TCP-র রিট্রান্সমিশন ও ফ্লো কন্ট্রোল ল্যাগ তৈরি করে যা UDP করে না।"
    },
    {
        "id": 62,
        "topic": "Transport Layer Protocols & Services",
        "question": "স্টপ-অ্যান্ড-ওয়েট (Stop-and-Wait) প্রোটোকলের প্রধান সীমাবদ্ধতা কোনটি?",
        "options": [
            "ক) ট্রান্সমিটার ইউটিলাইজেশন (Link Utilization) অত্যন্ত নিম্ন, কারণ একটি প্যাকেট পাঠিয়ে ACK আসার আগ পর্যন্ত প্রেরক অলস বসে থাকে",
            "খ) এতে কোনো বাফার লাগে না",
            "গ) এটি কোনো ডেটা পাঠাতে পারে না",
            "ঘ) এটি খুবই জটিল"
        ],
        "answer": "ক",
        "explanation": "স্টপ-অ্যান্ড-ওয়েটে চ্যানেল ক্যাপাসিটি বিশাল হলেও একবারে মাত্র ১টি প্যাকেট ইন-ফ্লাইট থাকতে পারে, ফলে লিঙ্কের সদ্ব্যবহার ($U_{sender}$) মারাত্মকভাবে কমে যায়।"
    },
    {
        "id": 63,
        "topic": "Transport Layer Protocols & Services",
        "question": "পাইপলাইন্ড প্রোটোকল 'Go-Back-N (GBN)'-এ রিসিভার কোন ধরণের স্বীকৃতি (ACK) পাঠায়?",
        "options": [
            "ক) কিউমুলেটিভ স্বীকৃতি (Cumulative ACK)",
            "খ) ইন্ডিভিজুয়াল একনলেজমেন্ট",
            "গ) নেগেটিভ ACK কেবল",
            "ঘ) কোনো ACK পাঠায় না"
        ],
        "answer": "ক",
        "explanation": "GBN কিউমুলেটিভ ACK ব্যবহার করে। যেমন ACK $n$ পাওয়া মানে হলো $n$ পর্যন্ত সমস্ত প্যাকেট রিসিভার সফলভাবে পেয়েছে। কোনো প্যাকেট হারালে $n$-এর পর থেকে উইন্ডোর সমস্ত প্যাকেট পুনরায় পাঠাতে হয়।"
    },
    {
        "id": 64,
        "topic": "Transport Layer Protocols & Services",
        "question": "সিলেক্টিভ রিপিট (Selective Repeat - SR) প্রোটোকল Go-Back-N থেকে কীভাবে আলাদা?",
        "options": [
            "ক) রিসিভার প্রতিটি ত্রুটিহীন প্যাকেটের জন্য আলাদা Individual ACK দেয় এবং ক্ষতিগ্রস্ত প্যাকেটগুলোকে মেমরিতে বাফার করে কেবল হারানো প্যাকেটটিকে রিট্রান্সমিট করায়",
            "খ) এটি কোনো উইন্ডো ব্যবহার করে না",
            "গ) এটি সমস্ত প্যাকেট বাতিল করে",
            "ঘ) এটি GBN-এর চেয়ে কম দক্ষ"
        ],
        "answer": "ক",
        "explanation": "Selective Repeat-এ অপ্রয়োজনীয় ডুপ্লিকেট রিট্রান্সমিশন এড়াতে রিসিভার আউট-অফ-অর্ডার প্যাকেট বাফার করে রাখে এবং প্রেরক কেবল যে প্যাকেটটি হারিয়েছে সেটিই পুনরায় পাঠায়।"
    },
    {
        "id": 65,
        "topic": "Transport Layer Protocols & Services",
        "question": "সিলেক্টিভ রিপিট (SR) প্রোটোকলে সিকোয়েন্স নম্বর স্পেস $k$ হলে উইন্ডো সাইজ $N$ সর্বোচ্চ কত হতে পারে?",
        "options": [
            "ক) $N \\le 2^{k-1}$ (সিকোয়েন্স নম্বরের মোট সংখ্যার অর্ধেক)",
            "খ) $N = 2^k$",
            "গ) $N = 2^k - 1$",
            "ঘ) $N = k$"
        ],
        "answer": "ক",
        "explanation": "উইন্ডো সাইজ মোট সিকোয়েন্স স্পেসের অর্ধেকের বেশি হলে পুরোনো প্যাকেটের রিট্রান্সমিশনকে নতুন উইন্ডোর প্যাকেট হিসেবে ভুল করার ঝুঁকি (Ambiguity) তৈরি হয়।"
    },
    {
        "id": 66,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP (Transmission Control Protocol)-এর অন্যতম প্রধান বৈশিষ্ট্য কোনটি?",
        "options": [
            "ক) সংযোগ-ভিত্তিক (Connection-oriented), নির্ভরযোগ্য বাইট-স্ট্রিম (Reliable Byte Stream) এবং ফুল-ডুপ্লেক্স সার্ভিস",
            "খ) অনির্ভরযোগ্য ও মেসেজ বাউন্ডারি ভিত্তিক",
            "গ) মাল্টিকাস্ট ও ব্রডকাস্ট সমর্থন করে",
            "ঘ) কোনো ফ্লো কন্ট্রোল নেই"
        ],
        "answer": "ক",
        "explanation": "TCP দুটি এন্ডপয়েন্টের মধ্যে থ্রি-ওয়ে হ্যান্ডশেকের মাধ্যমে ফুল-ডুপ্লেক্স নির্ভরযোগ্য বাইট-স্ট্রিম সংযোগ স্থাপন করে ডেটার সঠিক ডেলিভারি ও সিকোয়েন্স নিশ্চিত করে।"
    },
    {
        "id": 67,
        "topic": "Transport Layer Protocols & Services",
        "question": "কোনো অপশন ফিল্ড ছাড়া আদর্শ TCP হেডারের ন্যূনতম আকার কত বাইট?",
        "options": [
            "ক) ২০ বাইট",
            "খ) ৮ বাইট",
            "গ) ৪০ বাইট",
            "ঘ) ১৬ বাইট"
        ],
        "answer": "ক",
        "explanation": "TCP হেডারের সর্বনিম্ন আকার ২০ বাইট (যেখানে UDP মাত্র ৮ বাইট)। অপশন ফিল্ড যুক্ত থাকলে এটি সর্বোচ্চ ৬০ বাইট পর্যন্ত হতে পারে।"
    },
    {
        "id": 68,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP সংযোগ স্থাপনে থ্রি-ওয়ে হ্যান্ডশেকের (Three-Way Handshake) সঠিক ধাপ কোনটি?",
        "options": [
            "ক) SYN -> SYN-ACK -> ACK",
            "খ) ACK -> SYN -> SYN-ACK",
            "গ) SYN -> FIN -> ACK",
            "ঘ) HELLO -> REQUEST -> OK"
        ],
        "answer": "ক",
        "explanation": "১. ক্লায়েন্ট `SYN` সেগমেন্ট পাঠায়, ২. সার্ভার তা স্বীকার করে `SYN-ACK` পাঠায়, ৩. ক্লায়েন্ট চূড়ান্ত স্বীকৃতি হিসেবে `ACK` পাঠায় এবং সংযোগ প্রতিষ্ঠিত হয়।"
    },
    {
        "id": 69,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP সংযোগ সফলভাবে সমাপ্ত বা ক্লোজ করতে কোন ফ্ল্যাগ এবং কয়টি ধাপ ব্যবহৃত হয়?",
        "options": [
            "ক) FIN ফ্ল্যাগ; ৪টি ধাপের হ্যান্ডশেক (Four-Way Teardown)",
            "খ) RST ফ্ল্যাগ; ১টি ধাপ",
            "গ) SYN ফ্ল্যাগ; ২টি ধাপ",
            "ঘ) PSH ফ্ল্যাগ; ৩টি ধাপ"
        ],
        "answer": "ক",
        "explanation": "যেহেতু TCP ফুল-ডুপ্লেক্স, উভয় দিক আলাদাভাবে বন্ধ হতে হয়: $A$ পাঠায় FIN, $B$ পাঠায় ACK; পরবর্তীতে $B$ পাঠায় FIN এবং $A$ পাঠায় ACK (মোট ৪ ধাপ)।"
    },
    {
        "id": 70,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP হেডারে 'Sequence Number' মূলত কী নির্দেশ করে?",
        "options": [
            "ক) সেগমেন্টের ডেটা পে-লোডের প্রথম বাইটের বাইট-স্ট্রিম নম্বর",
            "খ) মোট প্যাকেটের সংখ্যা",
            "গ) রাউটারের আইপি",
            "ঘ) প্রেরকের পোর্ট নম্বর"
        ],
        "answer": "ক",
        "explanation": "TCP প্যাকেট কাউন্ট করে না বরং বাইট কাউন্ট করে। সিকোয়েন্স নম্বর হলো সেগমেন্টে পাঠানো বাইটগুলোর প্রথম বাইটের ক্রমিক নম্বর।"
    },
    {
        "id": 71,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP হেডারে 'Acknowledgment Number' কী প্রকাশ করে?",
        "options": [
            "ক) পরবর্তী যে বাইটটি পাওয়ার জন্য রিসিভার অপেক্ষা করছে (Next expected byte number)",
            "খ) ইতোমধ্যে পাওয়া শেষ প্যাকেটের সাইজ",
            "গ) পোর্ট নম্বর",
            "ঘ) সকেট আইডি"
        ],
        "answer": "ক",
        "explanation": "TCP-র ACK নম্বর হলো কিউমুলেটিভ: রিসিভার যদি $k$ নম্বর বাইট আশা করে, সে ACK হিসেবে $k$ পাঠায়, যার অর্থ $k-1$ পর্যন্ত সকল বাইট সঠিকভাবে পাওয়া গেছে।"
    },
    {
        "id": 72,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP ফ্লো কন্ট্রোল (Flow Control)-এর মূল উদ্দেশ্য কোনটি?",
        "options": [
            "ক) প্রেরক যাতে অতিরিক্ত দ্রুত ডেটা পাঠিয়ে রিসিভারের বাফার মেমরি উপচে (Overflow) না ফেলে",
            "খ) নেটওয়ার্কের রাউটারগুলোকে রক্ষা করা",
            "গ) ইন্টারনেটের বিল কমানো",
            "ঘ) পাসওয়ার্ড এনক্রিপ্ট করা"
        ],
        "answer": "ক",
        "explanation": "Flow Control নিশ্চিত করে যে দ্রুতগতির প্রেরক ধীরগতির গ্রাহকের বাফারকে ওভারফ্লো করবে না। গ্রাহক তার ফ্রি বাফার স্পেস `rwnd` (Receive Window) হেডারে জানিয়ে দেয়।"
    },
    {
        "id": 73,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP ফ্লো কন্ট্রোল এবং কনজেশন কন্ট্রোলের (Congestion Control) মধ্যে পার্থক্য কী?",
        "options": [
            "ক) ফ্লো কন্ট্রোল এন্ড রিসিভারের বাফার নিয়ন্ত্রণ করে, আর কনজেশন কন্ট্রোল ইন্টারমিডিয়েট নেটওয়ার্কের রাউটার ও লিঙ্কগুলোর ওভারলোড নিয়ন্ত্রণ করে",
            "খ) উভয়ই সম্পূর্ণ একই মেকানিজম",
            "গ) ফ্লো কন্ট্রোল রাউটারে চলে",
            "ঘ) কনজেশন কন্ট্রোল ক্যাবলের ক্ষতি রোধ করে"
        ],
        "answer": "ক",
        "explanation": "Flow Control হলো এন্ড-টু-এন্ড রিসিভারের সুরক্ষার জন্য ($rwnd$), আর Congestion Control হলো সমগ্র নেটওয়ার্ক ট্রাফিকের সুরক্ষার জন্য ($cwnd$)। প্রেরকের কার্যকরী উইন্ডো $= \\min(rwnd, cwnd)$।"
    },
    {
        "id": 74,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP কনজেশন কন্ট্রোলে AIMD (Additive Increase, Multiplicative Decrease)-এর আচরণ কোনটি?",
        "options": [
            "ক) কোনো লস না থাকলে প্রতি RTT-তে উইন্ডো সাইজ ১ MSS করে লিনিয়ারলি বাড়ে, এবং লস শনাক্ত হলে কনজেশন উইন্ডো অর্ধেক (halved) হয়ে যায়",
            "খ) উইন্ডো সাইজ সবসময় স্থির থাকে",
            "গ) লস হলে উইন্ডো দ্বিগুণ হয়",
            "ঘ) প্রতি সেকেন্ডে দ্বিগুণ বাড়ে"
        ],
        "answer": "ক",
        "explanation": "AIMD নেটওয়ার্ক স্ট্যাবিলিটির গ্যারান্টি দেয়: কোনো সমস্যা না থাকলে ধীরে ধীরে ১টি করে MSS বাড়ায় (Additive Increase) কিন্তু প্যাকেট ড্রপ হলে এক ধাক্কায় উইন্ডো অর্ধেক করে (Multiplicative Decrease)।"
    },
    {
        "id": 75,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP স্লো স্টার্ট (Slow Start) পর্যায়ে কনজেশন উইন্ডো ($cwnd$) কীভাবে বৃদ্ধি পায়?",
        "options": [
            "ক) প্রতি RTT-তে এক্সপোনেনশিয়ালি বা জ্যামিতিকভাবে দ্বিগুণ (Doubles every RTT: 1, 2, 4, 8...)",
            "খ) লিনিয়ারলি ১ MSS করে",
            "গ) দ্বিগুণ হারে কমে",
            "ঘ) কোনো পরিবর্তন হয় না"
        ],
        "answer": "ক",
        "explanation": "নাম 'Slow Start' হলেও এটি অত্যন্ত দ্রুত ব্যান্ডউইথ খুঁজে নিতে প্রতি সফল ACK-এর জন্য $cwnd$ বাড়িয়ে প্রতি RTT-তে উইন্ডো সাইজ দ্বিগুণ (Exponentially) করে।"
    },
    {
        "id": 76,
        "topic": "Transport Layer Protocols & Services",
        "question": "স্লো স্টার্ট থেকে কনজেশন অ্যাভয়ডেন্স (Congestion Avoidance) মোডে যাওয়ার রূপান্তরকারী সীমাকে কী বলে?",
        "options": [
            "ক) ssthresh (Slow Start Threshold)",
            "খ) MSS",
            "গ) MTU",
            "ঘ) TTL"
        ],
        "answer": "ক",
        "explanation": "যখন $cwnd \\ge ssthresh$ হয়, তখন এক্সপোনেনশিয়াল বৃদ্ধি বন্ধ হয়ে লিনিয়ার বৃদ্ধি (প্রতি RTT-তে ১ MSS) শুরু হয় যাকে Congestion Avoidance বলে।"
    },
    {
        "id": 77,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP ফাস্ট রিট্রান্সমিট (Fast Retransmit) কখন সক্রিয় হয়?",
        "options": [
            "ক) টাইমার এক্সপায়ার হওয়ার আগেই পরপর ৩টি ডুপ্লিকেট ACK (Triple Duplicate ACKs) আসলে",
            "খ) রিসিভার অফলাইন হলে",
            "গ) ক্যাবল ডিসকানেক্ট হলে",
            "ঘ) রাউটার রিবুট হলে"
        ],
        "answer": "ক",
        "explanation": "একই ACK পরপর ৩ বার ডুপ্লিকেট পাওয়া মানে মাঝের একটি প্যাকেট হারিয়েছে কিন্তু পরবর্তী প্যাকেটগুলো রিসিভার পাচ্ছে। ফলে দীর্ঘ টাইম-আউটের অপেক্ষা না করে অবিলম্বে হারানো প্যাকেট রিট্রান্সমিট করা হয়।"
    },
    {
        "id": 78,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP Tahoe এবং TCP Reno সংস্করণের মধ্যে প্রধান পার্থক্য কোথায়?",
        "options": [
            "ক) ৩টি ডুপ্লিকেট ACK পেলে Tahoe তার $cwnd$ নামিয়ে ১ MSS-এ নিয়ে যায়, কিন্তু Reno ফাস্ট রিকভারি করে $cwnd$ কে অর্ধেক ($\approx ssthresh$) থেকে শুরু করে",
            "খ) Tahoe অনেক আধুনিক",
            "গ) Reno-তে কোনো স্লো স্টার্ট নেই",
            "ঘ) Reno কোনো উইন্ডো সাইজ ব্যবহার করে না"
        ],
        "answer": "ক",
        "explanation": "TCP Reno ফাস্ট রিকভারি অ্যালগরিদম প্রবর্তন করে যা ট্রিপল ডুপ্লিকেট অ্যাকে উইন্ডো সাইজ ১ না করে অর্ধেক করে লিনিয়ার বৃদ্ধি বজায় রাখে।"
    },
    {
        "id": 79,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP-তে রিট্রান্সমিশন টাইম-আউট (RTO) সময় নির্ধারণ করতে কোন প্যারামিটার ডায়নামিকভাবে হিসাব করা হয়?",
        "options": [
            "ক) Smoothed Round-Trip Time (SRTT) এবং RTT বৈচিত্র্য (RTT Variation)",
            "খ) ব্যান্ডউইথ গুণফল",
            "গ) ইউজারের স্ক্রিন সাইজ",
            "ঘ) কেবল স্ট্যাটিক ১ সেকেন্ড সময়"
        ],
        "answer": "ক",
        "explanation": "TCP জ্যাকবসন-ক্যারেলস অ্যালগরিদম দিয়ে স্যাম্পল RTT-র এক্সপোনেনশিয়াল ওয়েটেড মুভিং এভারেজ (EWMA) ও ভ্যারিয়েন্স হিসাব করে ডায়নামিক RTO সেট করে।"
    },
    {
        "id": 80,
        "topic": "Transport Layer Protocols & Services",
        "question": "TCP হেডারে 'RST' (Reset) ফ্ল্যাগ কী উদ্দেশ্যে ব্যবহৃত হয়?",
        "options": [
            "ক) কোনো অবৈধ সেগমেন্ট পেলে বা অনুরোধকৃত পোর্টে কোনো লিসেনিং সার্ভিস না থাকলে সংযোগ তাৎক্ষণিকভাবে নাকচ/বাতিল করতে",
            "খ) স্বাভাবিকভাবে ডেটা পাঠাতে",
            "গ) কিউমুলেটিভ স্বীকৃতি জানাতে",
            "ঘ) বাফার বড় করতে"
        ],
        "answer": "ক",
        "explanation": "RST ফ্ল্যাগ সংযোগ অপ্রত্যাশিতভাবে ভেঙে গেলে বা বন্ধ পোর্টে SYN আসলে বিপরীত প্রান্তকে তৎক্ষণাৎ সকেট বন্ধ করার বার্তা পাঠায়।"
    },

    # Subtopic 4: Network Layer - Data Plane, IPv4 & IPv6 Addressing (81-100)
    {
        "id": 81,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "নেটওয়ার্ক লেয়ারের 'ফরওয়ার্ডিং' (Forwarding) এবং 'রাউটিং' (Routing)-এর মধ্যে পার্থক্য কী?",
        "options": [
            "ক) ফরওয়ার্ডিং হলো রাউটারের ইনপুট পোর্ট থেকে উপযুক্ত আউটপুট পোর্টে লোকাল প্যাকেট ট্রান্সফার (Data Plane), আর রাউটিং হলো সোর্স থেকে ডেস্টিনেশনের সামগ্রিক রুট নির্ধারণ (Control Plane)",
            "খ) ফরওয়ার্ডিং শুধুমাত্র সফটওয়্যারে হয়, রাউটিং হয় ফিজিক্যাল তারে",
            "গ) উভয়েই সম্পূর্ণ অভিন্ন ধারণা",
            "ঘ) রাউটিং শুধুমাত্র লোকাল এরিয়া নেটওয়ার্কে হয়"
        ],
        "answer": "ক",
        "explanation": "Forwarding হলো ন্যানোসেকেন্ডে ঘটা লোকাল হার্ডওয়্যার ডেটা-প্লেন অ্যাকশন, আর Routing হলো বিভিন্ন রাউটারের মধ্যে অ্যালগরিদমের সাহায্যে রাউটিং টেবিল গঠনের গ্লোবাল কন্ট্রোল-প্লেন অ্যাকশন।"
    },
    {
        "id": 82,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "রাউটারের ইনপুট কিউতে প্রথম প্যাকেটটি ব্লক হয়ে থাকার কারণে পেছনের অন্যান্য লাইনের প্যাকেটগুলোও আটকে যাওয়ার সমস্যাকে কী বলে?",
        "options": [
            "ক) Head-of-the-Line (HOL) Blocking",
            "খ) Starvation",
            "গ) Round Robin Delay",
            "ঘ) Deadlock"
        ],
        "answer": "ক",
        "explanation": "ইনপুট বাফারযুক্ত সুইচে যদি সামনের প্যাকেটটি অন্য কোনো ব্যস্ত আউটপুট পোর্টের জন্য অপেক্ষা করে, তবে পেছনের প্যাকেটগুলোর পোর্ট খালি থাকলেও তারা বের হতে পারে না; একে HOL Blocking বলে।"
    },
    {
        "id": 83,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "রাউটারের সুইচিং ফ্যাব্রিকের (Switching Fabric) সবচেয়ে দ্রুতগামী ও উচ্চ ব্যান্ডউইথ সম্পন্ন আর্কিটেকচার কোনটি?",
        "options": [
            "ক) Crossbar Switch (বা Interconnection Network)",
            "খ) Switching via Memory",
            "গ) Switching via Shared Bus",
            "ঘ) Software Controller"
        ],
        "answer": "ক",
        "explanation": "মেমরি এবং বাস সুইচিংয়ে একসাথে একটি মাত্র ট্রান্সফার সম্ভব, কিন্তু Crossbar Matrix-এ একাধিক ইনপুট ও আউটপুট একই সাথে সমান্তরালে প্যাকেট ট্রান্সফার করতে পারে।"
    },
    {
        "id": 84,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "IPv4 অ্যাড্রেস কত বিটের এবং এটি সাধারণত কোন নোটেশনে লেখা হয়?",
        "options": [
            "ক) ৩২ বিট; ডটেড-ডেসিমেল নোটেশন (যেমন 192.168.1.1)",
            "খ) ৬৪ বিট; হেক্সাডেসিমেল",
            "গ) ১২৮ বিট; কোলন নোটেশন",
            "ঘ) ১৬ বিট; বাইনারি"
        ],
        "answer": "ক",
        "explanation": "IPv4 হলো ৩২-বিট বিশিষ্ট লজিক্যাল অ্যাড্রেস যা ৮-বিট করে ৪টি অক্টেটে ভাগ করে ডটেড-ডেসিমেল ফরম্যাটে প্রকাশ করা হয়।"
    },
    {
        "id": 85,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "ক্লাসফুল IPv4 অ্যাড্রেসিংয়ে Class A, Class B এবং Class C এর প্রথম অক্টেটের বৈধ রেঞ্জ কত?",
        "options": [
            "ক) Class A: 1-126, Class B: 128-191, Class C: 192-223",
            "খ) Class A: 0-255, Class B: 1-100",
            "গ) Class A: 192-223, Class B: 128-191",
            "ঘ) Class A: 240-255"
        ],
        "answer": "ক",
        "explanation": "ঐতিহ্যবাহী ক্লাসে: Class A: 1-126 (127 লুপব্যাক), Class B: 128-191, Class C: 192-223, Class D (Multicast): 224-239, এবং Class E (Experimental): 240-255।"
    },
    {
        "id": 86,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "RFC 1918 অনুযায়ী ব্যক্তিগত বা প্রাইভেট আইপি অ্যাড্রেসের (Private IP Ranges) সঠিক তালিকা কোনটি?",
        "options": [
            "ক) 10.0.0.0/8, 172.16.0.0/12, এবং 192.168.0.0/16",
            "খ) 1.0.0.0/8, 8.8.8.8/32",
            "গ) 127.0.0.0/8 কেবল",
            "ঘ) 255.255.255.0/24"
        ],
        "answer": "ক",
        "explanation": "পাবলিক ইন্টারনেটে রাউট হয় না এমন সংরক্ষিত প্রাইভেট রেঞ্জ: Class A: 10.0.0.0 - 10.255.255.255; Class B: 172.16.0.0 - 172.31.255.255; Class C: 192.168.0.0 - 192.168.255.255।"
    },
    {
        "id": 87,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "CIDR (Classless Inter-Domain Routing) নোটেশন 192.168.10.0/26 এর সাবনেট মাস্ক কোনটি এবং এতে ব্যবহারের উপযোগী বৈধ হোস্ট আইপি সংখ্যা কত?",
        "options": [
            "ক) সাবনেট মাস্ক: 255.255.255.192; ব্যবহারযোগ্য হোস্ট: 62টি ($2^6 - 2$)",
            "খ) সাবনেট মাস্ক: 255.255.255.0; হোস্ট: 254টি",
            "গ) সাবনেট মাস্ক: 255.255.255.128; হোস্ট: 126টি",
            "ঘ) সাবনেট মাস্ক: 255.255.255.224; হোস্ট: 30টি"
        ],
        "answer": "ক",
        "explanation": "/26 মানে নেটওয়ার্ক বিট ২৬টি, অবশিষ্ট হোস্ট বিট ৩২ - ২৬ = ৬টি। সাবনেট মাস্ক = 255.255.255.192। মোট আইপি $2^6 = 64$টি, নেটওয়ার্ক ও ব্রডকাস্ট বাদ দিলে ব্যবহারযোগ্য হোস্ট = ৬২টি।"
    },
    {
        "id": 88,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "একটি সাবনেটের প্রথম আইপি এবং শেষ আইপি যথাক্রমে কী কাজে সংরক্ষিত থাকে?",
        "options": [
            "ক) প্রথমটি নেটওয়ার্ক অ্যাড্রেস (Network ID) এবং শেষটি ডিরেক্টেড ব্রডকাস্ট অ্যাড্রেস (Broadcast ID)",
            "খ) উভয়ই ইউজারের পিসির জন্য",
            "গ) প্রথমটি রাউটারের জন্য, শেষটি সুইচের জন্য",
            "ঘ) কোনো সংরক্ষণ থাকে না"
        ],
        "answer": "ক",
        "explanation": "কোনো সাবনেটের হোস্ট অংশের সমস্ত বিট ০ হলে তা Network ID এবং সমস্ত বিট ১ হলে তা Directed Broadcast Address হিসেবে সংরক্ষিত থাকে; এগুলো কোনো নির্দিষ্ট হোস্টকে দেওয়া যায় না।"
    },
    {
        "id": 89,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "লুপব্যাক অ্যাড্রেস (Loopback Address - 127.0.0.1) কী উদ্দেশ্যে ব্যবহৃত হয়?",
        "options": [
            "ক) কোনো প্যাকেট বাইরে না পাঠিয়ে নিজের ডিভাইসের নেটওয়ার্ক স্ট্যাক ও লোকাল সার্ভার সার্ভিস পরীক্ষা করতে",
            "খ) ইন্টারনেট স্পিড বাড়াতে",
            "গ) ওয়াইফাই পাসওয়ার্ড দিতে",
            "ঘ) ব্রডকাস্ট করতে"
        ],
        "answer": "ক",
        "explanation": "127.0.0.1 (localhost) ট্রাফিক নেটওয়ার্ক ইন্টারফেসে না পাঠিয়ে সরাসরি কার্নেল স্তরে নিজের ডিভাইসেই লুপব্যাক করে আইপিসি ও ডায়াগনস্টিক নিশ্চিত করে।"
    },
    {
        "id": 90,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "IPv4 হেডার ফরম্যাটে অপশন ছাড়া ন্যূনতম দৈর্ঘ্য কত এবং এতে Time to Live (TTL) ফিল্ডের ভূমিকা কী?",
        "options": [
            "ক) ন্যূনতম ২০ বাইট; TTL প্রতিটি রাউটার পার হওয়ার সময় ১ করে কমে এবং ০ হলে প্যাকেট ড্রপ হয়ে ইনফিনিট রাউটিং লুপ প্রতিরোধ করে",
            "খ) ৪০ বাইট; TTL গতি বাড়ায়",
            "গ) ৮ বাইট; TTL প্যাকেট সাইজ মাপে",
            "ঘ) ৬০ বাইট; TTL ব্যান্ডউইথ নির্ধারণ করে"
        ],
        "answer": "ক",
        "explanation": "IPv4 হেডার সাইজ ২০ বাইট। TTL প্রতি হপে ১ হ্রাস পায়; TTL=0 হলে রাউটার প্যাকেটটি ফেলে দিয়ে সোর্সকে একটি ICMP Time Exceeded বার্তা ফেরত দেয়।"
    },
    {
        "id": 91,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "IPv4 প্যাকেট ফ্র্যাগমেন্টেশনে (Fragmentation) কোন তিনটি হেডার ফিল্ড ব্যবহৃত হয়?",
        "options": [
            "ক) Identification, Flags (DF, MF), এবং Fragment Offset",
            "খ) TTL, Checksum, Protocol",
            "গ) Source IP, Destination IP, Port",
            "ঘ) Type of Service, Version, IHL"
        ],
        "answer": "ক",
        "explanation": "লিঙ্কের MTU প্যাকেটের আকারের চেয়ে ছোট হলে প্যাকেট বিভক্ত করতে Identification (প্যাকেট আইডি), Flags (MF=More Fragments), এবং Fragment Offset (৮-বাইট ব্লকে অবস্থানের মান) ব্যবহৃত হয়।"
    },
    {
        "id": 92,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "IPv4 প্যাকেট ফ্র্যাগমেন্টেশন কোন ডিভাইসে সম্পন্ন হতে পারে এবং পুনঃসংযোজন (Reassembly) কোথায় ঘটে?",
        "options": [
            "ক) ফ্র্যাগমেন্টেশন সোর্স হোস্ট বা যেকোনো ইন্টারমিডিয়েট রাউটারে হতে পারে, কিন্তু রিঅ্যাসেম্বলি শুধুমাত্র ফাইনাল ডেস্টিনেশন হোস্টে ঘটে",
            "খ) রিঅ্যাসেম্বলি পরবর্তী রাউটারে হয়",
            "গ) ফ্র্যাগমেন্টেশন কেবল সুইচে হয়",
            "ঘ) রিঅ্যাসেম্বলি কেবল ডিএনএসে হয়"
        ],
        "answer": "ক",
        "explanation": "রাউটার ওভারহেড কমাতে ইন্টারমিডিয়েট রাউটার ফ্র্যাগমেন্টগুলোকে জোড়া লাগায় না; চূড়ান্ত গন্তব্য এন্ড-সিস্টেমে সকল ফ্র্যাগমেন্ট পৌঁছানোর পর সেখানে Reassembly সম্পন্ন হয়।"
    },
    {
        "id": 93,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "NAT (Network Address Translation)-এর মূল কাজ কোনটি?",
        "options": [
            "ক) লোকাল নেটওয়ার্কের প্রাইভেট আইপি অ্যাড্রেসকে ইন্টারনেট রাউটেবল একক বা একাধিক পাবলিক আইপি অ্যাড্রেসে রূপান্তর করা",
            "খ) ম্যাক অ্যাড্রেস পরিবর্তন করা",
            "গ) ডোমেইন নেম কেনা",
            "ঘ) তারবিহীন নেটওয়ার্ক তৈরি"
        ],
        "answer": "ক",
        "explanation": "NAT প্রাইভেট আইপি ও পোর্ট নম্বরের ম্যাপিং টেবিল ব্যবহার করে অনেক ডিভাইসকে একটিমাত্র পাবলিক আইপি দিয়ে ইন্টারনেটের সাথে যুক্ত করার সুযোগ দেয়, যা IPv4 এর সংকট দীর্ঘায়িত করেছে।"
    },
    {
        "id": 94,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "IPv6 অ্যাড্রেস কত বিটের এবং এটি কয়টি অংশে হেক্সাডেসিমেল আকারে বিভক্ত থাকে?",
        "options": [
            "ক) ১২৮ বিট; ১৬ বিট করে মোট ৮টি হেক্সটেট (Hextet) কোলন (:) দিয়ে বিভক্ত",
            "খ) ৬৪ বিট; ৪ ভাগে",
            "গ) ২৫৬ বিট; ১৬ ভাগে",
            "ঘ) ৩২ বিট; ডট দিয়ে"
        ],
        "answer": "ক",
        "explanation": "IPv6 হলো ১২৮-বিট অ্যাড্রেস (যেমন `2001:0db8:85a3:0000:0000:8a2e:0370:7334`) যা বিশাল অ্যাড্রেস স্পেস ($2^{128}$) প্রদান করে।"
    },
    {
        "id": 95,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "IPv4-এর তুলনায় IPv6 হেডারের প্রধান কাঠামোগত সুবিধা কোনটি?",
        "options": [
            "ক) ফিক্সড ৪০ বাইটের সরলীকৃত বেস হেডার, কোনো চেকল্যাম ফিল্ড নেই এবং ইন্টারমিডিয়েট রাউটারে কোনো ফ্র্যাগমেন্টেশন করতে হয় না",
            "খ) এতে কোনো আইপি অ্যাড্রেস থাকে না",
            "গ) হেডার সাইজ ২০ বাইট",
            "ঘ) এটি রাউটিং টেবিল বন্ধ করে দেয়"
        ],
        "answer": "ক",
        "explanation": "IPv6 রাউটারের প্রসেসিং স্পিড বাড়াতে ফিক্সড ৪০ বাইটের সহজ হেডার ব্যবহার করে এবং রাউটার লেভেলে ফ্র্যাগমেন্টেশন সম্পূর্ণ নিষিদ্ধ করে (কেবল সোর্স হোস্ট ফ্র্যাগমেন্ট করতে পারে)।"
    },
    {
        "id": 96,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "ICMP (Internet Control Message Protocol) মূলত কী কাজে ব্যবহৃত হয়?",
        "options": [
            "ক) নেটওয়ার্ক লেয়ারের এরর রিপোর্টিং (যেমন Destination Unreachable) এবং ডায়াগনস্টিক ট্রাবলশুটিং (যেমন Ping ও Traceroute)",
            "খ) ওয়েব পেজ ব্রাউজিং",
            "গ) ভিডিও কলিং",
            "ঘ) মেইল ডাউনলোড"
        ],
        "answer": "ক",
        "explanation": "ICMP নেটওয়ার্ক ডিভাইসগুলোর মধ্যে ত্রুটি বার্তা ও ডায়াগনস্টিক সিগন্যাল বিনিময়ে ব্যবহৃত হয়। `ping` ইউটিলিটি ICMP Echo Request ও Reply ব্যবহার করে।"
    },
    {
        "id": 97,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "`traceroute` ইউটিলিটি সোর্স থেকে ডেস্টিনেশন পর্যন্ত সকল মধ্যবর্তী রাউটারের আইপি শনাক্ত করতে কোন মেকানিজম ব্যবহার করে?",
        "options": [
            "ক) ক্রমান্বয়ে TTL মান ১, ২, ৩... বাড়িয়ে প্যাকেট পাঠায় এবং রাউটারগুলো থেকে ICMP Time Exceeded বার্তা সংগ্রহ করে",
            "খ) ডিএনএস টেবিল ডাউনলোড করে",
            "গ) ম্যাক ব্রডকাস্ট করে",
            "ঘ) এসএসএইচ দিয়ে রাউটারে লগইন করে"
        ],
        "answer": "ক",
        "explanation": "Traceroute প্রথমে TTL=1 দিয়ে পাঠালে ১ম রাউটার ড্রপ করে ICMP পাঠায়, পরে TTL=2 দিয়ে ২য় রাউটারের আইপি পায়; এভাবে ক্রমান্বয়ে সম্পূর্ণ রুট ম্যাপিং করে।"
    },
    {
        "id": 98,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "লংগেস্ট প্রিফিক্স ম্যাচিং (Longest Prefix Match) নীতি রাউটার কখন প্রয়োগ করে?",
        "options": [
            "ক) রাউটিং টেবিলে কোনো ডেস্টিনেশন আইপির জন্য একাধিক সাবনেট এন্ট্রি মিললে যে এন্ট্রির সাবনেট মাস্ক সবচেয়ে বড়/নির্দিষ্ট সেটিকে বেছে নেয়",
            "খ) সবচেয়ে ছোট মাস্ক বেছে নেয়",
            "গ) প্রথম পাওয়া এন্ট্রি নেয়",
            "ঘ) র্যান্ডম এন্ট্রি নেয়"
        ],
        "answer": "ক",
        "explanation": "প্যাকেট ফরোয়ার্ডিংয়ে রাউটার সর্বদা সর্বাধিক নির্দিষ্ট (সবচেয়ে দীর্ঘ সাবনেট প্রিফিক্স /28 বনাম /24 হলে /28) ম্যাচিং রুল অনুযায়ী আউটপুট পোর্ট নির্ধারণ করে।"
    },
    {
        "id": 99,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "IPv4 থেকে IPv6-এ ট্রানজিশনের জন্য বহুল ব্যবহৃত তিনটি কৌশল কী কী?",
        "options": [
            "ক) Dual Stack (উভয় স্ট্যাক একসাথে চলা), Tunneling (IPv4-এর ভেতর IPv6 প্যাকেট এনক্যাপসুলেশন), এবং NAT-PT (অনুবাদ)",
            "খ) ডিলিট, ফরম্যাট ও রিস্টার্ট",
            "গ) হাব, রিপিটার ও ব্রিজ",
            "ঘ) কেবল তার বদলানো"
        ],
        "answer": "ক",
        "explanation": "যেহেতু সমগ্র ইন্টারনেটের কোটি কোটি ডিভাইস এক রাতে রূপান্তর সম্ভব নয়, তাই Dual-stack, IPv4 নেটওয়ার্কের ওপর দিয়ে Tunneling এবং প্রোটোকল ট্রান্সলেশন ব্যবহৃত হয়।"
    },
    {
        "id": 100,
        "topic": "Network Layer - Data Plane & IP Addressing",
        "question": "IPv6 অ্যাড্রেসে কোনো ব্রডকাস্ট (Broadcast) অ্যাড্রেস নেই। এর পরিবর্তে কোন ধরণের অ্যাড্রেসিং কৌশল ব্যবহৃত হয়?",
        "options": [
            "ক) মাল্টিকাস্ট (Multicast) এবং এনিকাস্ট (Anycast)",
            "খ) সার্কিট অ্যাড্রেসিং",
            "গ) লোকাল হাবিং",
            "ঘ) কেবল ইউনিকাস্ট"
        ],
        "answer": "ক",
        "explanation": "IPv6 অপচয় রোধ করতে ব্রডকাস্ট বাতিল করেছে; তার জায়গায় নির্দিষ্ট গ্রুপে পাঠাতে Multicast এবং নিকটতম যেকোনো একটি ইন্টারফেসে পৌঁছাতে Anycast ব্যবহার করে।"
    }
]

out_dir = "NTRCA 452 - AI"
os.makedirs(out_dir, exist_ok=True)
filename = os.path.join(out_dir, "অধ্যায়- ৭. Data Communications and Networking.json")

with open(filename, "w", encoding="utf-8") as f:
    json.dump(questions_part1, f, ensure_ascii=False, indent=2)

print(f"Saved Part 1 with {len(questions_part1)} questions successfully.")
