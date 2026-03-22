from django.shortcuts import render

def home(request):
    skills = {
        'Languages': ['Python', 'SQL', 'PL/SQL', 'JavaScript', 'HTML', 'CSS'],
        'Frameworks': ['Django', 'Flask', 'Next.js'],
        'Databases': ['MySQL', 'Oracle DB', 'SQLite'],
        'Tools': ['Git', 'GitHub', 'Docker'],
        'Domain': ['Full Stack Dev', 'Agentic Workflows', 'Data Visualization', 'REST APIs'],
    }
    achievements = [
        {
            'icon': '🏆',
            'title': 'Hackathon Finalist',
            'desc': 'Finalist in Code-a-Haunt 3.0 (National Level) — built an AI study assistant under tight deadlines.',
            'date': 'Mar 2026',
        },
        {
            'icon': '💡',
            'title': '100+ LeetCode Problems',
            'desc': 'Solved 100+ DSA problems covering arrays, linked lists, recursion, and trees.',
            'date': 'Oct 2025 – Present',
        },
        {
            'icon': '☁️',
            'title': 'Cloud Computing Certified',
            'desc': 'Earned a Cloud Computing certification, deepening expertise in cloud architecture.',
            'date': 'Apr 2025',
        },
    ]
    return render(request, 'core/home.html', {'skills': skills, 'achievements': achievements})


def about(request):
    return render(request, 'core/about.html')
