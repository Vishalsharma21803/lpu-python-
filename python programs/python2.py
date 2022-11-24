 -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 13:23:42 2022

@author: Vishal
"""

import random
print(random.random()) 
print(random.randint(1,9))
#to write multi line string use triple double comas

#slicing
b = "vishal sharma"
print(b[2:8])
c = "VISHAL SHARMA" 
print(c.lower())
# replacing letter h with d in my name 

d = "vishal"
print(d.replace("h","d"))

# concatenation
e = "radisson"
f = "the"
g = "school"
sum = e+f+g
print(sum)
sum1 = e+" "+f+" "+g
print(sum1)

# to print the word vishal in inverted commas
txt = "hii my name is \"vishal\" and i stydy at lpu"
print(txt)

#x += 2;  is equal to    x = x+2

a = 40
print(f"my age is {a}")
fruits = ["apples", "mango", "grapes", "watermelon", 1]
print(fruits)
print(len(fruits))
print(type(fruits))
print(fruits[2:5])
# append, insert, pop, etc ........... explore them


























