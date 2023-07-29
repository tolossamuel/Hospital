from django.urls import path
from . import views

app_name = "register_patient"
urlpatterns = [
    path('',views.Home,name='Home'),
    path('register-patient',views.RegisterPatient,name='register-patient'),
    path('register-doctor',views.RegisterDoctor,name='register-doctor'),
    path('nurse',views.Nurse,name='Nurse'),
    path('doctor/<int:pk>',views.Doctor,name='doctor'),
    path('nurse-patient/<int:pk>', views.nurse_patient, name="nurse_patient"),
    path('doctor-patient/<int:pk>', views.doctor_patient, name="doctor_patient")
]