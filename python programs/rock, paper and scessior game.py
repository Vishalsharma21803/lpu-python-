# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:12:24 2022

@author: Vishal
"""
import random
print("welcome to the game")
#rock paper & scissor
uc = input("Enter rock or paper or scissor:")
print(uc)
# uc-- userchoice       cc --- computer choice   cs---computer selection
cc = ["rock", "paper", "sessior"]
cs = random.choice(cc)
print(f"\n user choice {uc} and computer choice is {cs} \n")
if uc == "rock" and cs == "paper":
    print("you lost")
    
    