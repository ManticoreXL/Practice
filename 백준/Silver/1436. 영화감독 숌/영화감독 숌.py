import sys
input = sys.stdin.readline

n = int(input()) - 1

num = 666

while n > 0:
    num += 1
    if '666' in str(num):
        n -= 1

print(num)