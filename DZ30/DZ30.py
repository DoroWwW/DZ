
"""Так же есть пару замечаний по коду:

1) зачем переопределять __init__ и писать self.string = str(string). Ведь вы же наследуетесь от типа str. 
Там и так значение приведено к типу str... И зачем заводить новую переменную self.string и в неё записывать 
значение приведённое к str. Ведь у вас родительский класс, там и так уже self это значение типа str )))

2) проверять на String: if type(other) == String: исходя из предыдущего замечания никакого смысла нет.
 Можно существенно упростить код"

"""





class String(str):
    
        
    def __add__(self, other):
       
        return String(str(self) + str(other))
        
    
    def __sub__(self, other):
        
        if str(other) in str(self):
            return String(self.replace(str(other), ""))
        return String(self)
        
string1 = String("fdsf")
string2 = String(2343)
        
print(string1 + string2)
print(String("sdf") + 1)
print(String("132") - "13")
print(String("va7ll1") - 7)