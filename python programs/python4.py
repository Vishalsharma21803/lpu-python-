# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:36:55 2022

@author: Vishal
"""

import math
x = min(1,2,3)
y = max(5,6,8)
print(x)
print(y)

a = math.sqrt(64)
print(a)
b = math.floor(1.4)
print(b)
c = math.floor(-3.7)
print(c)

e = math.ceil(-9.7)
print(e)


''' for loop
three components are there
1. initialization
2. termination
3. increment/decrement   '''

student = ["anurag", "vishal", "vinod", "ankit"]
for i in student:
    print(i) #to print list items

for i in "anurag":
    print(i)
    
for i in student:
    if i == "ankit":
        break
    print(i)

color = ["red", "blur", "yellow", "green"]

for i in student:
    for j in color:
        print(i,j)
        
        
i = 1
while i < 5:
    j = 1
    while j < 10:
        print(i*j)
        j = j+1
    i = i+1
    print("\n")

import random
randomlist = []
for i in range(0,5):
  n = random.randint(1,10)
  randomlist.append(n)
print(randomlist)


''' another data type
    orderd and unchangeable '''

p = ("anurag", "vishal", "vinod", "ankit")
print(p)
print(type(p))
print(len(p))

q = list(p)
q[3] = "virus"
p = tuple(q)
print(p)


m = {"anurag", "vishal", "vinod", "ankit"}
print(m)
m.add("virus")
print(m)
y = {1, 2, 3}
x = m.union(y)
print(x)


# another data type: dictionary
#ordered, changable, no duplication
#works on the concept of key and value

d = {
     "name": "anurag",
     "company": "cipherschool",
     "college": "LPU",
     }
print(d)
print(d["college"])
d["degree"] = "Engineering"
print(d)
print(d.keys())
if "name" in d:
    print("yes it is")





































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    