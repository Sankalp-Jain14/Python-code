l1 =  [1,8,7,2,21]
print(l1) #[1,8,7,2,21]

# print(l1.sort())
#  This will not work because new string will not be retured instead the orginal string is modified


l1.sort()
print(l1) #[1, 2, 7, 8, 21] #THis will properly work



l1.reverse() #reverse the list
print(l1) #[21, 8, 7, 2, 1]


l1.append(45) # Insert 45 at the end
print(l1) #[21, 8, 7, 2, 1, 45]


l1.insert(2,34) #34 will bw inserted at index 2
print(l1) #[21, 8, 34, 7, 2, 1, 45]


l1.pop(1) # removes element at index 1
print(l1)  #[21, 34, 7, 2, 1, 45]

l1.remove(7) # removes 7 from the list
print(l1) #[21, 34, 2, 1, 45]

