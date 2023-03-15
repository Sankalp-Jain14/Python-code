# sets is a collection of non repetative elements

a={1,2,5,3,2,7}

print(type(a)) ## Prints <class 'set'>

print(a) #prints {1,2,5,3,2,7}


# Creating an empty set
b = set() 
print(type(b)) 
print(b)


b.add(2)
b.add(2)
b.add(4)
b.add(4)
print(b) ## Both of these would be printed 



# b.add([2,4,5]) ## Lists and Dictionary cannot be added because contents of lsts can be changed
b.add((1,4,5)) # Contents of tuples can be added
print(b)



