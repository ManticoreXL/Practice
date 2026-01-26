import sys
input = sys.stdin.readline

from itertools import combinations_with_replacement as dcombinations

N, M = map(int, input().split())

nums = []
for i in range(1, N + 1):
    nums.append(i)

dcoms = list(dcombinations(nums, M))

for c in dcoms:
    print(*c)