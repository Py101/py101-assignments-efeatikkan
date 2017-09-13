
# coding: utf-8

# In[21]:

from functools import reduce


# In[24]:

def factor(x):
    listx=[z for z in range(1,x+1)]
    
    fun_la=lambda a,b: a*b
    zz=reduce(fun_la,listx)
    print(zz)


# In[26]:

factor(4)


# In[ ]:



