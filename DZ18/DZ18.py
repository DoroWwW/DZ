"""
Прочитать сохранённый csv-файл из задания №17 и сохранить данные в excel-файл, кроме возраста – столбец с
 этими данными не нужен.

К заданию прикреплён пример как должно выглядеть содержания итогового файла.




Внимательно прочитайте задание и посмотрите прикреплённую к нему картинку. 
Данные в таблице необходимо перевернуть: данные про каждого человека необходимо
читать не слева-направо, а сверху-вниз.

"""
from random import randint
import pandas as pd
import csv
import openpyxl


def rand_id_gen():
    id_list = []
    for i in range(5):
        id_users = randint(1000,9990)
        id_list.append(id_users)
    return id_list

def person_num():
    users_pers = []
    for i in range(5):
        users = f"Person{i+1}"
        users_pers.append(users)
    return users_pers


book = openpyxl.Workbook()
sheet = book.active

user_pers = person_num()
row_number = 3
your_column = 4

id_list = rand_id_gen() 
row_number = 3
your_column = 3

def create_add_col(row_number,your_column,id_list):
    for i, value in enumerate(id_list, start=row_number):
        sheet.cell(row=i, column=your_column).value = value 


with open("data_name_number.csv",newline="") as csv_file:
    xlsx_file = csv.reader(csv_file)
    print(type(xlsx_file))
    sheet.insert_cols(1)
    
    
    for row in xlsx_file:
        sheet.append(row)
    sheet.delete_cols(3)
    sheet["C2"] = "User Id"
    create_add_col(3,3,id_list)
    create_add_col(3,4,user_pers)
   
    
   
   


# for row in sheet['A1:G37']:
#   for cell in row:
#     cell.value = None

       
# sheet["A2"] = 100
# sheet[1][0].value = "world"
# sheet.cell(row=1,column=1).value = "Hola"

book.save("data_name.xlsx")

df = pd.read_excel('data_name.xlsx')
df.T.to_excel('data_name.xlsx', index=False)
book = openpyxl.load_workbook('data_name.xlsx')
sheet = book.active
sheet.move_range("B5:F5", rows=-4)
sheet["A1"]=None
book.save('data_name.xlsx')


