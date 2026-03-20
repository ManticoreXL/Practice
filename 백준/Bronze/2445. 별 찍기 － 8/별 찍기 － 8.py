n = int(input())

for x in range(1, n):
    print("*"*(x)+" "*((n-x)*2)+"*"*(x))
    
print("*"*(n*2))

for x in range(1, n):
    print("*"*(n-x)+" "*(x*2)+"*"*(n-x))
    
              