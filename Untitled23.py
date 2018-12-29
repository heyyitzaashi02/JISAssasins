#!/usr/bin/env python
# coding: utf-8

# In[2]:


# program to perform the following string using standard library function
X = input("Enter your string")
l=len(X)
print("The length is", l)
Y = "Amisha"
Z= X+Y
print("After concatenation", Z)
print(''.join(reversed(X)))
old="I like Python"
new=old.replace("like","love")
print(new)
if X == Y:
    print("Equal")
else:
    print("Not Equal")


# In[ ]:




