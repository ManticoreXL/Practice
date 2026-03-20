s = input()

rs = ''.join(reversed(s))

if s==rs:
    print(1)
else:
    print(0)