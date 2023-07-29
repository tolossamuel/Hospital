from django.forms import ModelForm
from .models import Drug_Stor, drug_request
class DrugAdd(ModelForm):
    class Meta:
        model = Drug_Stor
        fields = '__all__'
class DrugRequestForm(ModelForm):
    class Meta:
        model = drug_request
        exclude = ['patient']

        
        
    

    