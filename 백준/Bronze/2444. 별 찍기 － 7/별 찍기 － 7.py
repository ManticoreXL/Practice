n = int(input())

for x in range(1, n):
    print(" "*(n-x)+"*"*(2*x-1))
print("*"*(2*n-1))
for x in range(1, n):
    print(" "*(x)+"*"*(2*(n-x)-1))