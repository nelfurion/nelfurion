from django.shortcuts import render
from public.models import portfolio
from public.models import contacts

def index(request):
    scheme = request.is_secure() and "https" or "http"
    options = {
    'host': request.get_host(),
    'scheme': scheme,
    }

    projects = portfolio.get_models(options)
    contacts_data = contacts.get_models(options)

    return render(request, 'public/index.html', {
        'projects': projects['projects'],
        'more_projects': projects['more_projects'],
        'hackTUES_video': projects['hackTUES_video'],
        'activities': projects['activities'],
        'contacts': contacts_data
    })
