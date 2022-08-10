#!/usr/bin/env python
# coding: utf-8

# # 1. Character Input
# 
# <i>Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.</i>

# In[1]:


name = input("Enter your Name: ")
age = int(input("Enter your age: "))
year = 2022 - age + 100
print(name + ", you will be 100 years old in the year " + str(year))


# In[ ]:




