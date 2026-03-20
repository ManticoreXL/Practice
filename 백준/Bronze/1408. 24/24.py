a, b, c = map(int, input().split(":"))
d, e, f = map(int, input().split(":"))

s = f - c
if s<0:
    s = s + 60
    e = e - 1

m = e - b
if m<0:
    m = m + 60
    d = d - 1

h = d - a
if h<0:
    h = h + 24

if h<10:
    print("0", end="")
    print(h, end=":")
else:
    print(h, end=":")

if m<10:
    print("0", end="")
    print(m, end=":")
else:
    print(m, end=":")

if s<10:
    print("0", end="")
    print(s)
else:
    print(s)