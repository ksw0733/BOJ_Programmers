import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = True
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            bfs(i, graph, visited)
            cnt += 1
    print(cnt)