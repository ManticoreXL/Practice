s = input()

a = []

for _ in range(26):
    a.append(0)
    
for x in s:
    if x == "a":
        a[0] = a[0] + 1
    elif x == "b":
        a[1] = a[1] + 1
    elif x == "c":
        a[2] = a[2] + 1
    elif x == "d":
        a[3] = a[3] + 1
    elif x == "e":
        a[4] = a[4] + 1
    elif x == "f":
        a[5] = a[5] + 1
    elif x == "g":
        a[6] = a[6] + 1
    elif x == "h":
        a[7] = a[7] + 1
    elif x == "i":
        a[8] = a[8] + 1
    elif x == "j":
        a[9] = a[9] + 1
    elif x == "k":
        a[10] = a[10] + 1
    elif x == "l":
        a[11] = a[11] + 1
    elif x == "m":
        a[12] = a[12] + 1
    elif x == "n":
        a[13] = a[13] + 1
    elif x == "o":
        a[14] = a[14] + 1
    elif x == "p":
        a[15] = a[15] + 1
    elif x == "q":
        a[16] = a[16] + 1
    elif x == "r":
        a[17] = a[17] + 1
    elif x == "s":
        a[18] = a[18] + 1
    elif x == "t":
        a[19] = a[19] + 1
    elif x == "u":
        a[20] = a[20] + 1    
    elif x == "v":
        a[21] = a[21] + 1
    elif x == "w":
        a[22] = a[22] + 1
    elif x == "x":
        a[23] = a[23] + 1
    elif x == "y":
        a[24] = a[24] + 1
    elif x == "z":
        a[25] = a[25] + 1

for x in range(26):
    print(a[x], end=" ")