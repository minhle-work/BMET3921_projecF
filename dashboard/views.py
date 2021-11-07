import csv

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import patient_information, csv_converter

@login_required()
def dashboard(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    return render(request, 'dashboard_home.html', {})

@login_required()
def file_converter(request):
    if request.method == "POST":
        if 'sign_out' in request.POST:
            logout(request)
            return redirect('/')
        elif 'convert_file' in request.POST:
            upload_file = csv_converter(infant_id=request.POST['infant_id'], file=request.FILES['upload'])
            full_name = upload_file.file.name
            name = full_name[:-4]
            csv_name = name + ".csv"
            # print(csv_name)

            separator_pos = []
            input_file = request.FILES['upload'].readlines()
            response = HttpResponse(content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename = "{}"'.format(csv_name)
            writer = csv.writer(response)
            writer.writerow(["Timestamp", "Product code", "Cb software version", "Temp 1", "Temp 2", "Air temp",
                             "DET", "Patient ctr temp", "Heater Pwr", "Patient mode", "Open bed mode",
                             "Closed bed mode",
                             "Humidity sp", "Relative humidity", "Boost air curtain", "Fan speed", "Heat sink",
                             "Last scale weight", "Oxygen sp", "Oxygen measurement", "SpO2", "Pulse rate",
                             "Alarms"])
            for string in input_file:
                reformatted_str = '{}'.format(string.strip()).replace("b\'", "").replace("\'", "")
                index_data = 0
                data_line = []
                for i in range(len(reformatted_str)):
                    if (reformatted_str[i] == ",") | (reformatted_str[i] == "_"):
                        separator_pos.append(i)
                while index_data < 23:
                    if index_data == 0:
                        data_line.append(reformatted_str[:separator_pos[index_data]])
                    else:
                        data_line.append(
                            reformatted_str[separator_pos[index_data - 1] + 1:separator_pos[index_data]])
                    index_data += 1
                # print(reformatted_str)
                # print(data_line)
                writer.writerow(data_line)
            upload_file.save()
            return response
    uploaded_files = csv_converter.objects.all()
    info = patient_information.objects.all()
    return render(request, 'dashboard_fileConverter.html', {"uploaded_files": uploaded_files,
                                                            "info": info})
def delete_profile(request, pk):
    if request.method == "POST":
        profiles = patient_information.objects.get(pk=pk)
        profiles.delete()
    return redirect('file_converter')


@login_required()
def patients_register(request):
    if request.method == "POST":
        if 'submit' in request.POST:
            infant_id = request.POST["infant_id"]
            infant_name = request.POST["infant_name"]
            date_of_birth = request.POST["date_of_birth"]
            parent_name = request.POST["parent_name"]
            phone_num = request.POST["phone_num"]
            email_add = request.POST["email_add"]
            house_add = request.POST["house_add"]
            device_id = request.POST["device_id"]
            date_started = request.POST["date_started"]

            infant_info = patient_information(infant_id=infant_id,infant_name=infant_name, date_of_birth=date_of_birth, parent_name=parent_name, phone_num=phone_num, email_add=email_add,
                                              house_add=house_add, device_id=device_id, date_started=date_started)

            infant_info.save()

            return redirect('file_converter')
        if 'sign_out' in request.POST:
            logout(request)
            return redirect('/')
    return render(request, 'dashboard_info_register.html', {})
