import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

count = 0

v = int(input())

for x in nums:
    if x == v:
        count += 1

print(count)