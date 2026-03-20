w = []
k = []

for x in range(2):
    for _ in range(10):
        a = int(input())
        if x == 0:
            w.append(a)
        else:
            k.append(a)
        
w.sort()
k.sort()

w = w[7:]
k = k[7:]

print(sum(w), sum(k))