s = int(input())
n = 1
sum = 0

while(True):
    sum = sum + n
    if sum<s:
        n = n + 1
    elif sum==s:
        break
    else:
        n = n - 1
        break
        
print(n)
        