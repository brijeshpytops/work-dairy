from django.shortcuts import render, redirect
from django.core.mail import send_mail
import random
from django.conf import settings
from .models import labor_register

def login_view(request):
    if request.method == 'POST':
        labor_id_ = request.POST['labor_id']
        password_ = request.POST['password']

        try:
            check_user = labor_register.objects.get(labor_id=labor_id_)
        except labor_register.DoesNotExist:
            print("User does not exist.")
        else:
            if check_user:
                if check_user.password == password_:
                    request.session['labor_id'] = labor_id_
                    if 'labor_id' in request.session:
                        return redirect('dashboard_view')
                    else:
                        print("login_page")
                else:
                    print("Labor_id or Password doesn't match.")

    return render(request, 'login.html')

def register_request_view(request):
    return render(request, 'register-request.html')

def forgot_password_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        try:
            check_user = labor_register.objects.get(email=email_)
        except labor_register.DoesNotExist:
            print("User does not exist.")
        else:   
            if check_user:
                otp_ = random.randint(111111, 999999)
           

                subject = 'OTP Verification | WORK-DIARY'
                message = f"Your otp is : {otp_}"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [f'{email_}']

                print(subject, message, from_email, recipient_list)
                send_mail(subject, message, from_email, recipient_list)
                check_user.otp = otp_
                check_user.save()
                context = {
                    'email':email_
                }
                
                return render(request, 'otp-verification.html', context)
    return render(request, 'forgot-password.html')

def otp_verify_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        otp_ = request.POST['otp']
        new_password_ = request.POST['new_password']
        confirm_password_ = request.POST['confirm_password']
        try:
            check_user = labor_register.objects.get(email=email_)
        except labor_register.DoesNotExist:
            print("User does not exist.")
        else:   
            if check_user:
                if check_user.otp == otp_:
                    if new_password_ == confirm_password_:
                        check_user.password = new_password_
                        check_user.save()
                        print("Password updated successfully")
                    else:
                        print("New password and Confirm password doesn't match")
                else:
                    print("Invalid otp")
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