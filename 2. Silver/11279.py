import sys
input = sys.stdin.readline

import heapq

N = int(input())

heap = []

for _ in range(N):
    num = int(input())

    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)