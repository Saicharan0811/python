#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Calculator
a=int(input("enter a number"))
b=int(input("enter a number"))
print("add:",a+b)
print("sub:",a-b)
print("multiplication:",a*b)
print("division:",a/b)


# In[2]:


#Indentation Error 
a=5
    b=2
print("add:",a+b)
#correct program
a=5
b=2
Print(“add:”,a+b)


# In[3]:


#compound interest
#p=principle,r=rate,t=time period,CI=compound interest,A=amount after time period
p=1000
r=2
t=3
A=p*((1+r/100)**t)
CI=A-p
print("amount after time period",A)
print("compound intrest:",CI)


# In[4]:


x1=int(input("enter the x1 value"))
x2=int(input("enter the x2 value"))
y1=int(input("enter the y1 value"))
y2=int(input("enter the y2 value"))
d=((x1-x2)**2+(y1-y2)**2)**(1/2)
print("distance between two given points is ",d)


# In[5]:


name=input("enter your name  ")
email_id=input("enter your email-id  :")
phone_no=int(input("enter your phone number  :"))
address=input("enter your address :")
print("Name:",name)
print("Email-id:",email_id)
print("Phone-no:",phone_no)
print("Address:",address)


# In[ ]:




