import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())

nums = []

for i in range(1, N + 1):
    nums.append(i)

coms = list(combinations(nums, M))

for c in coms:
    print(*c)