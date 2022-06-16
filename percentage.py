m1=float(input("Enter m1"))
m2=float(input("Enter m2"))
m3=float(input("Enter m3"))
m4=float(input("Enter m4"))
m5=float(input("Enter m5"))
p=(m1+m2+m3+m4+m5)*(0.2)
print(p)
if p>=90:
    print("grade A")
elif p>=80:
    print("grade B")
elif p>=70:
    print("grade C")
elif p>=60:
    print("grade D")
elif p>=40:
    print("grade E")
else:
    print("Fail")