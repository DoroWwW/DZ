"""""
Сделать программу в виде функций в которой нужно будет угадывать число.
"""

from random import randint


def game():
    random_value = randint(1, 100)
    print(f"Random value: {random_value}")
    while True:
        value = input("Enter the value: ")
        if value is None or value.isalpha():
            continue
           
        elif int(value) > random_value:
            print("You so close (your value > hidden value) ", "Try again", sep = "\n") 
            value = None
        elif int(value) < random_value:
            print("You so close (your value < hidden value) ", "Try again", sep = "\n")
            value = None
        elif int(value) == random_value:
            print("Congratulations!!!")
            break
    
    

#value = input("Enter the value: ")
game()
