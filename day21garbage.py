import gc
# print(dir(gc))
# gc.disable()
# gc.enable()
# print(gc.isenabled())




# # destructor
# # def __del__(self):
# class Test:
#     def __init__(self):
#        print("this is constructor ")
#     def __del__(self):
#         print("this is destructor")
# t=Test()
# print("end of application")
# #destructor last ma call bayaxa 


# #aba bich ma call hunxa ki nai  chieck(object delete bayasi matra call)
# import time
# class Test:
#     def __init__(self):
#        print("this is constructor ")
#     def __del__(self):
#         print("this is destructor")
# t=Test()
# print("consructor is call")
# time.sleep(5)
# t1=t
# t2=t
# del t
# print("t reference is delete. ")
# time.sleep(5)
# del t1
# print("t1 is delete")
# time.sleep(5)
# del t2
# print("t2 is delete")



class Test:
    def __init__(self):
       print("this is constructor ")
    def __del__(self):
        print("this is destructor")
l=[Test(),Test(),Test()]