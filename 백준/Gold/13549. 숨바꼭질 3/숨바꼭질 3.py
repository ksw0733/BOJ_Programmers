import sys
from collections import deque
input = sys.stdin.readline

def bfs(N, K):
    max_limit = 100001
    dist = [-1] * max_limit
    dist[N] = 0
    q = deque([N])
    
    while q:
        x = q.popleft()
        
        if x == K:
            return dist[x]
        
        if x * 2 < max_limit and dist[x * 2] == -1:
            dist[x * 2] = dist[x]
            q.appendleft(x * 2)
            
        if x - 1 >= 0 and dist[x - 1] == -1:
            dist[x - 1] = dist[x] + 1
            q.append(x - 1)
                    
        if x + 1 < max_limit and dist[x + 1] == -1:
            dist[x + 1] = dist[x] + 1
            q.append(x + 1)

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(bfs(N, K))