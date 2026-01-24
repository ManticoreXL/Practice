import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(maze, start_y, start_x, dest_y, dest_x, rows, cols):
    q = deque()
    q.append((start_y, start_x))

    visited = set()
    visited.add((start_y, start_x))

    while q:
        curr_y, curr_x = q.popleft()

        for i in range(4):
            next_y = curr_y + dy[i]
            next_x = curr_x + dx[i]

            if (0 <= next_y < rows) and (0 <= next_x < cols):
                if (maze[next_y][next_x] != 0) and ((next_y, next_x) not in visited):
                    visited.add((next_y, next_x))
                    q.append((next_y, next_x))
                    maze[next_y][next_x] = maze[curr_y][curr_x] + 1


N, M = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(N)]

BFS(maze, 0, 0, N - 1, M - 1, N, M)

print(maze[N - 1][M - 1])