# s="yuresh"
# for x in s:
#     print(x)


# s=input("enter a string:")
# i=0
# for x in s:
#     print(f"index of {x} is {i}")
#     i=i+1# i+=1


# for x in range(12,24,2):
#     if x%2==0:
#         print(x)

# list=eval(input("enter a list:"))
# sum=0
# for x in list:
#     sum=sum+x
# print("sum is:",sum)
# x=1
# while x<=10:
#     if x%3==0:
#         print(x)
#     x=x+1


# sum of n natural numbers

# n=int(input("enter a number:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("sum is:",sum)


# simple project
# print("what are calculate a sum,difference,product,division")
# match input("enter a choice:"):
#     case "sum":
#         a=int(input("enter 1st number:"))
#         b=int(input("enter 2nd number:"))
#         print("sum is:",a+b)
#     case "difference":
#         a=int(input("enter 1st number:"))
#         b=int(input("enter 2nd number:"))
#         print("difference is:",a-b)
#     case "product":
#         a=int(input("enter 1st number:"))
#         b=int(input("enter 2nd number:"))
#         print("product is:",a*b)
#     case "division":
#         a=int(input("enter 1st number:"))
#         b=int(input("enter 2nd number:"))
#         if b!=0:
#             print("division is:",a/b)
#         else:
#             print("cannot divide by zero")
#     case _:
#         print("invalid input")

#ifinite loop
# i=1
# while True:
   
#     i=i+1
#     print("yuresh",i)




#nested loop
# for i in range(1,6):
#     for j in range(6,12):
#         print(i,j)
# 
# n=int(input("enter row:"))
# m=int(input("enter column:"))
# for i in range(n):
#     for j in range(m):
#       print("#",end=" ") 
#     print()
        

# for j in range(5,0,-1):
#         print("#" * j)


# for i in range(5,0,-1):
#         ro=5-i
#         print(" "*ro + "#" * i)
    
# rows = 6
# for i in range(rows, 0, -1):
#     spaces = rows - i
#     print(' ' * spaces + '#' * i)\


# for i in range(5,0,-1):
#        print("#"*i)
# for i in range(1,5,1):
#        print("#"*i)

# for i in range(1,5,1):
#     for j in range(5):
#             print(i  ,end=" ")          
#     print("")

#output:
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j  ,end=" ")          
#     print("")
# #output:
# 1 
# 1 2
# 1 2 3
# 1 2 3 4         
    

# for i in range(6,1,-1):
#     for j in range(1,i-1):
#         print(j ,end=" ")
#     print("")


# n = 5
# for i in range(n):
#     for j in range(n):
#         print('*', end='') 
#     print()



# for j in range(1,6 ):
#         print(" " * (5-j)+"#"*j,)
# print("")


# n = 5
# for i in range(n):
    
#     for j in range(i, n):               # स्पेस प्रिन्ट गर्छ — left side खाली ठाउँ
#         print(' ', end='')

#     for j in range(i + 1):              # पहिलो set of '*'
#         print('*', end='')

#     for j in range(i + 1):              # दोश्रो set of '*'
#         print('*', end='')

#     print()                             # लाइन ब्रेक (new line)


# n = 5
# for i in range(n):
#     # spaces
#     for j in range(n - i - 1):
#         print(' ', end='')
#     # stars
#     for j in range(2 * i + 1):
#         print('*', end='')
#     # new line
#     print()


# for i in range(5):
#     if i ==2:
#         break
#     print(i)


# for i in range(5):
#     if i ==2:
#         continue
#     print(i)


# l=[120,340,560,230,450]
# for x in l:
#     if x>=500:
#         print("high value so i cannt buy ...:",x)
#         continue
#     print("low value:",x)


#for else
# l= [23,45,67,89,12]
# for i in l:
#     if i==100:
#         print("found")
#         break
# else:
#     print("not found")


#pass
# class a:
#     pass


# if True:
#     pass
# else:
#     print("hello")


#del statement

# s="yuresh"
# a=s
# b=a 
# del s
# print(a)



# differrent between del and none
# x=10
# x= None
# print(x)

#assignment 
#prime number
#strong number
# palindrome number/strong
# armstrong number
# factorial number
# fibonacci series
# swap two numbers
#harshad (nivent) number
# perfect number
#twin prime number


#prime number
# n=int(input("enter a number:"))
# if n<2:
#    print("not prime number")
# else:
#     for i in range(2,n):
#         if n%i==0:
#            print("not prime number:") 
#            break
#     else:
#       print("its prime number")




#  📌 Example 1:

# Number = 145

# Digits → 1, 4, 5
# 1!=1
# 4!=24

# 5!=120
# 1+24+120=145

# ✅ Yes, 145 is a Strong Number


# n=int(input("enter a number:"))
# temp=n
# sum=0
# while temp>0:
#     d=temp%10
#     f=1
#     for i in range(1, d+1):
#          f=f*i
#     sum=sum +f
#     temp= temp//10  #It is used to remove the last digit of a number after processing it.

# if sum==n:
#      print("it's a strong number")    
# else:
#      print("not storng ")


#palindrome
# n=int(input("enter number:"))
# temp=n
# rev=0

# while temp>0:
#      digit=temp%10
#      rev=rev*10+digit
#      temp=temp//10

# if rev==n:
#      print(n,"is palindrome number")
# else:
#      print("not palindrome"


#armstrong
n=int(input("enter number:"))
p=len(str(n))
temp=n
sum=0
while temp>0:
    digit=temp%10
    s=digit**p
    sum=sum+s
    temp//=10
    
if n==sum:
    print(n,"is a armstrong ")
else:
    print("not a armstrong")