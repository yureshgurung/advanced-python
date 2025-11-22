#types of method
 #instance method ,class method,static method
 
 
 #instance method: at least one refrence variable(class bitra) ,  1st agr self, inside class = selg and outside class = reference variable
 
 
# class Student:
#     def __init__(self,name, marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("hi",self.name)
#         print("your marks is ", self.marks)
#     def grade(self):
#         if self.marks>=80:
#             print("first grade") 
#         elif self.marks>=50:
#             print("second grade")
#         else:
#             print("your are fail ..")
        
        
# n=int(input("please enter a how manny student?/.   "))
# for i in range(n):
#     name=input("enter you name:")
#     marks=int(input("enter a marks:"))
#     s=Student(name,marks)
#     s.display()
#     s.grade()
#     print()        



#2 special instance methos : setter()/mudator: bahira  bata initialize , getter(),accessor:

#setter:  def setVariable(self, variable)
#getter: def getVarialbe (self)  return self.variable


# class Student:
#     def setName(self,name):
#         self.name=name
        
#     def getName(self):
#         return self.name
    
#     def setmarks(self,marks):
#         self.marks=marks
        
#     def getmarks(self):
#         return self.marks
 
# n=int(input("please enter a how manny student?/.   ")) 
# for i in range(n):
#     s=Student()
#     name=input("enter you name:")
#     s.setName(name)
    
#     marks=int(input("enter a marks:"))
#     s.setmarks(marks)
#     print("hi",s.getName())    
#     print("your are marks is", s.getmarks())
#     print()



#class method

# class Kale:
#     dept="computer"
#     @classmethod
#     def works(cls):
#       print(f"kale has {cls.dept} department")
# # a=Kale()
# # a.works()
# Kale.works()



# instance method vs class method



# #static method
# class A:
#     @staticmethod
#     def  add(x,y):
#         print("sum:",x+y)
        
#     @staticmethod
#     def subtract(x,y):
#         print("subtract:",x-y)
# A.add(5,6)  
# A.subtract(9,4)







#inner class

# class Outer:
#     def __init__(self):
#         print('i am outer class ')
#     class Inner:
#         def __init__(self):
#                print('i am inner class')
#         def m(self):
#                    print("inener method")

# i=Outer()
# a=i.Inner()
# a.m()

# i=Outer().Inner()  # good
# i.m()

# i=Outer().Inner().m()

# #automatic call class
# class Human:
#     def __init__(self):
#         self.name="ram"
#         self.Brain=self.Brain()
#         self.Head=self.Head()
        
#     class Brain:
#         def __init__(self):
#                print('i am brain')
#         def m(self):
#                    print(" brain inener method")
#     class Head:
#         def __init__(self):
#                print('i am head class')
#         def m(self):
#                    print(" head method")

# h=Human()
# h.Head.m()



# method within in method 
class Test:
    def m(self):
        def cal(a,b):
            print('sum',a+b)
            print('sub',a-b)
        cal(4,3)
        cal(8,3)
t= Test()
t.m()