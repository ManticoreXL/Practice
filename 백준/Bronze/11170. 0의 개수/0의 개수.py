t = int(input())

for _ in range(t):
    sum_ = 0
    a, b = map(int, input().split())
    for x in range(a, b+1):
        s = str(x)
        sum_ = sum_ + s.count("0")
    print(sum_)