#Important: This syntax will create an empty dictionary not set
a = {}
print(type(a))

#An empty set can be created using the following syntax
b = set()
print(type(b))

#METHODS IN SETS 
b = {1,2,3,4,5,6,7}
b.add(4)
b.add(5)
print(b)
print(len(b))
b.remove(2)
print(b)
print(b.pop())

b = {4,5,6,7,8,9}
b.union({8,11})
print(b.union)
b.intersection({8,11})
print(b)
print(b.clear())


