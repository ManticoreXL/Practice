n = int(input())

for x in range(n):
    print(" "*x+"*"*(n-x-1)+"*"+"*"*(n-x-1))