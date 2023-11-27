def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
        
m1 = int(input("Enter first number: "))
m2 = int(input("Enter second number: "))
m3 = int(input("Enter third number: "))

m = maximum(m1,m2,m3)
print("The maximum of given numbers is ", m)
