import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lans = []

for _ in range(k):
    lans.append(int(input()))

low = 1
high = max(lans)

while(low <= high):
    mid = (low + high) // 2

    amount = 0
    
    for l in lans:
        amount += l // mid

    if amount >= n:
        low = mid +1
    else:
        high = mid - 1

print(high)