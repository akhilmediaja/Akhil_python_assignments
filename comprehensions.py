#!/usr/bin/env python
# coding: utf-8

# In[1]:


res=[1,2,3,4,5]
r1 = ",".join(res)
print(r1)


# In[3]:


res=[1,2,3,4,5]
res1=[]
for i in res:
    res1.append(str(i))
print(res)
print(res1)
r1 = ",".join(res1)
print(r1)


# In[4]:


res=[1,2,3,4,5]
res1=[str(i) for i in res]# list comprehension
# for i in res:
#     res1.append(str(i))
print(res)
print(res1)
r1 = ",".join(res1)
print(r1)


# In[6]:


def check_even(x):
    return x%2==0
res=[1,2,3,4,5]
res1=[check_even(i) for i in res]# list comprehension
print(res)
print(res1)


# In[7]:


def check_even(x):
    print(x)
    return x%2==0

res=[1,"2",3,4,"5"] #[False, None,False,True,None]
res1=[check_even(i) if isinstance(i, int) else None for i in res ]# list comprehension
print(res)
print(res1)


# In[8]:


def check_even(x):
    print(x)
    return x%2==0

res=[1,"2",3,4,"5"] #[False, None,False,True,None]
res1=[check_even(i) for i in res if isinstance(i, int)]# list comprehension
print(res)
print(res1)


# In[9]:


def check_even(x):
    print(x)
    return x%2==0

res=[1,"2",3,4,"5"] #[False, None,False,True,None]
res1=[check_even(i) for i in res if isinstance(i, int) else None]# list comprehension
print(res)
print(res1)


# In[10]:


def check_even(x):
    print(x)
    return x%2==0

res=[1,"2",3,4,"5"] #[False, None,False,True,None]
res1=[check_even(i) if isinstance(i, int) for i in res ]# list comprehension
print(res)
print(res1)


# In[11]:


def check_even(x):
    print(x)
    return x%2==0

res=["1","2","3","4","5"] #[False, None,False,True,None]
res1=[check_even(i) for i in res if isinstance(i, int)]# list comprehension
print(res)
print(res1)


# In[12]:


def check_even(x):
    print(x)
    return x%2==0

res=[1,"2",3,"4","5"] #[False, None,False,True,None]
res1=(check_even(i) for i in res if isinstance(i, int))# tuple comprehension
print(res)
print(res1)


# In[14]:


def check_even(x):
    return x%2==0

res=[1,"2",3,"4","5"] #[False, None,False,True,None]
res1=(check_even(i) for i in res if isinstance(i, int))# tuple comprehension
print(res)
for i in res1:
    print(i)


# In[15]:


def check_even(x):
    print(x)
    return x%2==0

res=[1,"2",3,"4","5"] #[False, None,False,True,None]
res1=(check_even(i) for i in res if isinstance(i, int))# tuple comprehension
print(res)
print(res1)


# In[16]:


def check_even(x):
    print(x)
    return x%2==0

res=[1,"2",3,"4","5"] #[False, None,False,True,None]
res1=(check_even(i) for i in res if isinstance(i, int))# tuple comprehension
for i in res1:
    print("i=",i)
    break


# In[17]:


l=[1,2,-3,4,5,-6]
res={}
for i in l:
    res.update({i: "+VE" if i>0 else "-VE"})
print(res)


# In[18]:


l=[1,2,-3,4,5,-6]
res={i: "+VE" if i>0 else "-VE" for i in l}
# for i in l:
#     res.update({i: "+VE" if i>0 else "-VE"})
print(res)


# In[ ]:




