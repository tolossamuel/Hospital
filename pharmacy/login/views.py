from django.shortcuts import render,redirect
from .models import user_login
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        profetion = request.POST.get('profetion')
        if username and password and profetion :
            print(1234567890)
            user = authenticate(request, username=username, password=password, profetion = profetion)
            if user is not None:
                auth_login(request,user)
                redirectors = ""
                print(1234567890987654321)
                if profetion == "Doctor":
                    redirectors = 'stor:doctor_patients'
                elif (profetion == 'Nurse'):
                    redirectors = 'register_patient:Nurse'
                elif (profetion == 'Receptions'):
                    redirectors = 'register_patient:Home'
                elif (profetion == 'Pharmacy'):
                    redirectors = 'stor:pharma'
                return redirect(f"{redirectors}")
            else:
                return redirect('login:login')
    return render(request, 'login/signin.html')