n = int(input())

s = list(map(int, input().split()))

sums = 0

for x in s:
    if x <= n:
        sums = sums + x
    else:
        sums = sums + n
    
print(sums)