c = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    temp = c[a-1:b]
    temp.reverse()
    c = c[:a-1] + temp + c[b:]

for x in c:
    print(x, end=" ")