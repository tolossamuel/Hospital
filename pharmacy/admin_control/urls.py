from django.urls import path
from . import views
app_name = 'admin_control'
urlpatterns =[
    path('', views.admin_login, name = 'admin_login'),
    path('control-worker', views.control_worker, name= 'control_worker'),
    path('add-staff', views.add_staff, name= 'add_staff')
]