from django.shortcuts import render
import public.projects as projects

def index(request):
    return render(request, 'public/index.html', {
        'projects': projects.projects,
        'more_projects': projects.more_projects,
        'hackTUES_video': projects.hackTUES_video,
        'activities': projects.activities
    })
