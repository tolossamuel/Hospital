from . import views
from django.urls import path
app_name = 'stor'

urlpatterns = [
    path('add-drug', views.add_drug, name='add_drug'),
    path('Drug-Request/<int:pk>', views.DrugRequest, name='DrugRequest'),
    path('drug-exist/<str:pk>', views.check_drug, name='check_drug'),
    path('pharma', views.pharma, name = 'pharma'),
    path('done/<str:drug_name>/<int:pk>', views.sell_drug, name='sell_drug'),
    path('finish/<str:app_name>/<str:models_app_name>/<str:back>/<str:nameModels>/<int:pk>', views.delete_temp, name = 'delete_temp'),
    path('patients-doctor', views.doctor_patients, name="doctor_patients"),
    path('history-patients/<int:pk>', views.HistoryPatient, name = 'HistoryPatient'),
    path('drug-for-patient/<int:pk>', views.drug_for_patient, name = 'drug_for_patient'),
    path('labform/<int:pk>', views.labRequest, name='labform'),
    path('labratory/', views.labratory, name='labratory'),
    path('labratory-to-dr/<int:pk>', views.labratoryToDr, name='labratory-to-dr'),
    path('labratory-result/<int:pk>', views.LabratoryResult, name='labratory-result'),
    
]