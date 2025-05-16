import Ayush
import Tanmay
import Samridhi





def calc(a, b, op):
        
    if op == '-':
        Tanmay(a,b)
        
    elif op == '*':
        Samridhi(a,b)
        
    elif op == '/':
        Ayush(a,b)
        
    else:
        return "Invalid operation"


try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    op = input("Enter the operation (-, *, /): ")

    result = calc(a, b, op)
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numeric values.")
