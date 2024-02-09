#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Basic
# Variables and operators
a = 5
b = 2
result = a + b
print(result) 


# In[20]:


# Input and output
user_input = input("Enter your name: ")
print("Hello, " + user_input + "!")


# In[1]:


"""if statement:The if statement is used to conditionally execute a block of code
based on a specified condition."""

x = 10
if x > 5:
    print("x is greater than 5")



# In[2]:


"""if-else statement: The if-else statement allows you to specify two blocks of code,
 one to be executed if the condition is true, and the other if the condition is false."""

y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")


# In[36]:


"""if-elif-else statement: The if-elif-else statement is an extension of the if-else statement, 
allowing you to check multiple conditions sequentially."""

grade = 75
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("Fail")

    


# In[37]:


"""for loop:The for loop is used for iterating over a sequence
 (such as a list, tuple, string, etc.) or other iterable objects."""

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# In[38]:


"""
nested loop:A nested loop is a loop inside another loop.
It allows you to iterate over items in a sequence within another iteration."""

for i in range(3):
    for j in range(2):
        print(i, j)


# In[39]:


"""
while loop:The while loop is used to repeatedly execute a block of code as long
 as a specified condition is true."""

count = 0
while count < 5:
    print(count)
    count += 1


# In[40]:


"""
break statement:The break statement is used to exit a loop prematurely,
 regardless of whether the loop condition is true or false."""

for i in range(10):
    if i == 5:
        break
    print(i)


# In[41]:


"""
continue statement:The continue statement is used to skip the rest of the code inside
 a loop for the current iteration and move to the next iteration."""

for i in range(5):
    if i == 2:
        continue
    print(i)


# In[42]:


"""
pass statement:The pass statement is a null operation; nothing happens
 when it is executed. It is used as a placeholder where syntactically some
  code is required but no action is desired."""

for i in range(3):
    pass


# In[23]:


# Lists and list methods

"""
A list is a mutable, ordered collection of elements, and it can contain elements of different data types.
Lists are defined by enclosing elements in square brackets [] and separating them with commas.

"""
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.pop(2)
print(my_list)


# In[24]:


# Dictionaries and dictionary methods
"""
A dictionary is an unordered collection of key-value pairs, where each key must be unique.
Dictionaries are defined using curly braces {} and specifying key-value pairs.
"""

my_dict = {"name": "Siddhant", "age": 22, "city": "Pune"}
my_dict["gender"] = "Male"
del my_dict["age"]
print(my_dict)


# In[43]:


# Sets and set methods

"""
A set is an unordered collection of unique elements. Duplicates are not allowed in a set.
Sets are defined using curly braces {} or the set() constructor.
"""

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)


# In[18]:



"""FUNCTIONS: In Python, a function is a block of reusable code that performs a specific task or set of tasks. Functions allow you
to break down a program into smaller, modular pieces, making the code more organized, readable, and maintainable.
You define a function using the def keyword, followed by the function name and parameters. The function body is indented.
"""

def greet(name):
    print(f"Hello, {name}!")
greet("Sid")


# In[33]:


# String functions
my_string = "   Hello, World!   "
#uppercase = my_string.upper()
lowercase = my_string.lower()
#stripped = my_string.strip()
print(my_string.lower())


# In[35]:


# Date and time functions
import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(current_time)


# In[19]:


"""
The map function applies a given function to all items in an iterable
(e.g., a list) and returns a new iterable with the results."""

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

# Use the map function to apply the square function to each element in the list
squared_numbers = map(square, numbers)

squared_numbers_list = list(squared_numbers)

print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers_list)


# In[13]:


"""


Object-oriented programming (OOP) is based on four main principles or pillars:
encapsulation, inheritance, polymorphism, and abstraction.
1)Encapsulation:Encapsulation is the bundling of data and methods that operate on the data into a single unit known as a class.
It restricts direct access to some of the object's components and can prevent the accidental modification of data.
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private variable

    def get_age(self):
        return self.__age

student = Student("Alice", 20)
print(student.name)
print(student.get_age())


# In[7]:


"""Inheritance:Inheritance is a mechanism where a new class inherits properties and behaviors from an existing class.
It promotes code reusability and establishes a relationship between a parent (base/super) class and a child (derived/sub) class.
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

my_dog = Dog()
my_cat = Cat()

print(my_dog.speak())

print(my_cat.speak())


# In[8]:


"""Polymorphism:The word polymorphism means having many forms.
In programming, polymorphism means the same function name (but different signatures) being used for different types.
"""

def add(a, b):
    return a + b

print(add(5, 3))      
print(add("Hello", " World"))   


# In[9]:


"""Method overriding in Python occurs when a derived class provides a specific implementation
for a method that is already defined in its base class."""
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

# Calling the overridden method
dog.speak() 
cat.speak()


# In[46]:


#Reading from a File:

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


# In[45]:



#Writing to a File:

with open('example.txt', 'w') as file:
    file.write('Hello, this is a sample text.')


# In[47]:


#Appending to a File:

with open('example.txt', 'a') as file:
    file.write('\nThis line is appended.')


# In[48]:


#Exception Handling for File Operations:

try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

