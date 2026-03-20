n = int(input())
s = list(map(int, input().split()))
count = 0

for x in range(len(s)):
    if n == s[x]:
        count = count + 1
        
print(count)