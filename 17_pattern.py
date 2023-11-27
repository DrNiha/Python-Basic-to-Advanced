# Python program to print the given pattern

rows = 3
columns = 3

for i in range(rows):
    for j in range(columns):
        # Print '*' for the corners and the center
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end="   ")
        else:
            # Print space for the inner part
            print("    ", end="")

    # Move to the next line after completing each row
    print()

