t = int(input())

for _ in range(t):
    n = int(input())
    tt = 0
    tg = 0
    for _ in range(n):
        a, b = map(float, input().split())
        tt = tt + a
        tg = tg + a * b
        gpa = round(tg/tt, 1)
    print(int(tt), gpa)