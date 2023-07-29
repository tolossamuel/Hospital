from django.shortcuts import render, redirect
from django.db.models import Q
from .models import pay, ditale_price, total_price
from stor.models import Register_Patient
# Create your views here.
def search_patient(request):
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
    return render(request, 'payment/search_for_payment.html', dictionary)
def patient_pay(request, pk):
    request.session['patient_id'] = pk
    patient = Register_Patient.objects.get(id = pk)
    pay_patient = ""
    if pay.objects.filter(patient = patient).exists():
         pay_patient = pay.objects.filter(patine=patient)
    dictionary = {'pay_patient': pay_patient}
    return render(request, 'payment/pay_patients.html')
def payment_done(request, pk):
     pay_patient = pay.objects.get(id = pk)
     pay_ditaile = ditale_price(price = pay_patient.price,
                                source = "patinet payment",
                                patient = pay_patient.patient
                                )
     pay_ditaile.save()
     if (total_price.objects.filter(id = 1).exists()):
          total = total_price.objects.get(id = 1)
          total.total_price += int(pay_patient.price)
          total.save()
     else:
          total = total_price(id = 1, total_price = int(pay_patient.price))
          total.save()
     pay_patient.delete()
     patient_id =request.session['patient_id']
     return redirect('payment:patient_pay', patient_id)
