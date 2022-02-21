#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
    factorial = 1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            factorial *= i
    return factorial


# In[2]:


factorial(8)


# In[3]:


factorial(0)


# In[4]:


def factorial_rec(n):
    if n == 0:
        return 1
    return factorial_rec(n-1)


# In[5]:


factorial(5)

