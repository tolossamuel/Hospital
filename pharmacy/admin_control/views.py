from django.shortcuts import render,redirect
from login.models import user_login
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password, Superuser = True)
            if user is not None:
                auth_login(request,user)
                return redirect('admin_control:control_worker')
        else:
            return redirect('admin_control:admin_login')
    return render(request,'admin/admin.html')
@login_required(login_url='/admin-control')
def control_worker(request):
    Doctor_staf = user_login.objects.filter(profetion = 'Doctor')
    Nurse_staf = user_login.objects.filter(profetion = 'Nurse')
    pharmacy_staf =user_login.objects.filter(profetion = 'Pharmacy')
    lab_staf = user_login.objects.filter(profetion = 'Labratory')
    reception_staf = user_login.objects.filter(profetion = 'Reception')
    dictionary = {'doctor': Doctor_staf,
                  'nurse': Nurse_staf,
                  'pharmacy': pharmacy_staf,
                  'lab': lab_staf,
                  'reception':reception_staf}
    return render(request, 'admin/all_staf.html', dictionary)
@login_required(login_url='/admin-control')
def add_staff(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        username = request.POST.get('username')
        email = request.POST.get('email')
        profetion = request.POST.get('profetion')
        filed = request.POST.get('filed')
        sex = request.POST.get('sex')
        mobile = request.POST.get('mobile')
        if fname and lname and password and username and email and profetion and mobile and filed and sex:
            if password ==  confirm_password:
                if not(user_login.objects.filter(email = email).exists()):
                    if not(user_login.objects.filter(username = username)):
                        new_staff = user_login(first_name = fname,
                                               last_name = lname,
                                               username = username,
                                               password = password,
                                               profetion = profetion,
                                               filed = filed,
                                               mobile = mobile,
                                               gender = sex) 
                        new_staff.set_password(password)  
                        new_staff.save()
                        return redirect('admin_control:control_worker')   
                    else:
                        messages.error (request, 'username already exist')
                        return redirect('admin_control:add_staff')
                else:
                    messages.error (request, 'email already exist')
                    return redirect('admin_control:add_staff')
            else:
                messages.error (request, 'password doenot match ')
                return redirect('admin_control:add_staff')
        else:
            messages.error (request, 'username already exist')
            return redirect('admin_control:add_staff')
    dectionary = {'messages':messages}
    return render(request, 'admin/add_staff.html')
            