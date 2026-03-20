import sys
input = sys.stdin.readline

n = int(input())
numbers = []
stack = []
count = 1
result = []
flag = True

for _ in range(n):
    numbers.append(int(input()))

for num in numbers:
    while count <= num:
        stack.append(count)
        count += 1
        result.append("+")

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break

if flag:
    for i in result:
        print(i)
else:
    print("NO")