"""""
Сделать программу в виде функций в которой нужно будет угадывать число.
"""

from random import randint


def game(value):
    random_value = randint(1, 100)
    print(f"Random value: {random_value}")
    while True:
        if value is None or value.isalpha():
            value = input("Enter the valuE:")
           
        elif int(value) > random_value:
            print("You so close (your value > hidden value) ", "Try again", sep = "\n") 
            value = None
        elif int(value) < random_value:
            print("You so close (your value < hidden value) ", "Try again", sep = "\n")
            value = None
        elif int(value) == random_value:
            print("Congratulations!!!")
            break
    
    

value = input("Enter the value: ")
game(value)
