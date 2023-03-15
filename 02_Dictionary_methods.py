myDict = {
    "Fast" : "In a quick manner",
    "Sankalp" : "A Coder",
    "Marks" : [2,4,3,7],
    1:2,
    "anotherDict" :{'school':'player'}
}
 

print(myDict.keys()) # prints the keys of the dictionary
print(type(myDict.keys())) # Class is not lists but 'dict_keys'
print(list(myDict.keys())) # It is converted into lists


print(myDict.values()) # prints the values of the dictionary
print(myDict.items()) # PRints all the contents in the dictinary
 

print(myDict)

updateDict = {
    "lovish" : "Friend",
    "Shubham" :"Friend"
}

myDict.update(updateDict)
print(myDict)



# Difference between .get and [] brackets syntax 
# print(myDict["Sankalp2"]) // Throws error
print(myDict.get("Sankalp2")) # Prints NONE




