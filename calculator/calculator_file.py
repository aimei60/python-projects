def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculator(a, b, operation):
    
    if operation == "addition":
        print(addition(a, b))
    elif operation == "subtraction":
        print(subtraction(a, b))
    elif operation == "multiplication":
        print(multiplication(a, b))
    elif operation == "division":
        print(division(a, b))
    else:
        return "Invalid input."
        
calculator(5,4,"multiplication")