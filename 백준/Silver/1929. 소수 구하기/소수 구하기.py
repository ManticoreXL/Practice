def primecheck(a):
    if a == 1:
        return False
    else:
        for x in range(2, int(a ** 0.5) + 1):
            if a % x == 0:
                return False
        return True


a, b = map(int, input().split())

for x in range(a, b+1):
    if primecheck(x):
        print(x)