#hi
# try:
#     print(10 / 0   )
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
    
    
# try:
#     print(10 / 10  )
# except ZeroDivisionError:
# #     print("Cannot divide by zero.")
# try:
#     x=int(input("Enter a number: "))
#     y=int(input("Enter another number: "))
#     result = x / y
#     print(f"The result of {x} divided by {y} is {result}.")
# except BaseException as e:
#     print("Type of exception:", type(e))
#     print("class name of exception:", e.__class__.__name__)
#     print(f"An error occurred: {e}")
# finally:
#     print("Execution completed.")
    
    
    
    

#nested try except
# try:
#     a = int(input("Enter a number to divide 100: "))
#     try:
#         result = 100 / a
#     except ZeroDivisionError:
#         print("Cannot divide by zero.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
# finally:
#     print("Execution completed.")    



#building execption and userdefined execption

#user defined execption
class young(Exception):
    def __init__(self, age):
        self.age = age

class old(Exception):
    def __init__(self, age):
        self.age = age
        
age = int(input("Enter your age: "))
if age < 18:
    raise young("your age is too low87")
elif age > 60:
    raise old("your age is too high")
else:
    print("You are eligible.")




