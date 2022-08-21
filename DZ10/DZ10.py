"""Дан список состоящий из данных разного типа. 

Вернуть новый список, где при помощи функции map() каждый элемент типа int первоначального списка приведён к типу str, 
элементы всех остальных типов передаются в новый список без изменения их типа. 

В качестве входной функции в map() использовать lambda-функцию.
"""

from copy import deepcopy

values = [1, 2, '3', 'forth', 'end', 99, True, None]
values_others = []
values_int = list((map(lambda x: str(x) if type(x) == int  else values_others.append(x)  , deepcopy(values))))
# убираем None
#values_int = [i for i in values_int if i] 
values_int = [i for i in values_int if i is not None]
#values_int = list(filter(None, values_int))

print(values_int)
print(values_others)
