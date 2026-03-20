n = int(input())

for x in range(1, n+1):
    a, b = map(int, input().split())
    print("Case", x, end=": ")
    print(a+b)