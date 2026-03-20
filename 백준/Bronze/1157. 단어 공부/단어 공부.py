s = input().upper()
skind = list(set(s))

count_list = []

for x in skind:
    count = s.count(x)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    max_count = count_list.index(max(count_list))
    print(skind[max_count])