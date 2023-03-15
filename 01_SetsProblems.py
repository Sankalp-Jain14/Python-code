# Take the input as Hindi words and print them in english


myDict = {
    "Pankha": "Fan",
    "Vastu" :"Item",
    "Dabba":"Box"

}


print("Enter any one of the above words to get hindi meaning of it ", myDict.keys() )

a =input()

# print(myDict[a]) #This will throw error if the value os not present in dictionary
print(myDict.get(a)) #This will not throw error