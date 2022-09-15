"""
Создать программу-калькулятор в виде класса и несколько методов, 
как минимум сложение, вычитание, деление, умножение, возведение в степень и извлечение квадратного корня.

Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений, как минимум деление на 0.

Создать своё исключение, к примеру возведение в отрицательную степень.
"""

class Calculator(int):
    
    
    # val_1 = int (input('Введите число 1: '))
    # val_2 = int (input('Введите число 2: '))
    def sqrt(self):
        if "-" in str(self) :
           print("ахахах, иди учи уроки!") 

        else:   
            self = int(self) ** 0.5
            print(self)
                   
    

    def __truediv__(self, other):
        try:
            return int(self)/int(other)
        except ZeroDivisionError:
            print("ZeroDivisionError")
    

    
    
while True:        
   
          
    v =  input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n 5 Квадрат \n 6 Степень\n')
    if not v in ("1","2","3","4","5","6","0"):
        print("func not ex")
        continue 
    if v == "0":
        break
    try:           
        val_1 = int( input("Введите число 1: "))
        if v == "5":
            Calculator.sqrt(val_1)
            continue
        val_2 = int( input("Введите число 2: ") )
    except Exception:
        print("inc val")

    if v == "1":
        print(Calculator(val_1)+val_2)
    if v == "2":
        print(Calculator(val_1)-val_2)
    if v == "3":
        print(Calculator(val_1)/val_2)
    if v == "4":
        print(Calculator(val_1)*val_2)
    if v == "6":
        print(Calculator(val_1)**val_2)
    

    


    