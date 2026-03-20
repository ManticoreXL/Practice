s = input()

for x in s:
    c = ord(x) - 3
    if c < 65:
        c = c + 26
    print(chr(c), end="")