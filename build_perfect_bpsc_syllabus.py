# -*- coding: utf-8 -*-
"""
Generate the finalized, 100% complete BPSC Technical AI Syllabus file: 'BPSC technical syllabus.txt'
Deeply incorporating all 7 Semesters of BTEB Diploma in Computer Science & Technology Probidhan-2022
including:
- 1st Sem: 28511 Computer Office Application, 26711 Basic Electricity, 25911 Math-I
- 2nd Sem: 28521 Python, 28522 Graphics-I, 26811 Basic Electronics, 25921 Math-II
- 3rd Sem: 28531 Python App Dev, 28532 Graphics-II, 28533 IT Support, 26831 Digital Electronics-I, 25931 Math-III
- 4th Sem: 28541 Java, 28542 DSA, 28543 Computer Peripherals, 28544 Web-I, 26841 Digital Electronics-II
- 5th Sem: 28551 Java App Dev, 28552 Web-II, 28553 Comp Architecture & Microprocessor, 28554 Data Comm, 28555 OS
- 6th Sem: 28561 DBMS, 28562 Networking, 28563 Sensor & IoT, 28564 Microcontroller 8051, 28565 Surveillance Security, 25852 Industrial Mgmt
- 7th Sem: 28571 Digital Marketing, 28572 Network Admin & Linux, 28573 Cyber Security, 28574 Apps Development (Android/Kotlin), 28575 Multimedia & Animation, 65853 Innovation & Entrepreneurship
"""

import sys

# Read the current content
with open("BPSC technical syllabus.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the header and Table of Contents
old_toc = """--- প্রবিধান-২০২২ এর অতিরিক্ত বিশেষায়িত বিষয়সমূহ (ADDITIONAL SPECIALIZED SUBJECTS) ---
২১. সেন্সর ও ইন্টারনেট অব থিংস (Sensor & IoT System) [কোড: ২৮৫৬৩]
২২. কম্পিউটার পেরিফেরালস ও ইন্টারফেসিং (Computer Peripherals & Interfacing) [কোড: ২৮৫৪৩]
২৩. মাল্টিমিডিয়া, অ্যানিমেশন ও গ্রাফিক্স ডিজাইন (Graphics Design-I, II & Multimedia) [কোড: ২৮৫২২, ২৮৫৩২, ২৮৫৭৫]
২৪. ডিজিটাল মার্কেটিং টেকনিক ও ইন্ডাস্ট্রিয়াল ম্যানেজমেন্ট [কোড: ২৫৮৫১, ২৫৮৫২, ২৮৫৭১]"""

new_toc = """--- প্রবিধান-২০২২ এর অতিরিক্ত বিশেষায়িত বিষয়সমূহ (ADDITIONAL SPECIALIZED SUBJECTS) ---
২১. সেন্সর ও ইন্টারনেট অব থিংস (Sensor & IoT System) [কোড: ২৮৫৬৩]
২২. কম্পিউটার পেরিফেরালস ও ইন্টারফেসিং (Computer Peripherals & Interfacing) [কোড: ২৮৫৪৩]
২৩. মাল্টিমিডিয়া, অ্যানিমেশন ও গ্রাফিক্স ডিজাইন (Graphics Design-I, II & Multimedia) [কোড: ২৮৫২২, ২৮৫৩২, ২৮৫৭৫]
২৪. মোবাইল অ্যাপ্লিকেশন ডেভেলপমেন্ট (Mobile Application Development - Android & Kotlin) [কোড: ২৮৫৭৪]
২৫. ডিজিটাল মার্কেটিং টেকনিক ও ইন্ডাস্ট্রিয়াল ম্যানেজমেন্ট [কোড: ২৫৮৫১, ২৫৮৫২, ২৮৫৭১, ৬৫৮৫৩]"""

content = content.replace(old_toc, new_toc)

# Also update the metadata count at the top
content = content.replace(
    "মোট অধ্যায় / বিষয় সংখ্যা: ২০টি প্রধান বিষয় + ৪টি বিশেষায়িত সংযুক্ত বিষয়",
    "মোট অধ্যায় / বিষয় সংখ্যা: ২০টি প্রধান বিষয় + ৫টি বিশেষায়িত সংযুক্ত বিষয় (সর্বমোট ২৫টি বিষয়)"
)

# 2. Add Chapter 19.9 to Subject 19 for 25931 (Algebra, Conics, Mensuration & Differential Equations)
math_3_addition = r"""
অধ্যায় ১৯.৯: বীজগণিত, কনিক্স, পরিমিতি ও ডিফারেনশিয়াল সমীকরণ (Algebra, Conics & Mensuration - BTEB 25931)
   - আংশিক ভগ্নাংশ (Partial Fractions): লিনিয়ার ফ্যাক্টর, পুনরাবৃত্ত ফ্যাক্টর, দ্বিঘাত ফ্যাক্টর বিশিষ্ট ভগ্নাংশ পৃথকীকরণ।
   - সূচকীয় ধারা (Exponential Series): $e$-এর সংজ্ঞা ও মান ($2 < e < 3$), $e^x = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$ এর প্রমাণ ও সমস্যা সমাধান।
   - দ্বিপদী উপপাদ্য (Binomial Theorem): ধনাত্মক, ঋণাত্মক ও ভগ্নাংশ সূচকের জন্য দ্বিপদী উপপাদ্য, সাধারণ পদ ($T_{r+1} = \binom{n}{r} x^{n-r} y^r$), মধ্যপদ ও $x$-বর্জিত পদ নির্ণয়।
   - জ্যামিতি - বৃত্ত (Circle): বৃত্তের সাধারণ সমীকরণ ($x^2 + y^2 + 2gx + 2fy + c = 0$), কেন্দ্র $(-g, -f)$ ও ব্যাসার্ধ $\sqrt{g^2 + f^2 - c}$, স্পর্শক (Tangent) ও অভিলম্বের (Normal) সমীকরণ।
   - জ্যামিতি - কনিক্স (Conic Sections): কনিকের সংজ্ঞা, ফোকাস (Focus), নিয়ামক (Directrix) ও উৎকেন্দ্রিকতা ($e$):
     * পরাবৃত্ত (Parabola: $e = 1$, সমীকরণ $y^2 = 4ax$, শীর্ষবিন্দু, উপকেন্দ্রিক লম্বের দৈর্ঘ্য $4a$)।
     * উপবৃত্ত (Ellipse: $e < 1$, সমীকরণ $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, উৎকেন্দ্রিকতা $e = \sqrt{1 - b^2/a^2}$)।
     * অধিবৃত্ত (Hyperbola: $e > 1$, সমীকরণ $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$)।
   - পরিমিতি বা মেনসুরেশন (Mensuration):
     * ক্ষেত্রফল: ত্রিভুজ (সমবাহু $\frac{\sqrt{3}}{4}a^2$, সমদ্বিবাহু, বিষমবাহু হেরনের সূত্র), চতুর্ভুজ, সামান্তরিক, রম্বস, ট্রাপিজিয়াম, সুষম বহুভুজ, বৃত্ত, বৃত্তকলা (Sector) ও বৃত্তাংশ (Segment)।
     * তল ও আয়তন: আয়তাকার ঘনবস্তু ও ঘনক (Volume $V = lbh$, Diagonal $d = \sqrt{l^2+b^2+h^2}$), প্রিজম (Prism), সিলিন্ডার বা বেলন ($V = \pi r^2 h$, বক্রতলের ক্ষেত্রফল $2\pi rh$), পিরামিড (Pyramid), শঙ্কু বা কোণ ($V = \frac{1}{3}\pi r^2 h$, হেলানো উচ্চতা $l = \sqrt{r^2+h^2}$), গোলক ($V = \frac{4}{3}\pi r^3$, পৃষ্ঠতলের ক্ষেত্রফল $4\pi r^2$)।
   - সাধারণ ডিফারেনশিয়াল সমীকরণ (Ordinary Differential Equations): প্রথম ক্রম ও প্রথম মাত্রার সমীকরণ, চলক পৃথকীকরণ পদ্ধতি (Separation of Variables), সমমাত্রিক সমীকরণ এবং রৈখিক অন্তরক সমীকরণের ইন্টিগ্রেটিং ফ্যাক্টর ($IF = e^{\int P dx}$)।
"""

if "অধ্যায় ১৯.৯" not in content:
    # insert before Subject 20
    pos_s20 = content.find("----------------------------------------------------------------------------------------------------\nবিষয়- ২০: পূর্ণরূপ")
    if pos_s20 != -1:
        content = content[:pos_s20] + math_3_addition + "\n" + content[pos_s20:]

# 3. Add Subject 24: Apps Development (28574) and update Subject 25: Digital Marketing & Industrial Mgmt
apps_dev_content = r"""----------------------------------------------------------------------------------------------------
বিষয়- ২৪: মোবাইল অ্যাপ্লিকেশন ডেভেলপমেন্ট (Mobile Application Development - Android & Kotlin)
BTEB প্রবিধান-২০২২ সংশ্লিষ্ট কোর্স: Apps Development (28574 - ৭ম সেমিস্টার)
----------------------------------------------------------------------------------------------------
অধ্যায় ২৪.১: অ্যান্ড্রয়েড ও কোটলিন পরিবেশ (Android & Kotlin Environment - BTEB 28574 Unit 1)
   - অ্যান্ড্রয়েড অপারেটিং সিস্টেমের ইতিহাস, আর্কিটেকচার (Linux Kernel, HAL, ART/Dalvik Runtime, Native Libraries, Application Framework, Apps)।
   - কোটলিন (Kotlin) প্রোগ্রামিং ভাষা: বৈশিষ্ট্য, সিনট্যাক্স, ভ্যারিয়েবল (`val` ইমিউটেবল বনাম `var` মিউটেবল), ডেটা টাইপ, নাল-সেফটি (Null Safety: `Nullable ?`, Safe Call `?.`, Elvis Operator `?:`, Not-null assertion `!!`)।
   - কোটলিনে অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং: ক্লাস, অবজেক্ট, প্রাইমারি ও সেকেন্ডারি কনস্ট্রাক্টর, ইনহেরিটেন্স (`open` ক্লাস), ডেটা ক্লাস (`data class`), এক্সটেনশন ফাংশন, ল্যাম্বডা ও হাইয়ার অর্ডার ফাংশন।
   - অ্যান্ড্রয়েড স্টুডিও ও প্রজেক্ট স্ট্রাকচার: Android SDK, Gradle বিল্ড সিস্টেম (`build.gradle` - Project ও Module লেভেল), `AndroidManifest.xml` ফাইলের ভূমিকা, রিসোর্স ফোল্ডার (`res/layout`, `res/values/strings.xml`, `res/drawable`)।
   - ভার্চুয়াল এমুলেটর (AVD) এবং রিয়েল ডিভাইসে ইউএসবি ডিবাগিং (ADB) কনফিগারেশন।

অধ্যায় ২৪.২: অ্যাক্টিভিটি, ফ্র্যাগমেন্ট ও লাইফসাইকেল (Activities, Fragments & Lifecycle - BTEB 28574 Unit 2)
   - অ্যাক্টিভিটি (Activity) এর ধারণা ও স্ক্রিন ম্যানেজমেন্ট।
   - অ্যাক্টিভিটি লাইফসাইকেল মেথডস: `onCreate()`, `onStart()`, `onResume()`, `onPause()`, `onStop()`, `onDestroy()`, `onRestart()` - কখন কোন মেথড কল হয় এবং ব্যাক-স্ট্যাক আচরণ।
   - ফ্র্যাগমেন্ট (Fragment) এর ধারণা (পুনর্ব্যবহারযোগ্য সাব-অ্যাক্টিভিটি UI কম্পোনেন্ট)।
   - ফ্র্যাগমেন্ট লাইফসাইকেল মেথডস: `onAttach()`, `onCreateView()`, `onViewCreated()`, `onDestroyView()`, `onDetach()`।
   - ফ্র্যাগমেন্ট ম্যানেজার ও ট্রানজ্যাকশন: `FragmentManager`, `FragmentTransaction`, রানটাইমে ফ্র্যাগমেন্ট যোগ, প্রতিস্থাপন (`replace`) ও রিমুভ করা।
   - ফ্র্যাগমেন্ট ও অ্যাক্টিভিটির মধ্যে ডেটা আদান-প্রদান (Bundle, ViewModel, Interfaces)।

অধ্যায় ২৪.৩: অ্যান্ড্রয়েড ইউজার ইন্টারফেস ও জেটপ্যাক কম্পোজ (Android UI & Jetpack Compose - BTEB 28574 Unit 3)
   - এক্সএমএল (XML Layout) বনাম কোটলিন প্রোগ্রাম্যাটিক লেআউট এর পার্থক্য।
   - মৌলিক ইউআই উইজেটস: `TextView`, `EditText`, `Button`, `ImageView`, `CheckBox`, `RadioButton`, `RadioGroup`, `Switch`, `Spinner`, `ProgressBar`, `Toast`, `Snackbar`, `AlertDialog`।
   - লেআউট প্রকারভেদ ও বৈশিষ্ট্য:
     * `LinearLayout` (Horizontal ও Vertical ওরিয়েন্টেশন, `layout_weight`)
     * `RelativeLayout` (অন্যান্য ভিউয়ের সাপেক্ষে পজিশনিং)
     * `FrameLayout` (সিঙ্গেল চাইল্ড বা স্ট্যাকিং)
     * `TableLayout` (সারি ও কলাম)
     * `ConstraintLayout` (ফ্ল্যাট ভিউ হায়ারার্কি, অ্যাঙ্কর পয়েন্ট, পারফরম্যান্স বান্ধব আধুনিক লেআউট)।
   - অ্যাডভান্সড স্ক্রোলিং লিস্ট ভিউ:
     * `ListView` ও `GridView` এর সীমাবদ্ধতা।
     * `RecyclerView` আর্কিটেকচার: ভিউ-হোল্ডার প্যাটার্ন (`ViewHolder`), অ্যাডাপ্টার (`RecyclerView.Adapter`), লেআউট ম্যানেজার (`LinearLayoutManager`, `GridLayoutManager`, `StaggeredGridLayoutManager`)।
   - জেটপ্যাক কম্পোজ (Jetpack Compose): অ্যান্ড্রয়েডের আধুনিক ডিক্লারেটিভ ইউআই টুলকিট:
     * কম্পোজেবল ফাংশনস (`@Composable`)
     * স্টেট ম্যানেজমেন্ট (`remember`, `mutableStateOf()`)
     * বেসিক কম্পোজেবলস: `Column`, `Row`, `Box`, `Text`, `Button`, `LazyColumn` (রিসাইক্লার ভিউয়ের সমতুল্য)।

অধ্যায় ২৪.৪: ইনটেন্ট, নেভিগেশন ও ডেটা স্টোরেজ (Intents, Navigation & Storage - BTEB 28574 Units 4 & 5)
   - ইনটেন্ট (Intent) এর সংজ্ঞা ও প্রকারভেদ:
     * এক্সপ্লিসিট ইনটেন্ট (Explicit Intent - নির্দিষ্ট অ্যাক্টিভিটি লঞ্চ করা, যেমন `Intent(this, SecondActivity::class.java)`)।
     * ইমপ্লিসিট ইনটেন্ট (Implicit Intent - সিস্টেমের অন্যান্য অ্যাপ দিয়ে অ্যাকশন সম্পাদন, যেমন ওয়েবপেজ ওপেন, ফোন ডায়াল, মেইল সেন্ড, ক্যামেরা লঞ্চ)।
     * ইনটেন্ট ফিল্টার (`<intent-filter>`), অ্যাকশন, ক্যাটাগরি ও ডেটা টাইপ।
     * অ্যাক্টিভিটির মাঝে ডেটা পাসিং: `putExtra()`, `Bundle`, `getIntent()`।
   - অ্যান্ড্রয়েড নেভিগেশন কম্পোনেন্টস: Navigation Drawer, Bottom Navigation Bar, TabLayout with ViewPager2 (Swipe views), ফ্র্যাগমেন্ট ব্যাক-স্ট্যাক হ্যান্ডলিং।
   - ডেটা স্টোরেজ ম্যানেজমেন্ট (Data Storage Options):
     * ডিভাইস স্টোরেজ: ইন্টারনাল স্টোরেজ (প্রাইভেট ডেটা) বনাম এক্সটারনাল স্টোরেজ (শেয়ার্ড ফাইল ও মিডিয়া)।
     * শেয়ার্ড প্রেফারেন্সেস (SharedPreferences): কি-ভ্যালু পেয়ারে ছোট ডেটা সংরক্ষণ (লগইন স্টেট, সেটিংস, টোকেন), `apply()` বনাম `commit()`।
     * রুম পারসিস্টেন্স লাইব্রেরি (Room Database - SQLite-এর ওপর আধুনিক ওআরএম অ্যাবস্ট্রাকশন লেয়ার):
       - `@Entity` (ডাটাবেস টেবিল মডেল)
       - `@Dao` (Data Access Object - এসকিউএল কুয়েরি মেথডস `@Insert`, `@Update`, `@Delete`, `@Query`)
       - `@Database` (মেইন ডাটাবেস ক্লাস ও সিঙ্গলটন ইনস্ট্যান্স)।

অধ্যায় ২৪.৫: এপিআই নেটওয়ার্কিং, ব্যাকগ্রাউন্ড টাস্ক ও অ্যাপ প্রকাশনা (APIs, Background & Publishing - BTEB 28574 Unit 6)
   - অ্যান্ড্রয়েডে নেটওয়ার্কিং বেসিকস ও পারমিশন (`android.permission.INTERNET`, `ACCESS_NETWORK_STATE`)।
   - ব্যাকগ্রাউন্ড থ্রেডিং: মেইন ইউআই থ্রেড ব্লকিং রোধ, কোটলিন কোরুটিনস (Kotlin Coroutines: `launch`, `async`, `suspend` ফাংশন, `Dispatchers.IO`, `Dispatchers.Main`)।
   - রেস্টফুল এপিআই (RESTful API) কনজিউমিং:
     * রেট্রোফিট লাইব্রেরি (Retrofit HTTP Client): এপিআই ইন্টারফেস ডিফাইন করা, `@GET`, `@POST`, `@PUT`, `@DELETE` অ্যানোটেশন, বেস ইউআরএল, কনভার্টার ফ্যাক্টরি (Gson / Moshi)।
     * জেএসওএন ডেটা পার্সিং ও ডেটা বাইন্ডিং।
     * ফায়ারবেস রিয়েলটাইম ডেটাবেস ও ফায়ারস্টোর (Firebase Authentication & Database CRUD)।
   - অবস্থান ভিত্তিক সেবা (Location-Based Services - LBS): GPS, Network Provider, Google Play Services Location API, গুগল ম্যাপস (Google Maps SDK) ইন্টিগ্রেশন।
   - অ্যান্ড্রয়েড সিকিউরিটি ও কনটেন্ট প্রোভাইডার (Content Providers): কন্টাক্টস, গ্যালারি অ্যাক্সেস, রানটাইম পারমিশন হ্যান্ডলিং।
   - অ্যাপ প্রকাশনা ও ডেপ্লয়মেন্ট (Publishing Apps to Google Play Store):
     * অ্যাপ্লিকেশন ভার্সনিং (`versionCode`, `versionName`)।
     * কোড অবফাসকেশন ও শ্র্রিঙ্কিং (ProGuard / R8 রুলস)।
     * ডিজিটাল কি-স্টোর ও সাইনিং (KeyStore জেনারেশন, Private key, Release Signed APK / Android App Bundle `.aab`)।
     * গুগল প্লে কনসোল পলিসি, অ্যাপ লিস্টিং ও রিলিজ ম্যানেজমেন্ট।
"""

# Replace Subject 24 section header in content with Subject 25
if "বিষয়- ২৪: ডিজিটাল মার্কেটিং টেকনিক ও ইন্ডাস্ট্রিয়াল ম্যানেজমেন্ট" in content:
    content = content.replace(
        "----------------------------------------------------------------------------------------------------\nবিষয়- ২৪: ডিজিটাল মার্কেটিং টেকনিক ও ইন্ডাস্ট্রিয়াল ম্যানেজমেন্ট\nBTEB প্রবিধান-২০২২ সংশ্লিষ্ট কোর্স: Digital Marketing Technique (28571) ও Industrial Management (25852)\n----------------------------------------------------------------------------------------------------",
        apps_dev_content + "\n" + "----------------------------------------------------------------------------------------------------\nবিষয়- ২৫: ডিজিটাল মার্কেটিং টেকনিক ও ইন্ডাস্ট্রিয়াল ম্যানেজমেন্ট\nBTEB প্রবিধান-২০২২ সংশ্লিষ্ট কোর্স: Digital Marketing Technique (28571), Industrial Management (25852) ও Innovation & Entrepreneurship (65853)\n----------------------------------------------------------------------------------------------------"
    )
    # Also update chapter numbers in digital marketing
    content = content.replace("অধ্যায় ২৪.১:", "অধ্যায় ২৫.১:")
    content = content.replace("অধ্যায় ২৪.২:", "অধ্যায় ২৫.২:")

with open("BPSC technical syllabus.txt", "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Updated BPSC technical syllabus.txt successfully! ({len(content)} chars)")
