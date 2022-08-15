"""
Написать программу которая получит имя и возраст пользователя, проверяет возраст и выдаёт приветственное сообщение 
в зависимости от возраста:

- меньше нуля или ноль или не число: “Ошибка, повторите ввод”;

- больше нуля до 10 не включая: “Привет, шкет #Имя#”;

- от 10 до 18 включая: “Как жизнь #Имя#?”

- больше 18 и меньше 100: “Что желаете #Имя#?”

- в противном случае: “#Имя#, вы лжете - в наше время столько не живут...”

Программу необходимо завернуть в вечный цикл.

После очередной отработки кода, спрашивать у пользователя 'Желаете выйти? (Д/Y)'. 
Если ответ будет буква 'Д' или буква 'Y' в любом регистре, то произвести выход из вечного цикла. 
В противном случае продолжить выполнение программы заново.

"""






while True:

    name = input("Enter your name: ").title()
    age = input("Enter your age: ")

    if  age.isalpha() or int(age) <= 0 or not name.isalpha():
        print(">>Incorrect input<<", "   >Try again<", sep = "\n" )
        continue
    elif int(age)<10: 
        print(f"Hi {name} Jr. !")
    elif 10 <= int(age) <= 18:
        print(f"How it's going {name}?" )
    elif int(age) < 100:
        print("What you want {}?".format(name))
    else:
        print("%s you are lier, unfortunately, people don't live that long..."%(name))
    
    answer = input("""Want to stop? ("y"/"д"):""").lower()
    if answer in ("y", "д"):
        break

#Пшеничний Дмитро