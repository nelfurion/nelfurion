from django.shortcuts import render

def index(request):
    print('ASDASD')
    return render(request, 'public/index.html')
