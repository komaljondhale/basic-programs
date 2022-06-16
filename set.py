#Boolean
# a=True
# b=False
# print(type(a))
# print(type(b))

# a=bool(123)
# b=bool(0)
# c=bool("1")
# d=bool(1)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

#set
# set is an unordered collecton of items each item must be
# unique and ummutable. however a set itself is mutable.
# we can add or remove items from it. set can also use to
# perform mathematical operation like union intersection,
# difference etc.

# s1={10,20,30,40,50,'A',1.2,(1,2,3)}
# print(type(s1))
# print(s1)

#creating empty set using set function
# s1=set()
# print(type(s1))

#creating set object by using set function and list data
# s2=set([10,20,30])
# print(s2)
# print(type(s2))


#set methods
s1={10,20,30,40,10,20,30}
print(s1)
#add: add single item
s1.add(123)
print(s1)
#update: add multiple item
s1.update([7,8,9])
print(s1)
s1.update("abc")
print(s1)
s1.update({50:'A',60:'B'})
print(s1)
#remove
s1.remove(50)
print(s1)
#discard
s1.discard(200)
print(s1)
#set operations
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
print(s1|s2) #union
print(s1&s2) #intersection
print(s1-s2) #difference
print(s1^s2) #symmetric_difference

s1={1,2,3,4,5}
s2={4,5,6,7,8}
#isdisjoint()
print(s1.isdisjoint(s2))

#issubset()
s1={1,2,3,4,5,6,7,8,}
s2={1,2,3}
print(s1.issubset(s2))
print(s2.issubset(s1))

#issuperset()
s1={1,2,3,4,5,6,7,8}
s2={1,2,3}
print(s1.issuperset(s2))
print(s2.issuperset(s1))

#frozen set
f=frozenset([1,2,3])
print(type(f))

s1=input()
print(s1)
list2=s1.split(",")
print(list2)
arr=list(map(int,list2))
print(arr)
