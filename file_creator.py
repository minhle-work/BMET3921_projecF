import random

file_path = '/Users/peterle/Desktop/test_file/'
file_name = input("Enter file name: ")
output_file_path = file_path + file_name
print(output_file_path)
i = 0
#Simulation duration
duration = int(input("Simulation duration: "))

#String parameters
time_frame = "time"
product_code = "HYB"
control_sw_ver = "1.40"
temp_1 = input("Enter probe status (OPEN or CONNECTED): ").upper()
temp_2 = input("Enter probe status (OPEN or CONNECTED): ").upper()
air_temp = ""
DET = input("Desired environment temperature: ")
patient_control_temp = input("Desired control temperature: ")
heater_power = "100"
patient_mode = input("Patient mode (P or N): ").upper()
open_bed_mode = input("Open bed mode (O or N): ").upper()
closed_bed_mode = input("Closed bed mode (C or N): ").upper()
humidity_sp = "00"
humidity_relative = "063"
boost_air_curtain = "D"
fan_sp = "L"
heat_sink = "02043"
last_scale_weight = "0000"
oxy_sp = "00"
oxy_measure = "43"
spO2 = "000"
pulse_rate = "000"
alarms = "03"
end = "00"

index = 0
combined = ""
connect_status_1 = False
connect_status_2 = False
if 'CONNECTED' in temp_1:
    connect_status_1 = True
if 'CONNECTED' in temp_2:
    connect_status_2 = True
parameters = []
file = open(output_file_path, 'w')
while i<duration:
    if connect_status_1:
        temp_1 = str(round(random.uniform(float(patient_control_temp) - 1, float(patient_control_temp) + 0.5), 1))
    if connect_status_2:
        temp_2 = str(round(random.uniform(float(patient_control_temp) - 1, float(patient_control_temp) + 0.5), 1))
    air_temp = str(round(random.uniform(float(DET) - 1, float(DET) + 0.5), 1))
    parameters = [time_frame, product_code, control_sw_ver, temp_1, temp_2, air_temp, DET, patient_control_temp,
                  heater_power, patient_mode, open_bed_mode, closed_bed_mode, humidity_sp, humidity_relative,
                  boost_air_curtain, fan_sp, heat_sink, last_scale_weight, oxy_sp, oxy_measure, spO2, pulse_rate,
                  alarms, end]
    while index < 24:
        if index == 0:
            combined = parameters[index] + ","
        elif index == 1:
            combined = combined + parameters[index] + "_"
        elif index == 23:
            combined = combined + parameters[index]
        else:
            combined = combined + parameters[index] + ","
        index += 1

    file.write(combined)
    if i != (duration-1):
        file.write("\n")
    i += 1
    index = 0
file.close()

