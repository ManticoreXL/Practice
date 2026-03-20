n = int(input())

for _ in range(n):
    temp = 0
    p = int(input())
    for _ in range(p):
        a, b = input().split()
        if temp==0:
            temp = int(a)
            player = b
        elif temp < int(a):
            temp = int(a)
            player = b
    print(player)