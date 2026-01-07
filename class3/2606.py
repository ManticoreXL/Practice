import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
p = int(input())

graph = [[0] for _ in range(n + 1)]

for i in range(p):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque()
queue.append(1)

visited = [False] * (n + 1)
visited[1] = True

count = 0

while queue:
    curr = queue.pop()

    for next in graph[curr]:
        if visited[next] == False:
            visited[next] = True
            queue.appendleft(next)
            count += 1

print(count - 1)