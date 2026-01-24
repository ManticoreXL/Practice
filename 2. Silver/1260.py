import sys
input = sys.stdin.readline

from collections import deque


def get_neighbors(graph, node):
    neighbors = []

    for i in range(1, len(graph[node])):
        if graph[node][i] == 1:
            neighbors.append(i)

    return neighbors


def DFS(graph, node, visited: set):
    if node is None:
        return
    if node in visited:
        return
    
    visited.add(node)

    print(node, end=' ')

    neighbors = get_neighbors(graph, node)

    for n in neighbors:
        DFS(graph, n, visited)


def BFS(graph, node): 
    q = deque()

    visited = set()

    q.append(node)
    visited.add(node)

    while q:
        curr = q.popleft()

        print(curr, end=' ')

        neighbors = get_neighbors(graph, curr)

        for n in neighbors:
            if n not in visited:
                visited.add(n)
                q.append(n)

    print()


if __name__ == '__main__':

    n, m, v = map(int, input().split())

    graph = [[[0] for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    DFS(graph, v, set())
    print()
    BFS(graph, v)

# endif