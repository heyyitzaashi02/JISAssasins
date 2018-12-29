#!/usr/bin/env python
# coding: utf-8

# In[1]:


# program to swap the values of two variables using call by reference

# To take input from the user
# x = input('Enter value of x: ')
# y = input('Enter value of y: ')

x = 5
y = 10
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# In[ ]:




