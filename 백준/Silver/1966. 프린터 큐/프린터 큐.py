import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    q = deque([(docs[i], i) for i in range(n)])

    count = 0

    while q:
        flag = False

        for i in range(len(q)):
            if q[0][0] < q[i][0]:
                q.append(q.popleft())
                flag = True
                break

        if not flag:
            res = q.popleft()
            count += 1

            if res[1] == m:
                print(count)
                break
     