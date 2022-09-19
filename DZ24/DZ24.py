

"""Создать генератор геометрической прогрессии"""






def g_progression(start, step, size):
    count = 1
    while count <= size:
        yield start
        start *= step
        count += 1

start = int(input("Start value: "))
step =int(input("Step of prog: "))
size = int(input("Quantity of prog: "))

for ele in g_progression(start, step, size):
    print(ele)