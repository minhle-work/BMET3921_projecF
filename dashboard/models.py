from django.db import models

class patient_information (models.Model):
    infant_id = models.TextField(max_length=100, default="", editable=False)
    infant_name = models.TextField(max_length=1000, default="", editable=False)
    date_of_birth = models.DateField()
    parent_name = models.TextField(max_length=1000, default="", editable=False)
    phone_num = models.TextField(max_length=100, default="", editable=False)
    email_add = models.TextField(max_length=100, default="", editable=False)
    house_add = models.TextField(max_length=300, default="", editable=False)
    device_id = models.TextField(max_length=100, default="", editable=False)
    date_started = models.DateField()

    def __str__(self):
        return self.infant_name

class csv_converter (models.Model):
    infant_id = models.TextField(max_length=100, default="", editable=False)
    file = models.FileField(upload_to="txt_files/")
