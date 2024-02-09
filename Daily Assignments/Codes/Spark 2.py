#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install findspark')


# In[2]:


import pyspark
import findspark
findspark.init()


# In[3]:


from pyspark import SparkContext
sc = SparkContext("local", "RDD Transformation")
sc


# In[4]:


count_rdd = sc.parallelize([1,2,3,4,5,5,6,7,8,9])
print(count_rdd.count())


# In[5]:


from pyspark import SparkContext
sc = SparkContext.getOrCreate()
reduce_rdd = sc.parallelize([1,3,4,6])
print(reduce_rdd.reduce(lambda x, y : x + y))


# In[8]:


from pyspark import SparkContext
sc = SparkContext.getOrCreate()
save_rdd = sc.parallelize([1,2,3,4,5,6])
save_rdd.saveAsTextFile('file.txt')

