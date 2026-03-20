t = int(input())

for _ in range(t):
    q, s = input().split()
    q = int(q)
    q = q - 1
    rs = s[:q] + s[q+1:]
    print(rs)