#if we want to represent a unique values
#duplication are not allowed
#insertion order is not preseved(so not applicable a indexing , slicing)
#{}
#set mutable
#set heretogenous
# s={} #dictionary ho hai empty bayo bane
# s={12,34,54,"yuresh "}
# print(s)
 

# r=range(20)
# s=set(r)
# print(s)
# s={23,34,23,45}#duplication not allowed
# print(s)


#indexing and slicing
# print(s[:])#errror
# s.add(84)
# l=[34,65,23,45]
# s.update(l)#update huna lai sequece wa itreative
# print(s)

# s.pop()
# s.pop()
# s.pop()
# s.remove(34) #nabako lai error dinxa
# s.discard(100)#no error 
# print(s)


# #mathmatical operation on set
# s={23,34,23,45}
# d={23,54,83,75}
# print(s.union(d))
# print(s.intersection(d))
# print(s.difference(d))
# print(s.symmetric_difference(d))
#not valit : +,*, ==,!=,,< ......

# #membership operator
# print(23 in s)
# print(23 not in s)






# #set comprehenisve

# s={x for x in range(34) if x%2==0}
# print(s)
 





#dictionary
# python =dict
# c++/java=map
# peri/rupy=hash
# java script=json

#key:value
#key=unique,immutable
#value=heretogenous,mutable
#d={}
# d={1:"yuresh",2:"ram",3:"shara"}
# print(type(d))
# print(d)

# #DUPLICTION value allowed but key not allowed
# d={1:"yuresh",2:"ram",3:"ram"}
# di={1:"yuresh",1:"ram",3:"ram"}
# print(type(d))
# print(d)
# print(di)


# #heretogenous in both key and value
# d={1:"yuresh",2:34,"name":"ram",3:45.67,4:[23,45,67],5:(23,45,67),6:{23,45,67}}
# print(d)

# #mutable
# d={1:"yuresh",2:"ram",3:"shara"}
# d[2]="hari"
# d[4]="new"
# print(d)

#insertion order not preseved

# #accessing value by key
# d={1:"yuresh",2:"ram",3:"shara"}
# print(d[2])


# dict={
#     "name":"yuresh",
#     "age":23,
#     "address":"ktm",
#     "phone":9841234567,
  
# }
# print(dict["name"])


# #list convert into  dictionary
# l=[(1,"ram"),(2,"shyam"),(3,"hari")]
# d=dict(l)
# print(d)

# l=[(1,"ram","error"),(2,"shyam"),(3,"hari")]
# d=dict(l)
# print(d)
# #list -list ,list -tuple , tuple -list, tuple -tuple
# #not valid :set-list 
# l=[[1,"ram"],[2,"shyam"],[3,"hari"]]
# d=dict(l)

#form user
# d=eval(input("enter a dictionary: "))
# print(d)
# print(type(d))

# import ast

# d = ast.literal_eval(input("Enter dictionary: "))
# print(d)
# print(type(d))



# rec={}
# n=int(input("enter a numver of students:"))
# i=1
# while i<=n:
#     name=input("enter name:")
#     age=int(input("enter age:"))
#     rec[name]=age
#     i=i+1   
# print(rec)


# #while i<=n:
#     name=input("enter name:")
#     age=int(input("enter age:"))
#     address=input("enter address:")
#     phone=int(input("enter phone number:"))
#     student={
#         "name":name,
#         "age":age,
#         "address":address,
#         "phone":phone
#     }
#     print(student)
#     i=i+1



# # upadating dictionary
# d={1:"yuresh",2:"ram",3:"ram"} 
# d[2]="hari"
# d[4]="new"
# del d[1], d[3]
# print(d)
# d.clear()
# print(d)

#  #mathamatical operation (not valid : +,*,<,>,<=,>=)
# d={1:"yuresh",2:"ram",3:"ram"} 
# e={1:"yuresh",2:"ram",3:"ram"} 
# print(d==e  )# all equal hunu parxa key and value , order

# #membership operator(only key ma search garxa)
# d={1:"yuresh",2:"ram",3:"ram"} 
# print(2 in d) #key ma search garxa


# #functions (get(),pop() ,popitem()

# d={1:"yuresh",2:"ram",3:"ram"}
# print(d.get(2)) #key ko value return garxa , if key not found then return none
# print(d.get(5,"not found")) #if key not found then return "not found


# print(d.pop(1))
# print(d.pop(8,"not found"))


# #popiterm : ❗Note:
# # Before Python 3.7, dictionaries didn’t preserve insertion order, so popitem() would remove an arbitrary item.
# # But in Python 3.7+, it removes the last inserted item (like a stack - LIFO: Last In, First Out).
# print(d.popitem())
# print(d)


# #key(), values(), items()
# d={1:"yuresh",2:"ram",3:"ram"}
# print(d.keys())
# print(d.values())
# print(d.items)
# for k,v in d.items():
#     print("key:",k,"value:",v)  

# #copy
# d={1:"yuresh",2:"ram",3:"ram"}
# e=d.copy()
# e[6]="add gare"
# print(e)

#update
d={1:"yuresh",2:"ram",3:"ram"}
r={4:"shyam",5:"hari"}
d.update(r)
print(d)



s1 = {10: "Vaskar", 20: "Dipesh"}
s2 = {30: "Sumita", 40: "Nikita"}
s3 = {*s1, *s2}
print(s3)


t1 = (10, 20)
t2 = (30, 40)
t3 = (*t1, *t2)
print(t3)
