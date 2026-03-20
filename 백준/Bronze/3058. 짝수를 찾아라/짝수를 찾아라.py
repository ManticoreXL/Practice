t = int(input())
e = []

for _ in range(t):
    s = list(map(int, input().split()))
    s.sort()
    for x in s:
        if x % 2 == 0: # 짝수
            e.append(x)
    print(sum(e), e[0])
    e.clear()
