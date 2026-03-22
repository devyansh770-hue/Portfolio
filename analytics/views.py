from analytics.models import ProjectView
from django.shortcuts import render
from .models import ProjectView
from django.db.models import Count
def project_detail(request, id):
    project = Project.objects.get(id=id)

    # -------- TRACK VIEW --------
    ip = request.META.get('REMOTE_ADDR')

    ProjectView.objects.create(
        project=project,
        ip_address=ip
    )

    return render(request, 'projects/detail.html', {'project': project})


def dashboard(request):
    total_views = ProjectView.objects.count()

    project_data = (
        ProjectView.objects
        .values('project__title')
        .annotate(view_count=Count('id'))
        .order_by('-view_count')
    )

    labels = [item['project__title'] for item in project_data]
    values = [item['view_count'] for item in project_data]

    most_viewed = project_data.first()

    top_projects = project_data[:3]

    recent_views = ProjectView.objects.select_related('project').order_by('-viewed_at')[:5]

    context = {
        'total_views': total_views,
        'most_viewed': most_viewed,
        'labels': labels,
        'values': values,
        'top_projects': top_projects,
        'recent_views': recent_views,
    }

    return render(request, 'analytics/dashboard.html', context)