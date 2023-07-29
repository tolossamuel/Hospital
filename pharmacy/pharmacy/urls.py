
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stor.urls')),
    path('payment/', include('payment.urls')),
    path('register-nurse/', include('register_patient.urls')),
    path('login/', include('login.urls')),
    path('admin-control/', include('admin_control.urls'))
]
