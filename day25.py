#polymorphism: overloading(operator, method,constructor), overriding(method,constructor), duck typing, operator overloading
#operator overloading
# print(5+6) # + operator is overloaded to perform addition operation
# print("hello"+ " " + "world") # + operator is overloaded to perform concatenation operation



# class book:
#     def __init__(self,page):
#         self.pages=100
#     def __add__(self,other):
#         return self.pages+other.pages

# b1=book(100)
# b2=book(200)
# print(b1+b2) 

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __gt__(self,other):
#         return self.age>other.age

# s1=student("ajay",24)
# s2=student("vijay",22)
# print(s1>s2)



# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __mul__(self,other):
#        return self.salary*other.days
# class time:
#      def __init__(self,days):
       
#         self.days=days   
# t1=time(25)
# e1=employee("ajay",500)
# print(f" total amount of {e1.name} is:",e1*t1)