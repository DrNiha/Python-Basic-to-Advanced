n = int(input("Enter a number : "))
print(f"Reversed Multiplication Table for {n}:")
for i in range(10, 0, -1):
    product = n * i
    print(f"{n} x {i} = {product}")