empty_list = []

lst1 = ["one" , "two" , "Three" , "Four"]
lst2 = ['1','2' , '3' ,'4']
lst3 = ['1', '2' , "Three" ]
lst4 = [[1 , 21],[2,34] ]

print(lst1 , lst2 ,lst3 , lst4)
print(len(lst4)) # Prints length



lst1.append("Five")
print(lst1) # appends anything at last



lst4 = ["one"  , "Three" , "Four"]
lst4.insert(1,"Two")
print(lst4) # Insert "two" at index one

lst4.remove("Three")
print(lst4) # Removes "three" from list 

# lst4.append(lst2)
# print(lst4) #appends lst4 and lst1 but this goes as a list


# If you want as a element then 
lst4.extend(lst2)
print(lst4)



# delete Function 
lst5 = ["one" , "two" , "Three" , "Four"]
del lst5[2]
print(lst5) # Second element at index is deleted

a = lst5.pop()
print(a) # REturns the value at the top of the stack, So "Four" is returened
print(lst5) #Last element won't be printed


lst6 = ["one" , "two" , "Three" , "Four"]
if "one" in lst6:
    print("Item present")
if "six" not in lst6:
    print("Item not in list")




#Sorting
number = [3,6,2,7,8,5]
sorted_list = sorted(number)
print("New list made and the items are sorted ",sorted_list) #The new list is made for sorting if sorted function is used
print("Original list not changed" , number) #original list will not change

# if you want original list to change then,
number.sort()
print("Original list changed" , number) 





#Spliting -> Seprating the string and putting them in list
s = "one two three four "
lst7 = s.split()
print(lst7) #prints ['one', 'two', 'three', 'four'] and hence convert string into list

s2 = "one,two,three,four"
lst8 = s.split(',')
print(lst8)




#Slicing
numbers = [2,4,2,4,6,7,4,3,2]
print(numbers[2:5]) #prints from index 2 to index 4
print(numbers[:]) #prints whole list
print(numbers[::3]) #[start,end ,stepsJump]
print(numbers[1::2]) 
print("Number of two's are ",numbers.count(2)) # prints Number of two's 





#addittion of list
lst1 = ["one" , "two" , "Three" , "Four"]
lst2 = ['1','2' , '3' ,'4']

new_lst = lst1+lst2
print(new_lst)






#Loop in list
lst8 = ['one' , 'two' , 'Three' , 'four']
for ele in lst8:
    print(ele)


squares = []
for i in range(10):
    squares.append(i**2)
print(squares)  ##[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#Another way to do the same thing
squares = [i**2 for i in range(0,10)]
print(squares)


lst9 = [-10, -20 , 10 ,40 ,50]
lst10 = [2*i for i in lst9]
print(lst10)
          
