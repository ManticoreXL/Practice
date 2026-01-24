import sys
input = sys.stdin.readline

from collections import deque


def get_neighbors(graph, node):
    neighbors = []

    for i in range(1, len(graph[node])):
        if graph[node][i] == 1:
            neighbors.append(i)

    return neighbors


def BFS(graph, start, visited):
    q = deque()

    q.append(start)
    visited[start] = True

    while q:
        curr = q.popleft()

        neighbors = get_neighbors(graph, curr)

        for next in neighbors:
            if graph[curr][next] == 1 and visited[next] == False:
                visited[next] = True
                q.append(next)


N, M = map(int, input().split())

count = 0

graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())

    graph[u][v] = 1
    graph[v][u] = 1

for i in range(1, N + 1):
    if visited[i] == False:
        BFS(graph, i, visited)
        count += 1

print(count)