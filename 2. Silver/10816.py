import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
cards = list(map(int, input().split()))

dict = {}

for c in cards:
    if c not in dict.keys():
        dict[c] = 1
    else:
        dict[c] += 1

m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    if t not in dict.keys():
        print(0, end=' ')
    else:
        print(dict[t], end=' ')