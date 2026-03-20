p = int(input())

total_list = []

for x in range(p ):
    p_list = input().split()
    p_list = [str(p_list[0]), int(p_list[1]), int(p_list[2]), int(p_list[3])]
    total_list.append(p_list)

total_list.sort(key=lambda x:(-x[3], -x[2], -x[1]))
print(total_list[0][0])
print(total_list[-1][0])