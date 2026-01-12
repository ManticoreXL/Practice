import sys
input = sys.stdin.readline

N = int(input())

coord = list(map(int, input().split()))

unique = list(set(coord))
unique.sort()

comp = dict()

index = 0
for i in unique:
    comp[i] = index
    index += 1

for c in coord:
    print(comp[c], end=' ')