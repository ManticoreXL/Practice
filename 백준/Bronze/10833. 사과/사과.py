n = int(input())
ar = 0

for _ in range(n):
    a, b = map(int, input().split())
    ar = ar + b%a
    
print(ar)