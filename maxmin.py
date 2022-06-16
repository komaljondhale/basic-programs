a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a>=b and a>c:
    print("a is greater")
elif b>c and c>a:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
