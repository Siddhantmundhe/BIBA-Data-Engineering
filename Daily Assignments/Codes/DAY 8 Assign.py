#!/usr/bin/env python
# coding: utf-8

# In[70]:


import csv


# In[71]:



file = open('username.csv')


# In[72]:


csvreader = csv.reader(file)


# In[73]:


file.close()


# In[74]:


import csv
rows = []
with open("username.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)


# In[75]:


import pandas as pd


# In[76]:


data= pd.read_csv("username.csv")
data


# In[77]:


data.columns


# In[78]:


data.Username


# In[79]:


header = ['Username', 'Identifier', 'First name','Last name']
data = [['singhisking1', 1011, 'Ankit','Mundhe'], ['Bradpitt99', 4556, 'Akanksha','Negi']]
data = pd.DataFrame(data, columns=header)


# In[80]:


data.to_csv('username1.csv', index=False)


# In[81]:


""" 3. Processing Python Lists
Lists are a fundamental data structure in Python.
You can perform various operations on lists, such as iterating through them,
appending elements, or applying transformations.
Various operations can be performed on lists, such as slicing, appending, and iterating. Here's an example:"""

my_list = [1, 2, 3, 4, 5]
processed_list = [x * 2 for x in my_list]
print(processed_list)


# In[82]:


"""Lambda Functions in Python
Lambda functions are anonymous functions defined using the lambda keyword.
They are often used for short-term operations where a full function definition is not necessary."""


add = lambda x, y: x + y
result = add(3, 5)
print(result)


# In[83]:


"""Usage of Lambda Functions
Lambda functions are frequently used in situations where a small function is needed, such as when sorting or filtering data."""

# Sorting a list of tuples based on the second element using lambda
data = [(1, 5), (3, 2), (2, 8)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)


# In[84]:


strings = ['apple', 'banana', 'kiwi', 'orange']
sorted_strings = sorted(strings, key=lambda x: len(x))
print(sorted_strings)


# In[85]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)


# In[86]:


"""Filter Data in Python Lists using filter and lambda
The filter() function is used to filter elements from a list based on a given condition.
When combined with lambda, it becomes a powerful tool for filtering data."""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered_list)


# In[87]:


"""Using lambda() Function with map(), filter(), reduce()
Lambda functions can be used in conjunction with other built-in functions like map(), filter(),
and reduce() for more complex operations."""

from functools import reduce

# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# Using lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Using lambda with reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)

