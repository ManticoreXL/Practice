def selfnum(x):
    sum = x
    while(True):
        sum = sum + x % 10
        if x == x%10:
            break
        x = x // 10
    return sum

a = list(range(1, 10001))

b = []

x = 1

while(True):
    if x > 10000:
        break
    else:
        b.append(selfnum(x))
        x = x + 1

sta = set(a)
stb = set(b)

res = set(a) - set(b)
res = list(res)

res.sort()

for x in range(len(res)):
    print(res[x])