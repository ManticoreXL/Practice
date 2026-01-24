import sys
input = sys.stdin.readline

from collections import deque


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(y, x, rows, cols, field, visited):
    q = deque([(y, x)])
    visited[y][x] = True

    while q:
        curr_y, curr_x = q.popleft()
        
        for i in range(4):
            next_y = curr_y + dy[i]
            next_x = curr_x + dx[i]

            if (0 <= next_y < rows) and (0 <= next_x < cols):
                if (field[next_y][next_x] == 1) and (not visited[next_y][next_x]):
                    visited[next_y][next_x] = True
                    q.append((next_y, next_x))


T = int(input())

for _ in range(T):
    M, N, k = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    w = 0

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == False:
                BFS(i, j, N, M, field, visited)
                w += 1

    print(w)