import sys

maxnum = 0
counter = 0

for x in range(1, 10):
    a = int(sys.stdin.readline())
    if a > maxnum:
        maxnum = a
        counter = x
        
print(maxnum)
print(counter)