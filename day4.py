#list
a=[1,2,3,4,1]
# print(a)
# print(id(a))  # Prints <class 'list'>
# print(type(a))  # Prints <class 'list'>
# a.append(1) 
# print(a)  # Prints [1, 2, 3, 4, 1, 5]
# a.remove(1)
# print(id(a))  # Prints [2, 3, 4, 1, 5]
# a[2]=10
# print(a)  # Prints [2, 3, 10, 1,
# a.insert(2,7)
# print(a)  # Prints [2, 3, 7, 10,
# print(id(a))  # Prints the memory address of the list

# t = [1, 2, 3]
# t[1] = 10  # Error! Cannot change a tuple


# print(id(a))  # Prints the memory address of the list
# for x in a:
#     print(x)    


# tuples
#  but immutable
# immutable list 
# b=(1,2,3,4,1)
# # a=(1)
# # print(type(a))  # Prints <class 'int'>
# print(b)
# print(type(b))  # Prints <class 'tuple'>


#set
# unordered collection of unique elements
# no indexing, slicing, or other sequence-like behavior
#without duplicate
#mutable
# q={}
# print(type(q))  # Prints <class 'dict'>
# c={1,2,3,4,1}
# print(type(c))  # Prints <class 'set'>
# print(c)  # Prints {1, 2, 3, 4}
# c.add(5)
# print(c)  # Prints {1, 2, 3, 4,
# c.add(3)
# print(c)  # Prints {1, 2, 3, 4,
# c.remove(2)
# print(c)  # Prints {1, 3, 4, 5}


#frozenset
# immutable version of a set
# # cannot be changed after creation
# d=frozenset([1,2,3,4,1])
# print(type(d))  # Prints <class 'frozenset'>
# print("hi")
# print("hi bro")





#dictionary
# key value pair
# unordered collection
# mutable








#dictionary
# key value pair
# unordered collection
# mutable

dic={

    "name":"john",
    "age":30,
    "city":"newyork"
}
# print(type(dic))
# print(dic)
# print(dic["name"])
# dic["age"]=31
# print(dic)
# dic["name"]="love"

# dic["studentid"]=45
# print(dic)

# #range
# r=range(10,5,-1)
# print(type(r))
# # for i in r:
# #   print(i)

# print(r[0])
# print(r[2:3])

#bytes

b=[12,34,43]
# b=bytes(23,45,45)
by=bytes(b)
print(type(by))
print(b) 
