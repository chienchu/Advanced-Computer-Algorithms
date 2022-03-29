#!/usr/bin/env python
# coding: utf-8

# ## Question 1. Enumerate all feasible solutions and find the best one. Try the data sizes 8, 10, 11, 12, ... that you can solve for.

# In[18]:


import pandas as pd
from itertools import permutations
import time

data = pd.read_excel("./sum of completion times.xlsx", 
                     engine='openpyxl', index_col=0, header=None)

#if size==12: memory error
size = 10
jobs = []
start = time.time()

for i in range(size):
    jobs.append(list(data[i+1]))

pers = permutations(jobs, size)

orders = []
start = time.time()
sum_times = []

for per in pers:
    
    order = []
    order_time = 0
    sum_time = 0
    
    for i in range(size):
        order.append(per[i][0])
        if order_time >= per[i][2]:
            order_time += per[i][1]
        else:
            order_time = per[i][2]
            order_time += per[i][1]
        
        sum_time += order_time
    
    orders.append(order)
    sum_times.append(sum_time)
    
min_time, min_time_index = min((val, idx) 
                               for (idx, val) in enumerate(sum_times))
end = time.time()

print('最短sum of completion time:', min_time)
print('一個最佳job順序:', orders[min_time_index])
print('time_cost:', end-start)


# ## Question 2. Apply the SRPT (shortest remaining processing time first) algorithm to find an optimal solution value of the preemptive version. Compare the solution values with the optimal values of Question 1.

# In[20]:


import pandas as pd

data = pd.read_excel("./sum of completion times.xlsx", 
                     engine='openpyxl', index_col=0, header=None)


size = 50
jobs = []

for i in range(size):
    jobs.append(list(data[i+1]))


init = True
init_job = [None, float('Inf'), 0]
curr_time = 0
next_stop_time = 0
arrived_jobs = []
have_curr = True
sum_of_completion_times = 0

while len(jobs) or len(arrived_jobs) or have_curr:
    if init:
        curr_job = init_job
        init = False

    next_stop_time = min(curr_time + curr_job[1], 
                         min([jobs[i][2] for i in range(len(jobs))], 
                             default = float('Inf')))
    curr_job[1] = curr_job[1] - (next_stop_time - curr_time)


    # current job finish
    if curr_job[1] <= 0:
        curr_job[1] = 0
        if curr_job[0] != None:
            print('job', curr_job[0],'finish','time=',next_stop_time)
            sum_of_completion_times += next_stop_time
            have_curr = False
            curr_job = init_job

    remove_jobs = []
    for job in jobs:
        if job[2] == next_stop_time:
            arrived_jobs.append(job)
            remove_jobs.append(job)
    for job in remove_jobs:
        jobs.remove(job)

    min_p = curr_job[1]
    for job in arrived_jobs:
        if job[1] < min_p:
            temp_job = job
            min_p = job[1]

    if min_p != curr_job[1]:
        if curr_job[0] != None:
            arrived_jobs.append(curr_job)
        arrived_jobs.remove(temp_job)
        curr_job = temp_job
        have_curr = True

    curr_time = next_stop_time
    
print('sum of completion times:', sum_of_completion_times)


# ## Question 3. Develop a branch-and-bound algorithm to improve the problem-solving process of Question 1. You may use Breadth FS, Depth FS, Best FS, or other possible strategies for your design.

# ## DFS 無法跑完50個但在相同jobs數量下比第一題快
# ### jobs_num = 10，Q1:10sec 、DFS:6sec

# In[19]:


import pandas as pd
import time

data = pd.read_excel("./sum of completion times.xlsx", 
                     engine='openpyxl', index_col=0, header=None)

start = time.time()
size = 10

jobs = []
"""
    jobs[i][0]:job name
    jobs[i][1]:process time
    jobs[i][2]:arrive time
"""
for i in range(size):
    jobs.append(list(data[i+1]))


best_cost = float('Inf')

def calCost(per):
    order_time = 0
    sum_time = 0
    for i in range(len(per)):
        if order_time >= per[i][2]:
            order_time += per[i][1]
        else:
            order_time = per[i][2]
            order_time += per[i][1]
        sum_time += order_time
    return sum_time


def perm(n,begin,end):
    global best_cost
    global bestjob
    
    if begin>=end and calCost(n)<best_cost:
        best_cost = calCost(n)
            
    else:
        i=begin
        for num in range(begin,end):
            n[num],n[i]=n[i],n[num]
            perm(n,begin+1,end)
            n[num],n[i]=n[i],n[num]
            
            
perm(jobs, 0, len(jobs))
end = time.time()
print('最短sum of completion time:',best_cost)
print('time_cost:', end-start)


# ## non-preemptive SJF,可50個jobs都跑完,not branch and bound

# In[14]:


import pandas as pd

data = pd.read_excel("./sum of completion times.xlsx", 
                     engine='openpyxl', index_col=0, header=None)

size = 50
jobs = []

for i in range(size):
    jobs.append(list(data[i+1]))

curr_time = -1
next_stop_time = 0
done_jobs = []
count = 0
arrived_jobs = []
sum_of_completion_times = 0

while count < len(jobs):
    finish_job = None
    for job in jobs:
        if job[2] > curr_time and job[2] <= next_stop_time:
            arrived_jobs.append(job)
            
    min_p = float('Inf')
    for arrived_job in arrived_jobs:
        if arrived_job[1] < min_p:
            min_p = arrived_job[1]
            finish_job = arrived_job
    
    if finish_job != None:
        arrived_jobs.remove(finish_job)
        curr_time = next_stop_time
        next_stop_time = next_stop_time + min_p
        print('job', finish_job[0], '完成時間:', next_stop_time)
        sum_of_completion_times += next_stop_time
        
        count += 1
    
    else:
        next_stop_time += 1
        
print('sum of completion times:', sum_of_completion_times)

