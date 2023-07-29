from django.urls import path
from . import views
app_name = 'payment'
urlpatterns = [
    path('' , views.search_patient, name='search_patient'),
    path('patient-pay/<int:pk>', views.patient_pay, name = 'patient_pay')
]