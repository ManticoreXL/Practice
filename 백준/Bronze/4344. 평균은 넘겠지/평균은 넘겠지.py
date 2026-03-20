c = int(input())

for x in range(c):
    n = list(map(int, input().split()))
    average = sum(n[1:]) / n[0]
    over = []
    overpct = 0
    
    for x in n[1:]:
        if x > average:
            over.append(x)
    
    overpct = len(over) / n[0] * 100
    print("%.3f"%overpct+"%")