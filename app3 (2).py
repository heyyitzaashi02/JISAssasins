#!/usr/bin/env python
# coding: utf-8

# In[2]:


# find out maximum and minimum number

n=int(input("enter the number of element in the array: "))
list=[]
for i in range(0,n):
    number=int(input("enter the number of your choice: "))
    list.append(number)
print("you entered: {}".format(list))  
list.sort()
print("maximum element = {}".format(max(list)))
print("minimum element = {}".format(min(list)))


# In[ ]:




