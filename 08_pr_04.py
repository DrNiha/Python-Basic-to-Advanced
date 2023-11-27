def sum_recursive(num):
        if num<= 1:
            if num < 0:
                print("Enter positive number.")
            else:    
                return num
        else:
            return num + sum_recursive(num-1)

n = int(input("Enter a number:\n"))
sum = sum_recursive(n)
print("The sum is ", sum)   

