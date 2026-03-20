import sys
input = sys.stdin.readline

n, k = map(int, input().split())

numbers = []
result = []

# Insert numbers into the list
for i in range(1, n + 1):
    numbers.append(i)

# Make Josephus permutation
while len(numbers) != 0:
    for _ in range(k - 1):
        numbers.append(numbers.pop(0))
    result.append(numbers.pop(0))

# Print the result
print(f"<{', '.join(map(str, result))}>")