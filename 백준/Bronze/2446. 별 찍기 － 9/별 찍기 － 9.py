n = int(input())

for x in range(0, n-1):
    print(" "*(x)+"*"*(2*(n-x)-1))
    
print(" "*(n-1)+"*")

for x in range(0, n-1):
    print(" "*(n-x-2)+"*"*(2*x+3))