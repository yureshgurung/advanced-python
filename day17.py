# print("hi")
# import math 
# # help(math)
# print(math.sin(90))



#random module (for use a data science game devolpment , cryptography)
import random
# for i in range(10):
    # print(random.random())
    
    
    
# print(random.randint(1,6))
# print(random.uniform(1,20))




from random import *
# otp=''
# for i in range(6):
#     otp=otp+str(randint(0,9))
# print(otp)

#or
# print(randint(000000,999999))  # yasma 6 ota nai aauxa bane xaina


#fake data generate
alphabets="kdkdghkshjds ksdfjfkds"
digit="0123456789"
cities=['ktm','pokha','rampur','yampur']
designation=['qa','devops','ai/ml','backend']



def fake_name():
    name=choice(alphabets).upper()
    n=randint(0,9)
    for i in range(n):
        name=name +choice(alphabets)
        return name
print(fake_name())




# #python package
# function = collection of code 
# module= collection of  class, function, ....
# package= collection of module(__init__ .py)



