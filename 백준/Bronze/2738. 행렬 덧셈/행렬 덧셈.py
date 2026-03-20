import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())

mat = []

for i in range(rows):
    row = list(map(int, input().split()))
    mat.append(row)

for i in range(rows):
    row = list(map(int, input().split()))
    for j in range(cols):
        mat[i][j] += row[j]

for i in range(rows):
    for j in mat[i]:
        print(j, end=' ')
    print()