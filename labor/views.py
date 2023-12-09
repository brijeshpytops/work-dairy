from django.shortcuts import render, HttpResponse



def login_view(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        print(username, email)
        return render(request, 'login.html')
    return render(request, 'login.html')