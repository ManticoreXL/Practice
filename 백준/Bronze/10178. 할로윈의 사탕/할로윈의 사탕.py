import sys

t = int(input())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print("You get " + str(a//b) + " piece(s) " + "and your dad gets " + str(a%b) + " piece(s).")