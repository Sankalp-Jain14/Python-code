# A copy of array is made from other array but some values are not present in the array  while copying
# the data. Print those values
# input [1,3,2,5,4]   [3,6,5,2,8]
# output [6,8]
m = int(input())
n = int(input())

o = list()
ne = list()
for i in range(m):
    o.append(int(input()))

for i in range(n):
    ne.append(int(input()))

for i in o:
    if i not in ne:
        print(i, end = " ")
