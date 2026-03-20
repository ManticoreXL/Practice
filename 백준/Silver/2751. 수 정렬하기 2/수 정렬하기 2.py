import sys

n = int(input())
s = []

for x in range(n):
    a = int(sys.stdin.readline())
    s.append(a)

s.sort()
    
for x in range(n):
    print(s[x])
    
