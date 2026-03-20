n = int(input())

s = input()

A = 0
B = 0

for x in range(n):
    if s[x]=="A":
        A = A + 1
    else:
        B = B + 1
        
if A>B:
    print("A")
elif A<B:
    print("B")
else:
    print("Tie")