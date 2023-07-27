# Generated by Django 3.2.19 on 2023-07-27 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug_Stor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_drug', models.CharField(default=None, max_length=100)),
                ('quantity_drugs', models.IntegerField(default=0)),
                ('price_per_drug', models.IntegerField(default=0)),
                ('descriptions_drug', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Register_Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Middle_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('full_name', models.CharField(default='', max_length=100)),
                ('Age', models.IntegerField(default=0)),
                ('Sex', models.CharField(choices=[('Male', 'M'), ('Female', 'F')], max_length=10)),
                ('Address', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=15)),
                ('Emergency_Phone_Number', models.CharField(max_length=15)),
                ('Created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['Created_at'],
            },
        ),
        migrations.CreateModel(
            name='History_patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hisory_text', models.TextField(max_length=100000000)),
                ('patient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stor.register_patient')),
            ],
        ),
        migrations.CreateModel(
            name='drug_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now=True)),
                ('drug_name', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stor.register_patient')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name_Dr', models.CharField(max_length=50)),
                ('Last_name_Dr', models.CharField(max_length=50)),
                ('time_with_patient', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stor.register_patient')),
                ('patient_history', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stor.history_patient')),
            ],
        ),
    ]
