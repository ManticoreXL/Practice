a = int(input())
b = int(input())
c = int(input())

s = list(str(a*b*c))

for x in range(0, 10):
    print(s.count(str(x)))
        