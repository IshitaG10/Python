from art import logo

#Calculator

#Addition
def add(a,b):
    return a+b

#Subtract
def subtract(a,b):
    return a-b

#Multiply
def multiply(a,b):
    return a*b

#Divide
def divide(a,b):
    return a/b

operations = {
'+' : add,
'-' : subtract,
'*' : multiply,
'/' : divide
}

def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    should_continue = True
    while should_continue:
        for key in operations:
            print(key)
        
        operator = input("Choose the operation from above: ")
        num2 = float(input("Enter the second number: "))
        func = operations[operator]
        answer = func(num1,num2)
        print(f"{num1} {operator} {num2} = {answer}")

        if input("Type 'y' to continue the calculation with previous answer or type 'n' to start a calculation with new numbers ") == 'y':
            num1 = answer
        else:
            should_continue =  False
            calculator()
    
calculator()