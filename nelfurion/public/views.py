from django.shortcuts import render
from public.models import portfolio

def index(request):
    scheme = request.is_secure() and "https" or "http"
    projects = portfolio.get_projects({
    'host': request.get_host(),
    'scheme': scheme,
    })

    return render(request, 'public/index.html', {
        'projects': projects['projects'],
        'more_projects': projects['more_projects'],
        'hackTUES_video': projects['hackTUES_video'],
        'activities': projects['activities']
    })
