#!/usr/bin/env python
# coding: utf-8

# In[1]:


# program to display whether the input character is a digit or alphabet
ch = input("Enter a character: ")
if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
    print(ch, "is an Alphabet")
else:
    print(ch, "it is a number")


# In[ ]:




