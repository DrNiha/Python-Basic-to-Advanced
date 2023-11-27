l1 = [1, 2, 35, 49, 9876, 345678, 73, 000000]

#l1_sorted = l1.sort() this is not valid because when we run this code it will give output as NONE which means l1 is changed after sorting

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.append(77)
print(l1)

#l1.insert(23,4) this will give output as if we add 4 at the end of the list l1

l1.insert(4,23)
print(l1)

l1.pop(5)
print(l1)

l1.remove(9876)
print(l1)