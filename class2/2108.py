import sys
input = sys.stdin.readline

# Get trial count 
t = int(input())

numbers = list()
counts = dict()

# Get numbers
for _ in range(t):
    numbers.append(int(input()))

numbers.sort()

# Count frequency
for i in numbers:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

# Find max keys to calculate mode
max_value = max(counts.values())
max_keys = []
for i in counts:
    if counts[i] == max_value:
        max_keys.append(i)

# Calculate statistics
mean = round(sum(numbers) / len(numbers))
median = numbers[len(numbers) // 2]
mode = max_keys[1] if len(max_keys) > 1 else max_keys[0]
range = max(numbers) - min(numbers)

# Print result
print(mean)
print(median)
print(mode)
print(range)