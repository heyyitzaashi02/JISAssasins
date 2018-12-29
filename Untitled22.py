#!/usr/bin/env python
# coding: utf-8

# In[1]:


# program to accept three sides of triangleas input and print whether the trangle is valid or not
def checkValidity(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True        

a = int(input("value 1: "))
b = int(input("value 2: "))
c = int(input("value 3: "))

if checkValidity(a, b, c): 
    print("Valid")  
else: 
    print("Invalid") 


# In[ ]:




