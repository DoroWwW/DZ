"""
Создать 2 класса truck и car, которые являются наследниками класса auto из предыдущего домашнего задания.

Класс truck имеет дополнительный обязательный атрибут max_load.

Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention»,
 его реализацию сделать при помощи оператора super.!!!--!!!

А так же дополнительный метод load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение
 «load» и снова пауза 1 сек.

Класс car имеет дополнительный обязательный атрибут max_speed и при вызове

метода move, после появления надписи «move» должна появиться надпись

«max speed is <max_speed>». Вместо <max_speed> должно выводится значение обязательного атрибума max_speed.

Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.

"""
import time

class Auto:


    brand = "Honda"
    age = 0
    color = "black"
    mark = "Civic"
    weight = 1

    def __init__(self,brand,age=0,mark = "Civic"):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print("Move")
        

    def stop(self):
        print("Stop")

    def birthday(self,years):
        print(years)
        def loop(years):
            if not years.isdigit():
                print("Try again")
                years = input()
                loop(years)
            years = int(years) + 1
            self.age = years
            print(self.age)
        loop(years)


class Truck(Auto):
    def __init__(self,max_load):
        while True:
            if not max_load.isdigit():
                max_load = input("Try again: ")
            else:
                break

        self.max_load = max_load
        
    #так тоже можно
    # def func_time(given_func):
    #     def the_wrapper():
    #         print("1sec")
    #         time.sleep(1)
    #         given_func()
    #         time.sleep(1)
    #         print("1sec")
        
    #     return the_wrapper

    
    def load(self):
        print("1sec")
        time.sleep(1)
        print("load")
        time.sleep(1)
        print("1sec")



    def move(self):
        print("attention")
        super().move()
        



class Car(Auto):
    
    def __init__(self,max_speed):
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is{self.max_speed}")




truck_1 = Truck(input("Enter the max load: "))
truck_1.move() 
truck_1.load()
print(truck_1.max_load)
car_1 = Car(input("Enter the max speed: "))
print(car_1.max_speed)
car_1.move()
