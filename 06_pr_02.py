def farh(cel):
    return (cel * (9/5)) + 32 

temp = int(input("Enter the temperatur in farenheit:\n"))
t = farh(temp)

print("The temperature in celcius is ", t)