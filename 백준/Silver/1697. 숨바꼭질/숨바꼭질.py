from collections import deque

def BFS(N, K):
    if N == K:
        return 0

    q = deque()
    visited = [0] * 100_001

    visited[N] = 0
    q.append(N)
    
    while q:
        curr = q.popleft()

        neighbors = [curr - 1, curr + 1, curr * 2]

        for n in neighbors:
            if 0 <= n < 100_001 and not visited[n]:
                visited[n] = visited[curr] + 1
                q.append(n)

                if n == K:
                    return visited[n]

N, K = map(int, input().split())

print(BFS(N, K))

