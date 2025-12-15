def add(a,b):return a+b
def sub(a,b):return a-b
def mul(a,b):return a*b
def div(a,b):return a/b
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
 
ch=int(input("enter your choice:"))
a=int(input("enter num1:"))
b=int(input("enter num2:"))

if ch==1:
 print(add(a,b))
elif ch==2:
 print(sub(a,b))
elif ch==3:
 print(mul(a,b)) 
elif ch==4:
 print(div(a,b))
else:
 print("enter valid choice...")
