#!/usr/bin/env python
# coding: utf-8

# In[26]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

path = Path('.laborantum/texts/Homeworks/3. Matrices/11. Numpy Matrix Expression')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[27]:


import numpy as np


def formula(A, B, C, x):
    lhs = A.T @ (B + 2*C)    

    for i in range(lhs.shape[0]):
        for j in range(lhs.shape[1]):
            if i == j:
                lhs[i, j] += 3
    
    exp = np.exp(lhs)

    return exp @ x 


# 

# In[28]:


import time

start = time.time()

debug_result = [formula(**x) for x in debug_cases]
answer = [formula(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




