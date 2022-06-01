#### This is how to make a simple calculator using python

def add(x,y):
    return print(x + y)

def subtract(x,y):
    return print(x - y)

def multiply(x,y):
    return print(x * y)

def divide(x,y):
    return print(x / y)

print( "To select an operation enter; \n 1-add,\n 2-subtract, \n 3-multiply, \n 4-divide")

x = 6
y = 4

while True:
    operation = int(input("Choose an operation: "))
    if operation in (1, 2, 3, 4):
        if operation == 1:
            add(x, y)
        elif operation == 2:
            subtract(x, y)
        elif operation == 3:
            multiply(x, y)
        elif operation == 4:
            divide(x, y)

        next_calc  = float(input("Another calculation? 1-Yes, 2-No"))
        if next_calc == 2:
            break
        
    else:
        break






