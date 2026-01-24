import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.insert(0, 0)

sums = []

s = 0

for num in nums:
    s += num
    sums.append(s)

for _ in range(m):
    i, j = map(int, input().split())

    print(sums[j] - sums[i - 1])