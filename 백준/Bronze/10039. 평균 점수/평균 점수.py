score = 0

for x in range(0, 5):
    a = int(input())
    if a<40 :
        score = score + 40
    else:
        score = score + a
        
print(score//5)