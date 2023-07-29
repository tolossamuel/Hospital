from django.forms import ModelForm
from .models import Drug_Stor

class DrugAdd(ModelForm):
    class Meta:
        model = Drug_Stor
        fields = '__all__'