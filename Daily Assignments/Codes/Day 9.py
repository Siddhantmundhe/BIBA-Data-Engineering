#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Get Unique Values from a List Using Set Method
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# Use set() to get unique values
unique_values = set(my_list)

unique_list = list(unique_values)

print(unique_list)


# In[2]:


# Use Reduce Function
from functools import reduce

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]


check_duplicates = lambda acc, el: (acc[0] + [el], acc[1] + [el]) if el not in acc[1] else acc

# Use reduce to iterate over the list and check for duplicates
result, _ = reduce(check_duplicates, my_list, ([], []))

print(result)


# In[3]:


# Operator.countOf() method

import operator

def get_unique_values(input_list):
    count_dict = {}

    for item in input_list:
        count_dict[item] = count_dict.get(item, 0) + 1

    # Use countOf() to get unique values (count == 1)
    unique_values = [key for key, count in count_dict.items() if operator.countOf(input_list, key) == 1]

    return unique_values

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

unique_values = get_unique_values(my_list)

print(unique_values)


# In[4]:


#Get Unique Values From a List Using numpy.unique
import numpy as np


my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

unique_values = np.unique(my_list)

print(unique_values)


# In[5]:


# Get Unique Values From a List Using dict.fromkeys()

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

unique_dict = dict.fromkeys(my_list)

unique_values = list(unique_dict.keys())

print(unique_values)


# In[6]:


# Convert JSON String to Dictionary Python

import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

data_dict = json.loads(json_string)

print(data_dict)


# In[9]:


# Python Parse JSON String


import json

employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'

employee_dict = json.loads(employee)
print(employee_dict)
 
print(employee_dict['name'])


# In[17]:



import json
 
# Opening JSON file
f = open('data.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
 
# Closing file
f.close()



# In[1]:


# Python to JSON
import json
  
# Data to be written
dictionary = {
  "id": "04",
  "name": "sunil",
  "department": "HR"
}
  
# Serializing json
json_object = json.dumps(dictionary, indent = 4)
print(json_object)

