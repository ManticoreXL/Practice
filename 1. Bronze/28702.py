import sys
input = sys.stdin.readline

s1 = str(input().strip())
s2 = str(input().strip())
s3 = str(input().strip())

if s1.isdecimal():
    num = int(s1) + 3
elif s2.isdecimal():
    num = int(s2) + 2
elif s3.isdecimal():
    num = int(s3) + 1

if (num % 3 == 0) and (num % 5 == 0):
    res = "FizzBuzz"
elif (num % 3 == 0):
    res = "Fizz"
elif (num % 5 == 0):
    res = "Buzz"
else:
    res = num

print(res)