from django.shortcuts import render, HttpResponse



def login_view(request):
    return render(request, 'login.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def tasks_view(request):
    return render(request, 'tasks.html')