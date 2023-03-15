num = int(input())

def rec_sum(n):
    if n <=1:
        return n
    else:
        return n + rec_sum(n-1)
    

if num<1:
    print("positive number")
else:
    s = rec_sum(num)

print("the Sum of number is " + str(s))