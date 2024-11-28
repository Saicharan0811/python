#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=5
for i in range(0,5):
    for j in range(0,i+1):
        print(num,end=" ")
    print("\n")
    num=num-1


# In[2]:


a=input("enter any element")
if a.islower():
    print("given input is of lower case characters")
elif a.isupper():
    print("given input is of upper case characters")
elif a.isalnum():
    print("Given input are numbers")
else:
    print("special characters")


# In[4]:


#fibonacci series
a=int(input("enter the number of elements in fibonacci series"))
l=0
i=0
j=1
k=i+j
for l in range(0,a):
    print(i)
    i=j
    j=k
    k=i+j


# In[8]:


count=0
a=int(input("enter the lowest  range"))
b=int(input("enter the upper range"))
for n in range(a,b):
    if(n>0):
        for j in range(1,n+1):
            if(n%j==0):
                count=count+1
                        	
        if(count==2):
            print(n," is a prime number")
        count=0
    else:
        break


# In[12]:


import math as m
num1=int(input())
num2=int(input())
HCF=m.gcd(num1,num2)
LCM=int((num1*num2)/(HCF))
print(LCM)


# In[ ]:





# In[ ]:




