# ⚡ SkillSync AI — Intelligent Resume Analysis Platform

<div align="center">

**AI-Powered Resume Analyzer | Skill Gap Detection | Career Recommendations**

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django)
![Gemini AI](https://img.shields.io/badge/Google_Gemini-AI-red?style=for-the-badge&logo=google)
![Chart.js](https://img.shields.io/badge/Chart.js-Visualization-orange?style=for-the-badge&logo=chartdotjs)

</div>

---

## 📋 Project Overview

**SkillSync AI** is a full-stack web application that uses Google's Gemini AI to analyze resumes against job descriptions. It extracts skills from uploaded resumes (PDF/DOCX), compares them with job requirements, calculates a match score, and provides actionable recommendations to bridge skill gaps.

### 🎯 What This Project Does
1. **Upload** a resume (PDF or DOCX format)
2. **Paste** a job description to compare against
3. **AI analyzes** the resume using Google Gemini 2.5 Flash
4. **Dashboard** shows match score, skill gaps, radar/bar charts, strengths, and recommendations
5. **Download** a professional PDF report of the analysis

---

## 🏗️ Architecture & Tech Stack

```
┌──────────────────────────────────────────────────┐
│                    Frontend                       │
│  HTML5 + CSS3 + JavaScript + Chart.js             │
│  (Responsive: Mobile / Tablet / Desktop)          │
├──────────────────────────────────────────────────┤
│                   Django Views                    │
│  landing_view | upload_view | dashboard_view      │
│  history_view | download_report | api_chart_data  │
├──────────────────────────────────────────────────┤
│               Services Layer                      │
│  ┌─────────────┐ ┌────────────┐ ┌──────────────┐ │
│  │ PDF Parser  │ │AI Analyzer │ │PDF Generator │ │
│  │ (PyMuPDF +  │ │(Gemini API)│ │ (ReportLab)  │ │
│  │  python-docx)│ │            │ │              │ │
│  └─────────────┘ └────────────┘ └──────────────┘ │
├──────────────────────────────────────────────────┤
│              Database (SQLite)                    │
│  Resume Model | AnalysisResult Model              │
└──────────────────────────────────────────────────┘
```

### Technologies Used

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Django 5.x | Web framework, ORM, routing |
| **AI Engine** | Google Gemini 2.5 Flash | Resume analysis, skill extraction |
| **PDF Input** | PyMuPDF (fitz) | Extract text from PDF resumes |
| **DOCX Input** | python-docx | Extract text from Word resumes |
| **PDF Output** | ReportLab | Generate downloadable analysis reports |
| **Frontend** | HTML5, CSS3, JS | Responsive UI with animations |
| **Charts** | Chart.js | Radar and Bar chart visualizations |
| **Database** | SQLite | Data persistence |

---

## 📁 Project Structure

```
resume analyser/
├── manage.py                         # Django management script
├── requirements.txt                  # Python dependencies
├── .env                              # API keys (not in repo)
├── .gitignore                        # Git ignore rules
├── db.sqlite3                        # SQLite database
│
├── skillsync/                        # Django project settings
│   ├── settings.py                   # Configuration
│   ├── urls.py                       # Root URL routing
│   ├── wsgi.py                       # WSGI entry point
│   └── asgi.py                       # ASGI entry point
│
├── core/                             # Main application
│   ├── models.py                     # Resume & AnalysisResult models
│   ├── views.py                      # All view functions
│   ├── urls.py                       # App-level URL routing
│   ├── forms.py                      # Upload form with validation
│   ├── admin.py                      # Django admin configuration
│   │
│   ├── services/                     # Business logic layer
│   │   ├── ai_analyzer.py            # Gemini API integration
│   │   ├── pdf_parser.py             # PDF/DOCX text extraction
│   │   └── report_generator.py       # PDF report generation
│   │
│   ├── templates/core/               # HTML templates
│   │   ├── base.html                 # Base template with navbar/footer
│   │   ├── landing.html              # Homepage with hero section
│   │   ├── upload.html               # Resume upload form
│   │   ├── dashboard.html            # Analysis results + charts
│   │   └── history.html              # Past analyses list
│   │
│   └── static/core/css/
│       └── style.css                 # Complete design system
│
└── media/resumes/                    # Uploaded resume files
```

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.10+
- Google Gemini API key ([Get it here](https://aistudio.google.com/apikey))

### Steps

```bash
# 1. Clone the repository
git clone <repo-url>
cd "resume analyser"

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
echo GEMINI_API_KEY=your_api_key_here > .env
echo DJANGO_SECRET_KEY=your_secret_key >> .env

# 4. Run database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create admin superuser (optional)
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver

# 7. Open in browser
# http://127.0.0.1:8000/
```

---

## 🎨 Design System

| Token | Value | Usage |
|-------|-------|-------|
| **Primary** | `#0F0F0F` (Black) | Headings, navbar, buttons |
| **Accent** | `#E63946` (Deep Red) | CTAs, highlights, score rings |
| **Background** | `#F8F9FA` (Off-white) | Page backgrounds |
| **Text** | `#212529` (Dark Gray) | Body text |
| **Border** | `#DEE2E6` | Cards, dividers |

---

## 📊 Key Features

### 1. Smart Resume Parsing
- Extracts text from **PDF** (PyMuPDF) and **DOCX** (python-docx)
- Cleans extracted text (removes special chars, normalizes spacing)
- Handles tables and multi-page documents

### 2. AI-Powered Analysis (Gemini 2.5 Flash)
- Structured JSON prompt engineering for consistent outputs
- **Multi-model fallback**: If one Gemini model is rate-limited, automatically tries the next
- Models: `gemini-2.5-flash-lite` → `gemini-2.5-flash` → `gemini-3-flash-preview`

### 3. Dashboard Visualization
- **Score Ring**: Animated SVG circle showing match percentage
- **Radar Chart**: Skill proficiency comparison (yours vs required)
- **Bar Chart**: Side-by-side skill level comparison
- **Skill Tags**: Color-coded matched (green) and missing (red) skills

### 4. PDF Report Generation
- Professional multi-page PDF using ReportLab
- Includes: Overview table, score interpretation, skill comparison, recommendations
- Downloadable with one click

### 5. Fully Responsive Design
- **Mobile** (375px+): Hamburger menu, stacked layout
- **Tablet** (768px+): Adjusted grids, touch-friendly
- **Desktop** (1200px+): Full multi-column layout

---

## 🔧 How the AI Analysis Works

```
User uploads resume + pastes JD
            │
            ▼
    ┌───────────────┐
    │  PDF Parser   │ ── Extract raw text from file
    └───────┬───────┘
            │
            ▼
    ┌───────────────┐
    │  Clean Text   │ ── Remove special chars, normalize
    └───────┬───────┘
            │
            ▼
    ┌───────────────┐     Structured prompt with resume
    │  Gemini AI    │ ◄── text + JD + JSON schema
    │  (API Call)   │
    └───────┬───────┘
            │
            ▼
    ┌───────────────┐
    │  Validate &   │ ── Ensure all fields present,
    │  Sanitize     │    scores in range, categories valid
    └───────┬───────┘
            │
            ▼
    ┌───────────────┐
    │  Save to DB   │ ── Store in AnalysisResult model
    └───────┬───────┘
            │
            ▼
    ┌───────────────┐
    │  Dashboard    │ ── Render charts, tags, feedback
    └───────────────┘
```

---

## 🎯 Project Level Assessment

### Rating: **Early Intermediate** (Beginner+ to Intermediate)

| Category | Level | Details |
|----------|-------|---------|
| **Django Usage** | Intermediate | Multiple models, services layer, forms with validation |
| **AI Integration** | Beginner+ | API wrapper (no custom ML model) |
| **Frontend** | Intermediate | Custom CSS design system, Chart.js, responsive |
| **Architecture** | Intermediate | Separated services, clean project structure |
| **Database** | Intermediate | Relationships, JSON property helpers |
| **Error Handling** | Intermediate | Try-except, model fallback, user-friendly messages |
| **Testing** | Beginner | No automated tests yet |
| **Deployment** | Beginner | Local development only |
| **Security** | Beginner | No authentication system |

### What Makes It Intermediate:
- ✅ Separation of concerns (services folder)
- ✅ Multi-model AI fallback pattern
- ✅ Structured prompt engineering for JSON output
- ✅ PDF generation + parsing (both directions)
- ✅ Interactive data visualization
- ✅ Comprehensive responsive CSS design system

### What Would Make It Advanced:
- ❌ Add user authentication (login/signup)
- ❌ Add local skill matching (own algorithm, not just AI)
- ❌ Add resume structure validation (check for email, phone, sections)
- ❌ Add experience years extraction
- ❌ Write unit tests
- ❌ Deploy to production (Docker + cloud)
- ❌ Add background task processing (Celery)
- ❌ Add ATS compatibility scoring

---

## 👥 Team & Role Distribution

| Role | Name | Contribution |
|------|------|-------------|
| **AI/ML Engineer** | Akash | Gemini API integration, prompt engineering, AI response parsing |
| **Full-Stack Developer** | Ali Ahmad | Django backend, database models, frontend UI, Chart.js |
| **Third Member** | — | PDF parsing, report generation, testing |

---

## 📞 Interview Talking Points

### Key Technical Decisions:
1. **Why Gemini over OpenAI?** — Free tier, fast response, good JSON output capability
2. **Why services folder?** — Separation of concerns: views handle HTTP, services handle business logic
3. **Why JSON in TextField?** — Flexible schema for varying AI outputs; property helpers abstract JSON parsing
4. **Why multi-model fallback?** — Free tier rate limits differ per model; ensures high availability
5. **Why Chart.js?** — Lightweight, no build step required, works with Django templates directly

### Challenge Highlights:
- Handling inconsistent AI JSON outputs with regex cleanup + validation layer
- Rate limit management across multiple Gemini models
- Extracting text from complex PDF layouts (tables, multi-column)

---

## 📄 License

This project is for educational and demonstration purposes.

---

<div align="center">

**Built with ❤️ using Django + Google Gemini AI**

⚡ SkillSync AI — *Decode Your Resume's True Potential*

</div>
