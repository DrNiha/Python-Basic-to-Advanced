content = True
i = 1
with open("log.txt") as f:
    
    while content:
        i+=1
        content = f.readline()
        

        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")
            print(i)
     