from django.shortcuts import render,redirect
from .models import Drug_Stor,Register_Patient,drug_request,Doctor, History_patient
from .forms import DrugAdd, DrugRequestForm, HistoryPatientForm
from django.template.defaultfilters import linebreaksbr
from django.apps import apps
from django.db.models import Q
# Create your views here.
def add_drug(request):
    drug_form = DrugAdd()
    if request.method == 'POST':
         drug_form = DrugAdd(request.POST)
         if drug_form.is_valid():
              drug_form.save()
              return redirect('DrugRequest')
    all_drug = Drug_Stor.objects.all()
    dictionary = {'form' : drug_form, 'all_drug' : all_drug}
    return render(request,'add_drug.html',dictionary)
def DrugRequest(request,pk):
     patient = Register_Patient.objects.get(id = pk)
     if request.method == 'POST':
        drug_request_form = DrugRequestForm(request.POST)
        if drug_request_form.is_valid():
            drug_request_obj = drug_request_form.save(commit=False)
            drug_request_obj.patient = patient
            drug_request_obj.save()
            return redirect('HistoryPatient', pk)
     else:
        drug_request_form = DrugRequestForm()
     dictionary = {'form' : drug_request_form, 'patient' : patient}
     return render(request,'drug_request.html',dictionary)
def check_drug(request, pk):
     if Drug_Stor.objects.filter(name_drug = pk).exists():
          patient_drug = Drug_Stor.objects.get(name_drug = pk)
     else:
          patient_drug = ""
     if request.method == 'POST':
         patient_id = request.session['patient_id']
         return redirect('drug_for_patient',patient_id)
     return render(request, "checkDrug.html",{'patient_drug': patient_drug})
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
	return redirect('drug_for_patient',drug_id)
def doctor_patients(request):
     dr_patients= Doctor.objects.all()
     dictionary = {'patients_DR' : dr_patients}
     return render(request, 'patient_for_dr.html', dictionary)
def delete_temp(request,pk):
     complit_patients = Doctor.objects.get(id = pk)
     complit_patients.delete()
     return redirect('doctor_patients')
def HistoryPatient(request,pk):
     patient = Register_Patient.objects.get(id = pk)
     print(patient.First_Name)
     print(pk,12345678)
     pre_history_patient = History_patient.objects.get(patient = patient)
     if request.method == 'POST':
        text_history = request.POST.get('text_history')
        if text_history:
             pre_history_patient.hisory_text += (f"\n\n\nName Doctor : Samuel Tolossa\n{text_history}")
             pre_history_patient.save()
     formatted_comment = linebreaksbr(pre_history_patient.hisory_text)
     dictionary = {'historyText' : formatted_comment, 'history':pre_history_patient}
     return render(request, 'history_patient.html', dictionary)
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
def drug_for_patient(request, pk):
    request.session['patient_id'] = pk
    DrugPatient = []
    if(Register_Patient.objects.filter(id = pk).exists()):
                patient = Register_Patient.objects.get(id = pk)
                DrugPatient = drug_request.objects.filter(patient = patient)
    dictionary = {'DrugPatient':DrugPatient}
    if request.method =='POST':
         return redirect('pharma')
    return render(request, 'drug_for_patient.html', dictionary)