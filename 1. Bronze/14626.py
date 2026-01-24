import sys
input = sys.stdin.readline

isbn = str(input().strip())

star = isbn.find('*')
check = int(isbn[12])
sum = 0

for i in range(len(isbn) - 1):
    if i == star:
        continue

    d = int(isbn[i])

    if i % 2 == 0:
        sum += d
    elif i % 2 == 1:
        sum += d * 3

for i in range(0, 10):
    tmp = sum

    if star % 2 == 0:
        tmp += i
    elif star % 2 == 1:
        tmp += i * 3

    if ((10 - tmp % 10) % 10 == check):
        m = i
        break
    elif ((10 - tmp % 10) % 10 == 10):
        m = 0
        break

print(m)