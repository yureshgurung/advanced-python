# a=input("ennter number:"   )
# if a==2:
#     print('true')
# else:
#     print('false')

# a=input("ennter number:"   )
# if a==2:
#     print('true')
# elif a==3:
#     print('false')
# elif a==4:
#     print('maybe')
# else:
#     print('not in range')

#assigments
#smallest 3nunmber
# a=int(input("enter 1st number:"))
# b=int(input("enter 2nd number:"))
# c=int(input("enter 3rd number:"))
# if a<b and a<c:
#     print(a,"is smallest")      
# elif b<a and b<c:
#     print(b,"is smallest")  
# else:
#     print(c,"is smallest")


# # odd and even
# num=int(input("enter a number:"))
# if num%2==0:
#     print(num,"is even")
# else:
#     print(num,"is odd")

#switch statement
sub=input("enter subject:")
match sub:
    case "math":
        print("maths is good subject")
    case "science":
        print("science is good subject")
    case "english":
        print("english is good subject")
    case _:
        print("no subject found")


#using switch case
# list1=[0,1,2,3,4]
# n=int(input("enter a number:"))
# print(list1[n] if n<len(list1) else "no value found")


x = 15
if x > 10:
    if x % 2 == 0:
        print("Greater than 10 and Even")
    else:
        print("Greater than 10 and Odd")

