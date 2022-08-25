# a = input("a: " )
# if int(a.find(".",0)) != -1 or a.find("-",0,1) != -1:
#     print("minus")
# else:
#     print("plus")

#  if value[0] == "-":
#             if value.find(".",0) != -1 or value.find(",",0) != -1 : #dasdsad 
#                 return f"{minus},{fractional},{value}"
#             else:
#                 return f"{minus},{integer},{value}"
#         else:
#             if value.find(".",0) != -1 or value.find(",",0) != -1 :
#                 return f"{plus},{fractional},{value}"
#             else:
#                 return f"{plus},{integer},{value}"


value = "54,5"
#value = list(value)
# dot = []
# for i in value:
#     if i == "." or i == "," or i == "-":
#         dot.append(i)
#     elif not i.isdigit:
#         del value


# print(value)
# print(dot)



#value_1 = list(map(lambda x:x.replace(","," ",1),value))   
a = "1010001000100010010111001011"
value = value.replace(",", a)

print(value)
print( value.isdigit())
value = value.replace(a,",")
print(value)