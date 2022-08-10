"""
Ввести с клавиатуры целое число n.

Получить сумму кубов всех целых чисел от 1 до n(включая n). Исключения составляют все числа кратные цифре 3.

Реализовать в 2-х вариантах: используя цикл while и цикл for
"""

value = int(input("Enter the value: "))
sum = 0
for i in range(1, value+1):
 if not i % 3 == 0:   
    print(f"{i}^3 =", end = " ")
    i **=3
    print(i)
    sum += i
    print(f"sum:{sum}")

print(f"Total sum: {sum} ")

print("-------------method while------------")
counter = 0
i = 1 
sum = 0
while counter <= value:
    if counter % 3 == 0:
        counter += 1
        continue
    print(f"{counter}^3 =", end = " ")
    i = counter**3
    print(i)
    sum += i
    print(f"sum:{sum}")
    counter += 1
    


#Пшеничний Дмитро