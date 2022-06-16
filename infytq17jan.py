
#
# uppercase=0
# for i in s:
#     if i.isalpha():
#         letter+=1
#     if i.isnumeric():
#         digit+=

# """
# A string which is a mixture of letter and integer and special char
# from which find the number form the available digit
# after removing the duplicates.
# if an addition of numbers is not even number return-1.
# Ex: ifosys@334
# o/p: -1
# """

# input=input(": ")
# s=set()  #empty set
#
# for i in input:
#     if i.isdigit():
#         s.add(int(i))
# sum=0
# for i in s:
#     sum=sum=i
# if sum%2==0:
#     print("1")
# else:
#     print("-1")



#Reverse string without slice and reversed:
# eg:  abcd
#o/p->dcba
#using slicing
# s="ABCD"
# s=s[::-1]
# print(s)

#without slicing
# s="ABCD"
# s1=""
# for i in s:
#     s1=i+s1
# print(s1)

# in an airport, the airport authority decides to charge some minimum amount to
# the passengers who are carrying luggage with them. they set a threshold
# weight value, say T, if the luggage exceeds the weight threshold you should
# pay double the base amoount. if it is less than or equal to the
# threshold then you have to pay $1.
