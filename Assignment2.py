#!/usr/bin/env python
# coding: utf-8

# ### Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# 
# 
# 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# In[1]:


a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
b= []
for j in range (1,len(a)) :
    for i in range(len(a)-j) :
        if a[i][1]>a[i+1][1] :
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp

for i in range(len(a)) :
    b.append(a[i])
print(b)


# In[8]:


a = eval(input("Enter the list of tuple. The tuple will only contain two elements:"))
b= []
for j in range (1,len(a)) :
    for i in range(len(a)-j) :
        if a[i][1]>a[i+1][1] :
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp

for i in range(len(a)) :
    b.append(a[i])
print("The expected output is:",b)


# ### Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values
# 
# 
# Sample Output : {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}

# In[3]:


dict_of_alpha={}

for i in range(97,123):
    dict_of_alpha[chr(i)]=i

print(dict_of_alpha)


# In[ ]:




