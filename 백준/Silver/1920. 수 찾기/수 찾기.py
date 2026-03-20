import sys

def binsearch(target, list_):

    first_index = 0
    last_index = len(list_) - 1

    while first_index <= last_index:

        mid_index = (first_index + last_index) // 2

        if list_[mid_index] == target:
            return 1
        elif list_[mid_index] < target:
            first_index = mid_index + 1
        else:
            last_index = mid_index - 1

    return 0

a = int(input())

tl = list(map(int, sys.stdin.readline().split()))

b = int(input())

cl = list(map(int, sys.stdin.readline().split()))

tl.sort()

for x in cl:
    print(binsearch(x, tl))