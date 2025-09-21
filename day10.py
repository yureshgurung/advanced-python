#stirng
#'',""
#its not char all string  in pyhton

# a='a'
# g="yuresyhg"

# print(type(a))
# print(type(g))
# #but are string

# #multi line sting
# #using''' .......'''
# a='''my name is 
# yuresh gurun'''
# print(a)
# a="""my name is 
# yuresh gurun"""
# print(a)


# #escap sequence
# s="my name is \n yuresh gurung"
# print(s)

# s="my name is \" yuresh gurung\""
# print(s)
# s="it\'s  a dog"
# print(s)

# #access the charaters of a string
# # 1 indexing ,2 slicing
# s="my name is yuresh"
# i=0
# print("index of given string in both positive and negativeindex")
# for x in s:
#     print(f"the charaters {x} of positve index is {i} and negative index is {i-len(s)}")
#     i+=1



#slice operator
#beg-index:end index: step(0:n-1)
s="yuresh is a good person"
# print(s[0:5:2])
# #inverse
# print(s[::-1])#resverse gaxa
# print(s[::-2])#yasle chai step ko kam garxa
# b= reversed(s)
# for x in b:
#     print(x  , end="")

# print(s[2:7:-1]) #empty
# print(s[7:2:-1])



#mathmatical operation for string:+,*(concatentiaon and repeation)
# print("hi"+"ram")
# print("yuresh" *4)
# print(len("yuresh"))
# a="ram"
# print(a.__len__())



#membership operator in string(in ,not in)
# a="yuresh"
# print("y" in a)
# print("y" not in a)

#compare operator:<>,<=,>= == !=
# a="Ram"
# b="ram"
# # print(a==b)
# print(a<b)

# print("Yuresh"=="yuresh")
# print(chr(98))
# print(ord("a"))

#string: remove a space :rstip()(right ),lstrip()(left),strip()(both)
# a=input("enter a any name ")
# if a.strip()== "ram":
#     print("name is correct")
# else:
#     print("wrong  name")
 #or
# a=input("enter a any name ").strip()
# if a== "ram":
#     print("name is correct")
# else:
#     print("wrong  name")


#finding substring forward:find(),index(): backword: rfind(),rindex()
# a="yuresh"
# print(a.find("u"))
# # print(a.find("7"))#-1 means “not found”.
# print(a.rfind("u"))#positive index

a="yuresuh"
# print(a.find("u"))
# # print(a.find("7"))#-1 means “not found”.
# print(a.rfind("u"))#positive index
# print(a.find('e',1,5 ))

# print(a.find("t"))#no errror throw but return -1
# print(a.index("t"))#error throw garxa


# print(a.rfind("t"))#no errror throw but return -1
# print(a.rindex("t"))#error throw garxa

# #count:substring  --- count()
# a="ram"
# print(a.count("r"))


# #replace a substring :  rpalce()

# a="ram"
# print(a.replace("r","k"))
# print(a)

# a=" my name is ram gurung".split()#give a list
# print(a)

# w=['my', 'name', 'is', 'ram', 'gurung']
# a=' '.join(w)
# print(a)

#change a case of string
s="my name is yures gurung"
# print(s.upper())
# print(s.lower())
# print(s.swapcase())#yati lower xa bane upper and upper xa bane lower ma lanxa
# print(s.title())#word ko suru ko characters capital garxa
# print(s.capitalize())#paragraph ko suru ko word chai capital banaune


# #checking strarting and ending part of string
# print(s.startswith("my"))
# print(s.endswith("g"))


# #to check type of characters present in a string:isalnum
# print("ram123".isalnum())
# print("ram123".isalpha())
# print("ram123".isdigit())
# print("ram123".islower())
# print("ram123".isspace())

#formatting
name="yuresh"
age=21
print(f"my friend name is {name} and age is {age}")
print("my friend name is {0} and age is {1}".format(name,age))
print("my friend name is {a} and age is {b}".format(a=name,b=age))
print("my friend name is {:105d}".format(123))


print(dir(str))







