def binsearch(x, data):
    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start + end)//2

        if data[mid] == x:
            return 1
        elif data[mid] < x:
            start = mid + 1
        elif data[mid] > x:
            end = mid - 1

    return 0

n = int(input())

s = list(map(int, input().split()))

m = int(input())

d = list(map(int, input().split()))

s.sort()

for x in d:
    print(binsearch(x, s), end=" ")