a=int(input("Enter 3 digit  no:"))
b=a//100
c=a%100
d=c//10
e=c%10
f=b+c*10
if a==f:
    print("reverse")
else:
    print("not reverse")