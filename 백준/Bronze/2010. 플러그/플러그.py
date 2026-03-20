import sys

n = int(input())
c = 0

for _ in range(n):
    a = int(sys.stdin.readline())
    c = c + a - 1
    
print(c+1)