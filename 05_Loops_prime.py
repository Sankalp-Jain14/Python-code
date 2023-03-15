# Find prime numbers

num = int(input("Enter number"))
prime = True

for i in range (2,num):
    if num%i==0:
        prime = False
        print("Number is not prime")
        break
        
    else:
        prime = True


if (prime == True):
    print("Number is prime")

