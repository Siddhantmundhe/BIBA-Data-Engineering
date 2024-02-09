#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Numpy Code

import numpy as np

my_array = np.array([1, 2, 3, 4, 5])

squared_array = my_array ** 2

print("Original Array:", my_array)
print("Squared Array:", squared_array)


# In[2]:


# Creation of Arrays with Evenly Spaced Values

import numpy as np

array_arange = np.arange(0, 5, 1)

print("Using arange:")
print(array_arange)


# In[3]:


# Linespace

import numpy as np

array_linspace = np.linspace(0, 1, 10)

print("Using linspace:")
print(array_linspace)


# In[4]:


# Using endpoint and endspace

import numpy as np

array_linspace, step_size = np.linspace(0, 1, 5, endpoint=True, retstep=True)

print("Using linspace with endpoint and retstep:")
print("Array:", array_linspace)
print("Step size:", step_size)


# In[5]:


# Count Values in Pandas Dataframe

import pandas as pd

data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C', 'C']}
df = pd.DataFrame(data)

value_counts = df['Category'].value_counts()

print("Value Counts:")
print(value_counts)


# In[6]:


#CSV Files

import pandas as pd

df = pd.read_csv("username.csv")
print(df.head())


# In[7]:


# Using read table
import pandas as pd

df = pd.read_table("username.csv", delimiter =", ")
print(df.head())


# In[9]:


# Columns
import pandas as pd

import csv
 
with open("username.csv") as csv_file:

    csv_reader = csv.reader(csv_file)
 
    df = pd.DataFrame([csv_reader], index = None)

for val in list(df[1]):
    print(val)


# In[11]:


# Inner Join 
import pandas as pd
 

a = pd.DataFrame()

d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
 
a = pd.DataFrame(d)
 
b = pd.DataFrame()

d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)

df = pd.merge(a, b, on='id', how='inner')

df


# In[12]:


# Left Join
import pandas as pd

a = pd.DataFrame()

d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
 
a = pd.DataFrame(d)

b = pd.DataFrame()

d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)

df = pd.merge(a, b, on='id', how='left')

df


# In[13]:


# Right Join

import pandas as pd

a = pd.DataFrame()

d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
 
a = pd.DataFrame(d)

b = pd.DataFrame()

d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)

df = pd.merge(a, b, on='id', how='right')

df


# In[14]:


# Full Outer Join

import pandas as pd

a = pd.DataFrame()

d = {'id': [1, 2, 10, 12],
     'val1': ['a', 'b', 'c', 'd']}
 
a = pd.DataFrame(d)

b = pd.DataFrame()

d = {'id': [1, 2, 9, 8],
     'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)

df = pd.merge(a, b, on='id', how='outer')

df

