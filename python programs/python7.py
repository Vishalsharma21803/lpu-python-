a=int(input("enter the number: "))
if a == 0:
    print("neither prime nor composite")
elif a == 1:
    print("neither prime nor composite")
elif a == 2:
    print("prime number")
elif a<0:
    print("invalid input")

for i in range(2,a):
    if  a%i==0:
        print("not a prime number")
        break
else:
        print("prime number")



        