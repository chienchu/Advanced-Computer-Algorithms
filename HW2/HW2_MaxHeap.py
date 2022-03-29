#!/usr/bin/env python
# coding: utf-8

# In[1]:


def buildMaxHeap(array):
    n = len(array)
    for i in range((n-1)//2, -1, -1):
        heapify(array, i)
    print(array)


def heapify(array, i):
    left = i*2+1
    right = i*2+2
    if left < len(array) and array[left] > array[i]:
        largest = left
    else:
        largest = i
    if right < len(array) and array[right] > array[largest]:
        largest = right
        
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest)


def pop(array):
    if len(array) == 0:
        print("array is empty")
    else:
        array[0], array[-1] = array[-1], array[0]
        del array[-1]
        heapify(array, 0)
        
def insert(array, num):
    array.append(num)
    new = array.index(num)
    par = (new-1)//2
    while array[new] > array[par] and new > 0:
        array[new], array[par] = array[par], array[new]
        new = par
        par = (new-1)//2


# In[2]:


import pandas as pd
data = pd.read_excel("./HW2-data.xlsx",engine='openpyxl')
data = data.drop([0,2,3])
data = data.drop(['Name'], axis=1)
data


# In[3]:


heap_array = data.loc[1]
heap_array = heap_array.values.astype(int).tolist()


# In[4]:


buildMaxHeap(heap_array)


# In[5]:


trans = data.loc[4]
trans = trans.dropna()
trans = trans.values.astype(int).tolist()
print(len(trans))


# In[6]:


for i in range(len(trans)):
    if trans[i] == -1:
        pop(heap_array)
    else:
        insert(heap_array, trans[i])
        
                
total = 0
for i in range(len(heap_array)-1):
    total += abs(heap_array[i]-heap_array[i+1])
print(total)

