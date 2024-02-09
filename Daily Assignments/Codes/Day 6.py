#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python program to reverse a number(123=321)
no=int(input("Enter The No."))
reversedno=0
while no!=0:
    remainder=no%10
    no=no//10
    reversedno= reversedno*10 + remainder
print(reversedno)


# In[ ]:


#Python program to check a palindorme(12321)(Iterative)
no=int(input("Enter The No."))
original=no
reversedno=0
while no!=0:
    remainder=no%10
    no=no//10
    reversedno= reversedno*10 + remainder
if original==reversedno:
    print("It is a palindrome")
else:
    print("it is isnt")


# In[ ]:


n=int(input("Enter The No."))
flag=False
for i in range(2,n):
    if n%i==0:
        flag=True
        print("Not prime")
        break
if flag==False:
    print("prime")


# In[ ]:


#Find a factorial of the number

factorial=1
num=int(input())


if num==0 or num==1:
    print("Factorial of the num is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)

