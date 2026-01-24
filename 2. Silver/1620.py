import sys
input = sys.stdin.readline

n, m = map(int, input().split())

guide_dict = {}
guide_list = []
guide_list.append(0)

for i in range(1, n + 1):
    name = input().strip()

    guide_dict[name] = i
    guide_list.append(name)

for _ in range(m):
    query = input().strip()

    if query.isdigit():
        print(guide_list[int(query)])
    else:
        print(guide_dict[query])