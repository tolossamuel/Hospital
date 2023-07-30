from django.http import HttpResponse
from django.shortcuts import redirect,render
from .models import Register_Patient,Doctors,Nurses,Drug_Stor,patient_nurse
from .forms import DrugAdd
from django.db.models import Q
from login.models import user_login
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

# Create your views here.

@login_required(login_url='/login/')
def Home(request):
    
    if request.GET.get('search') != None :
        search = request.GET.get('search')
    else:
        search = '#'
    
    patients = Register_Patient.objects.filter(
        Q(Full_Name__icontains = search) 
        )
    patient_count = patients.count()
    
    context = {'patients':patients,'patient_count':patient_count}
    
    return render (request,"patient/home.html",context)

@login_required(login_url='/login/')
def RegisterPatient(request):
    if request.method == 'POST':
        First_Name = request.POST.get('First_Name')
        Middle_Name = request.POST.get('Middle_Name')
        Last_Name = request.POST.get('Last_Name')
        Father_Name = request.POST.get('Father_Name')
        Mother_Name = request.POST.get('Mother_Name')
        Sex = request.POST.get('Sex')
        Age = request.POST.get('Age')
        Address = request.POST.get('Address')
        Phone_number = request.POST.get('Phone_number')
        Emergency_Phone_number = request.POST.get('Emergency_Phone_number')
        Birth_Date = request.POST.get('Birth-Date')
        lis = [First_Name,Middle_Name,Last_Name,Father_Name,Mother_Name,Sex,Age,Address,Phone_number,Emergency_Phone_number,Birth_Date]
        try:
            patient = Register_Patient.objects.create(
                First_Name = First_Name,
                Middle_Name = Middle_Name,
                Last_Name = Last_Name,
                Father_Name = Father_Name,
                Mother_Name = Mother_Name,
                Sex= Sex,
                Address = Address,
                Phone_Number = Phone_number,
                Emergency_Phone_Number = Emergency_Phone_number,
                Birth_Day = Birth_Date,
                Age = Age,
            )
            patient_id = patient.id
            patient.save()
            return redirect('register_patient:nurse_patient',patient_id )
        except:
            print(lis)
    return render(request,"patient/register_patient.html")
@login_required(login_url='/login/')
def nurse_patient(request,pk):
    patient = Register_Patient.objects.get(id = pk)
    nurses = user_login.objects.filter(profetion = 'Nurse')
    if request.method == 'POST':
        nurse_id = request.POST.get('nurse_id')
        if nurse_id:
            nurse = user_login.objects.get(id = int(nurse_id))
            patient_to_nurse = patient_nurse(nurse = nurse, patient = patient)
            patient_to_nurse.save()
            print(1234567890)
            return redirect('register_patient:Home')
    dictionary = {'nurses':nurses}
    return render(request, 'patient/patient_nurse.html',dictionary)
@login_required(login_url='/login/')
def RegisterDoctor(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Doctor_Field = request.POST['Doctor-Field']
        Room = request.POST['Room']
        
        doctor = Doctors.objects.create(
            Name = Name,
            Doctor_Field = Doctor_Field,
            Room = Room,
        )
        doctor.save()
        return redirect('register_patient:register-doctor')
    return render(request,'patient/register_doctor.html')

@login_required(login_url='/login/')
def Nurse(request):
    user = request.user
    patient = patient_nurse.objects.filter(nurse = user)
    dictionary = {'patient':patient}
    return render(request, 'patient/nurse.html', dictionary)


@login_required(login_url='/login/')
def Doctor(request,pk):
    
    doctor = Doctors.objects.filter(Room=pk)
    patients = Nurses.objects.filter(doctor=doctor)
    context = {'doctor':doctor,'patients':patients}
    return render(request,'patient/doctor.html',context)
@login_required(login_url='/login/')
def doctor_patient(request,pk):
    user = request.user
    patient = Register_Patient.objects.get(id = pk)
    doctor = user_login.objects.filter(profetion = "Doctor")
    if request.method=='POST':
        doctors_id = request.POST.get('doctor_id')
        status = request.POST.get('status')
        if doctors_id and status:
            print(1234567)
            redirect_doctor = user_login.objects.get(id = doctors_id)
            patient_doctor = Nurses(patient = patient,
                                    status = status,
                                    doctor = redirect_doctor)
            patient_doctor.save()
            checked_pateint = patient_nurse.objects.get(nurse = user, patient = patient)
            checked_pateint.delete()
            return redirect('register_patient:Nurse')
    dictionary = {'doctor':doctor}
    return render(request, 'patient/doctor_patient.html', dictionary)