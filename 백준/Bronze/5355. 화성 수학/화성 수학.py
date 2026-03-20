def ad(x):
    return 3*x

def pct(x):
    return x+5

def shop(x):
    return x-7

def martmath(x, y):
    if y=="@":
        return ad(x)
    elif y=="%":
        return pct(x)
    elif y=="#":
        return shop(x)

n = int(input())

for x in range(n):
    a = list(input().split())
    a[0] = float(a[0])
    for y in range(1, len(a)):
        a[0] = martmath(a[0], a[y])
    print(format(a[0], ".2f"))