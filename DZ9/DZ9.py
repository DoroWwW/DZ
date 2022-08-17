"""""
Дан словарь, создать новый словарь при помощи конструкции генератор словаря, поменяв местами ключ и значение.
"""

#def make_dict(length):
    #dict_made = {}
    #i = 1
    #for i in range(length+1):
        #key = input(f"Enter the {i} key: ")
        #value =  input(f"Enter the {i} value: ")
        #dict_made.items(key, value)
        
   #print (dict_made)
    #return dict_made


#len = int(input("Enter the dict length"))
#make_dict(len)

from random import randint


old_dict = {1: 'dr', '5':'34', '-65':"bc", None: 0.76, 102: "1323BB"}
new_dict = {value: key for key, value in old_dict.items()}
print(new_dict)

"""def gen_dict(length):
    
    d ={}
    for i in range(length):
        d[randint(1,100)] = randint(1, 100)
    print(d)

a  = int(input("a: "))
gen_dict(a) """