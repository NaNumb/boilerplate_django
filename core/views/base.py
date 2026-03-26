from django.shortcuts import redirect

def index(request):
    # redirecting to /api
    # here would live non api views
    return redirect('health_status')