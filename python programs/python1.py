# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:00:55 2022

@author: Vishal
"""
a = 10 
b = 20


sol = a*a + b*b +2*a*b
#we can also write as (a+b)**2    or    a**2 + b**2 +2*a*b
print(sol)
soln = (a+b)**2
print(soln)
# for power(like a raise to power 2) by using pow(a,2)
soll = pow(a,2)
print(soll)
solln = pow(b,4)
print(solln)
# string is a set of characters 
#conditional statements --- koi condition ko lgakar hm usse kio certain kaam kra skte h 
x = 10
y = 30
if y > x:
    print("y is greater than x")
    #print aur sem colon ke bich mein 4 spaces hone chahiye (yahan pr enter dbakar hi kaam chal jayega)
A = 500
B = 1000
if A > B:
    print("A is greater than B")
else:
    print("B is greater than A")
c =20
d =40
#in a programing language to compare(equal) we use == (double equals to)
if c > d:
    print("c is greater than d")
elif c == d:
    print("c is equal to d")
else:
    print("d is greater than c")
Vishal = 85
if Vishal >= 90 and Vishal < 94:
    print("congrachulations you have got A grade")
elif Vishal >= 95:
    print("congrachulations you have got A+ grade")
elif Vishal > 80 and Vishal <=89:
    print("you have got B grade")
elif Vishal <50:
    print("you have failed")
else:
    print("you have passed") 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    