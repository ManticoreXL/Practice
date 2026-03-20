bill = int(input())
n = int(input())
sum = 0

for x in range(n):
    pr, ct = map(int, input().split())
    sum = sum + pr*ct
    
if sum==bill:
    print("Yes")
else:
    print("No")