import sys
input = sys.stdin.readline

from collections import Counter

n, m = map(int, input().split())

trees = list(map(int, input().split()))
counter = Counter(trees)
keys = counter.keys()

low = 0
high = max(counter.keys())

while (low <= high):
    mid = (low + high) // 2

    s = 0

    for t in keys:
        if t > mid:
            s += (t - mid) * counter[t]

    if s >= m:
        low = mid + 1
    else:
        high = mid - 1

print(high)