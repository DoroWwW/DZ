"""
Написать лямбда-функцию определяющую чётное/нечётное.

Функция принимает параметр (число) и если чётное, то выдаёт слово “чётное”, если нет - то “не чётное”.
"""

check_value = lambda value: print("even") if value%2==0 else print("odd")

value = int(input("Enter the value: "))
check_value(value)