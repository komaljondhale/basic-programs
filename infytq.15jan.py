# n=int(input("Enter number"))
# fact = 1
# i=1
# while i<n:
#     fact = fact*i
#     i=i+1
#     print("FACt is:",fact)

#Factorial
# n=int(input("Enter no: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
################################################3

#find the strong number(Strong number is a special number whose sum of the factorial of digits is equal to the original number.)145=1!+4!+5!==145

def strong_num(num):
    sum = 0
    fact = 1
    temp = num  #temp=145
    while num>0:
        rem=num%10  #rem=5
        num=num//10 #num=14
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    fact=1
    if sum==temp:
        print("This is strong no",sum)
    else:
        print("This is not strong no",sum)
strong_num(456)
