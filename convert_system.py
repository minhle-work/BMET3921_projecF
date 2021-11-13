file_path = '/Users/peterle/Desktop/test_file/'

import csv
file_name_1 = input("Enter file name to search: ")
input_file_path = file_path + file_name_1
print(input_file_path)
file_name_2 = file_name_1[0:-4] +".csv"
output_file_path = file_path + file_name_2
print(output_file_path)
input_file = open(input_file_path, 'r')
lines = input_file.readlines()

separator_pos = []

data_all = []
with open(output_file_path, 'w', newline='') as f:
    the_writer = csv.writer(f)
    the_writer.writerow(["Timestamp", "Product code", "Cb software version", "Temp 1", "Temp 2", "Air temp",
                        "DET", "Patient ctr temp", "Heater Pwr", "Patient mode", "Open bed mode", "Closed bed mode",
                        "Humidity sp", "Relative humidity", "Boost air curtain", "Fan speed", "Heat sink",
                        "Last scale weight", "Oxygen sp", "Oxygen measurement", "SpO2", "Pulse rate", "Alarms"])
    for string in lines:
        index_data = 0
        data_line = []
        for i in range(len(string)):
            if (string[i]==",") | (string[i]=="_"):
                separator_pos.append(i)
        while index_data < 23:
            if index_data == 0:
                data_line.append(string[:separator_pos[index_data]])
            else:
                data_line.append(string[separator_pos[index_data-1]+1:separator_pos[index_data]])
            index_data += 1
        the_writer.writerow(data_line)
        # print(data_line)
        # print(string)
        # print(separator_pos)
        # data_all.append(data_line)
# print(data_all)
input_file.close()


