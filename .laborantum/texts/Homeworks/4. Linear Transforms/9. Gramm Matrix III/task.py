#!/usr/bin/env python
# coding: utf-8

# In[7]:


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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/9. Gramm Matrix III")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[8]:


import numpy as np


def gram_matrix(B):
    return B @ B.T


def scalar_product(B, x, y):
    return y.T @ np.linalg.inv(B @ B.T).T @ x


# In[9]:


import time

start = time.time()

debug_result = [scalar_product(**x) for x in debug_cases]
answer = [scalar_product(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




