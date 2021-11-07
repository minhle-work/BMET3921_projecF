# Generated by Django 3.2.9 on 2021-11-06 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_patient_information_infant_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_information',
            name='house_add',
        ),
        migrations.AddField(
            model_name='patient_information',
            name='address_1',
            field=models.TextField(default='', editable=False, max_length=300),
        ),
    ]
