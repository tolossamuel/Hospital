# Generated by Django 3.2.19 on 2023-07-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_user_login_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_login',
            name='filed',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user_login',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
