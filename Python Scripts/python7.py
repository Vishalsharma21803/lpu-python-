def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
while True:
    choice=int(input("Enter your choice (1/2/3/4)"))
    if choice in (1,2,3,4):
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        
        if choice==1:
            print(num1,"+",num2,"=",num1+num2)
        elif choice==2:
            print(num1,"-",num2,"=",num1-num2)
        elif choice==3:
            print(num1,"*",num2,"=",num1*num2)
        elif choice==4:
            print(num1,"/",num2,"=",num1/num2)
        next=input("next calculation? (y/n) ")
        if next=="n":
            print('quitting....')
            break
        elif next == 'y':
            continue
        else:
            print("Invalid Input")
    else:
        print('wrong choice !!! quitting')
        break
