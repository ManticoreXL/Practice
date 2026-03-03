from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS(y, x, N, M, graph):
    q = deque()
    visited = [[0] * M for _ in range(N)]

    q.append((y, x))
    visited[y][x] = True

    person = 0

    while q:
        curr = q.popleft()

        cy, cx = curr

        if graph[cy][cx] == "P":
            person += 1

        for i in range(4):
            ny, nx = curr[0] + dy[i], curr[1] + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and graph[ny][nx] != "X":
                    visited[ny][nx] = True
                    q.append((ny, nx))

    return person


N, M = map(int, input().split())

campus = []

for i in range(N):
    row = input()
    campus.append(row)

    if row.find("I") != -1:
        y, x = i, row.find("I")

result = BFS(y, x, N, M, campus)

if not result:
    print("TT")
else:
    print(result)