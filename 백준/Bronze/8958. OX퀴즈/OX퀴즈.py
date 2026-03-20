n = int(input())
test = 0

for x in range(n):
    score = 0
    bonus = 0
    test = input()
    
    for x in test:
        if x == "O":
            bonus = bonus + 1
            score = score + bonus
        else:
            bonus = 0
    print(score)
        
    