"""
Написать программу которая состоит из вечного цикла ожидающего ввод числа или одно из значений:
"выход", "exit", "quit", "e" или "q" в любом регистре. При вводе одного из этих значений происходит выход 
из вечного цикла. При любом другом вводе вызывается отдельная функция которая умеет распознавать введённые числа.
Сама функция ничего не распечатывает, она возвращает строку, типа: "Вы ввели отрицательное дробное число: -6.7" или 
"Вы ввели не корректное число: Erdf"

Затем в цикле выводится это сообщение и цикл начинается заново ожидая следующего ввода.

Функция на вход принимает строку из ввода из вечного цикла. Анализирует её исключительно методом .isdigit() и 
другими методами строк, без доп.библиотек и переводит строку в число, если это возможно.

Функция умеет распознавать отрицательные числа и десятичные дроби, а так же распознаёт десятичные дроби как с точкой, так и
 с запятой.

Функция возвращает строку в которой описывается какое число введено - отрицательное или положительно, целое или дробное и 
выводит его или же сообщает, что введено не корректное число.

*Дополнительно: правильно распознаётся десятичная дробь без первого значащего нуля



Примеры:

-6,7 → Вы ввели отрицательное дробное число: -6.7

5 → Вы ввели положительное целое число: 5

5.4r → Вы ввели не корректное число: 5.4r

-.777 → Вы ввели отрицательное дробное число: -0.777

"""






def value_analysis(value):
    def check_float(value):
        if value.find(".",0) != -1 or value.find(",",0) != -1 : 
                return f"{fractional}"
        else:
            return f"{integer}"

    def replace(value):
        a = "1010001000100010010111001011"
        b = "1010001000111111001011100101"
        if  value.find(".",0) != -1: 
            value = value.replace(".", a,1)
        elif value.find(",",0) != -1:
            value = value.replace(",", a,1)
        if value[0] == "-":
            value = value.replace("-", b,1)
        return value
    def unreplace(value):
        a = "1010001000100010010111001011"
        b = "1010001000111111001011100101"
        if  value.find(a, 0) != -1: 
            value = value.replace(a,"." ,1)
        elif value.find(a, 0) != -1:
            value = value.replace(a, ",",1)
        if value.find(b, 0) != -1:
            value = value.replace(b, "-",1)
        return value
    minus = "отрицательное"
    plus = "положительное"
    integer = "целое"
    fractional = "дробное"
    value = replace(value)
    if not value.isdigit() or value =="":
        return  f"inc input{unreplace(value)}"
    else:
        value = unreplace(value)
        if value[0] == "-":
                check_float(value)
                return f"{minus},{check_float(value)},{value}"
        else:
            check_float(value)
            return f"{plus},{check_float(value)},{value}"

while True:
    users_step = input("""Enter the value:", "Stop the program("выход", "exit", "quit", "e", "q")""").lower()
    if users_step in ("выход", "exit", "quit", "e", "q"):
        break
    else:
        print(value_analysis(users_step))



    

