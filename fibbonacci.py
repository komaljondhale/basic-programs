# n=int(input("Enter no. of terms"))
# P=0
# N=1
# print(P,N,end=' ')
# i=1
# while i<=n:
#     R=P+N
#     print(R,end=' ')
#     P=N
#     N=R
#     i=i+1

#################################################
# n=int(input("Enter number:"))
# i=2
# while i<n:
#     if n%i==0:
#         print("Not prime no.")
#         break
#
#     i=i+1
# if n==1:
#     print("Prime")
######################################################
#wap to print all no. between 1 to 100
#
######################################################
#wap to take year input from user and print its roman equivalent
n=int(input("Enter no:"))
while n>0:
    if n>=1000:
        print("m",end=' ')
        n=n-1000
    elif n>=500:
        print("d",end=' ')
        n=n-500
    elif n>=100:
        print("c",end=' ')
        n=n-100
    elif n>=50:
        print("l",end=' ')
        n=n-50
    elif n>=10:
        print("x",end=' ')
        n=n-10
    elif n>=5:
        print("v",end=' ')
        n=n-5
    else:
        print("i",end=' ')
        n=n-1
