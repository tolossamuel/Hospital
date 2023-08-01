from django.shortcuts import render,redirect, get_object_or_404
from .models import Drug_Stor,Register_Patient,drug_request,User_lab_temporary,LabTestName,LabResult
from .forms import DrugAdd, DrugRequestForm,UserLabTemporaryForm
from django.template.defaultfilters import linebreaksbr
from django.apps import apps
from django.db.models import Q
from register_patient.models import Register_Patient, Doctors,Patient_History,Nurses
from login.models import user_login
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
# Create your views here.

@login_required(login_url='/login/')
def add_drug(request):
    if request.method == 'POST':
         name_drug = request.POST.get('drug_name')
         quantity_drugs = request.POST.get('quantity_drugs')
         price_per_drug = request.POST.get('price_per_drug')
         name_drug = request.POST.get('drug_name')
         descriptions_drug = request.POST.get('descriptions_drug')
         if Drug_Stor.objects.filter(name_drug = name_drug):
              drug_add = Drug_Stor.objects.get(name_drug = name_drug)
              drug_add.quantity_drugs += int(quantity_drugs)
              drug_add.price_per_drug = int(price_per_drug)
              drug_add.descriptions_drug = descriptions_drug
              drug_add.save()
         else:
              drug_add = Drug_Stor(name_drug = name_drug,
                                   quantity_drugs = int(quantity_drugs),
                                    price_per_drug = int(price_per_drug),
                                    descriptions_drug = descriptions_drug)
              drug_add.save()
    all_drug = Drug_Stor.objects.all()
    dictionary = {'all_drug' : all_drug}
    return render(request,'add_drug.html',dictionary)

@login_required(login_url='/login/')
def DrugRequest(request,pk):
     patient = Register_Patient.objects.get(id = pk)
     print(patient.Full_Name)
     if request.method == 'POST':
        drug_request_form = DrugRequestForm(request.POST)
        if drug_request_form.is_valid():
            drug_request_obj = drug_request_form.save(commit=False)
          
            drug_request_obj.patient = patient
            print(1234567890)
            print(drug_request_obj.patient.Full_Name)
            # error part =================================
            drug_request_obj.save()
            # ======================================
            print(1234567890)
            return redirect('stor:HistoryPatient', pk)
     else:
        drug_request_form = DrugRequestForm()
     dictionary = {'form' : drug_request_form, 'patient' : patient}
     return render(request,'drug_request.html',dictionary)
@login_required(login_url='/login/')
def check_drug(request, pk):
     if Drug_Stor.objects.filter(name_drug = pk).exists():
          patient_drug = Drug_Stor.objects.get(name_drug = pk)
     else:
          patient_drug = ""
     if request.method == 'POST':
         patient_id = request.session['patient_id']
         return redirect('stor:drug_for_patient',patient_id)
     return render(request, "checkDrug.html",{'patient_drug': patient_drug})
@login_required(login_url='/login/')
def sell_drug(request,drug_name,pk):
	drug_request_id = drug_request.objects.get(id = pk)
	if Drug_Stor.objects.filter(name_drug = drug_request_id.drug_name).exists():
			patient_drug = Drug_Stor.objects.get(name_drug = drug_request_id.drug_name)
			patient_drug.quantity_drugs -=1
			if patient_drug.quantity_drugs == 0:
					patient_drug.delete()
			else:
				patient_drug.save()
	drug_request_id.delete()
	drug_id = request.session['patient_id']
	return redirect('stor:drug_for_patient',drug_id)
@login_required(login_url='/login/')
def doctor_patients(request):
     user = request.user
     if Nurses.objects.filter(doctor = user).exists():
           dr_patients = Nurses.objects.filter(doctor = user)
     else:
           dr_patients = []
     dictionary = {'patients_DR' : dr_patients}
     return render(request, 'patient_for_dr.html', dictionary)
@login_required(login_url='/login/')
def delete_temp(request,pk):
     complit_patients = Nurses.objects.get(id = pk)
     complit_patients.delete()
     return redirect('stor:doctor_patients')
@login_required(login_url='/login/')
def HistoryPatient(request,pk):
     user = request.user
     patient = Register_Patient.objects.get(id = pk)
     if Patient_History.objects.filter(patient = patient).exists():
           pre_history_patient = Patient_History.objects.get(patient = patient)
     else:
           pre_history_patient = Patient_History(patient = patient,
												 doctor = user,
                                                 history_text = " ",
                                                 )
           pre_history_patient.save()
           
     if request.method == 'POST':
        text_history = request.POST.get('text_history')
        if text_history:
             pre_history_patient.history_text += (f"\n\n\nName Doctor : {user.first_name} {user.last_name}\n{text_history}")
             pre_history_patient.save()
     formatted_comment = linebreaksbr(pre_history_patient.history_text)
     dictionary = {'historyText' : formatted_comment, 'history':pre_history_patient}
     return render(request, 'history_patient.html', dictionary)
@login_required(login_url='/login/')
def pharma(request):
     patient_with_pharma = []
     if request.GET.get('search') != None :
        search = request.GET.get('search')
     else:
        search = '#'
    
     patients = Register_Patient.objects.filter(
        Q(Full_Name__icontains = search) 
        )
     patient_count = patients.count()
    
     dictionary = {'patients':patients}
     return render(request, 'pharma.html', dictionary)
@login_required(login_url='/login/')
def drug_for_patient(request, pk):
    request.session['patient_id'] = pk
    DrugPatient = []
    if(Register_Patient.objects.filter(id = pk).exists()):
                patient = Register_Patient.objects.get(id = pk)
                DrugPatient = drug_request.objects.filter(patient = patient)
    dictionary = {'DrugPatient':DrugPatient}
    if request.method =='POST':
         return redirect('stor:pharma')
    return render(request, 'drug_for_patient.html', dictionary)
def pharma(request):
     patient_with_pharma = []
     if request.GET.get('search') != None :
        search = request.GET.get('search')
     else:
        search = '#'
    
     patients = Register_Patient.objects.filter(
        Q(full_name__icontains = search) 
        )
     patient_count = patients.count()
    
     dictionary = {'patients':patients}
     return render(request, 'pharma.html', dictionary)
def labRequest(request, pk):
    
    user = Register_Patient.objects.get(pk=pk)
    print(user)
    if request.method == 'POST':
        selected_labs = request.POST.getlist('selected_labs')
        print(selected_labs, user)
        labs_str = ",".join(selected_labs)
        user_lab_temporary = User_lab_temporary(Patient_name=user, labs=labs_str)
        print(user_lab_temporary)
        user_lab_temporary.save()

        return redirect('stor:HistoryPatient', pk)
    
    sections = LabTestName.objects.all()
    print(sections)

    return render(request, 'labratory/lab_request_form.html', {'sections': sections})



def save_user_lab_temporary(request):
    if request.method == 'POST':
        form = UserLabTemporaryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)  # Save the form data without committing to the database
            selected_labs = request.POST.getlist('labs')  # Get the list of selected labs from the form
            instance.save_selected_labs(selected_labs)  # Save the selected labs using the model method
            return redirect('stor:success_url_name')  # Replace 'success_url_name' with the name of the URL pattern for the success page
    else:
        form = UserLabTemporaryForm()

    return render(request, 'labratory/lab_request_form.html', {'form': form})

def labratory(request):
    data = User_lab_temporary.objects.all()

    return render(request, 'labratory/labratory.html', {'data': data})

def labratoryToDr(request, pk):
     patient = Register_Patient.objects.get(id = pk)
     temp_lap = User_lab_temporary.objects.filter(Patient_name = patient)
     if request.method == "POST":
          result = request.POST.get('result')
          if result:               
               res = LabResult(Patient_name = patient, resulut = result )
               res.save()
               return redirect('stor:labratory')
     
     context = {
          'user' : temp_lap
     }
     
     return render(request, 'labratory/labratory_to_doctor.html', context)


def LabratoryResult(request, pk):
     # user  = User_lab_temporary.objects.get(pk = pk)
     patient = Register_Patient.objects.get(id = pk)
     # res = LabResult.objects.get(patient_name = user.Patient_name)
     lab_results = LabResult.objects.filter(Patient_name=patient)
     
     

     context = {
          'user': lab_results
     }

     return render(request, 'labratory/labratory_result.html', context)