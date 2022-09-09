








class String(str):
    def __init__(self, string):
        self.string = str(string)
        
    def __add__(self, other):
        if type(other) == String:
            return self.string + str(other.string)
        return self.string + str(other)
    
    def __sub__(self, other):
        if type(other) == String:
            substring = str(other.string)
        substring = str(other)
        if substring in self.string:
            return self.string.replace(substring, "")
        return self.string
        
string1 = String("fdsf")
string2 = String(2343)

print(string1 + string2)
print(string1 + 1)
print(String("132") - "13")
print(String("va7ll1") - 7)