#!/usr/bin/env python
# coding: utf-8

# In[1]:


def myreduce(function, iterable):
    it = iter(iterable)
    initializer = None
    if initializer is None:
        value = next(it)
    else:
        value = initializer
        
    for i in it:
        value = function(value,i)
    return value

l = [4,5,6,7,8,9]
myreduce(lambda x,y:x+y,l)


# In[13]:


def myfilter(n, lst):
    x = []
    y = []
    
    for i in lst:
        x.append(n(i))
    
    for i in range(0, len(x)):
        
        if x[i] == False:
            continue
        
        else:
            y.append(x[i])
    
    return y
        

def even_number(i):
    if i%2 == 0:
        return i
    else:
        return False

print(myfilter(even_number,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# In[2]:


str = 'ACADGILD'
l = []
for i in str:
    l.append(i)
print(l)


# In[3]:


l = ['x','y','z']
m = []
for i in l:
    for num in range(1,5):
        result = i*num
        m.append(result)
        
print(m)


# In[4]:


l = ['x','y','z']
m = []
for i in range(1,4):
    for j in l:
        k = j*i
        m.append(k)
print(m)


# In[5]:


l = [2,3,4]
m = []
for i in l:
    for j in range(0,3):
        k = i+j
        m.append([k])
print(m)


# In[6]:


l = [2,3,4,5]
n = []
for i in range(0,4):
    m = []
    for j in l:
        k = j+i
        m.append(k)
    n.append(m)
print(n)


# In[7]:


l = [1,2,3]
m = []
for i in l:
    for j in l:
        t = (i,j)
        m.append(t)
print(m)


# In[8]:


def longWord(n):
    new_arr = n.split(' ')
    st = max(new_arr)
    lng = (len(max(new_arr, key=len)))
    for i in n.split():
        if len(i)== lng:
            print(i)
    
longWord("my favourite food is mango and apples")


# In[9]:


class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
class Area(Triangle):
    def __init__(self,a,b,c):
        super(Area,self).__init__(a,b,c) 
        
    def getArea(self):
        
        s = (self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    
ae = Area(4,6,8)
ae.getArea()


# In[10]:


def filter_long_words(n,str):
    m =[]
    txt = str.split(" ")
    for i in txt:
        if len(i) > n:
            m.append(i)
    return m

filter_long_words(4,"my favourite food is apple and mango")


# In[11]:


str = ["my","favourite","is","apple"]
m = []
for i in str:
    j = len(i)
    m.append(j)
print(m)


# In[12]:


def vowelCheck():
    char = input("Enter a char :")
    if char in ('a','e','i','o','u'):
        return True
    else:
        return False

vowelCheck()


# In[ ]:




