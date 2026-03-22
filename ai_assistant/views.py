import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from projects.models import Project

# ------------------ STATIC CONTEXT ------------------
DEVYANSH_CONTEXT = """
You are an AI assistant on Devyansh Verma's developer portfolio. 
Answer questions about Devyansh in a helpful, concise, and professional tone.
You represent Devyansh — speak confidently about his work.

=== ABOUT DEVYANSH ===
Name: Devyansh Verma
Location: Kathua, Jammu and Kashmir, India
Email: devyansh770@gmail.com
LinkedIn: linkedin.com/in/devyansh770
GitHub: github.com/devyansh770-hue

=== SKILLS ===
Python, Django, Flask, SQL, JavaScript, REST APIs, AI workflows

=== INSTRUCTIONS ===
- Answer only portfolio-related questions
- Keep answers short (2–4 sentences)
- If unknown → say contact email
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