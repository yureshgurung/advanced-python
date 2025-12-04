# # abstraction and interface
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass    

# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width * self.height

# r=Rectangle(5,10)
# print("Area of Rectangle:",r.area())

# #public ,protected , private
# class Test:
#     def __init__(self):
#         self.public_var="i am public"  #not use _
#         self._protected_var="i am protected" #only use _ single underscore
#         self.__private_var="i am private" #use __ double underscore
# t=Test()
# print(t.public_var)           # Accessible
# print(t._protected_var)       # Accessible (by convention, should be treated as protected)
# #print(t.__private_var)      # Not Accessible, will raise AttributeError
# print(t._Test__private_var)   # Accessible through name mangling

# #public: Accessible from anywhere
# #protected: Accessible within the class and its subclasses
# #private: Accessible only within the class but can be accessed using name mangling
# class Test:
#     def __init__(self):
#         self.__c=30      #private
#     def m1(self):
#         print(self.__c)
# t=Test()
# t.m1()
# print(t._Test__c) #accessing private variable using name mangling
# #tehi bayara python teti private banera teti use no 


#data hiding
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def get_balance(self):
        #validation or other logic can be added here
        return self.__balance
acc = Account(1000)
print("Account Balance:", acc.get_balance())  # Accessing balance via public method
# print(acc.__balance) 


#abstraction: hiding internal details and showing only essential features


