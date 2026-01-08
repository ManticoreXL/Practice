import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    cols, rows, k = map(int, input().split())

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for _ in range(k):
        x, y = map(int, input().split())

        grid[x][y] = 1

    
    for r in grid:
        print(r)