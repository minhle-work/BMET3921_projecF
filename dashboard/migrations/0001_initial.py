# Generated by Django 3.2.9 on 2021-11-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient_information',
            fields=[

                ('infant_name', models.TextField(default='', editable=False, max_length=1000)),
                ('date_of_birth', models.DateField()),
                ('parent_name', models.TextField(default='', editable=False, max_length=1000)),
                ('phone_num', models.TextField(default='', editable=False, max_length=100)),
                ('email_add', models.TextField(default='', editable=False, max_length=100)),
                ('house_add', models.TextField(default='', editable=False, max_length=300)),
                ('device_id', models.TextField(default='', editable=False, max_length=100)),
                ('date_started', models.DateField()),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]