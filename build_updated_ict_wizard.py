# -*- coding: utf-8 -*-
import json
import os
import re

base_dir = r"c:\Users\bdCalling\Downloads\Mosabber\json -genarate-by-gemini"
json_dir = os.path.join(base_dir, "JSON Data", "NTRCA 313 and 325 - AI")

def to_bn(num):
    bn_digits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
    return ''.join(bn_digits[int(d)] if d.isdigit() else d for d in str(num))

# Load 7 Chapters
chapter_files = [
    ("ch1", "অধ্যায়- ক. কম্পিউটার বেসিক", "ক. কম্পিউটার বেসিক", "অধ্যায়- ক. কম্পিউটার বেসিক.json"),
    ("ch2", "অধ্যায়- খ. সংখ্যা পদ্ধতি", "খ. সংখ্যা পদ্ধতি", "অধ্যায়- খ. সংখ্যা পদ্ধতি.json"),
    ("ch3", "অধ্যায়- গ. উপাত্ত উপস্থাপন", "গ. উপাত্ত উপস্থাপন", "অধ্যায়- গ. উপাত্ত উপস্থাপন.json"),
    ("ch4", "অধ্যায়- ঘ. লজিক সার্কিট-বর্তনী", "ঘ. লজিক সার্কিট-বর্তনী", "অধ্যায়- ঘ. লজিক সার্কিট-বর্তনী.json"),
    ("ch5", "অধ্যায়- ঙ. অপারেটিং পদ্ধতি", "ঙ. অপারেটিং পদ্ধতি", "অধ্যায়- ঙ. অপারেটিং পদ্ধতি.json"),
    ("ch6", "অধ্যায়- চ. এলগোরিদম এবং ফ্লো চার্ট", "চ. এলগোরিদম এবং ফ্লো চার্ট", "অধ্যায়- চ. এলগোরিদম এবং ফ্লো চার্ট.json"),
    ("ch7", "অধ্যায়- ছ. ইন্টারনেট", "ছ. ইন্টারনেট", "অধ্যায়- ছ. ইন্টারনেট.json"),
]

chapters_data = []
total_questions = 0

for ch_id, title, short_title, fname in chapter_files:
    fpath = os.path.join(json_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        q_list = json.load(f)
    chapters_data.append({
        "id": ch_id,
        "title": title,
        "short": short_title,
        "count": len(q_list),
        "questions": q_list
    })
    total_questions += len(q_list)

bn_total = to_bn(total_questions)
print(f"Loaded {len(chapters_data)} chapters, total {total_questions} questions.")

# Read original HTML from pdf-image-convert-to-Json
source_html_path = r"c:\Users\bdCalling\Downloads\Mosabber\pdf-image-convert-to-Json\Ict-wizard-NTRCA-313-and-325.html"
with open(source_html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add CSS for topic-pill-badge
topic_badge_css = """
    /* Topic Pill Badge on Question Cards */
    .topic-pill-badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 11px;
      font-weight: 600;
      color: #1d4ed8;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-radius: 4px;
      padding: 1px 7px;
      margin-left: 8px;
      vertical-align: middle;
      white-space: nowrap;
    }
    .topic-pill-badge i {
      font-size: 10px;
      color: #3b82f6;
    }
    @media print {
      .topic-pill-badge {
        background: transparent !important;
        border: 1px solid #94a3b8 !important;
        color: #334155 !important;
      }
    }
"""

if ".topic-pill-badge" not in html:
    html = html.replace("</style>", topic_badge_css + "\n  </style>", 1)

# 2. Update Header Subtitle question count to Bengali 700
html = html.replace("৫৯৪টি প্রশ্ন", f"{bn_total}টি প্রশ্ন")
html = html.replace("formatNumber(594)", f"formatNumber({total_questions})")

# Set Noto Sans as Default Font
# A. In CSS
html = html.replace(
    "font-family: 'Hind Siliguri', 'Inter',",
    "font-family: 'Noto Sans Bengali', 'Inter',"
)

# B. In fontSelect dropdown (mark noto-sans as selected)
html = html.replace('<option value="noto-sans">', '<option value="noto-sans" selected>')


# C. In JS default state
html = html.replace("let savedFont = 'hind';", "let savedFont = 'noto-sans';")
html = html.replace("|| 'hind';", "|| 'noto-sans';")

# D. Remove background colors and borders on hover and click for options (Keep only text colors)
old_option_states_css = """    /* Practice Mode Option Interaction */
    body.practice-mode .option-cell {
      cursor: pointer;
      user-select: none;
    }

    body.practice-mode .option-cell:hover {
      background-color: #f1f5f9;
      border-color: #cbd5e1;
    }

    .option-cell.practice-correct {
      background-color: var(--success-light) !important;
      border-color: var(--success) !important;
    }

    .option-cell.practice-correct .opt-label,
    .option-cell.practice-correct .opt-text {
      color: #15803d !important;
      font-weight: 600;
    }

    .option-cell.practice-wrong {
      background-color: var(--danger-light) !important;
      border-color: var(--danger) !important;
    }

    .option-cell.practice-wrong .opt-label,
    .option-cell.practice-wrong .opt-text {
      color: #b91c1c !important;
    }

    .option-cell.practice-revealed {
      background-color: #ecfdf5 !important;
      border: 1px dashed var(--success) !important;
    }

    .option-cell.practice-revealed .opt-label,
    .option-cell.practice-revealed .opt-text {
      color: #15803d !important;
      font-weight: 600;
    }

    /* Show Answers Highlighting */
    .show-answers .option-cell.is-correct {
      background-color: #f0fdf4;
      border-color: #86efac;
    }

    .show-answers .option-cell.is-correct .opt-label,
    .show-answers .option-cell.is-correct .opt-text {
      color: #166534;
      font-weight: 600;
    }"""

new_option_states_css = """    /* Practice Mode Option Interaction - Cursor pointer ONLY before answering */
    body.practice-mode .question-block:not(.practice-answered) .option-cell {
      cursor: pointer;
      user-select: none;
    }
    body.practice-mode .question-block.practice-answered .option-cell {
      cursor: default;
      user-select: text;
    }

    /* Option Hover State: NO background, NO border, ONLY color change, and ONLY before answering */
    body.practice-mode .question-block:not(.practice-answered) .option-cell:hover {
      background-color: transparent !important;
      background: transparent !important;
      border: none !important;
      outline: none !important;
      box-shadow: none !important;
    }
    body.practice-mode .question-block:not(.practice-answered) .option-cell:hover .opt-label,
    body.practice-mode .question-block:not(.practice-answered) .option-cell:hover .opt-text {
      color: var(--primary) !important;
    }

    /* Once an option is chosen, hovering over any option of this question causes NO color or border change */
    body.practice-mode .question-block.practice-answered .option-cell:hover {
      background-color: transparent !important;
      background: transparent !important;
      border: none !important;
      outline: none !important;
      box-shadow: none !important;
    }

    .option-cell.practice-correct {
      background-color: transparent !important;
      background: transparent !important;
      border: none !important;
      outline: none !important;
      box-shadow: none !important;
    }

    .option-cell.practice-correct .opt-label,
    .option-cell.practice-correct .opt-text {
      color: #15803d !important;
      font-weight: 700;
    }

    .option-cell.practice-wrong {
      background-color: transparent !important;
      background: transparent !important;
      border: none !important;
      outline: none !important;
      box-shadow: none !important;
    }

    .option-cell.practice-wrong .opt-label,
    .option-cell.practice-wrong .opt-text {
      color: #b91c1c !important;
      font-weight: 700;
    }

    .option-cell.practice-revealed {
      background-color: transparent !important;
      background: transparent !important;
      border: none !important;
      outline: none !important;
      box-shadow: none !important;
    }

    .option-cell.practice-revealed .opt-label,
    .option-cell.practice-revealed .opt-text {
      color: #15803d !important;
      font-weight: 700;
    }

    /* Show Answers Highlighting: No background, no border, only color */
    .show-answers .option-cell.is-correct {
      background-color: transparent !important;
      background: transparent !important;
      border: none !important;
      outline: none !important;
      box-shadow: none !important;
    }

    .show-answers .option-cell.is-correct .opt-label,
    .show-answers .option-cell.is-correct .opt-text {
      color: #166534 !important;
      font-weight: 700;
    }"""

html = html.replace(old_option_states_css, new_option_states_css)
html = html.replace(old_option_states_css.replace('\n', '\r\n'), new_option_states_css.replace('\n', '\r\n'))

# Remove border from base .option-cell
html = html.replace("border: 1px solid transparent;", "border: none !important;")

# Lock option click once chosen
old_click_handler = """        // Click handler for practice mode
        cell.onclick = () => {
          if (!isPracticeMode) return;
          practiceAnswers[q.uid] = optIdx;
          render();
        };"""

new_click_handler = """        // Click handler for practice mode: locked once chosen
        cell.onclick = () => {
          if (!isPracticeMode) return;
          if (selectedIndex !== undefined) return;
          practiceAnswers[q.uid] = optIdx;
          render();
        };"""

html = html.replace(old_click_handler, new_click_handler)
html = html.replace(old_click_handler.replace('\n', '\r\n'), new_click_handler.replace('\n', '\r\n'))



# 3. Add Topic Filter in HTML markup
topic_filter_html = """
        <!-- Dynamic Topic Filter Dropdown -->
        <div class="select-wrap" id="topicSelectWrap">
          <select id="topicSelect" aria-label="টপিক নির্বাচন করুন">
            <option value="all">সকল টপিক</option>
          </select>
          <span class="select-arrow"><i class="fa-solid fa-chevron-down"></i></span>
        </div>
"""

# Place topic filter right next to chapterSelect
marker1 = '</div>\n\n        <div class="search-wrap">'
marker2 = '</div>\r\n\r\n        <div class="search-wrap">'

if marker1 in html:
    html = html.replace(marker1, '</div>\n' + topic_filter_html + '\n        <div class="search-wrap">', 1)
elif marker2 in html:
    html = html.replace(marker2, '</div>\r\n' + topic_filter_html + '\r\n        <div class="search-wrap">', 1)
else:
    # fallback insertion after chapterSelect select-wrap
    idx = html.find('id="chapterSelect"')
    wrap_end = html.find('</div>', idx) + 6
    html = html[:wrap_end] + '\n' + topic_filter_html + html[wrap_end:]

# 4. Replace chaptersData in JavaScript using exact slice (NO regex escape issues)
chapters_json_str = json.dumps(chapters_data, ensure_ascii=False)
ch_start = html.find("const chaptersData = [")
app_state = html.find("// Application State", ch_start)
if ch_start != -1 and app_state != -1:
    html = html[:ch_start] + f"const chaptersData = {chapters_json_str};\n\n    " + html[app_state:]
else:
    print("Warning: Could not locate chaptersData slice boundaries!")

# 5. Add currentTopic to Application State
html = html.replace(
    "let currentChapter = 'all';",
    "let currentChapter = 'all';\n    let currentTopic = 'all';"
)

# 6. Add updateTopicOptions function and update selectChapter
topic_js_logic = """
    // Dynamically update topic options based on current chapter
    function updateTopicOptions() {
      const topicSelect = document.getElementById('topicSelect');
      if (!topicSelect) return;
      topicSelect.innerHTML = '';

      let activeQuestions = [];
      if (currentChapter === 'all') {
        chaptersData.forEach(ch => activeQuestions.push(...ch.questions));
      } else {
        const ch = chaptersData.find(c => c.id === currentChapter);
        if (ch) activeQuestions.push(...ch.questions);
      }

      const topicCounts = {};
      activeQuestions.forEach(q => {
        if (q.topic) {
          topicCounts[q.topic] = (topicCounts[q.topic] || 0) + 1;
        }
      });

      const allOpt = document.createElement('option');
      allOpt.value = 'all';
      allOpt.textContent = `সকল টপিক (${formatNumber(activeQuestions.length)}টি)`;
      topicSelect.appendChild(allOpt);

      Object.keys(topicCounts).forEach(top => {
        const opt = document.createElement('option');
        opt.value = top;
        opt.textContent = `${top} (${formatNumber(topicCounts[top])}টি)`;
        if (top === currentTopic) opt.selected = true;
        topicSelect.appendChild(opt);
      });

      if (currentTopic !== 'all' && !topicCounts[currentTopic]) {
        currentTopic = 'all';
        topicSelect.value = 'all';
      } else {
        topicSelect.value = currentTopic;
      }
    }
"""

# Insert updateTopicOptions right before selectChapter
html = html.replace("function selectChapter(chId, save = true) {", topic_js_logic + "\n    function selectChapter(chId, save = true) {", 1)

# In selectChapter, reset currentTopic and call updateTopicOptions()
html = html.replace(
    "function selectChapter(chId, save = true) {\n      currentChapter = chId;",
    "function selectChapter(chId, save = true) {\n      currentChapter = chId;\n      currentTopic = 'all';\n      updateTopicOptions();"
)
html = html.replace(
    "function selectChapter(chId, save = true) {\r\n      currentChapter = chId;",
    "function selectChapter(chId, save = true) {\r\n      currentChapter = chId;\r\n      currentTopic = 'all';\r\n      updateTopicOptions();"
)

# In initUI(), initialize topicSelect listener and updateTopicOptions()
init_ui_search1 = "chSelect.addEventListener('change', (e) => selectChapter(e.target.value));"
init_ui_replace1 = """chSelect.addEventListener('change', (e) => selectChapter(e.target.value));

      // Topic Select Event Listener
      const topicSelectEl = document.getElementById('topicSelect');
      if (topicSelectEl) {
        topicSelectEl.addEventListener('change', (e) => {
          currentTopic = e.target.value;
          currentPage = 1;
          render();
        });
      }
      updateTopicOptions();"""

html = html.replace(init_ui_search1, init_ui_replace1, 1)

# 7. Update getFilteredQuestions() to filter by currentTopic and search topic
old_filter_code1 = """      if (searchQuery) {
        list = list.filter(q => {
          const qMatch = q.question.toLowerCase().includes(searchQuery);
          const optMatch = q.options.some(opt => opt.toLowerCase().includes(searchQuery));
          const expMatch = q.explanation ? q.explanation.toLowerCase().includes(searchQuery) : false;
          return qMatch || optMatch || expMatch;
        });
      }"""

old_filter_code2 = old_filter_code1.replace('\n', '\r\n')

new_filter_code = """      // Filter by Topic (if selected)
      if (currentTopic && currentTopic !== 'all') {
        list = list.filter(q => q.topic === currentTopic);
      }

      if (searchQuery) {
        list = list.filter(q => {
          const qMatch = q.question.toLowerCase().includes(searchQuery);
          const optMatch = q.options.some(opt => opt.toLowerCase().includes(searchQuery));
          const expMatch = q.explanation ? q.explanation.toLowerCase().includes(searchQuery) : false;
          const topMatch = q.topic ? q.topic.toLowerCase().includes(searchQuery) : false;
          return qMatch || optMatch || expMatch || topMatch;
        });
      }"""

if old_filter_code1 in html:
    html = html.replace(old_filter_code1, new_filter_code, 1)
elif old_filter_code2 in html:
    html = html.replace(old_filter_code2, new_filter_code, 1)

# 8. Update createQuestionNode to display topic badge
old_title_code1 = """      titleDiv.appendChild(qNumSpan);
      titleDiv.appendChild(qTextSpan);
      qBox.appendChild(titleDiv);"""

old_title_code2 = old_title_code1.replace('\n', '\r\n')

new_title_code = """      titleDiv.appendChild(qNumSpan);
      titleDiv.appendChild(qTextSpan);

      if (q.topic) {
        const topicSpan = document.createElement('span');
        topicSpan.className = 'topic-pill-badge';
        topicSpan.innerHTML = `<i class=\"fa-solid fa-tag\"></i> ${q.topic}`;
        titleDiv.appendChild(topicSpan);
      }

      qBox.appendChild(titleDiv);"""

if old_title_code1 in html:
    html = html.replace(old_title_code1, new_title_code, 1)
elif old_title_code2 in html:
    html = html.replace(old_title_code2, new_title_code, 1)

# 9. Update statsInfo in render() to show topic info
html = re.sub(
    r"statsInfo\.innerHTML = `মোট প্রশ্ন: <strong>\$\{formatNumber\(\d+\)\}</strong> টি \| প্রদর্শিত: <strong>\$\{formatNumber\(totalInView\)\}</strong> টি` \+\s*[\r\n]+\s*\(currentChapter !== 'all' \? ` \| <span>অধ্যায়: \$\{chaptersData\.find\(c=>c\.id===currentChapter\)\?\.short\}</span>` : ''\);",
    f"statsInfo.innerHTML = `মোট প্রশ্ন: <strong>${{formatNumber({total_questions})}}</strong> টি | প্রদর্শিত: <strong>${{formatNumber(totalInView)}}</strong> টি` + (currentChapter !== 'all' ? ` | <span>অধ্যায়: ${{chaptersData.find(c=>c.id===currentChapter)?.short}}</span>` : '') + (currentTopic !== 'all' ? ` | <span>টপিক: ${{currentTopic}}</span>` : '');",
    html
)

# Output files
targets = [
    os.path.join(base_dir, "index.html"),
    os.path.join(base_dir, "NTRCA-313-and-325-AI-Exam.html")
]

for t in targets:
    with open(t, "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully written:", os.path.basename(t), f"({len(html)} bytes)")
