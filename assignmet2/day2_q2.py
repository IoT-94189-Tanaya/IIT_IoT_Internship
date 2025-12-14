num=int(input("enter a 5 digit number "))
if num<10000 or num>99999:
    print("the number is not a 5 digit number")
else:
    temp=num
    rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
if temp==rev:
    print("palindrome number")
else :
    print("not palindrome number")
