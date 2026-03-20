a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

mk = a + b + c + d
ms = e + f + g + h

print(max(mk, ms))