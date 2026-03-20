x, y = map(int, input().split())

a = min(x, y)
b = max(x, y)


if a-b == 0:
    print(0)
    exit()
else:
    print(b-a-1)

for x in range(a+1, b):
    print(x, end=" ")