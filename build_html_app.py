# -*- coding: utf-8 -*-
import json
import os

# Load Chapter 1
ch1_path = r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\NTRCA 313 and 325 - AI\অধ্যায়- ক. কম্পিউটার বেসিক.json"
with open(ch1_path, "r", encoding="utf-8") as f:
    ch1_questions = json.load(f)

# Load Chapter 2
ch2_path = r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\NTRCA 313 and 325 - AI\অধ্যায়- খ. সংখ্যা পদ্ধতি.json"
with open(ch2_path, "r", encoding="utf-8") as f:
    ch2_questions = json.load(f)

# Load Chapter 3
ch3_path = r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\NTRCA 313 and 325 - AI\অধ্যায়- গ. উপাত্ত উপস্থাপন.json"
with open(ch3_path, "r", encoding="utf-8") as f:
    ch3_questions = json.load(f)

# Load Chapter 4
ch4_path = r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\NTRCA 313 and 325 - AI\অধ্যায়- ঘ. লজিক সার্কিট-বর্তনী.json"
with open(ch4_path, "r", encoding="utf-8") as f:
    ch4_questions = json.load(f)

# Load Chapter 5
ch5_path = r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\NTRCA 313 and 325 - AI\অধ্যায়- ঙ. অপারেটিং পদ্ধতি.json"
with open(ch5_path, "r", encoding="utf-8") as f:
    ch5_questions = json.load(f)

# Load Chapter 6
ch6_path = r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\NTRCA 313 and 325 - AI\অধ্যায়- চ. এলগোরিদম এবং ফ্লো চার্ট.json"
with open(ch6_path, "r", encoding="utf-8") as f:
    ch6_questions = json.load(f)

# Load Chapter 7
ch7_path = r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\NTRCA 313 and 325 - AI\অধ্যায়- ছ. ইন্টারনেট.json"
with open(ch7_path, "r", encoding="utf-8") as f:
    ch7_questions = json.load(f)

all_datasets = {
    "ch1": {
        "title": "অধ্যায়- ক. কম্পিউটার বেসিক",
        "questions": ch1_questions
    },
    "ch2": {
        "title": "অধ্যায়- খ. সংখ্যা পদ্ধতি",
        "questions": ch2_questions
    },
    "ch3": {
        "title": "অধ্যায়- গ. উপাত্ত উপস্থাপন",
        "questions": ch3_questions
    },
    "ch4": {
        "title": "অধ্যায়- ঘ. লজিক সার্কিট ও গেটস",
        "questions": ch4_questions
    },
    "ch5": {
        "title": "অধ্যায়- ঙ. অপারেটিং পদ্ধতি",
        "questions": ch5_questions
    },
    "ch6": {
        "title": "অধ্যায়- চ. এলগোরিদম এবং ফ্লো চার্ট",
        "questions": ch6_questions
    },
    "ch7": {
        "title": "অধ্যায়- ছ. ইন্টারনেট",
        "questions": ch7_questions
    }
}




html_template = """<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NTRCA 313 & 325 - AI | অধ্যায় ও টপিকভিত্তিক লাইভ এক্সাম ও প্রশ্নব্যাংক</title>
  <!-- Google Fonts for High Quality Bengali Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&family=Anek+Bangla:wght@400;500;600;700&family=Noto+Sans+Bengali:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Font Awesome Icons (Local driver with CDN fallback) -->
  <link rel="stylesheet" href="drivers/fontawesome/css/all.min.css" onerror="this.onerror=null;this.href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css';">
  <!-- KaTeX for Math/Logic Formulas -->
  <link rel="stylesheet" href="drivers/katex/katex.min.css" onerror="this.onerror=null;this.href='https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css';">
  <script defer src="drivers/katex/katex.min.js" onerror="this.onerror=null;this.src='https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js';"></script>

  <style>
    :root {
      --bg-page: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #0f172a;
      --text-sub: #334155;
      --text-muted: #64748b;
      --border-color: #e2e8f0;
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --primary-light: #eff6ff;
      --success: #16a34a;
      --success-light: #ecfdf5;
      --danger: #dc2626;
      --danger-light: #fef2f2;
      --warning: #d97706;
      --warning-light: #fffbeb;
      --topic-bg: #f1f5f9;
      --topic-text: #475569;
      --radius: 10px;
      --shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.07);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Hind Siliguri', 'Inter', -apple-system, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
    }

    /* Header */
    header.app-header {
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      border-top: 4px solid var(--primary);
      box-shadow: 0 4px 18px rgba(15, 23, 42, 0.04);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .header-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 14px 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .header-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }

    .brand-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-badge {
      width: 44px;
      height: 44px;
      background: linear-gradient(135deg, #1e40af, #3b82f6);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 12px;
      font-size: 20px;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }

    .brand-text h1 {
      font-size: 19px;
      font-weight: 700;
      color: #0f172a;
      letter-spacing: -0.3px;
    }

    .brand-text p {
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 500;
    }

    .mode-tabs {
      display: flex;
      background: #f1f5f9;
      padding: 4px;
      border-radius: 10px;
      gap: 4px;
    }

    .mode-tab {
      padding: 7px 15px;
      font-size: 13.5px;
      font-weight: 600;
      border: none;
      border-radius: 7px;
      background: transparent;
      color: var(--text-sub);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .mode-tab.active {
      background: #ffffff;
      color: var(--primary);
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }

    .mode-tab:hover:not(.active) {
      color: #0f172a;
    }

    /* Actions Strip */
    .controls-strip {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
      padding-top: 6px;
      border-top: 1px solid #f1f5f9;
    }

    .filters-group {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .select-wrap, .search-wrap {
      position: relative;
      display: flex;
      align-items: center;
    }

    .select-input {
      appearance: none;
      background: #ffffff;
      border: 1.5px solid var(--border-color);
      border-radius: 8px;
      padding: 7px 32px 7px 12px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-sub);
      cursor: pointer;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s;
      max-width: 280px;
    }

    .select-input:focus {
      border-color: var(--primary);
    }

    .select-arrow {
      position: absolute;
      right: 10px;
      pointer-events: none;
      font-size: 11px;
      color: var(--text-muted);
    }

    .search-input {
      padding: 7px 12px 7px 32px;
      border: 1.5px solid var(--border-color);
      border-radius: 8px;
      font-size: 13.5px;
      width: 220px;
      font-family: inherit;
      outline: none;
    }

    .search-input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }

    .search-icon {
      position: absolute;
      left: 10px;
      font-size: 12px;
      color: var(--text-muted);
    }

    .tool-btns {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .btn {
      padding: 7px 13px;
      font-size: 13px;
      font-weight: 600;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: #ffffff;
      color: var(--text-sub);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: inherit;
      transition: all 0.2s;
    }

    .btn:hover {
      background: #f8fafc;
      border-color: #cbd5e1;
    }

    .btn-primary {
      background: var(--primary);
      border-color: var(--primary);
      color: #ffffff;
    }

    .btn-primary:hover {
      background: var(--primary-hover);
      border-color: var(--primary-hover);
    }

    .btn-outline-danger {
      color: var(--danger);
      border-color: #fca5a5;
    }

    .btn-outline-danger:hover {
      background: var(--danger-light);
    }

    /* Live Exam Status Bar */
    .exam-timer-bar {
      display: none;
      background: linear-gradient(90deg, #1e293b, #0f172a);
      color: #ffffff;
      padding: 10px 20px;
      border-radius: 10px;
      margin-top: 14px;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    }

    .timer-display {
      font-size: 18px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: 0.5px;
    }

    .timer-display i {
      color: #fbbf24;
    }

    .exam-stats-pill {
      font-size: 13px;
      background: rgba(255,255,255,0.12);
      padding: 4px 12px;
      border-radius: 20px;
    }

    /* Main Container */
    .main-layout {
      max-width: 1280px;
      margin: 20px auto;
      padding: 0 20px;
      display: grid;
      grid-template-columns: 1fr 300px;
      gap: 24px;
    }

    /* Sheet / Practice Mode View */
    .questions-wrapper {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .question-card {
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
      transition: border-color 0.2s, box-shadow 0.2s;
    }

    .question-card:hover {
      border-color: #cbd5e1;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.06);
    }

    /* Meta bar with Question number and Topic Tag */
    .q-meta-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 10px;
    }

    .q-num {
      background: #eff6ff;
      color: var(--primary);
      font-weight: 700;
      font-size: 13px;
      padding: 3px 10px;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    .q-topic-badge {
      background: #f1f5f9;
      color: #475569;
      font-size: 12px;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 20px;
      border: 1px solid #e2e8f0;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .q-topic-badge:hover {
      background: #e2e8f0;
      color: #0f172a;
    }

    .q-title {
      font-size: 16px;
      font-weight: 600;
      color: #0f172a;
      line-height: 1.5;
      margin-bottom: 14px;
    }

    .options-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }

    .opt-btn {
      background: #f8fafc;
      border: 1.5px solid var(--border-color);
      border-radius: 8px;
      padding: 10px 14px;
      text-align: left;
      font-size: 14.5px;
      color: #1e293b;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .opt-btn:hover:not(.disabled) {
      background: #f1f5f9;
      border-color: #94a3b8;
    }

    .opt-prefix {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: #e2e8f0;
      color: #334155;
      font-weight: 700;
      font-size: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      transition: all 0.15s ease;
    }

    /* Option States */
    .opt-btn.selected {
      border-color: var(--primary);
      background: var(--primary-light);
    }

    .opt-btn.selected .opt-prefix {
      background: var(--primary);
      color: #ffffff;
    }

    .opt-btn.correct {
      border-color: var(--success) !important;
      background: var(--success-light) !important;
      color: #065f46 !important;
      font-weight: 600;
    }

    .opt-btn.correct .opt-prefix {
      background: var(--success) !important;
      color: #ffffff !important;
    }

    .opt-btn.wrong {
      border-color: var(--danger) !important;
      background: var(--danger-light) !important;
      color: #991b1b !important;
    }

    .opt-btn.wrong .opt-prefix {
      background: var(--danger) !important;
      color: #ffffff !important;
    }

    /* Explanation Box */
    .explanation-box {
      margin-top: 14px;
      background: #f0fdf4;
      border-left: 4px solid var(--success);
      padding: 12px 14px;
      border-radius: 0 8px 8px 0;
      font-size: 13.5px;
      color: #166534;
      line-height: 1.5;
      animation: fadeIn 0.25s ease;
    }

    .explanation-box strong {
      color: #14532d;
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 4px;
      font-size: 13px;
    }

    /* Sidebar Palette */
    .sidebar-palette {
      position: sticky;
      top: 100px;
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 16px;
      box-shadow: var(--shadow);
      max-height: calc(100vh - 120px);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .palette-title {
      font-size: 15px;
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .palette-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 6px;
    }

    .palette-item {
      aspect-ratio: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12.5px;
      font-weight: 600;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background: #f8fafc;
      color: var(--text-sub);
      cursor: pointer;
      transition: all 0.15s;
    }

    .palette-item:hover {
      border-color: var(--primary);
      background: var(--primary-light);
    }

    .palette-item.answered {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }

    .palette-item.correct {
      background: var(--success);
      color: #ffffff;
      border-color: var(--success);
    }

    .palette-item.wrong {
      background: var(--danger);
      color: #ffffff;
      border-color: var(--danger);
    }

    /* Score Modal */
    .modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.6);
      backdrop-filter: blur(4px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .score-card {
      background: #ffffff;
      border-radius: 16px;
      max-width: 500px;
      width: 100%;
      padding: 28px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.2);
      text-align: center;
      animation: popIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .score-badge {
      width: 72px;
      height: 72px;
      border-radius: 50%;
      background: #eff6ff;
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 32px;
      margin: 0 auto 16px;
    }

    .score-card h2 {
      font-size: 22px;
      color: #0f172a;
      margin-bottom: 6px;
    }

    .score-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin: 20px 0;
    }

    .score-box {
      background: #f8fafc;
      padding: 12px;
      border-radius: 10px;
      border: 1px solid #e2e8f0;
    }

    .score-box.correct-box {
      border-color: #86efac;
      background: #f0fdf4;
      color: #166534;
    }

    .score-box.wrong-box {
      border-color: #fca5a5;
      background: #fef2f2;
      color: #991b1b;
    }

    .score-box.unanswered-box {
      border-color: #e2e8f0;
      background: #f8fafc;
      color: #475569;
    }

    .score-val {
      font-size: 24px;
      font-weight: 700;
      line-height: 1.2;
    }

    .score-lbl {
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
    }

    /* Print / Exam Paper Layout */
    @media print {
      header.app-header, .sidebar-palette, .controls-strip, .mode-tabs, .btn, .search-wrap {
        display: none !important;
      }

      body {
        background: #ffffff !important;
        color: #000000 !important;
      }

      .main-layout {
        max-width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
      }

      .questions-wrapper {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        column-gap: 20px !important;
      }

      .question-card {
        border: none !important;
        border-bottom: 1px dashed #999 !important;
        border-radius: 0 !important;
        padding: 10px 0 !important;
        box-shadow: none !important;
        break-inside: avoid;
      }

      .opt-btn {
        background: transparent !important;
        border: none !important;
        padding: 3px 0 !important;
      }
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes popIn {
      from { opacity: 0; transform: scale(0.95); }
      to { opacity: 1; transform: scale(1); }
    }

    @media (max-width: 860px) {
      .main-layout {
        grid-template-columns: 1fr;
      }
      .sidebar-palette {
        display: none;
      }
      .options-grid {
        grid-template-columns: 1fr;
      }
      .search-input {
        width: 100%;
      }
    }
  </style>
</head>
<body>

  <!-- App Header -->
  <header class="app-header">
    <div class="header-container">
      <div class="header-top">
        <div class="brand-wrap">
          <div class="brand-badge"><i class="fa-solid fa-brain"></i></div>
          <div class="brand-text">
            <h1>NTRCA 313 & 325 - AI প্রশ্নব্যাংক</h1>
            <p><i class="fa-solid fa-graduation-cap"></i> শিক্ষক নিবন্ধন (আইসিটি প্রভাষক ও সহকারী শিক্ষক) মডেল টেস্ট</p>
          </div>
        </div>

        <!-- Mode Selectors -->
        <div class="mode-tabs">
          <button class="mode-tab active" id="tabPractice" onclick="setMode('practice')">
            <i class="fa-solid fa-book-open"></i> অনুশীলন মোড
          </button>
          <button class="mode-tab" id="tabExam" onclick="setMode('exam')">
            <i class="fa-solid fa-stopwatch"></i> লাইভ পরীক্ষা মোড
          </button>
          <button class="mode-tab" id="tabPaper" onclick="window.print()">
            <i class="fa-solid fa-print"></i> প্রিন্ট শিট
          </button>
        </div>
      </div>

      <!-- Controls & Filter Bar -->
      <div class="controls-strip">
        <div class="filters-group">
          <!-- Chapter Filter -->
          <div class="select-wrap">
            <select class="select-input" id="chapterSelect" onchange="onChapterChange()">
              <option value="ch1">অধ্যায়- ক. কম্পিউটার বেসিক (১০০ প্রশ্ন)</option>
              <option value="ch2">অধ্যায়- খ. সংখ্যা পদ্ধতি (১০০ প্রশ্ন)</option>
              <option value="ch3">অধ্যায়- গ. উপাত্ত উপস্থাপন (১০০ প্রশ্ন)</option>
              <option value="ch4">অধ্যায়- ঘ. লজিক সার্কিট ও গেটস (১০০ প্রশ্ন)</option>
              <option value="ch5">অধ্যায়- ঙ. অপারেটিং পদ্ধতি (১০০ প্রশ্ন)</option>
              <option value="ch6">অধ্যায়- চ. এলগোরিদম এবং ফ্লো চার্ট (১০০ প্রশ্ন)</option>
              <option value="ch7" selected>অধ্যায়- ছ. ইন্টারনেট (১০০ প্রশ্ন)</option>
              <option value="all7">সম্পূর্ণ সিলেবাস ক থেকে ছ একসাথে (৭০০ প্রশ্ন)</option>
            </select>
            <span class="select-arrow"><i class="fa-solid fa-chevron-down"></i></span>
          </div>

          <!-- Dynamic Topic Filter -->
          <div class="select-wrap">
            <select class="select-input" id="topicSelect" onchange="onTopicFilterChange()">
              <option value="all">সকল টপিক</option>
            </select>
            <span class="select-arrow"><i class="fa-solid fa-chevron-down"></i></span>
          </div>

          <!-- Search Input -->
          <div class="search-wrap">
            <span class="search-icon"><i class="fa-solid fa-magnifying-glass"></i></span>
            <input type="text" class="search-input" id="searchInput" placeholder="প্রশ্ন বা ব্যাখ্যা খুঁজুন..." oninput="filterQuestions()">
          </div>

          <!-- Upload Custom JSON Button -->
          <label class="btn" title="অন্য কোনো অধ্যায়ের JSON ফাইল নির্বাচন করুন">
            <i class="fa-solid fa-file-import"></i> JSON লোড করুন
            <input type="file" id="jsonFileInput" accept=".json" style="display: none;" onchange="handleFileUpload(event)">
          </label>
        </div>

        <div class="tool-btns">
          <button class="btn" id="toggleExpBtn" onclick="toggleExplanations()">
            <i class="fa-solid fa-lightbulb"></i> ব্যাখ্যা <span id="expStatusText">দেখান</span>
          </button>
          <button class="btn btn-outline-danger" onclick="resetAll()">
            <i class="fa-solid fa-rotate-right"></i> রিসেট
          </button>
        </div>
      </div>

      <!-- Live Exam Timer & Stats Bar -->
      <div class="exam-timer-bar" id="examBar">
        <div class="timer-display">
          <i class="fa-solid fa-clock"></i> বাকি সময়: <span id="timeLeft">৫০:০০</span>
        </div>
        <div style="display: flex; align-items: center; gap: 12px;">
          <div class="exam-stats-pill" id="examProgress">উত্তর দেওয়া হয়েছে: ০/১০০</div>
          <button class="btn btn-primary" onclick="submitExam()">
            <i class="fa-solid fa-paper-plane"></i> পরীক্ষা জমা দিন
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Content Layout -->
  <main class="main-layout" id="mainLayout">
    <!-- Questions List -->
    <section class="questions-wrapper" id="questionsContainer"></section>

    <!-- Sidebar Palette (Exam & Navigation) -->
    <aside class="sidebar-palette" id="sidebarPalette">
      <div class="palette-title">
        <span>প্রশ্ন তালিকা (<span id="paletteCount">১০০</span>)</span>
        <span style="font-size: 12px; color: var(--text-muted);" id="answeredCountBadge">উত্তর: ০</span>
      </div>
      <div class="palette-grid" id="paletteGrid"></div>
    </aside>
  </main>

  <!-- Score Modal -->
  <div class="modal-backdrop" id="scoreModal">
    <div class="score-card">
      <div class="score-badge"><i class="fa-solid fa-award"></i></div>
      <h2>পরীক্ষার ফলাফল</h2>
      <p style="color: var(--text-muted); font-size: 14px;" id="scoreSummaryText">অধ্যায়- ঘ. লজিক সার্কিট ও গেটস</p>
      
      <div class="score-grid">
        <div class="score-box correct-box">
          <div class="score-val" id="correctScore">০</div>
          <div class="score-lbl">সঠিক</div>
        </div>
        <div class="score-box wrong-box">
          <div class="score-val" id="wrongScore">০</div>
          <div class="score-lbl">ভুল</div>
        </div>
        <div class="score-box unanswered-box">
          <div class="score-val" id="unansweredScore">১০০</div>
          <div class="score-lbl">অনুত্তরিত</div>
        </div>
      </div>

      <div style="margin-bottom: 20px; font-size: 15px; font-weight: 600; color: #1e293b;">
        মোট প্রাপ্ত নম্বর: <span id="finalScore" style="color: var(--primary); font-size: 20px;">০</span> / <span id="totalPossibleMarks">১০০</span> 
        (<span id="percentScore">০%</span>)
      </div>

      <div style="display: flex; gap: 10px; justify-content: center;">
        <button class="btn btn-primary" onclick="closeScoreModal(true)">
          <i class="fa-solid fa-eye"></i> উত্তর ও ব্যাখ্যা পর্যালোচনা
        </button>
        <button class="btn" onclick="retakeExam()">
          <i class="fa-solid fa-arrow-rotate-left"></i> আবার পরীক্ষা দিন
        </button>
      </div>
    </div>
  </div>

  <script>
    // Embedded Datasets with Topics for Ch1, Ch2, Ch3, Ch4
    const DATASETS = __EMBEDDED_DATASETS__;

    const bnDigits = ['০','১','২','৩','৪','৫','৬','৭','৮','৯'];
    function toBn(num) {
      return String(num).replace(/\\d/g, d => bnDigits[d]);
    }

    const optMap = ['ক', 'খ', 'গ', 'ঘ'];
    let currentQuestions = [...DATASETS.ch7.questions];
    let userAnswers = {}; // { qId: selectedOptionIndex }
    let currentMode = 'practice'; // 'practice' | 'exam' | 'review'
    let showExplanations = false;
    let selectedTopic = 'all';
    let timerInterval = null;
    let secondsLeft = 50 * 60;

    // Init App
    window.addEventListener('DOMContentLoaded', () => {
      onChapterChange();
    });

    function onChapterChange() {
      const sel = document.getElementById('chapterSelect').value;
      if (sel === 'ch1') {
        currentQuestions = [...DATASETS.ch1.questions];
        document.getElementById('scoreSummaryText').textContent = DATASETS.ch1.title;
      } else if (sel === 'ch2') {
        currentQuestions = [...DATASETS.ch2.questions];
        document.getElementById('scoreSummaryText').textContent = DATASETS.ch2.title;
      } else if (sel === 'ch3') {
        currentQuestions = [...DATASETS.ch3.questions];
        document.getElementById('scoreSummaryText').textContent = DATASETS.ch3.title;
      } else if (sel === 'ch4') {
        currentQuestions = [...DATASETS.ch4.questions];
        document.getElementById('scoreSummaryText').textContent = DATASETS.ch4.title;
      } else if (sel === 'ch5') {
        currentQuestions = [...DATASETS.ch5.questions];
        document.getElementById('scoreSummaryText').textContent = DATASETS.ch5.title;
      } else if (sel === 'ch6') {
        currentQuestions = [...DATASETS.ch6.questions];
        document.getElementById('scoreSummaryText').textContent = DATASETS.ch6.title;
      } else if (sel === 'ch7') {
        currentQuestions = [...DATASETS.ch7.questions];
        document.getElementById('scoreSummaryText').textContent = DATASETS.ch7.title;
      } else if (sel === 'all7') {
        currentQuestions = [
          ...DATASETS.ch1.questions.map(q => ({...q, id: q.id})),
          ...DATASETS.ch2.questions.map(q => ({...q, id: q.id + 100})),
          ...DATASETS.ch3.questions.map(q => ({...q, id: q.id + 200})),
          ...DATASETS.ch4.questions.map(q => ({...q, id: q.id + 300})),
          ...DATASETS.ch5.questions.map(q => ({...q, id: q.id + 400})),
          ...DATASETS.ch6.questions.map(q => ({...q, id: q.id + 500})),
          ...DATASETS.ch7.questions.map(q => ({...q, id: q.id + 600})),
        ];
        document.getElementById('scoreSummaryText').textContent = 'NTRCA 313 & 325 সম্পূর্ণ সিলেবাস গ্র্যান্ড ফাইনাল মডেল টেস্ট (৭০০ প্রশ্ন)';
      }

      userAnswers = {};
      selectedTopic = 'all';
      populateTopics();
      secondsLeft = Math.ceil(currentQuestions.length * 0.5) * 60;
      renderQuestions();
      renderPalette();
      if (currentMode === 'exam') startTimer();
    }

    function populateTopics() {
      const topicSelect = document.getElementById('topicSelect');
      const counts = {};
      currentQuestions.forEach(q => {
        const t = q.topic || 'সাধারণ';
        counts[t] = (counts[t] || 0) + 1;
      });

      let options = `<option value="all">সকল টপিক (মোট ${toBn(currentQuestions.length)}টি)</option>`;
      for (const [topic, count] of Object.entries(counts)) {
        options += `<option value="${topic}">${topic} (${toBn(count)}টি)</option>`;
      }
      topicSelect.innerHTML = options;
      topicSelect.value = 'all';
    }

    function onTopicFilterChange() {
      selectedTopic = document.getElementById('topicSelect').value;
      renderQuestions();
      renderPalette();
    }

    function filterByTopicBadge(topic) {
      const topicSelect = document.getElementById('topicSelect');
      if (topicSelect) {
        topicSelect.value = topic;
        selectedTopic = topic;
        renderQuestions();
        renderPalette();
        window.scrollTo({ top: 120, behavior: 'smooth' });
      }
    }

    function setMode(mode) {
      currentMode = mode;
      document.getElementById('tabPractice').classList.toggle('active', mode === 'practice');
      document.getElementById('tabExam').classList.toggle('active', mode === 'exam');
      
      const examBar = document.getElementById('examBar');
      if (mode === 'exam') {
        examBar.style.display = 'flex';
        showExplanations = false;
        document.getElementById('toggleExpBtn').style.display = 'none';
        startTimer();
      } else {
        examBar.style.display = 'none';
        document.getElementById('toggleExpBtn').style.display = 'inline-flex';
        stopTimer();
      }
      renderQuestions();
      renderPalette();
    }

    function toggleExplanations() {
      showExplanations = !showExplanations;
      document.getElementById('expStatusText').textContent = showExplanations ? 'লুকান' : 'দেখান';
      renderQuestions();
    }

    function getFilteredQuestions() {
      const searchQuery = document.getElementById('searchInput').value.trim().toLowerCase();
      return currentQuestions.filter(q => {
        const matchesTopic = (selectedTopic === 'all') || (q.topic === selectedTopic);
        if (!matchesTopic) return false;
        if (!searchQuery) return true;
        return q.question.toLowerCase().includes(searchQuery) ||
               (q.topic && q.topic.toLowerCase().includes(searchQuery)) ||
               q.options.some(opt => opt.toLowerCase().includes(searchQuery)) ||
               (q.explanation && q.explanation.toLowerCase().includes(searchQuery));
      });
    }

    function renderQuestions() {
      const container = document.getElementById('questionsContainer');
      const filtered = getFilteredQuestions();

      if (filtered.length === 0) {
        container.innerHTML = '<div style="text-align:center; padding:50px 20px; color:#64748b; background:#fff; border-radius:10px; border:1px solid #e2e8f0;"><i class="fa-solid fa-magnifying-glass" style="font-size:28px; margin-bottom:10px; color:#94a3b8; display:block;"></i>এই ফিল্টারে কোনো প্রশ্ন পাওয়া যায়নি।</div>';
        return;
      }

      container.innerHTML = filtered.map(q => {
        const userSelected = userAnswers[q.id];
        const correctIndex = optMap.indexOf(q.answer);

        let optionsHtml = q.options.map((opt, idx) => {
          let btnClass = 'opt-btn';
          if (currentMode === 'practice' || currentMode === 'review') {
            if (userSelected !== undefined) {
              if (idx === correctIndex) {
                btnClass += ' correct';
              } else if (idx === userSelected) {
                btnClass += ' wrong';
              }
            }
          } else if (currentMode === 'exam') {
            if (userSelected === idx) {
              btnClass += ' selected';
            }
          }

          return `
            <button class="${btnClass}" onclick="selectOption(${q.id}, ${idx})">
              <span class="opt-prefix">${optMap[idx]}</span>
              <span>${opt}</span>
            </button>
          `;
        }).join('');

        let expHtml = '';
        if ((showExplanations || currentMode === 'review') && q.explanation) {
          expHtml = `
            <div class="explanation-box">
              <strong><i class="fa-solid fa-circle-check"></i> সঠিক উত্তর: ${q.answer} • সমাধান ও ব্যাখ্যা:</strong>
              <div>${q.explanation}</div>
            </div>
          `;
        }

        const topicBadge = q.topic ? `
          <span class="q-topic-badge" onclick="filterByTopicBadge('${q.topic}')" title="টপিক অনুযায়ী ফিল্টার করতে ক্লিক করুন">
            <i class="fa-solid fa-tag"></i> ${q.topic}
          </span>
        ` : '';

        return `
          <article class="question-card" id="q-card-${q.id}">
            <div class="q-meta-bar">
              <span class="q-num"><i class="fa-solid fa-circle-question"></i> প্রশ্ন ${toBn(q.id)}</span>
              ${topicBadge}
            </div>
            <div class="q-title">${q.question}</div>
            <div class="options-grid">${optionsHtml}</div>
            ${expHtml}
          </article>
        `;
      }).join('');

      updateProgress();
    }

    function selectOption(qId, optIdx) {
      if (currentMode === 'review') return;
      userAnswers[qId] = optIdx;
      renderQuestions();
      renderPalette();
    }

    function renderPalette() {
      const grid = document.getElementById('paletteGrid');
      const filtered = getFilteredQuestions();

      grid.innerHTML = filtered.map(q => {
        const answered = userAnswers[q.id] !== undefined;
        let pClass = 'palette-item';
        if (currentMode === 'review') {
          const correctIndex = optMap.indexOf(q.answer);
          if (userAnswers[q.id] === correctIndex) pClass += ' correct';
          else if (userAnswers[q.id] !== undefined) pClass += ' wrong';
        } else if (answered) {
          pClass += ' answered';
        }

        return `
          <div class="${pClass}" onclick="scrollToQuestion(${q.id})">
            ${toBn(q.id)}
          </div>
        `;
      }).join('');

      document.getElementById('paletteCount').textContent = toBn(filtered.length);
      const totalAns = Object.keys(userAnswers).length;
      document.getElementById('answeredCountBadge').textContent = `উত্তর: ${toBn(totalAns)}`;
    }

    function scrollToQuestion(id) {
      const el = document.getElementById(`q-card-${id}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    function updateProgress() {
      const answered = Object.keys(userAnswers).length;
      const total = currentQuestions.length;
      const p = document.getElementById('examProgress');
      if (p) {
        p.textContent = `উত্তর দেওয়া হয়েছে: ${toBn(answered)}/${toBn(total)}`;
      }
    }

    function startTimer() {
      stopTimer();
      secondsLeft = 50 * 60;
      updateTimerDisplay();
      timerInterval = setInterval(() => {
        secondsLeft--;
        updateTimerDisplay();
        if (secondsLeft <= 0) {
          stopTimer();
          alert('পরীক্ষার নির্ধারিত সময় শেষ হয়েছে!');
          submitExam();
        }
      }, 1000);
    }

    function stopTimer() {
      if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
      }
    }

    function updateTimerDisplay() {
      const m = Math.floor(secondsLeft / 60);
      const s = secondsLeft % 60;
      const fmt = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
      document.getElementById('timeLeft').textContent = toBn(fmt);
    }

    function submitExam() {
      stopTimer();
      let correct = 0;
      let wrong = 0;
      let unanswered = 0;

      const activeQList = getFilteredQuestions();

      activeQList.forEach(q => {
        const userChoice = userAnswers[q.id];
        const correctIndex = optMap.indexOf(q.answer);
        if (userChoice === undefined) {
          unanswered++;
        } else if (userChoice === correctIndex) {
          correct++;
        } else {
          wrong++;
        }
      });

      const netScore = Math.max(0, correct - (wrong * 0.25));
      const percent = Math.round((correct / activeQList.length) * 100);

      document.getElementById('correctScore').textContent = toBn(correct);
      document.getElementById('wrongScore').textContent = toBn(wrong);
      document.getElementById('unansweredScore').textContent = toBn(unanswered);
      document.getElementById('finalScore').textContent = toBn(netScore.toFixed(2));
      document.getElementById('totalPossibleMarks').textContent = toBn(activeQList.length);
      document.getElementById('percentScore').textContent = `${toBn(percent)}%`;

      document.getElementById('scoreModal').style.display = 'flex';
    }

    function closeScoreModal(goToReview = false) {
      document.getElementById('scoreModal').style.display = 'none';
      if (goToReview) {
        currentMode = 'review';
        showExplanations = true;
        renderQuestions();
        renderPalette();
      }
    }

    function retakeExam() {
      closeScoreModal();
      userAnswers = {};
      setMode('exam');
    }

    function resetAll() {
      if (confirm('আপনি কি সমস্ত উত্তর মুছে নতুন করে শুরু করতে চান?')) {
        userAnswers = {};
        if (currentMode === 'exam') startTimer();
        renderQuestions();
        renderPalette();
      }
    }

    function filterQuestions() {
      renderQuestions();
      renderPalette();
    }

    function handleFileUpload(event) {
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const data = JSON.parse(e.target.result);
          if (Array.isArray(data) && data.length > 0 && data[0].question) {
            currentQuestions = data;
            userAnswers = {};
            selectedTopic = 'all';
            document.getElementById('scoreSummaryText').textContent = file.name;
            populateTopics();
            secondsLeft = Math.ceil(data.length * 0.5) * 60;
            alert(`সফলভাবে ${toBn(data.length)}টি প্রশ্ন লোড করা হয়েছে!`);
            renderQuestions();
            renderPalette();
          } else {
            alert('ভুল ফাইল ফরম্যাট! প্রশ্ন সমৃদ্ধ বৈধ JSON ফাইল নির্বাচন করুন।');
          }
        } catch (err) {
          alert('JSON ফাইলটি পড়া সম্ভব হয়নি: ' + err.message);
        }
      };
      reader.readAsText(file);
    }
  </script>
</body>
</html>
"""

# Embed datasets
datasets_json = json.dumps(all_datasets, ensure_ascii=False)
final_html = html_template.replace("__EMBEDDED_DATASETS__", datasets_json)

# Output paths
output_files = [
    r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\NTRCA-313-and-325-AI-Exam.html",
    r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini\index.html"
]

for out_path in output_files:
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)

print("HTML apps updated successfully with Chapters 1, 2, 3 & 4.")
