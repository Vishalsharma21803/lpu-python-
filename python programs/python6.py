# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:18:46 2022

@author: Vishal
"""

# recursion function calls itself to perform a task
def factorial(x):
    if x==1:
        return 1
    else:
        return (x * factorial(x-1))
print(factorial(4))


def sum(x):
    if x<=1:
        return 1
    else:
        return (x + sum(x-1))
print(sum(5))


# reverse a number
numb = int(input("enter the "))