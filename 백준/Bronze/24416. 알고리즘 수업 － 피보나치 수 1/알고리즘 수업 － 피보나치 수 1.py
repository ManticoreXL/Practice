import sys
input = sys.stdin.readline

n = int(input())

def fibo1(n):
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 2

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    
    return f[n - 1]
    
def fibo2(n):
    return n - 2

print(fibo1(n), fibo2(n))