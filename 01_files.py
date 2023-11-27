
f = open('sample.txt') #by default the mode is read 'r' for other modes we have to give the attribute!!!
data = f.read(5) #reads first 5 characters from file
# data = f.read()
print(data)
f.close()