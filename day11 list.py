#list:group of element single entity ,dullplication allowed, insertion oreder is preserved
#properties: [],duplication allowed,insertion order is presevered(jun oder ma xanot change a oder ), heterogenous object are allowed,dynamic nature
# list=[10,23,51,45,10,"radheradhe"]

# # print(type(list))
# list.append(500)
# list.remove(10)
# print(list)
# a=[]
# print(a)
# l=eval(input("enter a list:"))
# print(l)
# print(type(l))

#output:
# enter a list:[10,23,45,63,41]
# [10, 23, 45, 63, 41]
# <class 'list'>

# l=list(range(10,23))
# l=list("yuresh")
# print(l)
# print(type(l))

#list access by two method: index ,  slice
# l=[10,43,34,34,34]
# print(id(l))
# # print(l[4])
# # print(l[-2])
# # print(l[5::-2])
# l[0]=12
# print(id(l))
# print(l)#mutuble

#traversisng of element of list
# l=[12,34,23,5,3,23]
# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

# for x in l:
#     print(x)


# #important  function of list
# # count(),len(),index()
# l=[12,34,23,5,3,23]
# print(len(l))
# print(l.count(10))
# print(l.index(3))


# #manupulating element of list
# l=[12,34,23,5,3,23]
# l.append(42)
# l.append("ram")
# print(l)
l=[]
# a=input("enter a  list number for storing:")
# print(a)
# l.append(a)
# print(l)
# for i in range(50,101):
#     if i%2==0:
#         l.append(i)
# print(l)



# l=[12,34,23,5,3,23]
# l.insert(1,788)
# print(l)

# l=[12,34,23,5,3,23]
# l[1]=23
# print(l)

 
# #extent function
# l=[12,34,23,5,3,23]
# k=["ram","radhe","radhe"]
# l.extend(k)
# # l.append(k)#list nai yak single hunxa
# # l.extend("ram")
# l.remove("ram")
# print(l)


# #remove all repeation 
# l=[12,34,23,5,3,23,34,35,34]
# x=int(input("enter a remove value:"))

# for i in l:
#     if x==i:
#         l.remove(x)
# print(l)

# while True:
#     if x in l:
#         l.remove(x)
#     else:
#         break
# print(l)


# pop()
# l=[12,34,23,5,3,23,34,35,34]
# l.pop()
# l.pop(4)#index ansur remove 4=3
# print(l)


# #order of element
# l=[12,34,23,5,3,23,34,35,34]
# l.reverse()
# print(l)


# #sort
# l=[12,34,23,5,3,23,34,35,34]
# l.sort()
# l.reverse()
# print(l)
# l=["ram",'ahd' 'dkfjdf']
# l.sort()
# print(l)

# #alissing and cloning
# l=[12,34,23,5,3,23,34,35,34]
# m=l
# print(id(l))
# print(id(m))
# m[1]=12
# print(m)
# print(l)
# l=[12,34,23,5,3,23,34,35,34]
# m=l[:] # or l.copy()
# print(id(l))
# print(id(m))
# m[1]=12
# print(m)
# print(l)
# l.clear()
# print(l)
 

# x=[12,34,54,64]
# y=[45,56,78,23]
# print(x+y)
# print(x+[67])
# print(x*2)
# print(x==y)


# x=[23,54,454,34,34]
# print(23 in x)
# x=[23,54,454,34,34,[23,45,34]]
# print(x[5][2])


# #list comprehensive vvvimp
# l=[]
# numbers=[i for i in range(1,5)]
# print(numbers)

# l=[]
# for i in range(1,5):
#     l.append(i)
# print(l)

# l=[]
# numbers=[i*i for i in range(1,5)]
# print(numbers)


# words=['ram', 'don','shyam']
# print([i[0] for i in words])



# x=[23,54,454,34,34]
# print([i for i in x if i%2==0])



l="my name is yuresh gurung".split()
p=[[x.upper(),len(x)]for x in l]
print(p)

