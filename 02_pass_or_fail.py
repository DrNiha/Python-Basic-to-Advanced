num1 = int(input("Enter marks of subject 1: "))
num2 = int(input("Enter marks of subject 2: "))
num3 = int(input("Enter marks of subject 3: "))

marks1 = (num1/100)*100
marks2 = (num2/100)*100
marks3 = (num3/100)*100
total = (num1+num2+num3)
percentage = ((total)/300)*100

if(percentage>40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass!!")
else:
    print("You are fail!!")
