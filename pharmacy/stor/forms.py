from django.forms import ModelForm,CheckboxSelectMultiple
from .models import Drug_Stor, drug_request,User_lab_temporary
class DrugAdd(ModelForm):
    class Meta:
        model = Drug_Stor
        fields = '__all__'
class DrugRequestForm(ModelForm):
    class Meta:
        model = drug_request
        exclude = ['patient']

class UserLabTemporaryForm(ModelForm):
    class Meta:
        model = User_lab_temporary
        fields = ['Patient_name', 'labs']
        widgets = {
            'labs': CheckboxSelectMultiple,  # Use CheckboxSelectMultiple widget for multi-select labs
        }
        
    

    