myDict = {
    "fast":"In a quick manner",
    "harry":"A coder",
    "marks":[1,2,5],
    "anotherdict":{"virat":"player"},
    1:2
}

print(myDict.keys())
print(type(myDict.keys()))
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items())
print(myDict.get("marks"))
print(myDict.get("marks2")) #throws an output NONE as marks 2 is not present in dictionary
#print(myDict["marks2"]) #throws an error as marks 2 is not present in dictionary
updateDict = {
    "Lovish" : "Friend"
}
myDict.update(updateDict)
#print(nyDict.update) wrong way
print(myDict)