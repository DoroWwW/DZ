"""""
Дан список чисел.

Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.

Подсказка: для хранения данных использовать словарь (ключ - само число, а значение - сколько раз оно встречается).
 Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in.
 """

from random import randint


def list_gen():
    length = int(input("Enter the length of list: "))
    new_list = []
    for i in range(length):
        new_list.append(randint(1,10))
    print(new_list)
    return new_list

def same_elements(new_list):
    same_e = {}
    for i in new_list:
        if same_e.get(i):
            same_e[i] += 1
        else: 
            same_e[i] = 1

    return same_e    



new_list = list_gen()

print(same_elements(new_list))
