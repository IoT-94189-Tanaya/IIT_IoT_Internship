print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
a=int(input("enter choice :"))
b=int(input("enter num1:"))
c=int(input("enter num2:"))
if a==1:
    print(b+c)
elif a==2:
    print(b-c)
elif a==3:
    print(b*c)
elif a==4:
    if c==0:
        print("cannot divide by 0")
    else:
         print(b/c)
else: 
 print("enter correct choice")