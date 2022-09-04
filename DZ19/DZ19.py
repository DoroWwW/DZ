
"""
Создать родительский класс auto, у которого есть атрибуты:

brand, age, cоlor, mark и weight.

А так же методы: move, birthday и stop.

Методы move и stop выводят сообщение на экран «move» и «stop»,а birthday увеличивает атрибут age на 1.

Атрибуты brand, age и mark являются обязательными при объявлении объекта.

"""




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
        
            
            


car_1 = Auto(input("Enter the brand of the car: "))
car_1.move()
car_1.stop()
car_1.birthday(input("Enter the age of the car: "))
print(car_1.brand,car_1.age,car_1.color,car_1.mark)
