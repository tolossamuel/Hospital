from . import views
from django.urls import path

urlpatterns = [
    path('add-drug', views.add_drug, name='add_drug'),
    path('Drug-Request/<int:pk>', views.DrugRequest, name='DrugRequest'),
    path('drug-exist/<str:pk>', views.check_drug, name='check_drug'),
    path('pharma', views.pharma, name = 'pharma'),
    path('done/<str:drug_name>/<int:pk>', views.sell_drug, name='sell_drug'),
    path('finish/<int:pk>', views.delete_temp, name = 'delete_temp'),
    path('patients-doctor', views.doctor_patients, name="doctor_patients"),
    path('history-patients/<int:pk>', views.HistoryPatient, name = 'HistoryPatient'),
    path('drug-for-patient/<int:pk>', views.drug_for_patient, name = 'drug_for_patient')
]