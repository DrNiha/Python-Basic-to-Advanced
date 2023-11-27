i = 1
j = 1
for i in range(1,11):
    if i % 3 != 0:
        i += 2
        continue
    if j % 3 == 0:
        break
    print(i+j)


