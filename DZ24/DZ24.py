

"""Создать генератор геометрической прогрессии"""



def g_progression(i):

    for value in range(i):
        yield 3**value
        value += 1
        

enter = int(input("Quantity of cubes: "))

for i in g_progression(enter):
    print(i)