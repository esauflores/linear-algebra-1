#!/usr/bin/env python
# coding: utf-8

# In[13]:


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

path = Path(".laborantum/texts/Homeworks/3. Matrices/14. Diagonal Matrices Product")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[14]:


import numpy as np

def DA_AD_product(D, A):

    DA = np.zeros((D.shape[0], A.shape[1])) 

    # Fast D @ A
    for i in range(D.shape[0]):
        for j in range(A.shape[1]):
            DA[i, j] = D[i, i] * A[i, j]

    AD = np.zeros((A.shape[0], D.shape[1]))
    
    # Fast A @ D
    for i in range(A.shape[0]):
        for j in range(D.shape[1]):
            AD[i, j] = A[i, j] * D[j, j]

    res = {
        'DA': DA,
        'AD': AD,
    }
    return res


# In[15]:


import time

start = time.time()

debug_result = [DA_AD_product(**x) for x in debug_cases]
answer = [DA_AD_product(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




