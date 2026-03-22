from django.shortcuts import render, get_object_or_404

PROJECTS = [
    {
        'slug': 'studyai',
        'title': 'StudyAI',
        'tagline': 'AI-powered study assistant with autonomous agents',
        'date': 'Mar 2026',
        'github': 'https://github.com/devyansh770-hue/AIStudyAssistant',
        'tags': ['Python', 'Django', 'Gemini API', 'SQLite', 'REST APIs'],
        'color': '#00f5d4',
        'icon': '🎓',
        'highlights': [
            'Architected a production-ready Django backend with a modular 5-app system and 9 relational models for scalable RESTful API design.',
            'Developed 3 autonomous AI agents — Quiz Generation, Schedule Advisor, and Tutor — leveraging Google Gemini API for structured, logic-driven outputs.',
            'Engineered a 5-layer security pipeline: OTP email verification, rate limiting, brute force protection, session management, and CSRF.',
        ],
        'problem': 'Students struggle with personalized study planning and self-assessment at scale.',
        'solution': 'Autonomous AI agents that adapt to each student\'s pace, generating quizzes, schedules, and tutoring sessions on demand.',
        'impact': 'Production-ready system with enterprise-grade security supporting concurrent multi-user sessions.',
    },
    {
        'slug': 'ai-resume-analyser',
        'title': 'AI Resume Analyser',
        'tagline': 'NLP-based resume-job description matching system',
        'date': 'Jan 2026 – Feb 2026',
        'github': 'https://github.com/devyansh770-hue',
        'tags': ['Python', 'Django', 'NLP', 'TF-IDF'],
        'color': '#f72585',
        'icon': '📄',
        'highlights': [
            'Developed an AI-based system to analyze resumes and match them with job descriptions using NLP techniques.',
            'Implemented keyword extraction and TF-IDF similarity scoring to evaluate resume relevance against job postings.',
            'Generated automated feedback to improve ATS compatibility and overall resume quality.',
        ],
        'problem': 'Job seekers don\'t know why their resumes get filtered out by ATS systems.',
        'solution': 'NLP pipeline that scores resume-job fit and provides actionable improvement feedback.',
        'impact': 'Helps candidates optimize resumes before applying, increasing interview call rates.',
    },
    {
        'slug': 'arogyacheck',
        'title': 'ArogyaCheck',
        'tagline': 'Full-stack health screening for rural populations',
        'date': 'Feb 2026 – Mar 2026',
        'github': 'https://github.com/jyotsnak1603/arogyacheck',
        'tags': ['Python', 'Django', 'Plotly', 'Matplotlib', 'Bootstrap'],
        'color': '#7b2fff',
        'icon': '🏥',
        'highlights': [
            'Engineered a full-stack health screening platform with complex business logic for 3 distinct user roles, addressing preventive care gaps in rural areas.',
            'Built a Django predictive engine analyzing 15+ health parameters to identify risks for chronic diseases including diabetes and heart disease.',
            'Optimized backend architecture achieving an 80% reduction in load time (from 35s to 7s) — critical for low-bandwidth rural areas.',
        ],
        'problem': 'Rural populations lack access to preventive healthcare screening and early disease detection.',
        'solution': 'A low-bandwidth-optimized platform with predictive health analytics accessible to patients, doctors, and admins.',
        'impact': '80% load time reduction — from 35 seconds to just 7 seconds — making it viable in low-connectivity regions.',
    },
    {
        'slug': 'research-publication-manager',
        'title': 'Research Publication Manager',
        'tagline': 'Centralized platform for faculty research workflows',
        'date': 'Jun 2025 – Jul 2025',
        'github': 'https://github.com/devyansh770-hue/Research-Publication-Manager',
        'tags': ['Python', 'Oracle DB', 'PL/SQL', 'Plotly', 'Streamlit'],
        'color': '#f77f00',
        'icon': '📚',
        'highlights': [
            'Engineered a centralized management platform to streamline research workflows for 100+ active faculty and student users.',
            'Architected a normalized Oracle database schema with 5+ tables and automated PL/SQL validation triggers.',
            'Reduced manual data entry errors by 85% while processing 500+ publication records.',
        ],
        'problem': 'University research teams used scattered spreadsheets causing data errors and lost publications.',
        'solution': 'Centralized Oracle-backed platform with automated PL/SQL validation ensuring data integrity.',
        'impact': '85% reduction in data entry errors across 500+ publication records for 100+ users.',
    },
]


def project_list(request):
    return render(request, 'projects/list.html', {'projects': PROJECTS})


def project_detail(request, slug):
    project = next((p for p in PROJECTS if p['slug'] == slug), None)
    if not project:
        from django.http import Http404
        raise Http404("Project not found")
    return render(request, 'projects/detail.html', {'project': project})
