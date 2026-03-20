r = []
count = 0

for x in range(10):
    n = int(input())
    r.append(n%42)
    
for x in range(42):
    if x in r:
        count = count + 1
        
print(count)