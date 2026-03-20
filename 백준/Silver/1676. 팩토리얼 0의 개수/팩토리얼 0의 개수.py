import math

count = 0
n = int(input())
s = math.factorial(n)
s = str(s)
s = list(s)
s.reverse()

for x in s:
    if x == "0":
        count = count + 1
    else:
        break

print(count)