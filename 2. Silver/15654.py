import sys
input = sys.stdin.readline

from itertools import permutations

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

pers = list(permutations(nums, M))

for p in pers:
    print(*p)