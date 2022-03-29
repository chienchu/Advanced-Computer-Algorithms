#!/usr/bin/env python
# coding: utf-8

# # woman-favored strategy

# In[ ]:


import pandas as pd

man_df = pd.read_csv(r"D:\NYCU\1101\Advanced Computer Algorithms\HW1\20_man.csv")
woman_df = pd.read_csv(r"D:\NYCU\1101\Advanced Computer Algorithms\HW1\20_woman.csv")
man_matched = ['-1']*20
woman_matched = ['-1']*20

def not_marriage_yet(men):
    for i in range(len(men)):
        if (men[i]=='-1'):
            return i
    return -1


def match_woman_by_rank(man_prefer_rank=1):
    woman_man_prefer = man_prefer_list[man_prefer_rank]-1

    if(woman_matched[woman_man_prefer]=='-1'):
        woman_matched[woman_man_prefer] = man_not_marriage
        man_matched[man_not_marriage] = woman_man_prefer

    elif(woman_matched[woman_man_prefer]!='-1'):
        woman_prefer_list = woman_df.loc[woman_man_prefer].values.tolist()

        if(woman_prefer_list.index(man_not_marriage+1) < woman_prefer_list.index(woman_matched[woman_man_prefer]+1)):
            man_matched[woman_matched[woman_man_prefer]] = '-1'
            woman_matched[woman_man_prefer] = man_not_marriage
            man_matched[man_not_marriage] = woman_man_prefer
        else:
            man_prefer_rank += 1
            match_woman_by_rank(man_prefer_rank)

            
while(not_marriage_yet(man_matched)+1):
    
    man_not_marriage = not_marriage_yet(man_matched)
    man_prefer_list = man_df.loc[man_not_marriage]
    match_woman_by_rank()


# In[ ]:


for i in range(len(man_matched)):
    man_matched[i] = 'M' + str(i+1) +' and W' + str(man_matched[i]+1)
man_matched


# # man-favored strategy

# In[ ]:


import pandas as pd

man_df = pd.read_csv(r"D:\NYCU\1101\Advanced Computer Algorithms\HW1\20_man.csv")
woman_df = pd.read_csv(r"D:\NYCU\1101\Advanced Computer Algorithms\HW1\20_woman.csv")
man_matched = ['-1']*20
woman_matched = ['-1']*20

def not_marriage_yet(women):
    for i in range(len(women)):
        if (women[i]=='-1'):
            return i
    return -1


def match_man_by_rank(woman_prefer_rank=1):
    man_woman_prefer = woman_prefer_list[woman_prefer_rank]-1

    if(man_matched[man_woman_prefer]=='-1'):
        man_matched[man_woman_prefer] = woman_not_marriage
        woman_matched[woman_not_marriage] = man_woman_prefer

    elif(man_matched[man_woman_prefer]!='-1'):
        man_prefer_list = man_df.loc[man_woman_prefer].values.tolist()

        if(man_prefer_list.index(woman_not_marriage+1) < man_prefer_list.index(man_matched[man_woman_prefer]+1)):
            woman_matched[man_matched[man_woman_prefer]] = '-1'
            man_matched[man_woman_prefer] = woman_not_marriage
            woman_matched[woman_not_marriage] = man_woman_prefer
        else:
            woman_prefer_rank += 1
            match_man_by_rank(woman_prefer_rank)

            
while(not_marriage_yet(woman_matched)+1):
    
    woman_not_marriage = not_marriage_yet(woman_matched)
    woman_prefer_list = woman_df.loc[woman_not_marriage]
    match_man_by_rank()


# In[ ]:


for i in range(len(woman_matched)):
    woman_matched[i] = 'W' + str(i+1) +' and M' + str(woman_matched[i]+1)
woman_matched


# In[ ]:




