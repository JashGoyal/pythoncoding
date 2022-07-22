myDict = {
    "fast": "In a Quick Manner",
    "Jash": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'Jash': 'Player'},
    1: 2
}

print(list(myDict.keys())) 
print(myDict.values())  
print(myDict.items())  
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "Jash": "A Dancer"
}
myDict.update(updateDict) 
print(myDict)

print(myDict.get("Jash")) 
print(myDict["Jash"]) 
print(myDict.get("Jash2"))
print(myDict["Jash2"]) 