#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().system('pip install pyspark')


# In[3]:


import os

os.environ["SPARK_HOME"] = "C:\spark\spark-3.5.0-bin-hadoop3"
os.environ["PYSPARK_PYTHON"]="C:\Python30"


# In[4]:


import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("practice").getOrCreate()

spark


# In[5]:


import pandas as pd    
data = [['Scott', 50], ['Jeff', 45], ['Thomas', 54],['Ann',34]] 
  
# Create the pandas DataFrame 
pandasDF = pd.DataFrame(data, columns = ['Name', 'Age']) 
  
# print dataframe. 
print(pandasDF)


# In[6]:


# Import SparkSession
from pyspark.sql import SparkSession
 
 
# Create SparkSession 
spark = SparkSession.builder       .master("local[1]")       .appName("SparkByExamples.com")       .getOrCreate() 

dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
rdd=spark.sparkContext.parallelize(dataList)


# In[17]:





# In[7]:


df = spark.read.csv("C:\Users\siddh\username.csv")
df
df.show()




# In[8]:


import pyspark
from pyspark.sql import SparkSession
# Create SparkSession 
spark = SparkSession.builder.appName("SparkByExamples.com") .getOrCreate() 
dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
rdd=spark.sparkContext.parallelize(dataList)
result = rdd.collect()
("RDD Contents:", result)


# In[9]:


import os
from pyspark.sql import SparkSession

# Set Python version for Spark
os.environ['PYSPARK_PYTHON'] = 'C:\Python30'

# Create Spark session
spark = SparkSession.builder     .appName("Test")     .config("spark.some.config.option", "some-value")     .config("spark.executor.memory", "2g")     .getOrCreate()

# Your DataFrame creation code
Employee = spark.createDataFrame([
    ('1', 'Joe', '70000', '1'),
    ('2', 'Henry', '80000', '2'),
    ('3', 'Sam', '60000', '2'),
    ('4', 'Max', '90000', '1')],
    ['Id', 'Name', 'Salary', 'DepartmentId']
)

# Show the DataFrame
Employee.show()


# In[11]:


import sys
print(sys.version)


# In[ ]:





# In[26]:





# In[8]:


import os
os.environ['PYSPARK_PYTHON'] = 'C:\Python30'


# In[10]:


from pyspark import SparkContext
sc = SparkContext.getOrCreate()
count_rdd = sc.parallelize([1,2,3,4,5,5,6,7,8,9])
print(count_rdd.count())


# In[21]:


from pyspark import SparkContext
sc = SparkContext.getOrCreate()
count_rdd = sc.parallelize([1,2,3,4,5,5,6,7,8,9])
print(count_rdd.count())


# In[22]:


from pyspark import SparkContext
sc = SparkContext.getOrCreate()
reduce_rdd = sc.parallelize([1,3,4,6])
print(reduce_rdd.reduce(lambda x, y : x + y))
from pyspark import SparkContext
sc = SparkContext.getOrCreate()
reduce_rdd = sc.parallelize([1,3,4,6])
print(reduce_rdd.reduce(lambda x, y : x + y))


# In[20]:


conda install -c cyclus java-jdk

