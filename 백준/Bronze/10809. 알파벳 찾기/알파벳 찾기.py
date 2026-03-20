from string import ascii_lowercase

alphabetlist = ascii_lowercase

s = input()

a = []

for x in alphabetlist:
    a.append(s.find(x))

for x in a:
    print(x, end=" ")