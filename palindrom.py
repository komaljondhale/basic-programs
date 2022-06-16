a=int(input("Enter 2 digit number:"))
b=a//10
c=a%10
d=b+c*10
if a==d:
    print("palindrom")
else:
    print("not palindrom")