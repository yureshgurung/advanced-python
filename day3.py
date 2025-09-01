#complex data type
a=3+4j
b=5-2j
# print(type(a))  # Prints <class 'complex'
# print(a.real)  # Prints 3.0
# print(a.imag)  # Prints 4.0 

# print(a+2)  # Prints (5+4j)
# print(a*2)  # Prints (6+8j)
# print(a+b)  # Prints (8+2j)
# print(a*b)  # Prints (23+2j)  
# print(abs(a))  # Prints 5.0 (magnitude of the complex number)
# print(a==b)  # Prints False
# print(a!=b)  # Prints True
# print(a**2)  # Prints (-7+24j) (square of the complex number)
# print(a/b)  # Prints (0.24+0.76j) (division
# print(pow(a,2))  # Prints (-7+24j) (a raised to the power of 2)
# print(complex(2,3))  # Prints (2+3j) (create complex number from real and imaginary parts)
# print(complex('1+2j'))  # Prints (1+2j) (
 

# boolean data type# print(type(True))  # Prints <class 'bool'>
a= True 
b= False 
# print(a+b)
# print(type(a+b))  # Prints <class 'int'>
  
#string data type
s="yuresh"
s2="gurung"
# print(s+s2)  # Prints yureshgurung
# print(s +" "+ s2)  # Prints yuresh gurung


# slicing string sytnax
# string_name[start_index:end_index-1]
# -3 -2 -1 0r 0 1 2
y="my name is yuresh guurng"
# print(y[0:7])  # Prints my name
# print(y[11:17])  # Prints yuresh
# print(y*2)
# print(len(y))
# print(y[0].upper()+y[1:])  # Prints My name is yuresh guurng



# type casting
# fundamental_data_type  = int, float, complex, bool, str
# a=3
# print(type(a))  # Prints <class 'int'>
# print(float(a))  # Prints 3.0
# print(complex(a))  # Prints (3+0j)
# print(bool(a))  # Prints True
# print(type(str(a)))  # Prints '3'
t="uursh"
# print(int(t))  # ValueError: invalid literal for int() with base 10: 'uursh'
y="123"
print(int(y))  # Prints 123




r=2.3
# print(int(r))  # Prints 2
e=3+4j
print(str(e))  # Prints (3+4j)
# print(int(e))  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'complex'
# print(bool(0.0))