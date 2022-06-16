#A
# for row in range(7):
#     for col in range(5):
#         if ((col == 0 or col == 4) and row != 0) or  ((row==0 or row ==3 ) and (col>0 and col<4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
#B
# for row in range(7):
#     for col in range(4):
#         if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row ==6) and (col>0 and col<4)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
#C
# for row in range(7):
#     for col in range(4):
#         if (col == 0 and (row!=0 and row!=6)) or ((row==0 or row == 6) and col>0):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()
#D
# for row in range(7):
#     for col in range(4):
#         if (col == 0) or (col ==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()
###########################################
# for row in range (5):
#     for col in range(5):
#         print("*",end=" ")
#     print() (i+1
##################################
# for i in range(4):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# for i in range(5):
#       for j in range(i+1):
#           print("*",end=" ")
#       print()

x = 'machine learning'
for i in range(len(x)):
       x[i].upper()
print (x)