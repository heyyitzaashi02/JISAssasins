#!/usr/bin/env python
# coding: utf-8

# In[1]:


#(Q-17) program to accept n number and store all prime numbers in array and display the array

class Prime:
    def check(self,p):
        print("Prime numbers are\n")
        for self.x in p:
            self.flag=0
            for self.i in range(2,self.x):
                if (self.x%self.i==0):
                    break
                else:
                    
                    print(self.x)
                    break
            
li=[]
n=int(input("Enter how many number you want to insert"))
print("Enter the numbers")
i=0
while(i<n):
    li.append(int(input()))
    i=i+1
gk=Prime()
gk.check(li)


# In[ ]:




