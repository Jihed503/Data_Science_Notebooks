#!/usr/bin/env python
# coding: utf-8

# In[6]:


# s: input string
def acronym_generator(s):
    # let's make a list containing the string words
    s_list = s.split()
    
    acr = '' #initialising the acronym
    for i in s_list:
        acr += i[0]
    return acr


# In[7]:


acronym_generator("North Atlantic Treaty Organization")

