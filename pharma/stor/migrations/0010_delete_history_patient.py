# Generated by Django 3.2.19 on 2023-07-25 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stor', '0009_remove_doctor_patient_history'),
    ]

    operations = [
        migrations.DeleteModel(
            name='History_patient',
        ),
    ]
