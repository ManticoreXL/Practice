import sys
input = sys.stdin.readline

n = int(input())
str = str(input())

chars = [c for c in str]
chars.pop()

sum = 0
for i in range(n):
    c = ord(str[i]) - 96
    sum += c * (31 ** i) % 1234567891

sum %= 1234567891
print(sum)