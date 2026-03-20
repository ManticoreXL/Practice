n = int(input())

for x in range(1, n):
    print("*"*x)
print("*"*n)
for x in range(1, n):
    print("*"*(n-x))