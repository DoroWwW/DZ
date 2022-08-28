"""
Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).

Создать файл и записать в него первые 2 строки и закрыть файл.

Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.

В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.
"""

from pickletools import string1


first_str = input("Enter the first string: ")
second_str = input("Enter the second string: ")
third_str = input("Enter the third string: ")
fourth_str = input("Enter the fourth string: ")
non_loop = lambda x: x + "\n"
with open("test15", "w") as file:
    file.write(first_str + "\n")
    file.write(second_str + "\n")
with open("test15", "a") as file:
    file.write(third_str + "\n")
    file.write(fourth_str + "\n")
