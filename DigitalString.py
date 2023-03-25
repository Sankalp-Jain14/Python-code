# Find the difference between largest occurence of a word minus the input taken by the user minus 1
# Example
# user input TEAMATE , 1  then output should be 2-1-1=0     because highest occ = 2 user input is 1 
# and we have to subtract 1 from the result    
s = input()
x = int(input())
l=[]
for i in s:
    l.append(i)

se = set(l)

c = set()
for i in se:
    c.add(l.count(i))

d = max(c) - min(c)

if d<x:
    print("0")
else:
    print(d-x)
