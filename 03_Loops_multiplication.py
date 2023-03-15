#Print table of a number entered by the user

num = int(input("Enter the number "))
for i in range(1,11):
    print(str(num) + " X "+ str(i) + "=" + str(num*i))

    print(f"{num}X{i}={num*i}") # another way to do the above process