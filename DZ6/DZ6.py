"""""
Сделать программу в виде функций в которой нужно будет угадывать число.
"""

from random import randint


def game(value):
    random_value = randint(1, 100)
    print(f"random value: {random_value}")
    while True:
            
        if value.isalpha():
            print("Try to enter the number!")
            value = input("Enter the value:")
            continue
        elif int(value) > random_value:
            print("You so close (your value > hidden value) ", "Try again", sep = "\n") 
            value = input("Enter the value:")  
        elif int(value) < random_value:
            print("You so close (your value < hidden value) ", "Try again", sep = "\n")
            value = input("Enter the value:")
        elif int(value) == random_value:
            print("Congratulations!!!")
            break
    print("Congratulations!!!")
    

value = input("Enter the value: ")
game(value)
print("Congratulations!!!")