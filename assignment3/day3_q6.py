def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a,b):
    return a/b
def module(a,b):
    return a%b
def calculate(op1, op2, operation):
    return operation(op1, op2)
print(calculate(20, 5, add))
print(calculate(25, 8, subtract))
print(calculate(30, 4, multiply))
print(calculate(34, 2, divide))
print(calculate(24, 5, module))