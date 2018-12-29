#!/usr/bin/env python
# coding: utf-8

# In[1]:


# program for accept basic salary

salary = int(input("enter your 1st no \n"))
if salary< 5000:
    hra=(15*salary)/100
    da=(150*salary)/100

    print("hra is",hra)
    print("da is",da)
    print("gross is",(hra+da+salary))

else:
    hra=(10*salary)/100
    da=(110*salary)/100

    print("hra is",hra)
    print("da is",da)
    print("gross is",(hra+da+salary))


# In[ ]:




