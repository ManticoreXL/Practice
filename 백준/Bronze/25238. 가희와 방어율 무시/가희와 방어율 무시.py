a, i = map(int, input().split())

d = a - (a * (i/100))

if d >= 100:
    print("0")
else:
    print("1")