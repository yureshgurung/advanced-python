

# Dynamic Typing:
# Python variables don’t require type declaration.
# The type is determined automatically based on the value.




# Rules for Variables in Python
#  1.Names can contain: letters (a-z, A-Z), numbers (0-9), and underscore _
#         age = 20
#         user_name = "Ram"
#  2.Names cannot start with a number
#  3.Cannot use Python keywords (like if, for, while, True)
#  4.Names are case-sensitive
#         age, Age, AGE are different variables
#  5.Use meaningful names
#  6.Use snake_case for variable names (words separated by underscores) 
#         user_name, total_amount


import keyword
# print(keyword.kwlist)  # List of all Python keywords
a=0b1001
# print(a)  # Octal representation, prints 10
a=12
# print(bin(a))  # Binary representation, prints 0b1100
# print(oct(a))  # Octal representation, prints 0o14
# print(hex(a))  # Hexadecimal representation, prints 0xc 
# print(int('0b1100',2))  # Convert binary string to integer, prints 12
# print(int('0o14',8))  # Convert octal string to integer, prints 12
# print(int('0xc',16))  # Convert hexadecimal string to integer, prints 12    

a=1.2e7
print(a)  # Prints 12000000.0
a=1.2e-3
print((a))  # Prints 0.0012