s = input()
v = ["a", "e", "i", "o", "u"]
count = 0

for x in s:
    if x in v:
        count = count + 1

print(count)