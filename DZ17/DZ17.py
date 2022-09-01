"""
Прочитать сохранённый json-файл из задания №16 и записать данные на диск в csv-файл, первой строкой 
которого озаглавив каждый столбец и добавив новый столбец “телефон”.
"""

import csv

import json

fieldname = ["Number","Name","Age"]
with open ("data_name.json") as json_file:
    csv_file = json.load(json_file)  
print(type(csv_file))
with open("data_name_number.csv","w",encoding="utf-8",newline="") as file:
    file_writer = csv.DictWriter(file, fieldnames = fieldname)
    file_writer.writeheader()
    for i ,b in csv_file.items():
        file_writer.writerow({"Number": i, "Name": b[0], "Age":b[1]})