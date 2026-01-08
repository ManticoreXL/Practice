import sys
input = sys.stdin.readline

from itertools import combinations

n = int(input())

pows = set()

t = 1

while (t ** 2) <= n:
    pows.add(t ** 2)
    t += 1

if n in pows:
    print(1)
    exit(0)

for s in pows:
    if (n - s) in pows:
        print(2)
        exit(0)

for i in pows:
    for j in pows:
        if (n - i - j) in pows:
            print(3)
            exit(0)

print(4)