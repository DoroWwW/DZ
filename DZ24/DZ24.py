

"""Создать генератор геометрической прогрессии"""



def g_progression(i):

    while i >0:
        i -=1
        yield i**3
        

enter = int(input("Quantity of cubes: "))

for i in g_progression(enter):
    print(i)