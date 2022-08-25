


def value_analysis(value):
    
    minus = False
    minus_wrd = "отрицательное"
    plus_wrd = "положительное"
    integer_wrd = "целое"
    fractional_wrd = "дробное"
    
    
    if value[0] == "-":
        minus = True
        value = value.replace("-","",1)

    if "," in value:
        value = value.split(",")
    elif "." in value:
        value = value.split(".")
        
    elif minus == True:
        if value.isdigit():
            return f"{minus_wrd} {integer_wrd} -{value} "
        else:
            return f"inc input: {value} "

    elif minus == False:
        if value.isdigit():
            return f"{plus_wrd} {integer_wrd} {value} "
        else:
            return f"inc input: {value} "
#-----------------------------------------------------------

    if len(value) == 2 and (value[0].isdigit() or value[0] == "") and value[1].isdigit():
        if minus == True:
            value = ".".join(value)
            return f"{minus_wrd} {fractional_wrd} -{value} "

        elif minus == False:
            value = ".".join(value)
            return f"{plus_wrd} {fractional_wrd} {value} "
    else:
        return f"inc input: {value} "
        
while True:
    users_step = input("""Enter the value:", "Stop the program("выход", "exit", "quit", "e", "q")""").lower()
    if users_step in ("выход", "exit", "quit", "e", "q"):
        break
    else:
        print(value_analysis(users_step))

