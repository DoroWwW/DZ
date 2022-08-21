"""
Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.

Подсказка:
"""

from datetime import datetime
import random 

time = datetime.now()

def func_time(given_func):
    def the_wrapper():
        start_func = datetime.now()
        given_func()
        elapsed_time = datetime.now() - start_func
        print(f"Elapsed time:{elapsed_time} ")
    return the_wrapper

@func_time
def rand_word():
    word = input("Enter the string: ").upper()
    word = random.choices(list(word), k =len(word)) 
    print(word)


@func_time
def firtree_gen():
    print("\n")
    while True:
        quantity = int(input("Enter the quantity of the pine needles: "))
        if  quantity == 0 or quantity >= 7:
            print("Wrong input!", "The max quantity is 6, min is 1", sep = "\n")
        else:   
            for i in range (1, quantity+1):
                space = (quantity - i)*" "
                i*=2 
                needles = i*"*"
                print(space,needles)
            break   
    print((quantity-1)*" ","|" )
        


# word = input("Enter the string: ").upper()
rand_word()
firtree_gen()
    

# while True:
#         quantity = int(input("Enter the quantity of the pine needles: "))
#         if  quantity ==0 or quantity >= 7:
#             print("Wrong input!", "The max quantity is 6, min is 1", sep = "\n")
#         else:
#             break

# firtree_gen(quantity)



