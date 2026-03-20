s = input()
lth = 0

for x in range(len(s)):
    if x==0:
        lth = lth + 10
    elif s[x-1]==s[x]:
        lth = lth + 5
    else:
        lth = lth + 10
            
print(lth)