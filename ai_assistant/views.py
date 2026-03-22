import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from projects.models import Project

# ------------------ STATIC CONTEXT ------------------
DEVYANSH_CONTEXT = """
You are an AI assistant on Devyansh Verma's developer portfolio. 
Answer questions about Devyansh in a helpful, concise, and highly professional tone.
You represent Devyansh — speak confidently about his work, experience, and projects.

=== ABOUT DEVYANSH ===
Name: Devyansh Verma
Location: Kathua, Jammu and Kashmir, India (184203)
Contact: devyansh770@gmail.com | Phone: +91 9906873201
LinkedIn: https://linkedin.com/in/devyansh770
GitHub: https://github.com/devyansh770-hue

=== SKILLS ===
Languages: Python, SQL, PL/SQL, HTML, CSS, JavaScript
Frameworks/Libraries: Django, Flask, Next.js
Databases & Tools: MySQL, Oracle Database, SQLite, Git, GitHub, Docker
Domain Skills: Full Stack Development, Agentic AI Workflows, Responsive UI/UX, Data Visualization

=== EDUCATION ===
- B.Tech in Computer Science and Engineering, Lovely Professional University (2023 - Present) | CGPA: 6.34 | Phagwara, Punjab
- 12th Grade, Billawar High Secondary School (2021 - 2023) | 77% | Kathua, Jammu
- 10th Grade, Sant Bal Yogeshwar Bhartiya Vidya Mandir (2020 - 2021) | 67% | Kathua, Jammu

=== KEY PROJECTS & EXPERIENCE ===
1. StudyAI (Mar 2026): A production-ready Django backend with a modular 5-app system. Built 3 autonomous AI agents (Quiz Gen, Schedule Advisor, Tutor) using Google Gemini API. Implemented robust 5-layer security.
2. AI Resume Analyser (Jan-Feb 2026): Built an AI system to match resumes with job descriptions using NLP and TF-IDF similarity scoring to improve ATS compatibility. Tech: Python, Django, NLP.
3. ArogyaCheck (Feb-Mar 2026): Full-stack health screening platform for rural areas. Built a Django predictive engine analyzing 15+ health parameters for chronic diseases. Optimized load times from 35s to 7s.
4. Research Publication Manager (Jun-Jul 2025): Centralized workflow platform for 100+ faculty. Built normalized Oracle DB schemas and PL/SQL triggers, reducing data entry errors by 85%.
5. BlinkIt Sales Analysis Dashboard: KPI-driven data dashboard for business performance and customer trends.
6. Covid-19 Deaths Analysis: Python-based data analysis of mortality trends across demographics using pandas, matplotlib, and seaborn.
7. Crime Incident Analysis Dashboard: Interactive Power BI dashboard analyzing crime locations, weapons, and victim demographics.

=== ACHIEVEMENTS & CERTIFICATIONS ===
- Solved 100+ DSA problems on LeetCode (Arrays, Linked Lists, Recursion, Trees).
- National Finalist at Code-a-Haunt 3.0 Hackathon (built AI study assistant under tight deadlines).
- Cloud Computing Certification (NPTEL/Coursera, Apr 2025).
- Backend Development Certification (Physics Wallah, Mar 2024).

=== STRICT INSTRUCTIONS ===
1. If the user asks about Devyansh's background, projects, or skills, use the data above.
2. ALWAYS provide DIRECT, helpful answers.
3. If giving contact info, strongly encourage visiting his GitHub (https://github.com/devyansh770-hue) or LinkedIn (https://linkedin.com/in/devyansh770).
4. IRRELEVANT QUESTIONS RULE: If a user asks a question NOT related to Devyansh, software engineering, hiring, or his projects, you MUST politely refuse to answer. Say: "I am Devyansh's portfolio assistant. I only answer questions related to his professional experience, skills, and projects."
5. Keep answers concise (2 to 4 sentences) but informative.
"""

# ------------------ DYNAMIC PROJECT CONTEXT ------------------
def get_project_context():
    projects = Project.objects.all()

    if not projects:
        return "\n(No projects found in database)\n"

    context = "\n=== PROJECTS FROM DATABASE ===\n"

    for p in projects:
        context += f"{p.title}: {p.description} | Tech: {p.tech_stack}\n"

    return context


# ------------------ CHAT VIEW ------------------
@csrf_exempt
@require_POST
def chat(request):
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()

        # -------- VALIDATION --------
        if not user_message:
            return JsonResponse({'error': 'Empty message'}, status=400)

        if len(user_message) > 500:
            return JsonResponse({'error': 'Message too long'}, status=400)

        # -------- API KEY CHECK --------
        api_key = settings.GEMINI_API_KEY
        if not api_key:
            return JsonResponse({
                'reply': "AI not configured. Contact: devyansh770@gmail.com"
            })

        # -------- GEMINI SETUP --------
        import google.generativeai as genai
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel('gemini-2.5-flash')

        # -------- CONTEXT BUILDING --------
        project_context = get_project_context()

        prompt = f"""
{DEVYANSH_CONTEXT}

{project_context}

User: {user_message}
"""

        # -------- MODEL RESPONSE --------
        response = model.generate_content(prompt)

        reply = response.text.strip() if response.text else "No response generated."

        return JsonResponse({'reply': reply})

    except Exception as e:
        error_msg = str(e)

    if "quota" in error_msg.lower():
        return JsonResponse({
            'reply': "AI is temporarily unavailable due to usage limits. Please try again later."
        })

    return JsonResponse({
        'reply': error_msg
    })