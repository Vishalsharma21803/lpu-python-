# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:16:55 2022

@author: Vishal
"""
#defining a function
def vishal():
    print("hi i am a user defined function")
vishal()

#paramtrised function, function capable of accepting value
def vishal(name):
    print("hi my name is "+name)

vishal("ankit")

def vishal(first_name, last_name):
    print("hi my name is " +first_name+" "+last_name)

vishal("ankit", "gupta")


# to give multiple names use *

def vishal(*name):
    print("my name is "+name[0]+" "+name[2]+" "+name[3]+" "+name[1])

vishal("vishal", "ankit", "ram", "amar")


def vishal(name1,name2,name3):
    print("my name is "+name1)
vishal(name1 = "anurag", name2 = "ankit", name3 = "sujal")


def vishal(name):
    for i in name:
        print("my name is "+i)
name = ["anurag", "ankit","ram","sita"]
vishal(name)


# return
def vishal(n):
    return n*5
print(vishal(5))























