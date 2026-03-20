import sys
input = sys.stdin.readline

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

m = 0

for s in size:
    if s % t != 0:
        m += s // t + 1
    else:
        m += s // t 

q = n // p
r = n % p

print(m)
print(q, r)