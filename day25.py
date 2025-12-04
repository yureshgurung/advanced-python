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


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __str__(self):
#         return f"student name is {self.name} object"
    

# s1=student("ajay",85)
# s2=student("vijay",90)
# print(s1)
# print(s2)


# class student:
#     def __init__(self,marks):
     
#         self.marks=marks
#     def __add__(self,other):
#         return student(self.marks + other.marks)
#     def __str__(self):
#         return f"total marks are {self.marks}"
    

# s1=student(85)
# s2=student(90)
# s3=student(175)
# print(s1+s2+s3)

# explain:Here is the **shortest and easiest** explanation:
# # ✅ **Short & Easy Explanation**
# ### `s1 + s2 + s3` works like this:
# 1. First:
#    s1 + s2 → student(85 + 90) = student(175)
# 2. Then:
#    student(175) + s3 → student(175 + 175) = student(350)
# 3. `print()` shows:`
#    total marks are 350
# Because your `__add__` method **adds marks and returns a new student object** each time.

# # ⭐ Final Output`
# total marks are 350




# method overriding: not supported ,python dynamic polymorphism
# class Test:
#     def sum(self, *a):# *a means "take any number of arguments"
#         total = 0
#         for x in a:
#             total = total + x
#         print("The sum is : ", total)

# t = Test()
# t.sum()
# t.sum(10)
# t.sum(10, 20)
# t.sum(10, 20, 30)
# t.sum(10, 20, 30, 40, 50, 60, 70, 30, 90)

#constructor overriding not supported in python

# class Test:
#     def __init__(self, *a):
#         print("all accepted")
        
# t = Test()
# t=Test(12,34,45,34)




#overriding(method,constructor)
class p:
    def proverty(self):
        print("i have a bike")
    def money(self):
        print("i have 1 lakh")
class c(p):
    def money(self):#overriding
        super().money()#calling parent class method
        print("i have 5 lakh") 
o=c()
o.proverty()
o.money()

#constructor overriding  
class parent:
    def __init__(self):
        print("parent class constructor")
class child(parent):
    def __init__(self):
        super().__init__()#calling parent class constructor
        print("child class constructor")    
c=child()




#duck typing
class bird:
    def fly(self):
        print("bird is flying")
class aeroplane:
    def fly(self):
        print("aeroplane is flying")
        
def func(obj):
    obj.fly()
i=[bird(),aeroplane()]
for obj in i:
    func(obj)

