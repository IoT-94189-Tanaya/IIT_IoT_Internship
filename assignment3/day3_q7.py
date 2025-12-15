def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
b=int(input("enter num1 for factorial:"))
print("Factorial of b:", factorial(b))
print("Power 3^4:", power(3,4))