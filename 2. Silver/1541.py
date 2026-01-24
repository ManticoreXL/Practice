import sys
input = sys.stdin.readline

expression = list(input().split('-'))

nums = []

for term in expression:
    term.rstrip()

    nums.append(list(map(int, term.split('+'))))

res = sum(nums[0])

for i in range(1, len(nums)):
    res -= sum(nums[i])

print(res)