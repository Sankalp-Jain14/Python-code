#creating tuples using ()
t=(1,2,4,5)
print(t)



t1 = ()  #empty tuple
print(t1)


# t2 = (1) # wrong way of declaring single tuple
t2 = (1,) 
print(t2)



# t[0] = 34
# print(t)  // Throws error because we cannot change the value unlike lists 
# and this is the basic difference between the two

t3 = (1,2,4,3,6,1,3)
print(t3.count(1))
print(t3.index(6))

