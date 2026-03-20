import sys

t = int(input())

for x in range(t):
    a, b = map(int, sys.stdin.readline().split(","))
    print(a+b)
    