import sys
input = sys.stdin.readline

n, k = map(int, input().split())

numbers = []
result = []

for i in range(1, n + 1):
    numbers.append(i)

while len(numbers) != 0:
    for _ in range(k - 1):
        numbers.append(numbers.pop(0))
    result.append(numbers.pop(0))

print(f"<{', '.join(map(str, result))}")