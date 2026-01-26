import sys
input = sys.stdin.readline

from collections import deque

def BFS(graph, start, visited, parents):
    q = deque()
    
    q.append(start)
    visited[start] = True

    while q:
        curr = q.popleft()
        visited[curr] = True

        for next in graph[curr]:
            if not visited[next]:
                parents[next] = curr
                visited[next] = True
                q.append(next)

    return parents


N = int(input())

adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N + 1)
parents = [0] * (N + 1)

BFS(adj, 1, visited, parents)

for p in parents[2:]:
    print(p)