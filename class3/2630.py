import sys
input = sys.stdin.readline

white_count = 0
blue_count = 0

def cut_paper(x, y, n):
    global white_count
    global blue_count

    curr_color = paper[x][y]
    is_same = True
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != curr_color:
                is_same = False
                break
        if not is_same:
            break

    if is_same:
        if curr_color == 0:
            white_count += 1
        else:
            blue_count += 1
        return
    
    half = n // 2
    cut_paper(x, y, half)
    cut_paper(x, y + half, half)
    cut_paper(x + half, y, half)
    cut_paper(x + half, y + half, half)

n = int(input())

paper= []

for _ in range(n):
    paper.append(list(map(int, input().split())))

cut_paper(0, 0, n)

print(white_count)
print(blue_count)

