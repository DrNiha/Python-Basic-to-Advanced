def table(num):
    for i in range(11):
        print(num, "x", i+1 , "=", num*(i+1))

n = int(input("Enter the number:\n"))

print(table(n))