# SkillSync AI - Project Explanation

Ye document **SkillSync AI (Resume Analyzer)** project ki puri details, architecture, aur file structure ko explain karta hai. Ye ek comprehensive guide hai taaki koi bhi naya developer ya user is project ko easily samajh sake.

## 1. Project Overview (Project Kya Hai?)
**SkillSync AI** ek AI-powered Resume Analyzer web application hai. Ye users ko apna resume upload karne aur use kisi specific **Job Description (JD)** se compare karne ki suvidha deta hai. Ye application **Google Gemini API** ka use karke resume ka text padhti hai aur batati hai ki resume us job ke liye kitna fit hai (ATS Score), kaunsi skills match hui hain, kaunsi missing hain, aur resume ko improve karne ke liye kya karna chahiye.

## 2. Technologies Used (Kaunsi Tech Use Hui Hai?)
- **Backend Framework:** Django (Python)
- **Database:** SQLite (default) / PostgreSQL (Supabase par migrate karne ka option set hai)
- **AI Engine:** Google Gemini API (`genai.Client`)
- **Frontend:** HTML, CSS (Templates with Django), JavaScript (Charts ke liye - mostly Chart.js)
- **PDF/Docx Parsing:** PyPDF2 ya similar library (`core/services/pdf_parser.py` me)
- **Report Generation:** PDF generation tools (like ReportLab, `core/services/report_generator.py` me)

## 3. Project Architecture (Data Kaise Flow Hota Hai?)
Application ka data flow kuch is tarah kaam karta hai:

1. **User Upload:** User `upload_view` par jaakar apna Resume (PDF/DOCX) aur Job Description dalta hai.
2. **Text Extraction:** `pdf_parser.py` us PDF ya DOCX file se raw text nikalta hai.
3. **AI Analysis:** `ai_analyzer.py` wo raw text aur job description **Gemini AI** ko bhejta hai. Gemini usko analyze karke ek JSON response deta hai (Match skills, missing skills, score).
4. **Database Storage:** `views.py` us response ko `AnalysisResult` table (Database) mein save kar deta hai.
5. **Dashboard Visualization:** User ko `dashboard_view` par redirect kiya jata hai, jahan charts aur data show hota hai.
6. **PDF Report:** User chahe toh `download_report_view` ke zariye apna final report PDF format me download kar sakta hai.

## 4. Folder & File Structure (Files Ka Kaam Kya Hai?)

### Main Project Folder (`skillsync/`)
Ye Django ka root folder hai jo poore project ko control karta hai.
- `settings.py`: Yahan project ki saari settings hain (Database, API Keys, Installed Apps). Humne isme Gemini API key (.env se) aur Supabase DB connect karne ka logic daala hai.
- `urls.py`: Project ki main routing (Jaise `/admin`, aur baki sab `core/urls.py` ko pass hota hai).

### Main App Folder (`core/`)
Ye application ka dil (heart) hai. Saara logic yahi par hai.
- `models.py`: Database tables (Schema). Isme 2 main tables hain:
  - `Resume`: Upload ki hui file, uska naam aur extracted text save karta hai.
  - `AnalysisResult`: AI ka final output (Score, Matched Skills, Feedback) save karta hai. Ye JSON format me skills ko database me save karta hai `@property` ka use karke.
- `views.py`: Request aane par kya response dena hai, wo yahan likha hai. (Upload page, Dashboard, History, etc.)
- `forms.py`: Django forms jo upload input (File aur Job Description) handle karte hain.
- `urls.py`: `core` app ke specific routes (Jaise `/upload`, `/dashboard/<id>`).

### Services Folder (`core/services/`)
Views ko halka rakhne ke liye, complex logic in alag files me likha gaya hai:
- `ai_analyzer.py`: Gemini API se baat karta hai. Ye prompt banata hai, API ko bhejta hai, aur response ko JSON me format karta hai.
- `pdf_parser.py`: Uploaded Resume file se readable text nikalne ka kaam karta hai.
- `report_generator.py`: Final analysis dashboard data ko ek PDF file me convert karta hai jise user download kar sake.

### Templates (`core/templates/core/`)
Yahan saari HTML files hain:
- `base.html`: Common layout (Header/Footer) jise baaki pages extend karte hain.
- `landing.html`: Home page.
- `upload.html`: Resume upload karne ka form.
- `dashboard.html`: AI ka result, charts aur details dikhane wala page.
- `history.html`: Purane analyses ki list.

### Static & Media (`static/` & `media/`)
- `media/resumes/`: Jo bhi user resume upload karta hai wo physical file yahan save hoti hai.
- `static/`: CSS, JS, Images yahan store hoti hain.

## 5. Security Features Addressed
- **API Key Hidden:** Gemini API key ko `.env` file me hide kar diya gaya hai aur `settings.py` ke zariye `os.environ` se safely load kiya gaya hai taaki wo GitHub par leak na ho.
- **Supabase Integration:** `.env` me `DATABASE_URL` daalkar easily production database (PostgreSQL) par switch kiya ja sakta hai `dj-database-url` library ki madad se.

---
**Summary:** SkillSync ek fully functioning, well-structured Django app hai jo AI ke power ko use karke job seekers ko apne resume improve karne me madad karta hai. Iska code modular (alag-alag files me properly divided) hai, jisse isme naye features add karna bohot aasan hai.
