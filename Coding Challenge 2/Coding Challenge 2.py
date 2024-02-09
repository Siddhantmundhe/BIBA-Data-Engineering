#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Reading CSV Data:
import pandas as pd
df= pd.read_csv("username.csv")


# In[8]:


# Read Data from CSV Files to Pandas Dataframes
df


# In[15]:


df.columns


# In[10]:


df.Username


# In[20]:


# Filter Data in Pandas Dataframe using query.
import pandas as pd

df = pd.read_csv("username.csv")

print("Column Names:")
print(df.columns)

df.columns = df.columns.str.strip()

# Filter data using a query
filtered_data = df.query('Identifier > 2500')

print("\nFiltered DataFrame:")
print(filtered_data)




# In[22]:


# Square using lambda function
def square(x):
    return x ** 2

square_lambda = lambda x: x ** 2


print(square(5))          # Output: 25
print(square_lambda(5))   # Output: 25


# In[23]:


# JSON Strings to Python dicts
import json

json_string_dict = '{"name": "Siddhant", "age": 22, "city": "Jalna"}'

python_dict = json.loads(json_string_dict)

print("Python Dictionary:")
print(python_dict)


# In[24]:


# JSON Strings to Python lists

json_string_list = '[1, 2, 3, 4, 5]'

python_list = json.loads(json_string_list)

print("Python List:")
print(python_list)

