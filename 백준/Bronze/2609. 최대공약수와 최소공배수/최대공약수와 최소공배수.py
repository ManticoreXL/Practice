def gcd(x, y):
    while y>0:
        x, y = y, x%y
    return x

def lcm(x, y):
    result = (x*y)//gcd(x, y)
    return result

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))
    