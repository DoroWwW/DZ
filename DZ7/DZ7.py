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
        quantity = 0
        for j in new_list:
            if i == j:
                quantity +=1
            
                same_e[i] = quantity
            
    return same_e    



new_list = list_gen()

print(same_elements(new_list))
