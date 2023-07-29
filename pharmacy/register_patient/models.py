from django.db import models
from login.models import user_login
# Create your models here.
sex = (
    ("Male","M"),
    ("Female","F"),
)
class Register_Patient(models.Model):
    """Model definition for Register_Patient."""

    First_Name = models.CharField(max_length=50)
    Middle_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Full_Name = models.CharField(max_length=200)
    Father_Name = models.CharField(max_length=150)
    Mother_Name = models.CharField(max_length=150)
    Age = models.IntegerField(default=0)
    Sex = models.CharField(max_length=10,choices=sex,default="None")
    Address = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=15)
    Emergency_Phone_Number = models.CharField(max_length=15)
    Birth_Day = models.DateField()
    Created_at = models.DateTimeField(auto_now=True)
    Nurse_Checked = models.BooleanField(default=False)

    class Meta:
        ordering = ['Created_at']
        
    def save(self, *args, **kwargs):
        self.Full_Name = f"{self.First_Name} {self.Middle_Name} {self.Last_Name}"
        super(Register_Patient, self).save(*args, **kwargs)
    def __str__(self):
        """Unicode representation of Register_Patient."""
        return self.Full_Name

class Doctors(models.Model):
    """Model definition for Doctors."""
    Name = models.CharField(max_length=100)
    Doctor_Field = models.CharField(max_length=150)
    Room = models.IntegerField(default=0)

    def __str__(self):
        """Unicode representation of Doctors."""
        return self.Name
class patient_nurse(models.Model):
    nurse = models.ForeignKey(user_login, on_delete=models.CASCADE)
    patient = models.ForeignKey(Register_Patient, on_delete=models.CASCADE)

class Nurses(models.Model):
    """Model definition for Nurse."""
    patient = models.ForeignKey(Register_Patient,on_delete=models.PROTECT)
    status = models.TextField(max_length=700)
    doctor = models.ForeignKey(user_login,on_delete=models.PROTECT)
    
    def __str__(self):
        """Unicode representation of Nurse."""
        return self.patient.Full_Name

class Drug_Stor(models.Model):
    name_drug = models.CharField(max_length=100, default=None)
    quantity_drugs = models.IntegerField(default= 0)
    price_per_drug = models.IntegerField(default= 0)
    descriptions_drug = models.TextField(max_length=1000)
    def __str__(self):
            return self.name_drug

class Prescribe_Request(models.Model):
    patient = models.ForeignKey(Register_Patient, on_delete=models.PROTECT)
    prescribe_time = models.DateTimeField(auto_now = True)
    prescribe_medication = models.CharField(max_length=100)
    prescribe_doctor = models.ForeignKey(Doctors,on_delete= models.PROTECT)
    def __str__(self):
        return self.patient.First_Name

class Patient_History(models.Model):
    patient = models.ForeignKey(Register_Patient, on_delete=models.PROTECT)
    doctor = models.ForeignKey(user_login,on_delete=models.PROTECT)
    history_text = models.TextField(max_length=100000000)
    history_time = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.patient.First_Name