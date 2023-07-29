# Generated by Django 3.2.19 on 2023-07-29 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register_patient', '0003_patient_nurse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_history',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]