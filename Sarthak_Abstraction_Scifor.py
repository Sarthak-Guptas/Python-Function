#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Abstraction
# Abstraction is a fundamental concept in object-oriented programming that involves 
# simplifying complex systems by modeling classes based on real-world entities
# and hiding the unnecessary details from the user. It allows you to focus on the essential 
# features and ignore the non-essential ones. In Python, abstraction is often achieved through the
# use of classes and methods


# In[3]:


from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Concrete subclass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Running on four legs"

# Concrete subclass
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

    def move(self):
        return "Walking gracefully"

# Usage
dog = Dog()
cat = Cat()

print("Dog:", dog.make_sound(), "-", dog.move())
print("Cat:", cat.make_sound(), "-", cat.move())


# In[ ]:




