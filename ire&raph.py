x = float(input("Enter a number: "))
y = float(input("Enter a number: "))
operators = input("choose an operator (+, -, *, /): " )


# addition
if operators == "+" :
    result = x + y          # handles float
    to_int = int(result)
    if result.is_integer():
        if x.is_integer():  
            x = int(x)
        if y.is_integer():
            y = int(y)
        print(f"{x} + {y} = {to_int}")
    else: 
        print(result)       # handles float

# subtraction
elif operators == "-" :
    result = x - y
    to_int = int(result)
    if result.is_integer():
        if x.is_integer():
            x = int(x)
        if y.is_integer():
            y = int(y)
        print(f"{x} - {y} = {to_int}")
    else: 
        print(result)

# multiplication
elif operators == "*" :
    result = x * y
    to_int = int(result)
    if result.is_integer():
        if x.is_integer():
            x = int(x)
        if y.is_integer():
            y = int(y)
        print(f"{x} * {y} = {to_int}")
    else: 
        print(result)

# division
elif operators == "/" :
    if y == 0:
        print("undefined")
    else:
        result = x / y
        to_int = int(result)
        if result.is_integer():
            if x.is_integer():
                x = int(x)
            if y.is_integer():
                y = int(y)
            print(f"{x} / {y} = {to_int}")
        else: 
            print(result)
            
else:
    print("SYBAU, Choose a valid operator")
