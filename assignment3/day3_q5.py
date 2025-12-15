def greet(name="Python User"):
    print("Hello",name)
greet()
greet("Tanaya")
def student(name,age):
    print("Name:",name)
    print("Age:",age)

student(age=22,name="Tanaya")
def add(a, b):
    return a + b
def operate(a, b, func):
    return func(a, b)
print("Operation Result:",operate(22,3,add))