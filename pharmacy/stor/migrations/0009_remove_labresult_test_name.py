# Generated by Django 3.2.19 on 2023-08-01 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stor', '0008_labresult_test_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labresult',
            name='test_name',
        ),
    ]