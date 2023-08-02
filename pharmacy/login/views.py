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
                if profetion == "Doctor" and user.profetion == "Doctor":
                    return redirect('stor:doctor_patients')
                elif (profetion == 'Nurse' and user.profetion == "Nurse"):
                    return redirect('register_patient:Nurse')
                elif (profetion == 'Receptions' and user.profetion == "Receptions"):
                    return redirect('register_patient:Home')
                elif (profetion == 'Pharmacy' and user.profetion == "Pharmacy"):
                    return redirect('stor:pharma')
                elif (profetion == 'Reception' and user.profetion == "Reception"):
                    return redirect('register_patient:Home')
                elif (profetion == 'Labratory' and user.profetion == 'Labratory'):
                    return redirect('stor:labratory')
                else:
                    return redirect('login:logout')
            else:
                return redirect('login:login')
    return render(request, 'login/signin.html')
def logout(request):
    user = request.user
    if user.is_superuser:
        auth.logout(request)
        return redirect('admin_control:admin_login')
    auth.logout(request)
    return redirect('login:login')