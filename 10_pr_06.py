def inch(cm):
    return cm * 2.54

length = float(input("Enter the length:\n"))
l = inch(length)
print("Length in centimeters is ", l)