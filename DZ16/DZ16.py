"""
Созадать словарь в качестве ключа которого будет 6-ти значное число, а в качестве значений кортеж 
состоящий из 2-х элементов – имя(str), возраст(int). Сделать около 5-6 элементов словаря. 
Записать данный словарь на диск в json-файл.

"""
import random
import json


def rand(n=6):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

dict_2 = {}
names = ["John","Bob","Luke","Matt","Jake"]
for i in range(5):
    dict_2[rand()] = (names[i], random.randint(1,99))
print(dict_2)

with open("data_name.json", "w") as name_file:
    jsonfile = json.dump(dict_2, name_file, ensure_ascii=False)

