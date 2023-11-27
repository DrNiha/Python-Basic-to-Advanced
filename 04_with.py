with open('another.txt', 'r') as f:
    a = f.read()
print(a)

# NO NEED TO CLOSE THE FILE EXPLICITLY AS WE ARE USING WITH STATEMENT