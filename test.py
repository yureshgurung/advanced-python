# import add as m # as use for alishing (short name)


# print("add number",m.add(2,3))
# # print("add number",module.add(2,3))#not use aa m


# #directly acess
# #use from ......import
# from module import add # not use a m  we are dirctly acess )

# from module import * # all acess
# print("add number",add(2,3))

# from module import add as sum
# print("add number",sum(2,3))

# #various possibilties of import
# import modulename
# import modulename,  modulename
# import modulename as m
# import modulename as m ,  modulename as m2
# from module import modulename
# from module import modulename ,modulename
# from module import module as sum
# from module import module as sum ,memberr as ms
# from module import * # all acess



#module comflict
# different  module bata same function call garda confilct hunxa
# from module import *
# from module1 import *

# print("sum of two number:", add(2,3))# its form module1 ( first ko lai second le replace garxa)


# #yati malai first ko mmodule chahema
# from module import  add as a
# from module1 import add as b

# print("sum of two number:", a(2,3))



#reloading of module: pvm le(python readable ) yauta module template baunauxa jun chai fast access hos banera
#disadvantage : original module ma change garda chai pvm change hudena 
#then we are use reloading function

# import time
# import module1
# module1.add(3,2)
# print("our program is on sleep")
# time.sleep(15)
# print("our program is wake up")
# # import module1
# import importlib
# importlib.reload(module1)
# module1.add(2,8)

 

#dir() (list dinxa current module bitra k k xa banera dinxa)
# import time
# print(dir(time))

# print(dir())

# help(time)


  #doc string
# """ hi my name is yures """   
# print(__doc__)

print(__file__)

import os 
print(os.path.dirname(os.path.abspath(__file__)))



print(__name__)