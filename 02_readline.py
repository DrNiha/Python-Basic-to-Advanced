f = open('sample.txt') 
data = f.readline() # 1 readline func for reading 1 line 
print(data)
data = f.readline()
print(data)
f.close()


'''
rb is written when working with binary files
and
rt is written when working with text files

t in rt is written or assumed by default'''