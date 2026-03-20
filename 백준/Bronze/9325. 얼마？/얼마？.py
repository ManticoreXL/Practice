t = int(input())

for _ in range(t):
    s = int(input())
    o = int(input())
    for _ in range(o):
        a, b = map(int, input().split())
        s = s + a * b
    print(s)