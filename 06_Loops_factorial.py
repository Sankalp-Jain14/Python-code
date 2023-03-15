num = int(input())
factorial =   1
for i in range(1,num+1):
    factorial = i * factorial
    print(factorial) # prints every step of factorial
    

print(f"The factorial of this number is {factorial}")