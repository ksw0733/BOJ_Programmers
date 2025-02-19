import sys
from collections import deque
input = sys.stdin.readline


N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]


for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))


def bfs(start, k):
    queue = deque([start])
    visited = set([start])
    count = 0
    
    while queue:
        node = queue.popleft()
        for neighbor, usado in graph[node]:
            if neighbor not in visited and usado >= k:
                visited.add(neighbor)
                queue.append(neighbor)
                count += 1
    
    return count


results = []
for _ in range(Q):
    k, v = map(int, input().split())
    results.append(str(bfs(v, k)))

sys.stdout.write("\n".join(results) + "\n")