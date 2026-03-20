import math

x, y, r = map(int, input().split())
x_, y_, r_ = map(int, input().split())

d = math.sqrt(abs((x-x_)**2)+abs((y-y_)**2))

if d >= r+r_:
    print("NO")
else:
    print("YES")