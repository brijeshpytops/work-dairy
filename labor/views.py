from django.shortcuts import render, HttpResponse



def login_view(request):
    return render(request, 'login.html')

def register_request_view(request):
    return render(request, 'register-request.html')

def forgot_password_view(request):
    return render(request, 'forgot-password.html')

def otp_verify_view(request):
    return render(request, 'otp-verification.html')



def dashboard_view(request):
    return render(request, 'dashboard.html')

def tasks_view(request):
    return render(request, 'tasks.html')

def parties_view(request):
    return render(request, 'parties.html')

def payments_view(request):
    return render(request, 'payments.html')

def profile_view(request):
    return render(request, 'profile.html')